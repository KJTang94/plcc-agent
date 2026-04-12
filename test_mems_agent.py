import unittest
import json
from unittest.mock import Mock, patch
from mems_agent import MemsAgent, AgentState

class TestMemsAgentToolCalling(unittest.TestCase):
    def setUp(self):
        self.mock_api_key = "test-api-key"
        self.agent = MemsAgent(api_key=self.mock_api_key)
    
    @patch.object(MemsAgent, '_call_llm')
    def test_single_tool_call(self, mock_call_llm):
        mock_call_llm.side_effect = [
            json.dumps({"action": "tool", "tool_name": "get_users", "args": {}}),
            json.dumps({"action": "summarize", "reason": "已获取用户列表"})
        ]
        
        with patch.object(self.agent.mems_api, 'get_users') as mock_get_users:
            mock_get_users.return_value = json.dumps({
                "success": True,
                "count": 3,
                "data": [
                    {"id": 1, "username": "admin", "name": "管理员"},
                    {"id": 2, "username": "user1", "name": "用户1"},
                    {"id": 3, "username": "user2", "name": "用户2"}
                ]
            })
            
            result = self.agent.run("获取所有用户列表")
            
            self.assertEqual(mock_get_users.call_count, 1)
            self.assertIn("用户列表", result)
    
    @patch.object(MemsAgent, '_call_llm')
    def test_multiple_tool_calls_sequence(self, mock_call_llm):
        mock_call_llm.side_effect = [
            json.dumps({"action": "tool", "tool_name": "get_users", "args": {}}),
            json.dumps({"action": "tool", "tool_name": "get_roles", "args": {}}),
            json.dumps({"action": "summarize", "reason": "已获取用户和角色信息"})
        ]
        
        with patch.object(self.agent.mems_api, 'get_users') as mock_get_users, \
             patch.object(self.agent.mems_api, 'get_roles') as mock_get_roles:
            
            mock_get_users.return_value = json.dumps({
                "success": True,
                "count": 2,
                "data": [{"id": 1, "username": "admin"}, {"id": 2, "username": "user"}]
            })
            
            mock_get_roles.return_value = json.dumps({
                "success": True,
                "count": 3,
                "data": [{"id": 1, "name": "管理员"}, {"id": 2, "name": "普通用户"}, {"id": 3, "name": "访客"}]
            })
            
            result = self.agent.run("获取用户列表和角色列表")
            
            self.assertEqual(mock_get_users.call_count, 1)
            self.assertEqual(mock_get_roles.call_count, 1)
            self.assertIn("用户", result)
            self.assertIn("角色", result)
    
    @patch.object(MemsAgent, '_call_llm')
    def test_tool_call_with_parameters(self, mock_call_llm):
        mock_call_llm.side_effect = [
            json.dumps({"action": "tool", "tool_name": "get_user", "args": {"user_id": 1}}),
            json.dumps({"action": "summarize", "reason": "已获取用户详情"})
        ]
        
        with patch.object(self.agent.mems_api, 'get_user') as mock_get_user:
            mock_get_user.return_value = json.dumps({
                "success": True,
                "data": {"id": 1, "username": "admin", "name": "管理员", "email": "admin@example.com"}
            })
            
            result = self.agent.run("获取ID为1的用户详细信息")
            
            mock_get_user.assert_called_once_with(user_id=1)
            self.assertIn("admin", result)
            self.assertIn("管理员", result)
    
    @patch.object(MemsAgent, '_call_llm')
    def test_tool_call_with_login_first(self, mock_call_llm):
        mock_call_llm.side_effect = [
            json.dumps({"action": "tool", "tool_name": "login", "args": {}}),
            json.dumps({"action": "tool", "tool_name": "get_users", "args": {}}),
            json.dumps({"action": "summarize", "reason": "登录成功并获取用户列表"})
        ]
        
        with patch.object(self.agent.mems_api, 'login') as mock_login, \
             patch.object(self.agent.mems_api, 'get_users') as mock_get_users:
            
            mock_login.return_value = json.dumps({
                "success": True,
                "user_id": 1,
                "username": "admin",
                "message": "登录成功"
            })
            
            mock_get_users.return_value = json.dumps({
                "success": True,
                "count": 5,
                "data": []
            })
            
            result = self.agent.run("先登录然后获取用户列表")
            
            self.assertEqual(mock_login.call_count, 1)
            self.assertEqual(mock_get_users.call_count, 1)
            self.assertIn("登录", result)
    
    @patch.object(MemsAgent, '_call_llm')
    def test_three_tool_calls_in_sequence(self, mock_call_llm):
        mock_call_llm.side_effect = [
            json.dumps({"action": "tool", "tool_name": "get_users", "args": {}}),
            json.dumps({"action": "tool", "tool_name": "get_roles", "args": {}}),
            json.dumps({"action": "tool", "tool_name": "get_alarms", "args": {}}),
            json.dumps({"action": "summarize", "reason": "已获取用户、角色和告警信息"})
        ]
        
        with patch.object(self.agent.mems_api, 'get_users') as mock_get_users, \
             patch.object(self.agent.mems_api, 'get_roles') as mock_get_roles, \
             patch.object(self.agent.mems_api, 'get_alarms') as mock_get_alarms:
            
            mock_get_users.return_value = json.dumps({"success": True, "count": 3, "data": []})
            mock_get_roles.return_value = json.dumps({"success": True, "count": 2, "data": []})
            mock_get_alarms.return_value = json.dumps({"success": True, "count": 10, "data": []})
            
            result = self.agent.run("获取用户列表、角色列表和告警列表")
            
            self.assertEqual(mock_get_users.call_count, 1)
            self.assertEqual(mock_get_roles.call_count, 1)
            self.assertEqual(mock_get_alarms.call_count, 1)
            self.assertIn("用户", result)
            self.assertIn("角色", result)
            self.assertIn("告警", result)
    
    @patch.object(MemsAgent, '_call_llm')
    def test_tool_not_found(self, mock_call_llm):
        mock_call_llm.side_effect = [
            json.dumps({"action": "tool", "tool_name": "unknown_tool", "args": {}}),
            json.dumps({"action": "summarize", "reason": "工具调用完成"})
        ]
        
        result = self.agent.run("调用一个不存在的工具")
        
        self.assertEqual(len(self.agent.graph), 2)
        self.assertIn("工具", result)
    
    @patch.object(MemsAgent, '_call_llm')
    def test_direct_summarize_without_tool_call(self, mock_call_llm):
        mock_call_llm.return_value = json.dumps({
            "action": "summarize", 
            "reason": "用户的问题不需要调用工具，可以直接回答"
        })
        
        result = self.agent.run("你好，请问你是谁？")
        
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
