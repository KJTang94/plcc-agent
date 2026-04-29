
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试 PLCC Agent
"""

import sys
from plcc_agent import PlccAgent


def main():
    print("=" * 60)
    print("PLCC Agent 测试")
    print("=" * 60)
    
    try:
        print("\n1. 初始化 PLCC Agent...")
        agent = PlccAgent()
        print("   [OK] Agent 初始化成功!")
        print(f"   [OK] 共加载 {len(agent.tools)} 个工具")
        
        # 打印前 10 个工具
        print("\n2. 工具列表 (前 10 个):")
        for i, tool in enumerate(agent.tools[:10], 1):
            desc = tool.description
            if len(desc) > 100:
                desc = desc[:100] + "..."
            print(f"   {i}. {tool.name}: {desc}")
        if len(agent.tools) > 10:
            print(f"   ... 还有 {len(agent.tools) - 10} 个工具")
        
        print("\n" + "=" * 60)
        print("测试完成! PLCC Agent 已准备就绪。")
        print("要启动交互模式，请运行: python plcc_agent.py")
        print("=" * 60)
        
        return 0
        
    except Exception as e:
        print(f"\n[ERROR] 测试失败: {str(e)}")
        import traceback
        print("\n完整错误信息:")
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

