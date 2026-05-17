from typing import List, Dict, Any, Optional, TypedDict


class ParameterInfo(TypedDict, total=False):
    name: str
    type: str
    required: bool
    description: str
    children: List['ParameterInfo']


class ToolInfo:
    def __init__(self, name, description, func, parameters: Optional[List[ParameterInfo]] = None):
        self.name = name
        self.description = description
        self.func = func
        self.parameters = parameters or []


def create_tools(mems_api) -> List[ToolInfo]:
    tools = []

    tools.append(ToolInfo(
        name="login",
        description="用户登录，获取访问令牌。在调用其他需要认证的接口之前，需要先调用此接口。",
        func=mems_api.login
    ))

    tools.append(ToolInfo(
        name="get_alarm_config",
        description="查询告警通知配置信息",
        func=mems_api.get_alarm_config,
    ))

    tools.append(ToolInfo(
        name="add_alarm_config",
        description="配置告警通知。参数：data (object) - 请求体数据，字段：data.common (object, 必填) - 告警通知形式；data.common.popup_window (boolean, 必填) - 桌面弹窗；data.common.sound_light (boolean, 必填) - 声光；data.common.text_messages (boolean, 必填) - 短信；data.emergency (object, 必填) - 告警通知形式；data.emergency.popup_window (boolean, 必填) - 桌面弹窗；data.emergency.sound_light (boolean, 必填) - 声光；data.emergency.text_messages (boolean, 必填) - 短信；data.important (object, 必填) - 告警通知形式；data.important.popup_window (boolean, 必填) - 桌面弹窗；data.important.sound_light (boolean, 必填) - 声光；data.important.text_messages (boolean, 必填) - 短信",
        func=mems_api.add_alarm_config,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.common (object, 必填) - 告警通知形式；data.common.popup_window (boolean, 必填) - 桌面弹窗；data.common.sound_light (boolean, 必填) - 声光；data.common.text_messages (boolean, 必填) - 短信；data.emergency (object, 必填) - 告警通知形式；data.emergency.popup_window (boolean, 必填) - 桌面弹窗；data.emergency.sound_light (boolean, 必填) - 声光；data.emergency.text_messages (boolean, 必填) - 短信；data.important (object, 必填) - 告警通知形式；data.important.popup_window (boolean, 必填) - 桌面弹窗；data.important.sound_light (boolean, 必填) - 声光；data.important.text_messages (boolean, 必填) - 短信', 'children': [{'name': 'common', 'type': 'object', 'required': True, 'description': '告警通知形式', 'children': [{'name': 'popup_window', 'type': 'boolean', 'required': True, 'description': '桌面弹窗'}, {'name': 'sound_light', 'type': 'boolean', 'required': True, 'description': '声光'}, {'name': 'text_messages', 'type': 'boolean', 'required': True, 'description': '短信'}]}, {'name': 'emergency', 'type': 'object', 'required': True, 'description': '告警通知形式', 'children': [{'name': 'popup_window', 'type': 'boolean', 'required': True, 'description': '桌面弹窗'}, {'name': 'sound_light', 'type': 'boolean', 'required': True, 'description': '声光'}, {'name': 'text_messages', 'type': 'boolean', 'required': True, 'description': '短信'}]}, {'name': 'important', 'type': 'object', 'required': True, 'description': '告警通知形式', 'children': [{'name': 'popup_window', 'type': 'boolean', 'required': True, 'description': '桌面弹窗'}, {'name': 'sound_light', 'type': 'boolean', 'required': True, 'description': '声光'}, {'name': 'text_messages', 'type': 'boolean', 'required': True, 'description': '短信'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_alarm_confirm_by_user",
        description="确认告警。参数：user_id (integer, 必填) - 用户id, data (array[integer]) - 请求体数据，字段：data (array[integer])",
        func=mems_api.add_alarm_confirm_by_user,
        parameters=[
            {'name': 'user_id', 'type': 'integer', 'required': True, 'description': '用户id'},
            {'name': 'data', 'type': 'array[integer]', 'required': True, 'description': '请求体数据；字段：data (array[integer])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_alarm_confirm_status",
        description="查询已确认的告警",
        func=mems_api.get_alarm_confirm_status,
    ))

    tools.append(ToolInfo(
        name="get_alarm_count",
        description="查询告警总数",
        func=mems_api.get_alarm_count,
    ))

    tools.append(ToolInfo(
        name="add_alarm_define",
        description="上传单个告警定义。参数：data (object) - 请求体数据，字段：data.desc (string, 可选)；data.id (integer, 可选)；data.level (string, 可选)；data.name (string, 可选)；data.owners (string, 可选)；data.rule (string, 可选)",
        func=mems_api.add_alarm_define,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.desc (string, 可选)；data.id (integer, 可选)；data.level (string, 可选)；data.name (string, 可选)；data.owners (string, 可选)；data.rule (string, 可选)', 'children': [{'name': 'desc', 'type': 'string', 'required': False, 'description': ''}, {'name': 'id', 'type': 'integer', 'required': False, 'description': ''}, {'name': 'level', 'type': 'string', 'required': False, 'description': ''}, {'name': 'name', 'type': 'string', 'required': False, 'description': ''}, {'name': 'owners', 'type': 'string', 'required': False, 'description': ''}, {'name': 'rule', 'type': 'string', 'required': False, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_alarm_define_by",
        description="查询指定id的告警定义。参数：id (integer, 必填) - 告警定义id",
        func=mems_api.get_alarm_define_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '告警定义id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_alarm_defines",
        description="查询所有的告警定义",
        func=mems_api.get_alarm_defines,
    ))

    tools.append(ToolInfo(
        name="add_alarm_defines",
        description="上传告警定义。参数：data (object) - 请求体数据，字段：data.defines (array[PbAlarmDefine], 必填)；data.defines[].desc (string, 可选)；data.defines[].id (integer, 可选)；data.defines[].level (string, 可选)；data.defines[].name (string, 可选)；data.defines[].owners (string, 可选)；data.defines[].rule (string, 可选)",
        func=mems_api.add_alarm_defines,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.defines (array[PbAlarmDefine], 必填)；data.defines[].desc (string, 可选)；data.defines[].id (integer, 可选)；data.defines[].level (string, 可选)；data.defines[].name (string, 可选)；data.defines[].owners (string, 可选)；data.defines[].rule (string, 可选)', 'children': [{'name': 'defines', 'type': 'array[PbAlarmDefine]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'desc', 'type': 'string', 'required': False, 'description': ''}, {'name': 'id', 'type': 'integer', 'required': False, 'description': ''}, {'name': 'level', 'type': 'string', 'required': False, 'description': ''}, {'name': 'name', 'type': 'string', 'required': False, 'description': ''}, {'name': 'owners', 'type': 'string', 'required': False, 'description': ''}, {'name': 'rule', 'type': 'string', 'required': False, 'description': ''}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_alarm_defines_by_s",
        description="删除指定id的告警定义。参数：ids (string, 必填) - 告警定义id列表，以,间隔",
        func=mems_api.delete_alarm_defines_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '告警定义id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_alarm_defines_file",
        description="上传告警定义（文件形式）。参数：data (object) - 请求体数据，字段：data.fileContent (array[integer], 可选)；data.fileName (string, 可选)；data.is_zip (boolean, 可选)；data.op (string, 可选)",
        func=mems_api.add_alarm_defines_file,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.fileContent (array[integer], 可选)；data.fileName (string, 可选)；data.is_zip (boolean, 可选)；data.op (string, 可选)', 'children': [{'name': 'fileContent', 'type': 'array[integer]', 'required': False, 'description': ''}, {'name': 'fileName', 'type': 'string', 'required': False, 'description': ''}, {'name': 'is_zip', 'type': 'boolean', 'required': False, 'description': ''}, {'name': 'op', 'type': 'string', 'required': False, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_alarm_unconfirmed_number",
        description="查询未确认的告警数",
        func=mems_api.get_alarm_unconfirmed_number,
    ))

    tools.append(ToolInfo(
        name="get_alarms",
        description="查询告警，结果按照时间排序。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_alarms,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_alarms_unconfirmed",
        description="查询未确认的告警列表",
        func=mems_api.get_alarms_unconfirmed,
    ))

    tools.append(ToolInfo(
        name="get_aoe_results",
        description="查询AOE执行结果。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_aoe_results,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_aoes_models",
        description="查询所有AOE",
        func=mems_api.get_aoes_models,
    ))

    tools.append(ToolInfo(
        name="add_aoes_models",
        description="保存AOE。参数：data (array[AoeModel]) - 请求体数据，字段：data (array[AoeModel]) - aoe模型；data[].actions (array[ActionEdge], 必填) - 动作列表；data[].actions[].action (string, 必填) - 无动作；data[].actions[].aoe_id (integer, 必填) - AOE id；data[].actions[].failure_mode (string, 必填) - 失败模式；data[].actions[].name (string, 必填) - 动作名称；data[].actions[].source_node (integer, 必填) - 源节点；data[].actions[].target_node (integer, 必填) - 目标节点；data[].events (array[EventNode], 必填) - 节点列表；data[].events[].aoe_id (integer, 必填) - AOE id；data[].events[].expr (object, 必填) - 表达式对象；data[].events[].id (integer, 必填) - 节点id；data[].events[].name (string, 必填) - 节点名；data[].events[].node_type (string, 必填) - 节点类型；data[].events[].timeout (integer, 必填) - 事件还未发生时等待超时时间；data[].id (integer, 必填) - aoe id；data[].name (string, 必填) - aoe名称；data[].trigger_type (object, 必填) - 简单固定周期触发；data[].trigger_type.SimpleRepeat (object, 必填) - 时间对象；data[].variables (array[array[any]], 必填) - 用户自定义的变量：变量名和表达式",
        func=mems_api.add_aoes_models,
        parameters=[
            {'name': 'data', 'type': 'array[AoeModel]', 'required': True, 'description': '请求体数据；字段：data (array[AoeModel]) - aoe模型；data[].actions (array[ActionEdge], 必填) - 动作列表；data[].actions[].action (string, 必填) - 无动作；data[].actions[].aoe_id (integer, 必填) - AOE id；data[].actions[].failure_mode (string, 必填) - 失败模式；data[].actions[].name (string, 必填) - 动作名称；data[].actions[].source_node (integer, 必填) - 源节点；data[].actions[].target_node (integer, 必填) - 目标节点；data[].events (array[EventNode], 必填) - 节点列表；data[].events[].aoe_id (integer, 必填) - AOE id；data[].events[].expr (object, 必填) - 表达式对象；data[].events[].id (integer, 必填) - 节点id；data[].events[].name (string, 必填) - 节点名；data[].events[].node_type (string, 必填) - 节点类型；data[].events[].timeout (integer, 必填) - 事件还未发生时等待超时时间；data[].id (integer, 必填) - aoe id；data[].name (string, 必填) - aoe名称；data[].trigger_type (object, 必填) - 简单固定周期触发；data[].trigger_type.SimpleRepeat (object, 必填) - 时间对象；data[].variables (array[array[any]], 必填) - 用户自定义的变量：变量名和表达式', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'actions', 'type': 'array[ActionEdge]', 'required': True, 'description': '动作列表', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '动作列表', 'children': [{'name': 'action', 'type': 'string', 'required': True, 'description': '无动作'}, {'name': 'aoe_id', 'type': 'integer', 'required': True, 'description': 'AOE id'}, {'name': 'failure_mode', 'type': 'string', 'required': True, 'description': '失败模式'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '动作名称'}, {'name': 'source_node', 'type': 'integer', 'required': True, 'description': '源节点'}, {'name': 'target_node', 'type': 'integer', 'required': True, 'description': '目标节点'}]}]}, {'name': 'events', 'type': 'array[EventNode]', 'required': True, 'description': '节点列表', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '节点列表', 'children': [{'name': 'aoe_id', 'type': 'integer', 'required': True, 'description': 'AOE id'}, {'name': 'expr', 'type': 'object', 'required': True, 'description': '表达式对象', 'children': [{'name': 'rpn', 'type': 'array[Token]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'Binary', 'type': 'string', 'required': True, 'description': 'Mathematical operations.'}]}]}]}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '节点id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '节点名'}, {'name': 'node_type', 'type': 'string', 'required': True, 'description': '节点类型'}, {'name': 'timeout', 'type': 'integer', 'required': True, 'description': '事件还未发生时等待超时时间'}]}]}, {'name': 'id', 'type': 'integer', 'required': True, 'description': 'aoe id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': 'aoe名称'}, {'name': 'trigger_type', 'type': 'object', 'required': True, 'description': '简单固定周期触发', 'children': [{'name': 'SimpleRepeat', 'type': 'object', 'required': True, 'description': '时间对象', 'children': [{'name': 'nanos', 'type': 'integer', 'required': True, 'description': '剩余纳秒'}, {'name': 'secs', 'type': 'integer', 'required': True, 'description': '秒'}]}]}, {'name': 'variables', 'type': 'array[array[any]]', 'required': True, 'description': '用户自定义的变量：变量名和表达式'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_aoes_models_by_version_by_v",
        description="查询指定版本的AOE。参数：v (integer, 必填) - 版本id",
        func=mems_api.get_aoes_models_by_version_by_v,
        parameters=[
            {'name': 'v', 'type': 'integer', 'required': True, 'description': '版本id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_aoes_models_for_apply",
        description="查询根据版本号组装的AOE应用对象。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_aoes_models_for_apply,
        parameters=[
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_aoes_models_by_s",
        description="删除指定id的AOE。参数：ids (string, 必填) - AOE_id列表，以,间隔",
        func=mems_api.delete_aoes_models_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': 'AOE_id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_aoes_models_by",
        description="根据id查询指定的AOE。参数：id (integer, 必填) - AOE_id, version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_aoes_models_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': 'AOE_id'},
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_aoes_models_file",
        description="保存AOE（文件形式）。参数：data (object) - 请求体数据，字段：data.fileContent (array[integer], 可选)；data.fileName (string, 可选)；data.is_zip (boolean, 可选)；data.op (string, 可选)",
        func=mems_api.add_aoes_models_file,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.fileContent (array[integer], 可选)；data.fileName (string, 可选)；data.is_zip (boolean, 可选)；data.op (string, 可选)', 'children': [{'name': 'fileContent', 'type': 'array[integer]', 'required': False, 'description': ''}, {'name': 'fileName', 'type': 'string', 'required': False, 'description': ''}, {'name': 'is_zip', 'type': 'boolean', 'required': False, 'description': ''}, {'name': 'op', 'type': 'string', 'required': False, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_aoes_models_file2",
        description="保存AOE（多文件形式）。参数：data (object) - 请求体数据，字段：data.file (array[string], 必填)",
        func=mems_api.add_aoes_models_file2,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.file (array[string], 必填)', 'children': [{'name': 'file', 'type': 'array[string]', 'required': True, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_aoes_version",
        description="查询所有的AOE版本信息",
        func=mems_api.get_aoes_version,
    ))

    tools.append(ToolInfo(
        name="add_aoes_version",
        description="新增AOE版本。参数：data (object) - 请求体数据，字段：data.note (string, 必填) - 提交时的注释；data.tree_id (string, 必填) - 对应的tree_id；data.version (integer, 必填) - 版本号",
        func=mems_api.add_aoes_version,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.note (string, 必填) - 提交时的注释；data.tree_id (string, 必填) - 对应的tree_id；data.version (integer, 必填) - 版本号', 'children': [{'name': 'note', 'type': 'string', 'required': True, 'description': '提交时的注释'}, {'name': 'tree_id', 'type': 'string', 'required': True, 'description': '对应的tree_id'}, {'name': 'version', 'type': 'integer', 'required': True, 'description': '版本号'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_aoes_version_by_v",
        description="删除某一个AOE版本。参数：v (integer, 必填) - 版本id",
        func=mems_api.delete_aoes_version_by_v,
        parameters=[
            {'name': 'v', 'type': 'integer', 'required': True, 'description': '版本id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_auths",
        description="查询所有权限",
        func=mems_api.get_auth_auths,
    ))

    tools.append(ToolInfo(
        name="add_auth_auths",
        description="新增权限。参数：data (array[Authority]) - 请求体数据，字段：data (array[Authority]) - 权限；data[].desc (string, 必填) - 权限描述；data[].id (integer, 必填) - 权限ID；data[].method (string, 必填) - 请求方法；data[].name (string, 必填) - 权限名称；data[].url (string, 必填) - 权限可操作的url资源地址",
        func=mems_api.add_auth_auths,
        parameters=[
            {'name': 'data', 'type': 'array[Authority]', 'required': True, 'description': '请求体数据；字段：data (array[Authority]) - 权限；data[].desc (string, 必填) - 权限描述；data[].id (integer, 必填) - 权限ID；data[].method (string, 必填) - 请求方法；data[].name (string, 必填) - 权限名称；data[].url (string, 必填) - 权限可操作的url资源地址', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'desc', 'type': 'string', 'required': True, 'description': '权限描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '权限ID'}, {'name': 'method', 'type': 'string', 'required': True, 'description': '请求方法'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '权限名称'}, {'name': 'url', 'type': 'string', 'required': True, 'description': '权限可操作的url资源地址'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_auths_by_role",
        description="查询指定角色的所有权限。参数：id (integer, 必填) - 角色id",
        func=mems_api.get_auth_auths_by_role,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '角色id'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_auth_auths_by_s",
        description="删除指定id的删除权限。参数：ids (string, 必填) - 权限id列表，以,间隔",
        func=mems_api.delete_auth_auths_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '权限id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_auth_login",
        description="执行登录。参数：data (array[any]) - 请求体数据，字段：data (array[any])",
        func=mems_api.add_auth_login,
        parameters=[
            {'name': 'data', 'type': 'array[any]', 'required': True, 'description': '请求体数据；字段：data (array[any])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_menus",
        description="查询所有菜单",
        func=mems_api.get_auth_menus,
    ))

    tools.append(ToolInfo(
        name="add_auth_menus",
        description="新增菜单。参数：data (array[Menuitem]) - 请求体数据，字段：data (array[Menuitem]) - 菜单；data[].group (string, 必填) - 分组；data[].id (integer, 必填) - 菜单ID；data[].name (string, 必填) - 名称；data[].url (string, 必填) - 菜单对应的url地址",
        func=mems_api.add_auth_menus,
        parameters=[
            {'name': 'data', 'type': 'array[Menuitem]', 'required': True, 'description': '请求体数据；字段：data (array[Menuitem]) - 菜单；data[].group (string, 必填) - 分组；data[].id (integer, 必填) - 菜单ID；data[].name (string, 必填) - 名称；data[].url (string, 必填) - 菜单对应的url地址', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'group', 'type': 'string', 'required': True, 'description': '分组'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '菜单ID'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '名称'}, {'name': 'url', 'type': 'string', 'required': True, 'description': '菜单对应的url地址'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_menus_by_role",
        description="查询指定角色的所有菜单。参数：id (integer, 必填) - 角色id",
        func=mems_api.get_auth_menus_by_role,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '角色id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_menus_by_user",
        description="查询指定用户的所有菜单。参数：id (integer, 必填) - 用户id",
        func=mems_api.get_auth_menus_by_user,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '用户id'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_auth_menus_by_s",
        description="删除指定id的菜单。参数：ids (string, 必填) - 菜单id列表，以,间隔",
        func=mems_api.delete_auth_menus_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '菜单id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_auth_register",
        description="用户注册。参数：data (array[any]) - 请求体数据，字段：data (array[any])",
        func=mems_api.add_auth_register,
        parameters=[
            {'name': 'data', 'type': 'array[any]', 'required': True, 'description': '请求体数据；字段：data (array[any])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_roles",
        description="查询所有角色",
        func=mems_api.get_auth_roles,
    ))

    tools.append(ToolInfo(
        name="update_auth_roles",
        description="修改角色。参数：data (object) - 请求体数据，字段：data.id (integer, 必填) - 角色ID；data.name (string, 必填) - 角色名称；data.role2authority (array[integer], 必填) - 角色权限关联表，一个角色可以拥有多个权限；data.role2menu (array[integer], 必填) - 角色菜单关联表，一个角色可以拥有多个菜单",
        func=mems_api.update_auth_roles,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.id (integer, 必填) - 角色ID；data.name (string, 必填) - 角色名称；data.role2authority (array[integer], 必填) - 角色权限关联表，一个角色可以拥有多个权限；data.role2menu (array[integer], 必填) - 角色菜单关联表，一个角色可以拥有多个菜单', 'children': [{'name': 'id', 'type': 'integer', 'required': True, 'description': '角色ID'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '角色名称'}, {'name': 'role2authority', 'type': 'array[integer]', 'required': True, 'description': '角色权限关联表，一个角色可以拥有多个权限'}, {'name': 'role2menu', 'type': 'array[integer]', 'required': True, 'description': '角色菜单关联表，一个角色可以拥有多个菜单'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_auth_roles",
        description="新增角色。参数：data (array[Role]) - 请求体数据，字段：data (array[Role]) - 角色；data[].id (integer, 必填) - 角色ID；data[].name (string, 必填) - 角色名称；data[].role2authority (array[integer], 必填) - 角色权限关联表，一个角色可以拥有多个权限；data[].role2menu (array[integer], 必填) - 角色菜单关联表，一个角色可以拥有多个菜单",
        func=mems_api.add_auth_roles,
        parameters=[
            {'name': 'data', 'type': 'array[Role]', 'required': True, 'description': '请求体数据；字段：data (array[Role]) - 角色；data[].id (integer, 必填) - 角色ID；data[].name (string, 必填) - 角色名称；data[].role2authority (array[integer], 必填) - 角色权限关联表，一个角色可以拥有多个权限；data[].role2menu (array[integer], 必填) - 角色菜单关联表，一个角色可以拥有多个菜单', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'id', 'type': 'integer', 'required': True, 'description': '角色ID'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '角色名称'}, {'name': 'role2authority', 'type': 'array[integer]', 'required': True, 'description': '角色权限关联表，一个角色可以拥有多个权限'}, {'name': 'role2menu', 'type': 'array[integer]', 'required': True, 'description': '角色菜单关联表，一个角色可以拥有多个菜单'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_roles_by_s",
        description="根据ids查询角色。参数：ids (string, 必填) - 角色id列表，以,间隔",
        func=mems_api.get_auth_roles_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '角色id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_auth_roles_by_s",
        description="删除指定id的删除角色。参数：ids (string, 必填) - 角色id列表，以,间隔",
        func=mems_api.delete_auth_roles_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '角色id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_user_groups",
        description="查询所有用户组",
        func=mems_api.get_auth_user_groups,
    ))

    tools.append(ToolInfo(
        name="update_auth_user_groups",
        description="修改用户组。参数：data (object) - 请求体数据，字段：data.id (integer, 必填) - 用户组ID；data.name (string, 必填) - 用户组名称；data.user_group2role (array[integer], 必填) - 用户组角色关联表，一个用户组可以拥有多个角色",
        func=mems_api.update_auth_user_groups,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.id (integer, 必填) - 用户组ID；data.name (string, 必填) - 用户组名称；data.user_group2role (array[integer], 必填) - 用户组角色关联表，一个用户组可以拥有多个角色', 'children': [{'name': 'id', 'type': 'integer', 'required': True, 'description': '用户组ID'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '用户组名称'}, {'name': 'user_group2role', 'type': 'array[integer]', 'required': True, 'description': '用户组角色关联表，一个用户组可以拥有多个角色'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_auth_user_groups",
        description="新增用户组。参数：data (array[UserGroup]) - 请求体数据，字段：data (array[UserGroup]) - 用户组；data[].id (integer, 必填) - 用户组ID；data[].name (string, 必填) - 用户组名称；data[].user_group2role (array[integer], 必填) - 用户组角色关联表，一个用户组可以拥有多个角色",
        func=mems_api.add_auth_user_groups,
        parameters=[
            {'name': 'data', 'type': 'array[UserGroup]', 'required': True, 'description': '请求体数据；字段：data (array[UserGroup]) - 用户组；data[].id (integer, 必填) - 用户组ID；data[].name (string, 必填) - 用户组名称；data[].user_group2role (array[integer], 必填) - 用户组角色关联表，一个用户组可以拥有多个角色', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'id', 'type': 'integer', 'required': True, 'description': '用户组ID'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '用户组名称'}, {'name': 'user_group2role', 'type': 'array[integer]', 'required': True, 'description': '用户组角色关联表，一个用户组可以拥有多个角色'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_auth_user_groups_by_s",
        description="删除指定id的用户组。参数：ids (string, 必填) - 用户组id列表，以,间隔",
        func=mems_api.delete_auth_user_groups_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '用户组id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_user_groups_by",
        description="查询指定id用户组。参数：id (integer, 必填) - 用户组id",
        func=mems_api.get_auth_user_groups_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '用户组id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_users",
        description="查询所有用户",
        func=mems_api.get_auth_users,
    ))

    tools.append(ToolInfo(
        name="update_auth_users",
        description="修改用户。参数：data (object) - 请求体数据，字段：data.password (array[integer], 必填) - 加密后的用户密码；data.password_update_time (integer, 必填) - 最近一次密码修改时间；data.pub_info (object, 必填) - 用户 - 公开信息；data.pub_info.desc (string, 可选) - 描述；data.pub_info.email (string, 可选) - 用户的邮箱；data.pub_info.expiration_time (integer, 可选) - 过期时间；data.pub_info.id (integer, 必填) - 用户ID；data.pub_info.name (string, 必填) - 用户名称；data.pub_info.phone_number (string, 可选) - 用户的手机号；data.pub_info.special_role (array[integer], 必填) - 特别分配的角色；data.pub_info.user_group (integer, 必填) - 所属用户组的id（用户与用户组关联表，一个用户只能属于一个用户组）",
        func=mems_api.update_auth_users,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.password (array[integer], 必填) - 加密后的用户密码；data.password_update_time (integer, 必填) - 最近一次密码修改时间；data.pub_info (object, 必填) - 用户 - 公开信息；data.pub_info.desc (string, 可选) - 描述；data.pub_info.email (string, 可选) - 用户的邮箱；data.pub_info.expiration_time (integer, 可选) - 过期时间；data.pub_info.id (integer, 必填) - 用户ID；data.pub_info.name (string, 必填) - 用户名称；data.pub_info.phone_number (string, 可选) - 用户的手机号；data.pub_info.special_role (array[integer], 必填) - 特别分配的角色；data.pub_info.user_group (integer, 必填) - 所属用户组的id（用户与用户组关联表，一个用户只能属于一个用户组）', 'children': [{'name': 'password', 'type': 'array[integer]', 'required': True, 'description': '加密后的用户密码'}, {'name': 'password_update_time', 'type': 'integer', 'required': True, 'description': '最近一次密码修改时间'}, {'name': 'pub_info', 'type': 'object', 'required': True, 'description': '用户 - 公开信息', 'children': [{'name': 'desc', 'type': 'string', 'required': False, 'description': '描述'}, {'name': 'email', 'type': 'string', 'required': False, 'description': '用户的邮箱'}, {'name': 'expiration_time', 'type': 'integer', 'required': False, 'description': '过期时间'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '用户ID'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '用户名称'}, {'name': 'phone_number', 'type': 'string', 'required': False, 'description': '用户的手机号'}, {'name': 'special_role', 'type': 'array[integer]', 'required': True, 'description': '特别分配的角色'}, {'name': 'user_group', 'type': 'integer', 'required': True, 'description': '所属用户组的id（用户与用户组关联表，一个用户只能属于一个用户组）'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_auth_users",
        description="新增用户。参数：data (object) - 请求体数据，字段：data.password (array[integer], 必填) - 加密后的用户密码；data.password_update_time (integer, 必填) - 最近一次密码修改时间；data.pub_info (object, 必填) - 用户 - 公开信息；data.pub_info.desc (string, 可选) - 描述；data.pub_info.email (string, 可选) - 用户的邮箱；data.pub_info.expiration_time (integer, 可选) - 过期时间；data.pub_info.id (integer, 必填) - 用户ID；data.pub_info.name (string, 必填) - 用户名称；data.pub_info.phone_number (string, 可选) - 用户的手机号；data.pub_info.special_role (array[integer], 必填) - 特别分配的角色；data.pub_info.user_group (integer, 必填) - 所属用户组的id（用户与用户组关联表，一个用户只能属于一个用户组）",
        func=mems_api.add_auth_users,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.password (array[integer], 必填) - 加密后的用户密码；data.password_update_time (integer, 必填) - 最近一次密码修改时间；data.pub_info (object, 必填) - 用户 - 公开信息；data.pub_info.desc (string, 可选) - 描述；data.pub_info.email (string, 可选) - 用户的邮箱；data.pub_info.expiration_time (integer, 可选) - 过期时间；data.pub_info.id (integer, 必填) - 用户ID；data.pub_info.name (string, 必填) - 用户名称；data.pub_info.phone_number (string, 可选) - 用户的手机号；data.pub_info.special_role (array[integer], 必填) - 特别分配的角色；data.pub_info.user_group (integer, 必填) - 所属用户组的id（用户与用户组关联表，一个用户只能属于一个用户组）', 'children': [{'name': 'password', 'type': 'array[integer]', 'required': True, 'description': '加密后的用户密码'}, {'name': 'password_update_time', 'type': 'integer', 'required': True, 'description': '最近一次密码修改时间'}, {'name': 'pub_info', 'type': 'object', 'required': True, 'description': '用户 - 公开信息', 'children': [{'name': 'desc', 'type': 'string', 'required': False, 'description': '描述'}, {'name': 'email', 'type': 'string', 'required': False, 'description': '用户的邮箱'}, {'name': 'expiration_time', 'type': 'integer', 'required': False, 'description': '过期时间'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '用户ID'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '用户名称'}, {'name': 'phone_number', 'type': 'string', 'required': False, 'description': '用户的手机号'}, {'name': 'special_role', 'type': 'array[integer]', 'required': True, 'description': '特别分配的角色'}, {'name': 'user_group', 'type': 'integer', 'required': True, 'description': '所属用户组的id（用户与用户组关联表，一个用户只能属于一个用户组）'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_users_by_user_group",
        description="根据分组id查询用户信息。参数：id (integer, 必填) - 分组id",
        func=mems_api.get_auth_users_by_user_group,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '分组id'},
        ]
    ))

    tools.append(ToolInfo(
        name="update_auth_users_password_by",
        description="更改用户密码。参数：id (integer, 必填) - 用户id, data (array[any]) - 请求体数据，字段：data (array[any])",
        func=mems_api.update_auth_users_password_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '用户id'},
            {'name': 'data', 'type': 'array[any]', 'required': True, 'description': '请求体数据；字段：data (array[any])'},
        ]
    ))

    tools.append(ToolInfo(
        name="update_auth_users_reset_password_by",
        description="重置用户密码。参数：id (integer, 必填) - 用户id",
        func=mems_api.update_auth_users_reset_password_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '用户id'},
        ]
    ))

    tools.append(ToolInfo(
        name="update_auth_users_roles_by",
        description="绑定已有用户的角色信息。参数：id (integer, 必填) - 用户id, data (array[integer]) - 请求体数据，字段：data (array[integer])",
        func=mems_api.update_auth_users_roles_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '用户id'},
            {'name': 'data', 'type': 'array[integer]', 'required': True, 'description': '请求体数据；字段：data (array[integer])'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_auth_users_by_s",
        description="删除指定id的用户。参数：ids (string, 必填) - 用户id列表，以,间隔",
        func=mems_api.delete_auth_users_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '用户id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_users_by",
        description="查询指定id用户。参数：id (integer, 必填) - 用户id",
        func=mems_api.get_auth_users_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '用户id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_commands",
        description="查询历史设点执行结果。参数：sender_id (integer, 可选) - , point_id (integer, 可选) - 测点id, start (integer, 可选) - 开始时间, end (integer, 可选) - 结束时间, date (string, 可选) - 时间字符串，yyyy-MM-dd, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_commands,
        parameters=[
            {'name': 'sender_id', 'type': 'integer', 'required': False, 'description': ''},
            {'name': 'point_id', 'type': 'integer', 'required': False, 'description': '测点id'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_common_map",
        description="执行map映射操作。参数：data (object) - 请求体数据，字段：data.Query (array[integer], 必填) - 查询",
        func=mems_api.add_common_map,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.Query (array[integer], 必填) - 查询', 'children': [{'name': 'Query', 'type': 'array[integer]', 'required': True, 'description': '查询'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_config",
        description="查询Eig配置",
        func=mems_api.get_config,
    ))

    tools.append(ToolInfo(
        name="add_config",
        description="保存Eig配置。参数：data (object) - 请求体数据，字段：data.properties (object, 必填) - 主要配置属性；data.properties2 (object, 必填) - 次要配置属性",
        func=mems_api.add_config,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.properties (object, 必填) - 主要配置属性；data.properties2 (object, 必填) - 次要配置属性', 'children': [{'name': 'properties', 'type': 'object', 'required': True, 'description': '主要配置属性'}, {'name': 'properties2', 'type': 'object', 'required': True, 'description': '次要配置属性'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_controls_aoes",
        description="对指定id的AOE采取指定动作，启动/停止/更新。参数：data (object) - 请求体数据，字段：data.AoeActions (array[AoeAction], 必填) - AOE指令列表；data.AoeActions[].StartAoe (integer, 必填) - 开始AOE",
        func=mems_api.add_controls_aoes,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.AoeActions (array[AoeAction], 必填) - AOE指令列表；data.AoeActions[].StartAoe (integer, 必填) - 开始AOE', 'children': [{'name': 'AoeActions', 'type': 'array[AoeAction]', 'required': True, 'description': 'AOE指令列表', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': 'AOE指令列表', 'children': [{'name': 'StartAoe', 'type': 'integer', 'required': True, 'description': '开始AOE'}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_controls_points",
        description="执行测点控制。参数：data (object) - 请求体数据，字段：data.analogs (array[SetFloatValue], 必填)；data.analogs[].point_id (integer, 必填)；data.analogs[].sender_id (integer, 必填)；data.analogs[].timestamp (integer, 必填)；data.analogs[].yt_command (number, 必填)；data.discretes (array[SetIntValue], 必填)；data.discretes[].point_id (integer, 必填)；data.discretes[].sender_id (integer, 必填)；data.discretes[].timestamp (integer, 必填)；data.discretes[].yk_command (integer, 必填)",
        func=mems_api.add_controls_points,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.analogs (array[SetFloatValue], 必填)；data.analogs[].point_id (integer, 必填)；data.analogs[].sender_id (integer, 必填)；data.analogs[].timestamp (integer, 必填)；data.analogs[].yt_command (number, 必填)；data.discretes (array[SetIntValue], 必填)；data.discretes[].point_id (integer, 必填)；data.discretes[].sender_id (integer, 必填)；data.discretes[].timestamp (integer, 必填)；data.discretes[].yk_command (integer, 必填)', 'children': [{'name': 'analogs', 'type': 'array[SetFloatValue]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'point_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'sender_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'timestamp', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'yt_command', 'type': 'number', 'required': True, 'description': ''}]}]}, {'name': 'discretes', 'type': 'array[SetIntValue]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'point_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'sender_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'timestamp', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'yk_command', 'type': 'integer', 'required': True, 'description': ''}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_controls_points_by_alias",
        description="执行测点控制（通过别名）。参数：data (object) - 请求体数据，字段：data.analogs (array[SetFloatValue2], 必填)；data.analogs[].point_alias (string, 必填)；data.analogs[].sender_id (integer, 必填)；data.analogs[].timestamp (integer, 必填)；data.analogs[].yt_command (number, 必填)；data.discretes (array[SetIntValue2], 必填)；data.discretes[].point_alias (string, 必填)；data.discretes[].sender_id (integer, 必填)；data.discretes[].timestamp (integer, 必填)；data.discretes[].yk_command (integer, 必填)",
        func=mems_api.add_controls_points_by_alias,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.analogs (array[SetFloatValue2], 必填)；data.analogs[].point_alias (string, 必填)；data.analogs[].sender_id (integer, 必填)；data.analogs[].timestamp (integer, 必填)；data.analogs[].yt_command (number, 必填)；data.discretes (array[SetIntValue2], 必填)；data.discretes[].point_alias (string, 必填)；data.discretes[].sender_id (integer, 必填)；data.discretes[].timestamp (integer, 必填)；data.discretes[].yk_command (integer, 必填)', 'children': [{'name': 'analogs', 'type': 'array[SetFloatValue2]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'point_alias', 'type': 'string', 'required': True, 'description': ''}, {'name': 'sender_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'timestamp', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'yt_command', 'type': 'number', 'required': True, 'description': ''}]}]}, {'name': 'discretes', 'type': 'array[SetIntValue2]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'point_alias', 'type': 'string', 'required': True, 'description': ''}, {'name': 'sender_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'timestamp', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'yk_command', 'type': 'integer', 'required': True, 'description': ''}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_controls_points_by_expr",
        description="执行测点控制（通过公式）。参数：data (object) - 请求体数据，字段：data.commands (array[SetPointValue], 必填)；data.commands[].command (object, 必填) - 表达式对象；data.commands[].command.rpn (array[Token], 必填)；data.commands[].point_id (integer, 必填)；data.commands[].sender_id (integer, 必填)；data.commands[].timestamp (integer, 必填)",
        func=mems_api.add_controls_points_by_expr,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.commands (array[SetPointValue], 必填)；data.commands[].command (object, 必填) - 表达式对象；data.commands[].command.rpn (array[Token], 必填)；data.commands[].point_id (integer, 必填)；data.commands[].sender_id (integer, 必填)；data.commands[].timestamp (integer, 必填)', 'children': [{'name': 'commands', 'type': 'array[SetPointValue]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'command', 'type': 'object', 'required': True, 'description': '表达式对象', 'children': [{'name': 'rpn', 'type': 'array[Token]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'Binary', 'type': 'string', 'required': True, 'description': 'Mathematical operations.'}]}]}]}, {'name': 'point_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'sender_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'timestamp', 'type': 'integer', 'required': True, 'description': ''}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_controls_points_with_source_by_source",
        description="执行测点控制（通过其他数据源）。参数：source (integer, 必填) - 数据源id, data (array[MeasureValue]) - 请求体数据，字段：data (array[MeasureValue])；data[].analog_value (number, 必填) - 模拟量值；data[].discrete_value (integer, 必填) - 离散量值；data[].is_discrete (boolean, 必填) - 是否离散量；data[].is_transformed (boolean, 必填) - 是否已经变换；data[].point_id (integer, 必填) - 对应的测点；data[].timestamp (integer, 必填) - 时间戳；data[].transformed_analog (number, 必填) - 变换后的模拟量值；data[].transformed_discrete (integer, 必填) - 变换后的离散量值",
        func=mems_api.add_controls_points_with_source_by_source,
        parameters=[
            {'name': 'source', 'type': 'integer', 'required': True, 'description': '数据源id'},
            {'name': 'data', 'type': 'array[MeasureValue]', 'required': True, 'description': '请求体数据；字段：data (array[MeasureValue])；data[].analog_value (number, 必填) - 模拟量值；data[].discrete_value (integer, 必填) - 离散量值；data[].is_discrete (boolean, 必填) - 是否离散量；data[].is_transformed (boolean, 必填) - 是否已经变换；data[].point_id (integer, 必填) - 对应的测点；data[].timestamp (integer, 必填) - 时间戳；data[].transformed_analog (number, 必填) - 变换后的模拟量值；data[].transformed_discrete (integer, 必填) - 变换后的离散量值', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'analog_value', 'type': 'number', 'required': True, 'description': '模拟量值'}, {'name': 'discrete_value', 'type': 'integer', 'required': True, 'description': '离散量值'}, {'name': 'is_discrete', 'type': 'boolean', 'required': True, 'description': '是否离散量'}, {'name': 'is_transformed', 'type': 'boolean', 'required': True, 'description': '是否已经变换'}, {'name': 'point_id', 'type': 'integer', 'required': True, 'description': '对应的测点'}, {'name': 'timestamp', 'type': 'integer', 'required': True, 'description': '时间戳'}, {'name': 'transformed_analog', 'type': 'number', 'required': True, 'description': '变换后的模拟量值'}, {'name': 'transformed_discrete', 'type': 'integer', 'required': True, 'description': '变换后的离散量值'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_cns",
        description="查询拓扑。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_cns,
        parameters=[
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_cns",
        description="新增拓扑。参数：data (array[CN]) - 请求体数据，字段：data (array[CN]) - 连接节点；data[].id (integer, 必填) - 连接节点id；data[].psr_id (string, 必填) - 资源id；data[].terminals (array[integer], 必填) - 端子id数组",
        func=mems_api.add_devices_cns,
        parameters=[
            {'name': 'data', 'type': 'array[CN]', 'required': True, 'description': '请求体数据；字段：data (array[CN]) - 连接节点；data[].id (integer, 必填) - 连接节点id；data[].psr_id (string, 必填) - 资源id；data[].terminals (array[integer], 必填) - 端子id数组', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'id', 'type': 'integer', 'required': True, 'description': '连接节点id'}, {'name': 'psr_id', 'type': 'string', 'required': True, 'description': '资源id'}, {'name': 'terminals', 'type': 'array[integer]', 'required': True, 'description': '端子id数组'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_defines",
        description="查询所有设备定义",
        func=mems_api.get_devices_defines,
    ))

    tools.append(ToolInfo(
        name="update_devices_defines",
        description="修改设备定义。参数：data (object) - 请求体数据，字段：data.desc (string, 必填) - 设备定义的描述；data.id (integer, 必填) - 定义id；data.name (string, 必填) - 设备类别名称；data.prop_groups (array[PropGroupDefine], 必填) - 设备属性；data.prop_groups[].desc (string, 必填) - 属性定义描述；data.prop_groups[].name (string, 必填) - 属性定义标识；data.prop_groups[].prop_defines (array[integer], 必填) - 设备属性实际描述；data.rsr_type (string, 必填) - 电力设备类型；data.terminal_num (integer, 必填) - 端口数量",
        func=mems_api.update_devices_defines,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.desc (string, 必填) - 设备定义的描述；data.id (integer, 必填) - 定义id；data.name (string, 必填) - 设备类别名称；data.prop_groups (array[PropGroupDefine], 必填) - 设备属性；data.prop_groups[].desc (string, 必填) - 属性定义描述；data.prop_groups[].name (string, 必填) - 属性定义标识；data.prop_groups[].prop_defines (array[integer], 必填) - 设备属性实际描述；data.rsr_type (string, 必填) - 电力设备类型；data.terminal_num (integer, 必填) - 端口数量', 'children': [{'name': 'desc', 'type': 'string', 'required': True, 'description': '设备定义的描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '定义id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '设备类别名称'}, {'name': 'prop_groups', 'type': 'array[PropGroupDefine]', 'required': True, 'description': '设备属性', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '设备属性', 'children': [{'name': 'desc', 'type': 'string', 'required': True, 'description': '属性定义描述'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '属性定义标识'}, {'name': 'prop_defines', 'type': 'array[integer]', 'required': True, 'description': '设备属性实际描述'}]}]}, {'name': 'rsr_type', 'type': 'string', 'required': True, 'description': '电力设备类型'}, {'name': 'terminal_num', 'type': 'integer', 'required': True, 'description': '端口数量'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_defines",
        description="新增设备定义。参数：data (array[RsrDefine]) - 请求体数据，字段：data (array[RsrDefine]) - 设备定义；data[].desc (string, 必填) - 设备定义的描述；data[].id (integer, 必填) - 定义id；data[].name (string, 必填) - 设备类别名称；data[].prop_groups (array[PropGroupDefine], 必填) - 设备属性；data[].prop_groups[].desc (string, 必填) - 属性定义描述；data[].prop_groups[].name (string, 必填) - 属性定义标识；data[].prop_groups[].prop_defines (array[integer], 必填) - 设备属性实际描述；data[].rsr_type (string, 必填) - 电力设备类型；data[].terminal_num (integer, 必填) - 端口数量",
        func=mems_api.add_devices_defines,
        parameters=[
            {'name': 'data', 'type': 'array[RsrDefine]', 'required': True, 'description': '请求体数据；字段：data (array[RsrDefine]) - 设备定义；data[].desc (string, 必填) - 设备定义的描述；data[].id (integer, 必填) - 定义id；data[].name (string, 必填) - 设备类别名称；data[].prop_groups (array[PropGroupDefine], 必填) - 设备属性；data[].prop_groups[].desc (string, 必填) - 属性定义描述；data[].prop_groups[].name (string, 必填) - 属性定义标识；data[].prop_groups[].prop_defines (array[integer], 必填) - 设备属性实际描述；data[].rsr_type (string, 必填) - 电力设备类型；data[].terminal_num (integer, 必填) - 端口数量', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'desc', 'type': 'string', 'required': True, 'description': '设备定义的描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '定义id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '设备类别名称'}, {'name': 'prop_groups', 'type': 'array[PropGroupDefine]', 'required': True, 'description': '设备属性', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '设备属性', 'children': [{'name': 'desc', 'type': 'string', 'required': True, 'description': '属性定义描述'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '属性定义标识'}, {'name': 'prop_defines', 'type': 'array[integer]', 'required': True, 'description': '设备属性实际描述'}]}]}, {'name': 'rsr_type', 'type': 'string', 'required': True, 'description': '电力设备类型'}, {'name': 'terminal_num', 'type': 'integer', 'required': True, 'description': '端口数量'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_defines_by_s",
        description="删除指定id的设备定义。参数：ids (string, 必填) - 设备定义id列表，以,间隔",
        func=mems_api.delete_devices_defines_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '设备定义id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_defines_by",
        description="根据id查询对应的设备定义。参数：id (integer, 必填) - 设备定义id",
        func=mems_api.get_devices_defines_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '设备定义id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_devs",
        description="查询所有设备列表。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_devs,
        parameters=[
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="update_devices_devs",
        description="修改设备。参数：data (object) - 请求体数据，字段：data.container_id (integer, 可选)；data.define_id (integer, 必填) - 设备定义id；data.desc (string, 必填) - 设备描述；data.id (integer, 必填) - 设备id；data.name (string, 必填) - 设备名称；data.prop_group_ids (array[integer], 必填) - 设备属性分组id列表；data.terminals (array[Terminal], 必填) - 设备的端口；data.terminals[].device (integer, 必填) - 设备id；data.terminals[].id (integer, 必填) - 端口id",
        func=mems_api.update_devices_devs,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.container_id (integer, 可选)；data.define_id (integer, 必填) - 设备定义id；data.desc (string, 必填) - 设备描述；data.id (integer, 必填) - 设备id；data.name (string, 必填) - 设备名称；data.prop_group_ids (array[integer], 必填) - 设备属性分组id列表；data.terminals (array[Terminal], 必填) - 设备的端口；data.terminals[].device (integer, 必填) - 设备id；data.terminals[].id (integer, 必填) - 端口id', 'children': [{'name': 'container_id', 'type': 'integer', 'required': False, 'description': ''}, {'name': 'define_id', 'type': 'integer', 'required': True, 'description': '设备定义id'}, {'name': 'desc', 'type': 'string', 'required': True, 'description': '设备描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '设备id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '设备名称'}, {'name': 'prop_group_ids', 'type': 'array[integer]', 'required': True, 'description': '设备属性分组id列表'}, {'name': 'terminals', 'type': 'array[Terminal]', 'required': True, 'description': '设备的端口', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '设备的端口', 'children': [{'name': 'device', 'type': 'integer', 'required': True, 'description': '设备id'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '端口id'}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_devs",
        description="新增设备。参数：data (array[NetworkRsr]) - 请求体数据，字段：data (array[NetworkRsr]) - 设备对象；data[].container_id (integer, 可选)；data[].define_id (integer, 必填) - 设备定义id；data[].desc (string, 必填) - 设备描述；data[].id (integer, 必填) - 设备id；data[].name (string, 必填) - 设备名称；data[].prop_group_ids (array[integer], 必填) - 设备属性分组id列表；data[].terminals (array[Terminal], 必填) - 设备的端口；data[].terminals[].device (integer, 必填) - 设备id；data[].terminals[].id (integer, 必填) - 端口id",
        func=mems_api.add_devices_devs,
        parameters=[
            {'name': 'data', 'type': 'array[NetworkRsr]', 'required': True, 'description': '请求体数据；字段：data (array[NetworkRsr]) - 设备对象；data[].container_id (integer, 可选)；data[].define_id (integer, 必填) - 设备定义id；data[].desc (string, 必填) - 设备描述；data[].id (integer, 必填) - 设备id；data[].name (string, 必填) - 设备名称；data[].prop_group_ids (array[integer], 必填) - 设备属性分组id列表；data[].terminals (array[Terminal], 必填) - 设备的端口；data[].terminals[].device (integer, 必填) - 设备id；data[].terminals[].id (integer, 必填) - 端口id', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'container_id', 'type': 'integer', 'required': False, 'description': ''}, {'name': 'define_id', 'type': 'integer', 'required': True, 'description': '设备定义id'}, {'name': 'desc', 'type': 'string', 'required': True, 'description': '设备描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '设备id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '设备名称'}, {'name': 'prop_group_ids', 'type': 'array[integer]', 'required': True, 'description': '设备属性分组id列表'}, {'name': 'terminals', 'type': 'array[Terminal]', 'required': True, 'description': '设备的端口', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '设备的端口', 'children': [{'name': 'device', 'type': 'integer', 'required': True, 'description': '设备id'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '端口id'}]}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_devs_by_s",
        description="删除指定id的设备。参数：ids (string, 必填) - 设备id列表，以,间隔",
        func=mems_api.delete_devices_devs_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '设备id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_devs_by",
        description="根据ID查询设备对象。参数：id (integer, 必填) - 设备id, version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_devs_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '设备id'},
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_islands",
        description="查询电气岛。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_islands,
        parameters=[
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_islands",
        description="根据版本号apply电气岛。参数：data (integer) - 请求体数据，字段：data (integer)",
        func=mems_api.add_devices_islands,
        parameters=[
            {'name': 'data', 'type': 'integer', 'required': True, 'description': '请求体数据；字段：data (integer)'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_measure_defs",
        description="查询设备测点。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_measure_defs,
        parameters=[
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="update_devices_measure_defs",
        description="修改设备测点。参数：data (array[MeasureDef]) - 请求体数据，字段：data (array[MeasureDef]) - 测点定义；data[].dev_id (integer, 必填)；data[].id (integer, 必填)；data[].phase (string, 必填) - 量测相位；data[].point_id (integer, 必填)；data[].terminal_id (integer, 必填)",
        func=mems_api.update_devices_measure_defs,
        parameters=[
            {'name': 'data', 'type': 'array[MeasureDef]', 'required': True, 'description': '请求体数据；字段：data (array[MeasureDef]) - 测点定义；data[].dev_id (integer, 必填)；data[].id (integer, 必填)；data[].phase (string, 必填) - 量测相位；data[].point_id (integer, 必填)；data[].terminal_id (integer, 必填)', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'dev_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'phase', 'type': 'string', 'required': True, 'description': '量测相位'}, {'name': 'point_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'terminal_id', 'type': 'integer', 'required': True, 'description': ''}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_measure_defs",
        description="新增设备测点。参数：data (array[MeasureDef]) - 请求体数据，字段：data (array[MeasureDef]) - 测点定义；data[].dev_id (integer, 必填)；data[].id (integer, 必填)；data[].phase (string, 必填) - 量测相位；data[].point_id (integer, 必填)；data[].terminal_id (integer, 必填)",
        func=mems_api.add_devices_measure_defs,
        parameters=[
            {'name': 'data', 'type': 'array[MeasureDef]', 'required': True, 'description': '请求体数据；字段：data (array[MeasureDef]) - 测点定义；data[].dev_id (integer, 必填)；data[].id (integer, 必填)；data[].phase (string, 必填) - 量测相位；data[].point_id (integer, 必填)；data[].terminal_id (integer, 必填)', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'dev_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'phase', 'type': 'string', 'required': True, 'description': '量测相位'}, {'name': 'point_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'terminal_id', 'type': 'integer', 'required': True, 'description': ''}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_measure_defs",
        description="删除指定id的设备测点。参数：data (array[integer]) - 请求体数据，字段：data (array[integer])",
        func=mems_api.delete_devices_measure_defs,
        parameters=[
            {'name': 'data', 'type': 'array[integer]', 'required': True, 'description': '请求体数据；字段：data (array[integer])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_point_tree",
        description="查询测点树（测点在设备树中的路径）。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_point_tree,
        parameters=[
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_prop_defines",
        description="查询所有设备属性定义",
        func=mems_api.get_devices_prop_defines,
    ))

    tools.append(ToolInfo(
        name="update_devices_prop_defines",
        description="修改设备属性定义。参数：data (object) - 请求体数据，字段：data.data_type (string, 必填) - 属性类型；data.data_unit (string, 必填) - 数据单位；data.desc (string, 必填) - 属性定义描述；data.id (integer, 必填) - 属性定义id；data.name (string, 必填) - 属性定义标识",
        func=mems_api.update_devices_prop_defines,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.data_type (string, 必填) - 属性类型；data.data_unit (string, 必填) - 数据单位；data.desc (string, 必填) - 属性定义描述；data.id (integer, 必填) - 属性定义id；data.name (string, 必填) - 属性定义标识', 'children': [{'name': 'data_type', 'type': 'string', 'required': True, 'description': '属性类型'}, {'name': 'data_unit', 'type': 'string', 'required': True, 'description': '数据单位'}, {'name': 'desc', 'type': 'string', 'required': True, 'description': '属性定义描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '属性定义id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '属性定义标识'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_prop_defines",
        description="新增设备属性定义。参数：data (array[PropDefine]) - 请求体数据，字段：data (array[PropDefine]) - 设备属性；data[].data_type (string, 必填) - 属性类型；data[].data_unit (string, 必填) - 数据单位；data[].desc (string, 必填) - 属性定义描述；data[].id (integer, 必填) - 属性定义id；data[].name (string, 必填) - 属性定义标识",
        func=mems_api.add_devices_prop_defines,
        parameters=[
            {'name': 'data', 'type': 'array[PropDefine]', 'required': True, 'description': '请求体数据；字段：data (array[PropDefine]) - 设备属性；data[].data_type (string, 必填) - 属性类型；data[].data_unit (string, 必填) - 数据单位；data[].desc (string, 必填) - 属性定义描述；data[].id (integer, 必填) - 属性定义id；data[].name (string, 必填) - 属性定义标识', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'data_type', 'type': 'string', 'required': True, 'description': '属性类型'}, {'name': 'data_unit', 'type': 'string', 'required': True, 'description': '数据单位'}, {'name': 'desc', 'type': 'string', 'required': True, 'description': '属性定义描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '属性定义id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '属性定义标识'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_prop_defines_by_s",
        description="删除指定id的设备属性定义。参数：ids (string, 必填) - 设备属性定义id列表，以,间隔",
        func=mems_api.delete_devices_prop_defines_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '设备属性定义id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_prop_groups",
        description="查询所有设备属性分组。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_prop_groups,
        parameters=[
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="update_devices_prop_groups",
        description="修改设备属性分组。参数：data (array[RsrPropGroup]) - 请求体数据，字段：data (array[RsrPropGroup]) - 设备属性分组；data[].defines (array[integer], 必填) - 设备属性定义列表；data[].id (integer, 必填)；data[].name (string, 必填) - 分组名称，用于显示，以及匹配PropGroupDefine；data[].props (array[PropValue], 必填) - 设备属性实际描述；data[].props[].U8 (integer, 必填)；data[].rsr_id (integer, 必填) - resource id",
        func=mems_api.update_devices_prop_groups,
        parameters=[
            {'name': 'data', 'type': 'array[RsrPropGroup]', 'required': True, 'description': '请求体数据；字段：data (array[RsrPropGroup]) - 设备属性分组；data[].defines (array[integer], 必填) - 设备属性定义列表；data[].id (integer, 必填)；data[].name (string, 必填) - 分组名称，用于显示，以及匹配PropGroupDefine；data[].props (array[PropValue], 必填) - 设备属性实际描述；data[].props[].U8 (integer, 必填)；data[].rsr_id (integer, 必填) - resource id', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'defines', 'type': 'array[integer]', 'required': True, 'description': '设备属性定义列表'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'name', 'type': 'string', 'required': True, 'description': '分组名称，用于显示，以及匹配PropGroupDefine'}, {'name': 'props', 'type': 'array[PropValue]', 'required': True, 'description': '设备属性实际描述', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '设备属性实际描述', 'children': [{'name': 'U8', 'type': 'integer', 'required': True, 'description': ''}]}]}, {'name': 'rsr_id', 'type': 'integer', 'required': True, 'description': 'resource id'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_prop_groups",
        description="新增设备属性分组。参数：data (array[RsrPropGroup]) - 请求体数据，字段：data (array[RsrPropGroup]) - 设备属性分组；data[].defines (array[integer], 必填) - 设备属性定义列表；data[].id (integer, 必填)；data[].name (string, 必填) - 分组名称，用于显示，以及匹配PropGroupDefine；data[].props (array[PropValue], 必填) - 设备属性实际描述；data[].props[].U8 (integer, 必填)；data[].rsr_id (integer, 必填) - resource id",
        func=mems_api.add_devices_prop_groups,
        parameters=[
            {'name': 'data', 'type': 'array[RsrPropGroup]', 'required': True, 'description': '请求体数据；字段：data (array[RsrPropGroup]) - 设备属性分组；data[].defines (array[integer], 必填) - 设备属性定义列表；data[].id (integer, 必填)；data[].name (string, 必填) - 分组名称，用于显示，以及匹配PropGroupDefine；data[].props (array[PropValue], 必填) - 设备属性实际描述；data[].props[].U8 (integer, 必填)；data[].rsr_id (integer, 必填) - resource id', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'defines', 'type': 'array[integer]', 'required': True, 'description': '设备属性定义列表'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'name', 'type': 'string', 'required': True, 'description': '分组名称，用于显示，以及匹配PropGroupDefine'}, {'name': 'props', 'type': 'array[PropValue]', 'required': True, 'description': '设备属性实际描述', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '设备属性实际描述', 'children': [{'name': 'U8', 'type': 'integer', 'required': True, 'description': ''}]}]}, {'name': 'rsr_id', 'type': 'integer', 'required': True, 'description': 'resource id'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_prop_groups_by_s",
        description="根据id列表查看设备属性分组列表。参数：ids (string, 必填) - 设备属性分组id列表，以,间隔, version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_prop_groups_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '设备属性分组id列表，以,间隔'},
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_prop_groups_by_s",
        description="删除指定id的设备属性分组。参数：ids (string, 必填) - 设备属性分组id列表，以,间隔",
        func=mems_api.delete_devices_prop_groups_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '设备属性分组id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_resources_clear",
        description="清空资源",
        func=mems_api.delete_devices_resources_clear,
    ))

    tools.append(ToolInfo(
        name="get_devices_version",
        description="查询电气岛所有版本",
        func=mems_api.get_devices_version,
    ))

    tools.append(ToolInfo(
        name="add_devices_version",
        description="新增电气岛版本。参数：data (object) - 请求体数据，字段：data.note (string, 必填) - 提交时的注释；data.tree_id (string, 必填) - 对应的tree_id；data.version (integer, 必填) - 版本号",
        func=mems_api.add_devices_version,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.note (string, 必填) - 提交时的注释；data.tree_id (string, 必填) - 对应的tree_id；data.version (integer, 必填) - 版本号', 'children': [{'name': 'note', 'type': 'string', 'required': True, 'description': '提交时的注释'}, {'name': 'tree_id', 'type': 'string', 'required': True, 'description': '对应的tree_id'}, {'name': 'version', 'type': 'integer', 'required': True, 'description': '版本号'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_version_by",
        description="删除指定id的电气岛版本。参数：id (integer, 必填) - 版本id",
        func=mems_api.delete_devices_version_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '版本id'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_ems_request_by_ems",
        description="对指定id的ems执行请求。参数：ems_id (string, 必填) - ems_id, data (object) - 请求体数据，字段：data.content (string, 可选)；data.function (string, 可选)；data.header_keys (array[string], 必填)；data.header_values (array[string], 必填)；data.id (integer, 可选)；data.url (string, 可选)",
        func=mems_api.add_ems_request_by_ems,
        parameters=[
            {'name': 'ems_id', 'type': 'string', 'required': True, 'description': 'ems_id'},
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.content (string, 可选)；data.function (string, 可选)；data.header_keys (array[string], 必填)；data.header_values (array[string], 必填)；data.id (integer, 可选)；data.url (string, 可选)', 'children': [{'name': 'content', 'type': 'string', 'required': False, 'description': ''}, {'name': 'function', 'type': 'string', 'required': False, 'description': ''}, {'name': 'header_keys', 'type': 'array[string]', 'required': True, 'description': ''}, {'name': 'header_values', 'type': 'array[string]', 'required': True, 'description': ''}, {'name': 'id', 'type': 'integer', 'required': False, 'description': ''}, {'name': 'url', 'type': 'string', 'required': False, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_ems_by",
        description="查询指定id的ems。参数：id (string, 必填) - ems_id",
        func=mems_api.get_ems_by,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': True, 'description': 'ems_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_ems_list",
        description="查询所有的ems",
        func=mems_api.get_ems_list,
    ))

    tools.append(ToolInfo(
        name="add_file_tree",
        description="执行filetree的操作。参数：data (object) - 请求体数据，字段：data.op (string, 必填) - 文件树的操作类型；data.op_paths (array[string], 必填)；data.path (string, 可选)；data.tree_id (string, 必填)；data.version (integer, 可选)",
        func=mems_api.add_file_tree,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.op (string, 必填) - 文件树的操作类型；data.op_paths (array[string], 必填)；data.path (string, 可选)；data.tree_id (string, 必填)；data.version (integer, 可选)', 'children': [{'name': 'op', 'type': 'string', 'required': True, 'description': '文件树的操作类型'}, {'name': 'op_paths', 'type': 'array[string]', 'required': True, 'description': ''}, {'name': 'path', 'type': 'string', 'required': False, 'description': ''}, {'name': 'tree_id', 'type': 'string', 'required': True, 'description': ''}, {'name': 'version', 'type': 'integer', 'required': False, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_file_tree_by",
        description="保存filetree的一个节点。参数：id (string, 必填) - tree_id, data (string) - 请求体数据，字段：data (string)",
        func=mems_api.add_file_tree_by,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': True, 'description': 'tree_id'},
            {'name': 'data', 'type': 'string', 'required': True, 'description': '请求体数据；字段：data (string)'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_file_tree_version",
        description="提交filetree版本。参数：data (object) - 请求体数据，字段：data.note (string, 必填) - 提交时的注释；data.tree_id (string, 必填) - 对应的tree_id；data.version (integer, 必填) - 版本号",
        func=mems_api.add_file_tree_version,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.note (string, 必填) - 提交时的注释；data.tree_id (string, 必填) - 对应的tree_id；data.version (integer, 必填) - 版本号', 'children': [{'name': 'note', 'type': 'string', 'required': True, 'description': '提交时的注释'}, {'name': 'tree_id', 'type': 'string', 'required': True, 'description': '对应的tree_id'}, {'name': 'version', 'type': 'integer', 'required': True, 'description': '版本号'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_brief_results",
        description="查询报表结果（简洁模式）。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_flows_brief_results,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_controls",
        description="执行报表动作。参数：data (string) - 请求体数据，字段：data (string) - 开始",
        func=mems_api.add_flows_controls,
        parameters=[
            {'name': 'data', 'type': 'string', 'required': True, 'description': '请求体数据；字段：data (string) - 开始'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_debug",
        description="报表节点测试。参数：data (array[any]) - 请求体数据，字段：data (array[any])",
        func=mems_api.add_flows_debug,
        parameters=[
            {'name': 'data', 'type': 'array[any]', 'required': True, 'description': '请求体数据；字段：data (array[any])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_models",
        description="查询报表。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_flows_models,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': False, 'description': '测点id（优先）'},
            {'name': 'ids', 'type': 'string', 'required': False, 'description': '测点id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="update_flows_models",
        description="修改报表。参数：data (array[DffModel]) - 请求体数据，字段：data (array[DffModel])；data[].actions (array[DfActionEdge], 必填) - 边；data[].actions[].action (object, 必填) - 对单个Dataframe进行运算；data[].actions[].desc (string, 必填)；data[].actions[].flow_id (integer, 必填)；data[].actions[].name (string, 必填)；data[].actions[].source_node (integer, 必填)；data[].actions[].target_node (integer, 必填)；data[].aoe_var (array[any], 可选) - destination of aoe variable；data[].id (integer, 必填) - dff id；data[].is_on (boolean, 必填) - should schedule；data[].name (string, 必填) - dff name；data[].nodes (array[DfNode], 必填) - 节点；data[].nodes[].flow_id (integer, 必填)；data[].nodes[].id (integer, 必填)；data[].nodes[].name (string, 必填)；data[].nodes[].node_type (object, 必填) - query data source；data[].save_mode (string, 必填) - Data frame save mode；data[].trigger_type (object, 必填) - Dataframe flow 启动的方式；data[].trigger_type.SimpleRepeat (object, 必填) - 时间对象",
        func=mems_api.update_flows_models,
        parameters=[
            {'name': 'data', 'type': 'array[DffModel]', 'required': True, 'description': '请求体数据；字段：data (array[DffModel])；data[].actions (array[DfActionEdge], 必填) - 边；data[].actions[].action (object, 必填) - 对单个Dataframe进行运算；data[].actions[].desc (string, 必填)；data[].actions[].flow_id (integer, 必填)；data[].actions[].name (string, 必填)；data[].actions[].source_node (integer, 必填)；data[].actions[].target_node (integer, 必填)；data[].aoe_var (array[any], 可选) - destination of aoe variable；data[].id (integer, 必填) - dff id；data[].is_on (boolean, 必填) - should schedule；data[].name (string, 必填) - dff name；data[].nodes (array[DfNode], 必填) - 节点；data[].nodes[].flow_id (integer, 必填)；data[].nodes[].id (integer, 必填)；data[].nodes[].name (string, 必填)；data[].nodes[].node_type (object, 必填) - query data source；data[].save_mode (string, 必填) - Data frame save mode；data[].trigger_type (object, 必填) - Dataframe flow 启动的方式；data[].trigger_type.SimpleRepeat (object, 必填) - 时间对象', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'actions', 'type': 'array[DfActionEdge]', 'required': True, 'description': '边', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '边', 'children': [{'name': 'action', 'type': 'object', 'required': True, 'description': '对单个Dataframe进行运算', 'children': [{'name': 'Eval', 'type': 'array[Expr]', 'required': True, 'description': '对单个Dataframe进行运算', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '对单个Dataframe进行运算', 'children': [{'name': 'rpn', 'type': 'array[Token]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'Binary', 'type': 'string', 'required': True, 'description': 'Mathematical operations.'}]}]}]}]}]}, {'name': 'desc', 'type': 'string', 'required': True, 'description': ''}, {'name': 'flow_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'name', 'type': 'string', 'required': True, 'description': ''}, {'name': 'source_node', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'target_node', 'type': 'integer', 'required': True, 'description': ''}]}]}, {'name': 'aoe_var', 'type': 'array[any]', 'required': False, 'description': 'destination of aoe variable'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': 'dff id'}, {'name': 'is_on', 'type': 'boolean', 'required': True, 'description': 'should schedule'}, {'name': 'name', 'type': 'string', 'required': True, 'description': 'dff name'}, {'name': 'nodes', 'type': 'array[DfNode]', 'required': True, 'description': '节点', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '节点', 'children': [{'name': 'flow_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'name', 'type': 'string', 'required': True, 'description': ''}, {'name': 'node_type', 'type': 'object', 'required': True, 'description': 'query data source', 'children': [{'name': 'Source', 'type': 'object', 'required': True, 'description': '直接导入数据', 'children': [{'name': 'Data', 'type': 'any', 'required': True, 'description': '直接导入数据'}]}]}]}]}, {'name': 'save_mode', 'type': 'string', 'required': True, 'description': 'Data frame save mode'}, {'name': 'trigger_type', 'type': 'object', 'required': True, 'description': 'Dataframe flow 启动的方式', 'children': [{'name': 'SimpleRepeat', 'type': 'object', 'required': True, 'description': '时间对象', 'children': [{'name': 'nanos', 'type': 'integer', 'required': True, 'description': '剩余纳秒'}, {'name': 'secs', 'type': 'integer', 'required': True, 'description': '秒'}]}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_models",
        description="新增报表。参数：data (array[DffModel]) - 请求体数据，字段：data (array[DffModel])；data[].actions (array[DfActionEdge], 必填) - 边；data[].actions[].action (object, 必填) - 对单个Dataframe进行运算；data[].actions[].desc (string, 必填)；data[].actions[].flow_id (integer, 必填)；data[].actions[].name (string, 必填)；data[].actions[].source_node (integer, 必填)；data[].actions[].target_node (integer, 必填)；data[].aoe_var (array[any], 可选) - destination of aoe variable；data[].id (integer, 必填) - dff id；data[].is_on (boolean, 必填) - should schedule；data[].name (string, 必填) - dff name；data[].nodes (array[DfNode], 必填) - 节点；data[].nodes[].flow_id (integer, 必填)；data[].nodes[].id (integer, 必填)；data[].nodes[].name (string, 必填)；data[].nodes[].node_type (object, 必填) - query data source；data[].save_mode (string, 必填) - Data frame save mode；data[].trigger_type (object, 必填) - Dataframe flow 启动的方式；data[].trigger_type.SimpleRepeat (object, 必填) - 时间对象",
        func=mems_api.add_flows_models,
        parameters=[
            {'name': 'data', 'type': 'array[DffModel]', 'required': True, 'description': '请求体数据；字段：data (array[DffModel])；data[].actions (array[DfActionEdge], 必填) - 边；data[].actions[].action (object, 必填) - 对单个Dataframe进行运算；data[].actions[].desc (string, 必填)；data[].actions[].flow_id (integer, 必填)；data[].actions[].name (string, 必填)；data[].actions[].source_node (integer, 必填)；data[].actions[].target_node (integer, 必填)；data[].aoe_var (array[any], 可选) - destination of aoe variable；data[].id (integer, 必填) - dff id；data[].is_on (boolean, 必填) - should schedule；data[].name (string, 必填) - dff name；data[].nodes (array[DfNode], 必填) - 节点；data[].nodes[].flow_id (integer, 必填)；data[].nodes[].id (integer, 必填)；data[].nodes[].name (string, 必填)；data[].nodes[].node_type (object, 必填) - query data source；data[].save_mode (string, 必填) - Data frame save mode；data[].trigger_type (object, 必填) - Dataframe flow 启动的方式；data[].trigger_type.SimpleRepeat (object, 必填) - 时间对象', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'actions', 'type': 'array[DfActionEdge]', 'required': True, 'description': '边', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '边', 'children': [{'name': 'action', 'type': 'object', 'required': True, 'description': '对单个Dataframe进行运算', 'children': [{'name': 'Eval', 'type': 'array[Expr]', 'required': True, 'description': '对单个Dataframe进行运算', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '对单个Dataframe进行运算', 'children': [{'name': 'rpn', 'type': 'array[Token]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'Binary', 'type': 'string', 'required': True, 'description': 'Mathematical operations.'}]}]}]}]}]}, {'name': 'desc', 'type': 'string', 'required': True, 'description': ''}, {'name': 'flow_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'name', 'type': 'string', 'required': True, 'description': ''}, {'name': 'source_node', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'target_node', 'type': 'integer', 'required': True, 'description': ''}]}]}, {'name': 'aoe_var', 'type': 'array[any]', 'required': False, 'description': 'destination of aoe variable'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': 'dff id'}, {'name': 'is_on', 'type': 'boolean', 'required': True, 'description': 'should schedule'}, {'name': 'name', 'type': 'string', 'required': True, 'description': 'dff name'}, {'name': 'nodes', 'type': 'array[DfNode]', 'required': True, 'description': '节点', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '节点', 'children': [{'name': 'flow_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'name', 'type': 'string', 'required': True, 'description': ''}, {'name': 'node_type', 'type': 'object', 'required': True, 'description': 'query data source', 'children': [{'name': 'Source', 'type': 'object', 'required': True, 'description': '直接导入数据', 'children': [{'name': 'Data', 'type': 'any', 'required': True, 'description': '直接导入数据'}]}]}]}]}, {'name': 'save_mode', 'type': 'string', 'required': True, 'description': 'Data frame save mode'}, {'name': 'trigger_type', 'type': 'object', 'required': True, 'description': 'Dataframe flow 启动的方式', 'children': [{'name': 'SimpleRepeat', 'type': 'object', 'required': True, 'description': '时间对象', 'children': [{'name': 'nanos', 'type': 'integer', 'required': True, 'description': '剩余纳秒'}, {'name': 'secs', 'type': 'integer', 'required': True, 'description': '秒'}]}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_flows_models_by_s",
        description="删除指定id的报表。参数：ids (string, 必填) - 报表id列表，以,间隔",
        func=mems_api.delete_flows_models_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '报表id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_models_file2",
        description="新增报表（多文件形式）。参数：data (object) - 请求体数据，字段：data.file (array[string], 必填)",
        func=mems_api.add_flows_models_file2,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.file (array[string], 必填)', 'children': [{'name': 'file', 'type': 'array[string]', 'required': True, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_models_json",
        description="查询报表（自定义JSON格式）。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_flows_models_json,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': False, 'description': '测点id（优先）'},
            {'name': 'ids', 'type': 'string', 'required': False, 'description': '测点id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_prog_file2",
        description="解析prog（多文件形式）。参数：data (object) - 请求体数据，字段：data.file (array[string], 必填)",
        func=mems_api.add_flows_prog_file2,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.file (array[string], 必填)', 'children': [{'name': 'file', 'type': 'array[string]', 'required': True, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_reload_dff_by_flow",
        description="重新加载报表。参数：flow_id (string, 必填) - 报表id",
        func=mems_api.add_flows_reload_dff_by_flow,
        parameters=[
            {'name': 'flow_id', 'type': 'string', 'required': True, 'description': '报表id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_result_keys",
        description="查询报表结果keys。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_flows_result_keys,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': False, 'description': '测点id（优先）'},
            {'name': 'ids', 'type': 'string', 'required': False, 'description': '测点id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_results",
        description="根据id查询报表执行结果。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_flows_results,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_flows_results",
        description="删除指定报表id指定key的报表结果。参数：data (array[any]) - 请求体数据，字段：data (array[any])",
        func=mems_api.delete_flows_results,
        parameters=[
            {'name': 'data', 'type': 'array[any]', 'required': True, 'description': '请求体数据；字段：data (array[any])'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_results_rename",
        description="重命名报表结果（简洁模式）。参数：data (array[any]) - 请求体数据，字段：data (array[any])",
        func=mems_api.add_flows_results_rename,
        parameters=[
            {'name': 'data', 'type': 'array[any]', 'required': True, 'description': '请求体数据；字段：data (array[any])'},
        ]
    ))

    tools.append(ToolInfo(
        name="update_flows_results_by_by_key",
        description="query_flows_result_and_eval。参数：id (string, 必填) - 报表id, key (string, 必填) - key, data (array[Expr]) - 请求体数据，字段：data (array[Expr]) - 表达式对象；data[].rpn (array[Token], 必填)；data[].rpn[].Binary (string, 必填) - Mathematical operations.",
        func=mems_api.update_flows_results_by_by_key,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': True, 'description': '报表id'},
            {'name': 'key', 'type': 'string', 'required': True, 'description': 'key'},
            {'name': 'data', 'type': 'array[Expr]', 'required': True, 'description': '请求体数据；字段：data (array[Expr]) - 表达式对象；data[].rpn (array[Token], 必填)；data[].rpn[].Binary (string, 必填) - Mathematical operations.', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'rpn', 'type': 'array[Token]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'Binary', 'type': 'string', 'required': True, 'description': 'Mathematical operations.'}]}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_results_by_by_key_by_view",
        description="query_flows_result_in_view。参数：id (string, 必填) - 报表id, key (string, 必填) - key, view (string, 必填) - view, data (array[Expr]) - 请求体数据，字段：data (array[Expr]) - 表达式对象；data[].rpn (array[Token], 必填)；data[].rpn[].Binary (string, 必填) - Mathematical operations.",
        func=mems_api.get_flows_results_by_by_key_by_view,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': True, 'description': '报表id'},
            {'name': 'key', 'type': 'string', 'required': True, 'description': 'key'},
            {'name': 'view', 'type': 'string', 'required': True, 'description': 'view'},
            {'name': 'data', 'type': 'array[Expr]', 'required': True, 'description': '请求体数据；字段：data (array[Expr]) - 表达式对象；data[].rpn (array[Token], 必填)；data[].rpn[].Binary (string, 必填) - Mathematical operations.', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'rpn', 'type': 'array[Token]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'Binary', 'type': 'string', 'required': True, 'description': 'Mathematical operations.'}]}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_results_json",
        description="根据id查询报表执行结果（Parquet格式）。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_flows_results_json,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_results_json_rows",
        description="根据id查询报表执行结果（逐行写入方式）。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_flows_results_json_rows,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_running",
        description="查询运行中的报表",
        func=mems_api.get_flows_running,
    ))

    tools.append(ToolInfo(
        name="get_flows_simple_models",
        description="查询报表（不包含Dataframe）。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_flows_simple_models,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': False, 'description': '测点id（优先）'},
            {'name': 'ids', 'type': 'string', 'required': False, 'description': '测点id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_unrun",
        description="查询未运行的报表",
        func=mems_api.get_flows_unrun,
    ))

    tools.append(ToolInfo(
        name="get_flows_view",
        description="查询报表展示模型。参数：id (string, 可选) - 展示模型id, flow_id (integer, 可选) - 报表id",
        func=mems_api.get_flows_view,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': False, 'description': '展示模型id'},
            {'name': 'flow_id', 'type': 'integer', 'required': False, 'description': '报表id'},
        ]
    ))

    tools.append(ToolInfo(
        name="update_flows_view",
        description="修改报表展示模型。参数：data (object) - 请求体数据，字段：data.config (any, 必填)；data.echart_js (string, 可选)；data.exprs (string, 必填)；data.flow_id (integer, 必填)；data.id (integer, 必填)；data.is_show (boolean, 必填)；data.layout (any, 必填)；data.name (string, 必填)；data.plot_template (string, 必填)；data.plot_type (string, 必填)；data.refresh_interval (integer, 可选)；data.series_style (any, 必填)",
        func=mems_api.update_flows_view,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.config (any, 必填)；data.echart_js (string, 可选)；data.exprs (string, 必填)；data.flow_id (integer, 必填)；data.id (integer, 必填)；data.is_show (boolean, 必填)；data.layout (any, 必填)；data.name (string, 必填)；data.plot_template (string, 必填)；data.plot_type (string, 必填)；data.refresh_interval (integer, 可选)；data.series_style (any, 必填)', 'children': [{'name': 'config', 'type': 'any', 'required': True, 'description': ''}, {'name': 'echart_js', 'type': 'string', 'required': False, 'description': ''}, {'name': 'exprs', 'type': 'string', 'required': True, 'description': ''}, {'name': 'flow_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'is_show', 'type': 'boolean', 'required': True, 'description': ''}, {'name': 'layout', 'type': 'any', 'required': True, 'description': ''}, {'name': 'name', 'type': 'string', 'required': True, 'description': ''}, {'name': 'plot_template', 'type': 'string', 'required': True, 'description': ''}, {'name': 'plot_type', 'type': 'string', 'required': True, 'description': ''}, {'name': 'refresh_interval', 'type': 'integer', 'required': False, 'description': ''}, {'name': 'series_style', 'type': 'any', 'required': True, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_view",
        description="新增报表展示模型。参数：data (object) - 请求体数据，字段：data.config (any, 必填)；data.echart_js (string, 可选)；data.exprs (string, 必填)；data.flow_id (integer, 必填)；data.id (integer, 必填)；data.is_show (boolean, 必填)；data.layout (any, 必填)；data.name (string, 必填)；data.plot_template (string, 必填)；data.plot_type (string, 必填)；data.refresh_interval (integer, 可选)；data.series_style (any, 必填)",
        func=mems_api.add_flows_view,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.config (any, 必填)；data.echart_js (string, 可选)；data.exprs (string, 必填)；data.flow_id (integer, 必填)；data.id (integer, 必填)；data.is_show (boolean, 必填)；data.layout (any, 必填)；data.name (string, 必填)；data.plot_template (string, 必填)；data.plot_type (string, 必填)；data.refresh_interval (integer, 可选)；data.series_style (any, 必填)', 'children': [{'name': 'config', 'type': 'any', 'required': True, 'description': ''}, {'name': 'echart_js', 'type': 'string', 'required': False, 'description': ''}, {'name': 'exprs', 'type': 'string', 'required': True, 'description': ''}, {'name': 'flow_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'is_show', 'type': 'boolean', 'required': True, 'description': ''}, {'name': 'layout', 'type': 'any', 'required': True, 'description': ''}, {'name': 'name', 'type': 'string', 'required': True, 'description': ''}, {'name': 'plot_template', 'type': 'string', 'required': True, 'description': ''}, {'name': 'plot_type', 'type': 'string', 'required': True, 'description': ''}, {'name': 'refresh_interval', 'type': 'integer', 'required': False, 'description': ''}, {'name': 'series_style', 'type': 'any', 'required': True, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_flows_view_by_s",
        description="删除指定id的报表展示模型。参数：ids (string, 必填) - 报表展示模型id列表，以,间隔",
        func=mems_api.delete_flows_view_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '报表展示模型id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_graphs_apply_additional",
        description="设置svg是否显示。参数：data (array[any]) - 请求体数据，字段：data (array[any])",
        func=mems_api.add_graphs_apply_additional,
        parameters=[
            {'name': 'data', 'type': 'array[any]', 'required': True, 'description': '请求体数据；字段：data (array[any])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_graphs_apply_models_by_path",
        description="获取应用版本某个名称的svg。参数：path (string, 必填) - svg名称",
        func=mems_api.get_graphs_apply_models_by_path,
        parameters=[
            {'name': 'path', 'type': 'string', 'required': True, 'description': 'svg名称'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_graphs_apply_paths",
        description="获取应用版本的所有svg名称",
        func=mems_api.get_graphs_apply_paths,
    ))

    tools.append(ToolInfo(
        name="add_graphs_apply_version",
        description="应用一个svg版本。参数：data (integer) - 请求体数据，字段：data (integer)",
        func=mems_api.add_graphs_apply_version,
        parameters=[
            {'name': 'data', 'type': 'integer', 'required': True, 'description': '请求体数据；字段：data (integer)'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_graphs_models",
        description="新增svg。参数：data (array[PbFile]) - 请求体数据，字段：data (array[PbFile])；data[].fileContent (array[integer], 可选)；data[].fileName (string, 可选)；data[].is_zip (boolean, 可选)；data[].op (string, 可选)",
        func=mems_api.add_graphs_models,
        parameters=[
            {'name': 'data', 'type': 'array[PbFile]', 'required': True, 'description': '请求体数据；字段：data (array[PbFile])；data[].fileContent (array[integer], 可选)；data[].fileName (string, 可选)；data[].is_zip (boolean, 可选)；data[].op (string, 可选)', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'fileContent', 'type': 'array[integer]', 'required': False, 'description': ''}, {'name': 'fileName', 'type': 'string', 'required': False, 'description': ''}, {'name': 'is_zip', 'type': 'boolean', 'required': False, 'description': ''}, {'name': 'op', 'type': 'string', 'required': False, 'description': ''}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_graphs_models_by_path",
        description="根据path查询指定的svg内容。参数：path (string, 必填) - svg名称, version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_graphs_models_by_path,
        parameters=[
            {'name': 'path', 'type': 'string', 'required': True, 'description': 'svg名称'},
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_graphs_models_by_path",
        description="删除指定名称的svg。参数：path (string, 必填) - svg名称列表，以,间隔",
        func=mems_api.delete_graphs_models_by_path,
        parameters=[
            {'name': 'path', 'type': 'string', 'required': True, 'description': 'svg名称列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_graphs_paths",
        description="查询所有svg的名称。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_graphs_paths,
        parameters=[
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_graphs_version",
        description="查询所有的svg版本信息",
        func=mems_api.get_graphs_version,
    ))

    tools.append(ToolInfo(
        name="add_graphs_version",
        description="提交svg版本。参数：data (object) - 请求体数据，字段：data.note (string, 必填) - 提交时的注释；data.tree_id (string, 必填) - 对应的tree_id；data.version (integer, 必填) - 版本号",
        func=mems_api.add_graphs_version,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.note (string, 必填) - 提交时的注释；data.tree_id (string, 必填) - 对应的tree_id；data.version (integer, 必填) - 版本号', 'children': [{'name': 'note', 'type': 'string', 'required': True, 'description': '提交时的注释'}, {'name': 'tree_id', 'type': 'string', 'required': True, 'description': '对应的tree_id'}, {'name': 'version', 'type': 'integer', 'required': True, 'description': '版本号'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_graphs_version_by_v",
        description="删除指定svg版本。参数：v (integer, 必填) - 版本id",
        func=mems_api.delete_graphs_version_by_v,
        parameters=[
            {'name': 'v', 'type': 'integer', 'required': True, 'description': '版本id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_config_by_lcc",
        description="查询指定lcc的告警通知配置信息。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarm_config_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_alarm_config_by_lcc",
        description="配置指定lcc的告警通知格式。参数：lcc_id (string, 必填) - lcc_id, data (object) - 请求体数据，字段：data.common (object, 必填) - 告警通知形式；data.common.popup_window (boolean, 必填) - 桌面弹窗；data.common.sound_light (boolean, 必填) - 声光；data.common.text_messages (boolean, 必填) - 短信；data.emergency (object, 必填) - 告警通知形式；data.emergency.popup_window (boolean, 必填) - 桌面弹窗；data.emergency.sound_light (boolean, 必填) - 声光；data.emergency.text_messages (boolean, 必填) - 短信；data.important (object, 必填) - 告警通知形式；data.important.popup_window (boolean, 必填) - 桌面弹窗；data.important.sound_light (boolean, 必填) - 声光；data.important.text_messages (boolean, 必填) - 短信",
        func=mems_api.add_lcc_alarm_config_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.common (object, 必填) - 告警通知形式；data.common.popup_window (boolean, 必填) - 桌面弹窗；data.common.sound_light (boolean, 必填) - 声光；data.common.text_messages (boolean, 必填) - 短信；data.emergency (object, 必填) - 告警通知形式；data.emergency.popup_window (boolean, 必填) - 桌面弹窗；data.emergency.sound_light (boolean, 必填) - 声光；data.emergency.text_messages (boolean, 必填) - 短信；data.important (object, 必填) - 告警通知形式；data.important.popup_window (boolean, 必填) - 桌面弹窗；data.important.sound_light (boolean, 必填) - 声光；data.important.text_messages (boolean, 必填) - 短信', 'children': [{'name': 'common', 'type': 'object', 'required': True, 'description': '告警通知形式', 'children': [{'name': 'popup_window', 'type': 'boolean', 'required': True, 'description': '桌面弹窗'}, {'name': 'sound_light', 'type': 'boolean', 'required': True, 'description': '声光'}, {'name': 'text_messages', 'type': 'boolean', 'required': True, 'description': '短信'}]}, {'name': 'emergency', 'type': 'object', 'required': True, 'description': '告警通知形式', 'children': [{'name': 'popup_window', 'type': 'boolean', 'required': True, 'description': '桌面弹窗'}, {'name': 'sound_light', 'type': 'boolean', 'required': True, 'description': '声光'}, {'name': 'text_messages', 'type': 'boolean', 'required': True, 'description': '短信'}]}, {'name': 'important', 'type': 'object', 'required': True, 'description': '告警通知形式', 'children': [{'name': 'popup_window', 'type': 'boolean', 'required': True, 'description': '桌面弹窗'}, {'name': 'sound_light', 'type': 'boolean', 'required': True, 'description': '声光'}, {'name': 'text_messages', 'type': 'boolean', 'required': True, 'description': '短信'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_alarm_confirm_by_lcc_by_user",
        description="指定lcc确认告警。参数：lcc_id (string, 必填) - lcc_id, user_id (integer, 必填) - 用户id, data (array[integer]) - 请求体数据，字段：data (array[integer])",
        func=mems_api.add_lcc_alarm_confirm_by_lcc_by_user,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'user_id', 'type': 'integer', 'required': True, 'description': '用户id'},
            {'name': 'data', 'type': 'array[integer]', 'required': True, 'description': '请求体数据；字段：data (array[integer])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_confirm_status_by_lcc",
        description="查询指定lcc的已确认告警。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarm_confirm_status_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_count_by_lcc",
        description="查询指定lcc的告警总数。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarm_count_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_alarm_define_by_lcc",
        description="上传指定lcc的单个告警定义。参数：lcc_id (string, 必填) - lcc_id, data (object) - 请求体数据，字段：data.desc (string, 可选)；data.id (integer, 可选)；data.level (string, 可选)；data.name (string, 可选)；data.owners (string, 可选)；data.rule (string, 可选)",
        func=mems_api.add_lcc_alarm_define_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.desc (string, 可选)；data.id (integer, 可选)；data.level (string, 可选)；data.name (string, 可选)；data.owners (string, 可选)；data.rule (string, 可选)', 'children': [{'name': 'desc', 'type': 'string', 'required': False, 'description': ''}, {'name': 'id', 'type': 'integer', 'required': False, 'description': ''}, {'name': 'level', 'type': 'string', 'required': False, 'description': ''}, {'name': 'name', 'type': 'string', 'required': False, 'description': ''}, {'name': 'owners', 'type': 'string', 'required': False, 'description': ''}, {'name': 'rule', 'type': 'string', 'required': False, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_define_by_lcc_by",
        description="查询指定lcc中指定id的告警定义。参数：lcc_id (string, 必填) - lcc_id, id (integer, 必填) - 告警id",
        func=mems_api.get_lcc_alarm_define_by_lcc_by,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '告警id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_defines_by_lcc",
        description="查询指定lcc的所有告警定义。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarm_defines_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_alarm_defines_by_lcc",
        description="上传指定lcc的告警定义。参数：lcc_id (string, 必填) - lcc_id, data (object) - 请求体数据，字段：data.defines (array[PbAlarmDefine], 必填)；data.defines[].desc (string, 可选)；data.defines[].id (integer, 可选)；data.defines[].level (string, 可选)；data.defines[].name (string, 可选)；data.defines[].owners (string, 可选)；data.defines[].rule (string, 可选)",
        func=mems_api.add_lcc_alarm_defines_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.defines (array[PbAlarmDefine], 必填)；data.defines[].desc (string, 可选)；data.defines[].id (integer, 可选)；data.defines[].level (string, 可选)；data.defines[].name (string, 可选)；data.defines[].owners (string, 可选)；data.defines[].rule (string, 可选)', 'children': [{'name': 'defines', 'type': 'array[PbAlarmDefine]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'desc', 'type': 'string', 'required': False, 'description': ''}, {'name': 'id', 'type': 'integer', 'required': False, 'description': ''}, {'name': 'level', 'type': 'string', 'required': False, 'description': ''}, {'name': 'name', 'type': 'string', 'required': False, 'description': ''}, {'name': 'owners', 'type': 'string', 'required': False, 'description': ''}, {'name': 'rule', 'type': 'string', 'required': False, 'description': ''}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_lcc_alarm_defines_by_lcc_by_s",
        description="删除指定lcc的指定id们的告警定义。参数：lcc_id (string, 必填) - lcc_id, ids (string, 必填) - 告警定义id列表，以,间隔",
        func=mems_api.delete_lcc_alarm_defines_by_lcc_by_s,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '告警定义id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_unconfirmed_number_by_lcc",
        description="查询指定lcc的未确认告警数。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarm_unconfirmed_number_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarms_unconfirmed_by_lcc",
        description="查询指定lcc的未确认告警列表。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarms_unconfirmed_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarms_by_lcc",
        description="查询指定lcc的告警结果 查询告警，结果按照时间排序。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_lcc_alarms_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_allmodels_bytes_by_lcc",
        description="导出指定lcc的所有模型字节数组。参数：lcc_id (string, 必填) - lcc_id, lang (string, 必填) - 语言",
        func=mems_api.get_lcc_allmodels_bytes_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'lang', 'type': 'string', 'required': True, 'description': '语言'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_allmodels_bytes_by_lcc",
        description="导入指定lcc的所有模型字节数组。参数：lcc_id (string, 必填) - lcc_id, data (string) - 请求体数据，字段：data (string)",
        func=mems_api.add_lcc_allmodels_bytes_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'string', 'required': True, 'description': '请求体数据；字段：data (string)'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_aoe_results_by_lcc",
        description="查询指定lcc的AOE执行结果。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_lcc_aoe_results_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_aoes_models_by_lcc",
        description="查询指定lcc的AOE。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - aoe id列表，以,间隔",
        func=mems_api.get_lcc_aoes_models_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'id', 'type': 'string', 'required': False, 'description': 'aoe id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_aoes_models_by_lcc",
        description="保存指定lcc的AOE。参数：lcc_id (string, 必填) - lcc_id, data (array[AoeModel]) - 请求体数据，字段：data (array[AoeModel]) - aoe模型；data[].actions (array[ActionEdge], 必填) - 动作列表；data[].actions[].action (string, 必填) - 无动作；data[].actions[].aoe_id (integer, 必填) - AOE id；data[].actions[].failure_mode (string, 必填) - 失败模式；data[].actions[].name (string, 必填) - 动作名称；data[].actions[].source_node (integer, 必填) - 源节点；data[].actions[].target_node (integer, 必填) - 目标节点；data[].events (array[EventNode], 必填) - 节点列表；data[].events[].aoe_id (integer, 必填) - AOE id；data[].events[].expr (object, 必填) - 表达式对象；data[].events[].id (integer, 必填) - 节点id；data[].events[].name (string, 必填) - 节点名；data[].events[].node_type (string, 必填) - 节点类型；data[].events[].timeout (integer, 必填) - 事件还未发生时等待超时时间；data[].id (integer, 必填) - aoe id；data[].name (string, 必填) - aoe名称；data[].trigger_type (object, 必填) - 简单固定周期触发；data[].trigger_type.SimpleRepeat (object, 必填) - 时间对象；data[].variables (array[array[any]], 必填) - 用户自定义的变量：变量名和表达式",
        func=mems_api.add_lcc_aoes_models_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'array[AoeModel]', 'required': True, 'description': '请求体数据；字段：data (array[AoeModel]) - aoe模型；data[].actions (array[ActionEdge], 必填) - 动作列表；data[].actions[].action (string, 必填) - 无动作；data[].actions[].aoe_id (integer, 必填) - AOE id；data[].actions[].failure_mode (string, 必填) - 失败模式；data[].actions[].name (string, 必填) - 动作名称；data[].actions[].source_node (integer, 必填) - 源节点；data[].actions[].target_node (integer, 必填) - 目标节点；data[].events (array[EventNode], 必填) - 节点列表；data[].events[].aoe_id (integer, 必填) - AOE id；data[].events[].expr (object, 必填) - 表达式对象；data[].events[].id (integer, 必填) - 节点id；data[].events[].name (string, 必填) - 节点名；data[].events[].node_type (string, 必填) - 节点类型；data[].events[].timeout (integer, 必填) - 事件还未发生时等待超时时间；data[].id (integer, 必填) - aoe id；data[].name (string, 必填) - aoe名称；data[].trigger_type (object, 必填) - 简单固定周期触发；data[].trigger_type.SimpleRepeat (object, 必填) - 时间对象；data[].variables (array[array[any]], 必填) - 用户自定义的变量：变量名和表达式', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'actions', 'type': 'array[ActionEdge]', 'required': True, 'description': '动作列表', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '动作列表', 'children': [{'name': 'action', 'type': 'string', 'required': True, 'description': '无动作'}, {'name': 'aoe_id', 'type': 'integer', 'required': True, 'description': 'AOE id'}, {'name': 'failure_mode', 'type': 'string', 'required': True, 'description': '失败模式'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '动作名称'}, {'name': 'source_node', 'type': 'integer', 'required': True, 'description': '源节点'}, {'name': 'target_node', 'type': 'integer', 'required': True, 'description': '目标节点'}]}]}, {'name': 'events', 'type': 'array[EventNode]', 'required': True, 'description': '节点列表', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '节点列表', 'children': [{'name': 'aoe_id', 'type': 'integer', 'required': True, 'description': 'AOE id'}, {'name': 'expr', 'type': 'object', 'required': True, 'description': '表达式对象', 'children': [{'name': 'rpn', 'type': 'array[Token]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'Binary', 'type': 'string', 'required': True, 'description': 'Mathematical operations.'}]}]}]}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '节点id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '节点名'}, {'name': 'node_type', 'type': 'string', 'required': True, 'description': '节点类型'}, {'name': 'timeout', 'type': 'integer', 'required': True, 'description': '事件还未发生时等待超时时间'}]}]}, {'name': 'id', 'type': 'integer', 'required': True, 'description': 'aoe id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': 'aoe名称'}, {'name': 'trigger_type', 'type': 'object', 'required': True, 'description': '简单固定周期触发', 'children': [{'name': 'SimpleRepeat', 'type': 'object', 'required': True, 'description': '时间对象', 'children': [{'name': 'nanos', 'type': 'integer', 'required': True, 'description': '剩余纳秒'}, {'name': 'secs', 'type': 'integer', 'required': True, 'description': '秒'}]}]}, {'name': 'variables', 'type': 'array[array[any]]', 'required': True, 'description': '用户自定义的变量：变量名和表达式'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_lcc_aoes_models_by_lcc_by_s",
        description="删除指定lcc指定id的AOE。参数：lcc_id (string, 必填) - lcc_id, ids (string, 必填) - AOE_id列表，以,间隔",
        func=mems_api.delete_lcc_aoes_models_by_lcc_by_s,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'ids', 'type': 'string', 'required': True, 'description': 'AOE_id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_auth_users_by_lcc",
        description="查询指定lcc的所有用户。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_auth_users_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_commands_by_lcc",
        description="查询指定lcc的历史设点执行结果。参数：lcc_id (string, 必填) - lcc_id, sender_id (integer, 可选) - , point_id (integer, 可选) - 测点id, start (integer, 可选) - 开始时间, end (integer, 可选) - 结束时间, date (string, 可选) - 时间字符串，yyyy-MM-dd, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_lcc_commands_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'sender_id', 'type': 'integer', 'required': False, 'description': ''},
            {'name': 'point_id', 'type': 'integer', 'required': False, 'description': '测点id'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_common_map_by_lcc",
        description="执行指定lcc的map映射操作。参数：lcc_id (string, 必填) - lcc_id, data (object) - 请求体数据，字段：data.Query (array[integer], 必填) - 查询",
        func=mems_api.add_lcc_common_map_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.Query (array[integer], 必填) - 查询', 'children': [{'name': 'Query', 'type': 'array[integer]', 'required': True, 'description': '查询'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_config_by_lcc",
        description="查询指定lcc的配置。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_config_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_config_by_lcc",
        description="保存指定lcc的配置。参数：lcc_id (string, 必填) - lcc_id, data (object) - 请求体数据，字段：data.properties (object, 必填) - 主要配置属性；data.properties2 (object, 必填) - 次要配置属性",
        func=mems_api.add_lcc_config_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.properties (object, 必填) - 主要配置属性；data.properties2 (object, 必填) - 次要配置属性', 'children': [{'name': 'properties', 'type': 'object', 'required': True, 'description': '主要配置属性'}, {'name': 'properties2', 'type': 'object', 'required': True, 'description': '次要配置属性'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_controls_by_lcc",
        description="执行Lcc操作。参数：lcc_id (string, 必填) - lcc_id, data (string) - 请求体数据，字段：data (string) - 强制退出",
        func=mems_api.add_lcc_controls_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'string', 'required': True, 'description': '请求体数据；字段：data (string) - 强制退出'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_logs_bytes_by_lcc",
        description="查询指定lcc的日志。参数：lcc_id (string, 必填) - lcc_id, is_query_size (boolean, 可选) - 是否限制文件大小",
        func=mems_api.get_lcc_logs_bytes_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'is_query_size', 'type': 'boolean', 'required': False, 'description': '是否限制文件大小'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_measures_by_lcc",
        description="查询指定lcc的历史量测。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_lcc_measures_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_points_import_str_by_lcc",
        description="加载LCC的测点到base服务。参数：lcc_id (string, 必填) - lcc_id, data (string) - 请求体数据，字段：data (string)",
        func=mems_api.add_lcc_points_import_str_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'string', 'required': True, 'description': '请求体数据；字段：data (string)'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_points_models_by_lcc",
        description="查询指定lcc的测点信息。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - , name (string, 可选) - , is_soe (boolean, 可选) - ",
        func=mems_api.get_lcc_points_models_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'id', 'type': 'string', 'required': False, 'description': ''},
            {'name': 'name', 'type': 'string', 'required': False, 'description': ''},
            {'name': 'is_soe', 'type': 'boolean', 'required': False, 'description': ''},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_points_models_by_lcc",
        description="保存指定lcc的测点信息。参数：lcc_id (string, 必填) - lcc_id, data (array[Measurement]) - 请求体数据，字段：data (array[Measurement]) - 测点对象；data[].alarm_level1_expr (string, 必填) - 告警级别1的表达式；data[].alarm_level2_expr (string, 必填) - 告警级别2的表达式；data[].alias_id (string, 必填) - 字符串id；data[].change_expr (string, 必填) - 判断是否\\\"变化\\\"的公式，用于变化上传或储存；data[].data_unit (string, 必填) - 单位；data[].desc (string, 必填) - Description；data[].expression (string, 必填) - 如果是计算点，这是表达式；data[].init_value (integer, 必填) - 默认值存储在8个字节，需要根据is_discrete来转换成具体的值；data[].inv_trans_expr (string, 必填) - 逆变换公式；data[].is_computing_point (boolean, 必填) - 是否是计算点；data[].is_discrete (boolean, 必填) - 是否是离散量；data[].is_realtime (boolean, 必填) - 如是，则不判断是否\\\"变化\\\"，均上传；data[].is_soe (boolean, 必填) - 是否是soe点；data[].lower_limit (number, 必填) - 下限，用于坏数据辨识；data[].point_id (integer, 必填) - 唯一的id；data[].point_name (string, 必填) - 测点名；data[].trans_expr (string, 必填) - 变换公式；data[].upper_limit (number, 必填) - 上限，用于坏数据辨识；data[].zero_expr (string, 必填) - 判断是否为0值的公式",
        func=mems_api.add_lcc_points_models_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'array[Measurement]', 'required': True, 'description': '请求体数据；字段：data (array[Measurement]) - 测点对象；data[].alarm_level1_expr (string, 必填) - 告警级别1的表达式；data[].alarm_level2_expr (string, 必填) - 告警级别2的表达式；data[].alias_id (string, 必填) - 字符串id；data[].change_expr (string, 必填) - 判断是否\\"变化\\"的公式，用于变化上传或储存；data[].data_unit (string, 必填) - 单位；data[].desc (string, 必填) - Description；data[].expression (string, 必填) - 如果是计算点，这是表达式；data[].init_value (integer, 必填) - 默认值存储在8个字节，需要根据is_discrete来转换成具体的值；data[].inv_trans_expr (string, 必填) - 逆变换公式；data[].is_computing_point (boolean, 必填) - 是否是计算点；data[].is_discrete (boolean, 必填) - 是否是离散量；data[].is_realtime (boolean, 必填) - 如是，则不判断是否\\"变化\\"，均上传；data[].is_soe (boolean, 必填) - 是否是soe点；data[].lower_limit (number, 必填) - 下限，用于坏数据辨识；data[].point_id (integer, 必填) - 唯一的id；data[].point_name (string, 必填) - 测点名；data[].trans_expr (string, 必填) - 变换公式；data[].upper_limit (number, 必填) - 上限，用于坏数据辨识；data[].zero_expr (string, 必填) - 判断是否为0值的公式', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'alarm_level1_expr', 'type': 'string', 'required': True, 'description': '告警级别1的表达式'}, {'name': 'alarm_level2_expr', 'type': 'string', 'required': True, 'description': '告警级别2的表达式'}, {'name': 'alias_id', 'type': 'string', 'required': True, 'description': '字符串id'}, {'name': 'change_expr', 'type': 'string', 'required': True, 'description': '判断是否"变化"的公式，用于变化上传或储存'}, {'name': 'data_unit', 'type': 'string', 'required': True, 'description': '单位'}, {'name': 'desc', 'type': 'string', 'required': True, 'description': 'Description'}, {'name': 'expression', 'type': 'string', 'required': True, 'description': '如果是计算点，这是表达式'}, {'name': 'init_value', 'type': 'integer', 'required': True, 'description': '默认值存储在8个字节，需要根据is_discrete来转换成具体的值'}, {'name': 'inv_trans_expr', 'type': 'string', 'required': True, 'description': '逆变换公式'}, {'name': 'is_computing_point', 'type': 'boolean', 'required': True, 'description': '是否是计算点'}, {'name': 'is_discrete', 'type': 'boolean', 'required': True, 'description': '是否是离散量'}, {'name': 'is_realtime', 'type': 'boolean', 'required': True, 'description': '如是，则不判断是否"变化"，均上传'}, {'name': 'is_soe', 'type': 'boolean', 'required': True, 'description': '是否是soe点'}, {'name': 'lower_limit', 'type': 'number', 'required': True, 'description': '下限，用于坏数据辨识'}, {'name': 'point_id', 'type': 'integer', 'required': True, 'description': '唯一的id'}, {'name': 'point_name', 'type': 'string', 'required': True, 'description': '测点名'}, {'name': 'trans_expr', 'type': 'string', 'required': True, 'description': '变换公式'}, {'name': 'upper_limit', 'type': 'number', 'required': True, 'description': '上限，用于坏数据辨识'}, {'name': 'zero_expr', 'type': 'string', 'required': True, 'description': '判断是否为0值的公式'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_lcc_points_models_by_lcc",
        description="删除指定lcc的测点。参数：lcc_id (string, 必填) - lcc_id, data (array[integer]) - 请求体数据，字段：data (array[integer])",
        func=mems_api.delete_lcc_points_models_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'array[integer]', 'required': True, 'description': '请求体数据；字段：data (array[integer])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_running_aoes_by_lcc",
        description="查询指定lcc运行中的AOE。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_running_aoes_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_soes_by_lcc",
        description="查询指定lcc的SOE。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_lcc_soes_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_tag_defines_by_lcc_by_group",
        description="查询指定lcc指定分组的标签名称及id列表。参数：lcc_id (string, 必填) - lcc_id, group (integer, 必填) - 分组id",
        func=mems_api.get_lcc_tag_defines_by_lcc_by_group,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'group', 'type': 'integer', 'required': True, 'description': '分组id'},
        ]
    ))

    tools.append(ToolInfo(
        name="update_lcc_tags_by_lcc_by_group",
        description="更新指定lcc指定分组下标签名和测点数组关系。参数：lcc_id (string, 必填) - lcc_id, group (integer, 必填) - 分组id, data (array[array[any]]) - 请求体数据，字段：data (array[array[any]])",
        func=mems_api.update_lcc_tags_by_lcc_by_group,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'group', 'type': 'integer', 'required': True, 'description': '分组id'},
            {'name': 'data', 'type': 'array[array[any]]', 'required': True, 'description': '请求体数据；字段：data (array[array[any]])'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_tags_by_lcc_by_group",
        description="查询指定lcc指定分组下标签id对应的测点数组。参数：lcc_id (string, 必填) - lcc_id, group (integer, 必填) - 分组id, data (array[integer]) - 请求体数据，字段：data (array[integer])",
        func=mems_api.add_lcc_tags_by_lcc_by_group,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'group', 'type': 'integer', 'required': True, 'description': '分组id'},
            {'name': 'data', 'type': 'array[integer]', 'required': True, 'description': '请求体数据；字段：data (array[integer])'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_lcc_tags_by_lcc_by_group",
        description="删除指定lcc指定分组下标签id和测点的关系。参数：lcc_id (string, 必填) - lcc_id, group (integer, 必填) - 分组id, data (array[array[any]]) - 请求体数据，字段：data (array[array[any]])",
        func=mems_api.delete_lcc_tags_by_lcc_by_group,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'group', 'type': 'integer', 'required': True, 'description': '分组id'},
            {'name': 'data', 'type': 'array[array[any]]', 'required': True, 'description': '请求体数据；字段：data (array[array[any]])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_transports_models_by_lcc",
        description="查询指定lcc的通道信息。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - 通道id列表，以,间隔, transport_type (string, 可选) - 通道类型",
        func=mems_api.get_lcc_transports_models_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'id', 'type': 'string', 'required': False, 'description': '通道id列表，以,间隔'},
            {'name': 'transport_type', 'type': 'string', 'required': False, 'description': '通道类型'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_transports_models_by_lcc",
        description="保存指定lcc的通道信息。参数：lcc_id (string, 必填) - lcc_id, data (array[Transport]) - 请求体数据，字段：data (array[Transport])；data[].MbcTcp (object, 必填) - ModbusTcp客户端通道信息；data[].MbcTcp.connections (array[MbConnection], 必填) - Modbus通道连接信息；data[].MbcTcp.id (integer, 必填) - 通道id；data[].MbcTcp.name (string, 必填) - 通道名称；data[].MbcTcp.tcp_server (array[any], 必填) - 服务端的ip和port",
        func=mems_api.add_lcc_transports_models_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'data', 'type': 'array[Transport]', 'required': True, 'description': '请求体数据；字段：data (array[Transport])；data[].MbcTcp (object, 必填) - ModbusTcp客户端通道信息；data[].MbcTcp.connections (array[MbConnection], 必填) - Modbus通道连接信息；data[].MbcTcp.id (integer, 必填) - 通道id；data[].MbcTcp.name (string, 必填) - 通道名称；data[].MbcTcp.tcp_server (array[any], 必填) - 服务端的ip和port', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'MbcTcp', 'type': 'object', 'required': True, 'description': 'ModbusTcp客户端通道信息', 'children': [{'name': 'connections', 'type': 'array[MbConnection]', 'required': True, 'description': 'Modbus通道连接信息', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': 'Modbus通道连接信息', 'children': [{'name': 'coil_write_code', 'type': 'integer', 'required': False, 'description': ''}, {'name': 'default_polling_period_in_milli', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'delay_between_requests', 'type': 'integer', 'required': True, 'description': '两条请求直接的间隔'}, {'name': 'holding_write_code', 'type': 'integer', 'required': False, 'description': ''}, {'name': 'max_read_bit_count', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'max_read_register_count', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'max_write_bit_count', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'max_write_register_count', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'mb_data_configure', 'type': 'array[RegisterData]', 'required': True, 'description': 'register settings', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': 'register settings', 'children': [{'name': 'data_id', 'type': 'integer', 'required': True, 'description': '数据标识'}, {'name': 'point_ids', 'type': 'array[integer]', 'required': True, 'description': '对应的测点Id'}, {'name': 'polling_period_in_milli', 'type': 'integer', 'required': True, 'description': '轮询周期，毫秒'}]}]}, {'name': 'name', 'type': 'string', 'required': True, 'description': ''}, {'name': 'point_id', 'type': 'integer', 'required': True, 'description': '通道状态对应的测点号'}, {'name': 'point_id_to_rd', 'type': 'object', 'required': True, 'description': 'key is point id, value is position of register data'}, {'name': 'polling_period_to_data', 'type': 'object', 'required': True, 'description': '轮询周期不同的数据, key is period in milli, value is position.'}, {'name': 'protocol_type', 'type': 'string', 'required': True, 'description': 'Modbus协议类型'}, {'name': 'register_addr_to_rd', 'type': 'object', 'required': True, 'description': 'key:寄存器地址,value:setting中vec<RegisterData>的位置'}, {'name': 'slave_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'timeout_in_milli', 'type': 'integer', 'required': True, 'description': '超时设置'}]}]}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '通道id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '通道名称'}, {'name': 'tcp_server', 'type': 'array[any]', 'required': True, 'description': '服务端的ip和port'}]}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_lcc_transports_models_by_lcc_by_s",
        description="删除指定lcc指定id的通道。参数：lcc_id (string, 必填) - lcc_id, ids (string, 必填) - 通道id列表，以,间隔",
        func=mems_api.delete_lcc_transports_models_by_lcc_by_s,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '通道id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_unrun_aoes_by_lcc",
        description="查询指定lcc未运行的AOE。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_unrun_aoes_by_lcc,
        parameters=[
            {'name': 'lcc_id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_by",
        description="查询指定id的lcc。参数：id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_by,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': True, 'description': 'lcc_id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_list",
        description="查询所有的lcc",
        func=mems_api.get_lcc_list,
    ))

    tools.append(ToolInfo(
        name="get_logs_bytes",
        description="查询日志字节数组。参数：is_query_size (boolean, 可选) - 是否限制文件大小",
        func=mems_api.get_logs_bytes,
        parameters=[
            {'name': 'is_query_size', 'type': 'boolean', 'required': False, 'description': '是否限制文件大小'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_measureinits_by_day",
        description="量测值初始化。参数：day (integer, 必填) - 时间戳",
        func=mems_api.add_measureinits_by_day,
        parameters=[
            {'name': 'day', 'type': 'integer', 'required': True, 'description': '时间戳'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_measures",
        description="查询历史量测。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_measures,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_multi_import_bytes",
        description="导入所有模型字节数组。参数：data (string) - 请求体数据，字段：data (string)",
        func=mems_api.add_multi_import_bytes,
        parameters=[
            {'name': 'data', 'type': 'string', 'required': True, 'description': '请求体数据；字段：data (string)'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_north_dataframe_by_flow_by_node",
        description="加载其他mems来的Dataframe。参数：flow (integer, 必填) - 报表id, node (integer, 必填) - 节点id, data (string) - 请求体数据，字段：data (string)",
        func=mems_api.add_north_dataframe_by_flow_by_node,
        parameters=[
            {'name': 'flow', 'type': 'integer', 'required': True, 'description': '报表id'},
            {'name': 'node', 'type': 'integer', 'required': True, 'description': '节点id'},
            {'name': 'data', 'type': 'string', 'required': True, 'description': '请求体数据；字段：data (string)'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_north_restart",
        description="重启北向服务",
        func=mems_api.add_north_restart,
    ))

    tools.append(ToolInfo(
        name="get_ping",
        description="查看ping结果",
        func=mems_api.get_ping,
    ))

    tools.append(ToolInfo(
        name="get_plans_models",
        description="查询所有计划",
        func=mems_api.get_plans_models,
    ))

    tools.append(ToolInfo(
        name="update_plans_models",
        description="修改计划。参数：data (object) - 请求体数据，字段：data.desc (string, 必填) - 计划描述；data.id (integer, 必填) - 计划id；data.name (string, 必填) - 计划名称；data.plan (array[array[any]], 必填) - 计划内容数组，tuple格式为(开始时间:u64, 结束时间:u64, 功率值:f64)",
        func=mems_api.update_plans_models,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.desc (string, 必填) - 计划描述；data.id (integer, 必填) - 计划id；data.name (string, 必填) - 计划名称；data.plan (array[array[any]], 必填) - 计划内容数组，tuple格式为(开始时间:u64, 结束时间:u64, 功率值:f64)', 'children': [{'name': 'desc', 'type': 'string', 'required': True, 'description': '计划描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '计划id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '计划名称'}, {'name': 'plan', 'type': 'array[array[any]]', 'required': True, 'description': '计划内容数组，tuple格式为(开始时间:u64, 结束时间:u64, 功率值:f64)'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_plans_models",
        description="新增计划。参数：data (object) - 请求体数据，字段：data.desc (string, 必填) - 计划描述；data.id (integer, 必填) - 计划id；data.name (string, 必填) - 计划名称；data.plan (array[array[any]], 必填) - 计划内容数组，tuple格式为(开始时间:u64, 结束时间:u64, 功率值:f64)",
        func=mems_api.add_plans_models,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.desc (string, 必填) - 计划描述；data.id (integer, 必填) - 计划id；data.name (string, 必填) - 计划名称；data.plan (array[array[any]], 必填) - 计划内容数组，tuple格式为(开始时间:u64, 结束时间:u64, 功率值:f64)', 'children': [{'name': 'desc', 'type': 'string', 'required': True, 'description': '计划描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '计划id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '计划名称'}, {'name': 'plan', 'type': 'array[array[any]]', 'required': True, 'description': '计划内容数组，tuple格式为(开始时间:u64, 结束时间:u64, 功率值:f64)'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_plans_models_by_ids",
        description="查询指定id的计划列表。参数：ids (string, 必填) - 计划id列表，以,间隔",
        func=mems_api.get_plans_models_by_ids,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '计划id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_plans_models_by_s",
        description="删除指定id的计划。参数：ids (string, 必填) - 计划id列表，以,间隔",
        func=mems_api.delete_plans_models_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '计划id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_plans_models_by",
        description="查询指定id的计划。参数：id (integer, 必填) - 计划id",
        func=mems_api.get_plans_models_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '计划id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_plans_paths",
        description="查询所有计划路径",
        func=mems_api.get_plans_paths,
    ))

    tools.append(ToolInfo(
        name="update_plans_paths",
        description="修改计划路径。参数：data (object) - 请求体数据",
        func=mems_api.update_plans_paths,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_plans_paths",
        description="新增计划路径。参数：data (object) - 请求体数据",
        func=mems_api.add_plans_paths,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_plans_paths",
        description="删除指定的计划路径。参数：data (array[string]) - 请求体数据，字段：data (array[string])",
        func=mems_api.delete_plans_paths,
        parameters=[
            {'name': 'data', 'type': 'array[string]', 'required': True, 'description': '请求体数据；字段：data (array[string])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_points_models",
        description="查询所有测点",
        func=mems_api.get_points_models,
    ))

    tools.append(ToolInfo(
        name="add_points_models",
        description="保存测点。参数：data (array[Measurement]) - 请求体数据，字段：data (array[Measurement]) - 测点对象；data[].alarm_level1_expr (string, 必填) - 告警级别1的表达式；data[].alarm_level2_expr (string, 必填) - 告警级别2的表达式；data[].alias_id (string, 必填) - 字符串id；data[].change_expr (string, 必填) - 判断是否\\\"变化\\\"的公式，用于变化上传或储存；data[].data_unit (string, 必填) - 单位；data[].desc (string, 必填) - Description；data[].expression (string, 必填) - 如果是计算点，这是表达式；data[].init_value (integer, 必填) - 默认值存储在8个字节，需要根据is_discrete来转换成具体的值；data[].inv_trans_expr (string, 必填) - 逆变换公式；data[].is_computing_point (boolean, 必填) - 是否是计算点；data[].is_discrete (boolean, 必填) - 是否是离散量；data[].is_realtime (boolean, 必填) - 如是，则不判断是否\\\"变化\\\"，均上传；data[].is_soe (boolean, 必填) - 是否是soe点；data[].lower_limit (number, 必填) - 下限，用于坏数据辨识；data[].point_id (integer, 必填) - 唯一的id；data[].point_name (string, 必填) - 测点名；data[].trans_expr (string, 必填) - 变换公式；data[].upper_limit (number, 必填) - 上限，用于坏数据辨识；data[].zero_expr (string, 必填) - 判断是否为0值的公式",
        func=mems_api.add_points_models,
        parameters=[
            {'name': 'data', 'type': 'array[Measurement]', 'required': True, 'description': '请求体数据；字段：data (array[Measurement]) - 测点对象；data[].alarm_level1_expr (string, 必填) - 告警级别1的表达式；data[].alarm_level2_expr (string, 必填) - 告警级别2的表达式；data[].alias_id (string, 必填) - 字符串id；data[].change_expr (string, 必填) - 判断是否\\"变化\\"的公式，用于变化上传或储存；data[].data_unit (string, 必填) - 单位；data[].desc (string, 必填) - Description；data[].expression (string, 必填) - 如果是计算点，这是表达式；data[].init_value (integer, 必填) - 默认值存储在8个字节，需要根据is_discrete来转换成具体的值；data[].inv_trans_expr (string, 必填) - 逆变换公式；data[].is_computing_point (boolean, 必填) - 是否是计算点；data[].is_discrete (boolean, 必填) - 是否是离散量；data[].is_realtime (boolean, 必填) - 如是，则不判断是否\\"变化\\"，均上传；data[].is_soe (boolean, 必填) - 是否是soe点；data[].lower_limit (number, 必填) - 下限，用于坏数据辨识；data[].point_id (integer, 必填) - 唯一的id；data[].point_name (string, 必填) - 测点名；data[].trans_expr (string, 必填) - 变换公式；data[].upper_limit (number, 必填) - 上限，用于坏数据辨识；data[].zero_expr (string, 必填) - 判断是否为0值的公式', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'alarm_level1_expr', 'type': 'string', 'required': True, 'description': '告警级别1的表达式'}, {'name': 'alarm_level2_expr', 'type': 'string', 'required': True, 'description': '告警级别2的表达式'}, {'name': 'alias_id', 'type': 'string', 'required': True, 'description': '字符串id'}, {'name': 'change_expr', 'type': 'string', 'required': True, 'description': '判断是否"变化"的公式，用于变化上传或储存'}, {'name': 'data_unit', 'type': 'string', 'required': True, 'description': '单位'}, {'name': 'desc', 'type': 'string', 'required': True, 'description': 'Description'}, {'name': 'expression', 'type': 'string', 'required': True, 'description': '如果是计算点，这是表达式'}, {'name': 'init_value', 'type': 'integer', 'required': True, 'description': '默认值存储在8个字节，需要根据is_discrete来转换成具体的值'}, {'name': 'inv_trans_expr', 'type': 'string', 'required': True, 'description': '逆变换公式'}, {'name': 'is_computing_point', 'type': 'boolean', 'required': True, 'description': '是否是计算点'}, {'name': 'is_discrete', 'type': 'boolean', 'required': True, 'description': '是否是离散量'}, {'name': 'is_realtime', 'type': 'boolean', 'required': True, 'description': '如是，则不判断是否"变化"，均上传'}, {'name': 'is_soe', 'type': 'boolean', 'required': True, 'description': '是否是soe点'}, {'name': 'lower_limit', 'type': 'number', 'required': True, 'description': '下限，用于坏数据辨识'}, {'name': 'point_id', 'type': 'integer', 'required': True, 'description': '唯一的id'}, {'name': 'point_name', 'type': 'string', 'required': True, 'description': '测点名'}, {'name': 'trans_expr', 'type': 'string', 'required': True, 'description': '变换公式'}, {'name': 'upper_limit', 'type': 'number', 'required': True, 'description': '上限，用于坏数据辨识'}, {'name': 'zero_expr', 'type': 'string', 'required': True, 'description': '判断是否为0值的公式'}]}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_points_models",
        description="删除指定id的测点（body形式）。参数：data (array[integer]) - 请求体数据，字段：data (array[integer])",
        func=mems_api.delete_points_models,
        parameters=[
            {'name': 'data', 'type': 'array[integer]', 'required': True, 'description': '请求体数据；字段：data (array[integer])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_points_models_for_apply",
        description="获取根据版本号组装的测点应用对象。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_points_models_for_apply,
        parameters=[
            {'name': 'version', 'type': 'integer', 'required': False, 'description': '版本号，可选，若为空则默认0号版本'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_points_models_by_s",
        description="删除指定id的测点。参数：ids (string, 必填) - 测点id列表，以,间隔",
        func=mems_api.delete_points_models_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '测点id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_points_models_file",
        description="保存测点（文件形式）。参数：data (object) - 请求体数据，字段：data.fileContent (array[integer], 可选)；data.fileName (string, 可选)；data.is_zip (boolean, 可选)；data.op (string, 可选)",
        func=mems_api.add_points_models_file,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.fileContent (array[integer], 可选)；data.fileName (string, 可选)；data.is_zip (boolean, 可选)；data.op (string, 可选)', 'children': [{'name': 'fileContent', 'type': 'array[integer]', 'required': False, 'description': ''}, {'name': 'fileName', 'type': 'string', 'required': False, 'description': ''}, {'name': 'is_zip', 'type': 'boolean', 'required': False, 'description': ''}, {'name': 'op', 'type': 'string', 'required': False, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="add_points_models_file2",
        description="保存测点（多文件形式）。参数：data (object) - 请求体数据，字段：data.file (array[string], 必填)",
        func=mems_api.add_points_models_file2,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.file (array[string], 必填)', 'children': [{'name': 'file', 'type': 'array[string]', 'required': True, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_points_remote",
        description="查询控制器与测点的对应关系",
        func=mems_api.get_points_remote,
    ))

    tools.append(ToolInfo(
        name="add_points_remote",
        description="更新控制器与测点的关系。参数：data (array[any]) - 请求体数据，字段：data (array[any])",
        func=mems_api.add_points_remote,
        parameters=[
            {'name': 'data', 'type': 'array[any]', 'required': True, 'description': '请求体数据；字段：data (array[any])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_points_source",
        description="查询所有测点数据源",
        func=mems_api.get_points_source,
    ))

    tools.append(ToolInfo(
        name="add_points_source",
        description="保存测点数据源。参数：data (array[array[any]]) - 请求体数据，字段：data (array[array[any]])",
        func=mems_api.add_points_source,
        parameters=[
            {'name': 'data', 'type': 'array[array[any]]', 'required': True, 'description': '请求体数据；字段：data (array[array[any]])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_points_version",
        description="查询所有的测点版本信息",
        func=mems_api.get_points_version,
    ))

    tools.append(ToolInfo(
        name="add_points_version",
        description="新增测点版本。参数：data (object) - 请求体数据，字段：data.note (string, 必填) - 提交时的注释；data.tree_id (string, 必填) - 对应的tree_id；data.version (integer, 必填) - 版本号",
        func=mems_api.add_points_version,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.note (string, 必填) - 提交时的注释；data.tree_id (string, 必填) - 对应的tree_id；data.version (integer, 必填) - 版本号', 'children': [{'name': 'note', 'type': 'string', 'required': True, 'description': '提交时的注释'}, {'name': 'tree_id', 'type': 'string', 'required': True, 'description': '对应的tree_id'}, {'name': 'version', 'type': 'integer', 'required': True, 'description': '版本号'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_points_version_by_v",
        description="删除某一个测点版本。参数：v (integer, 必填) - 版本id",
        func=mems_api.delete_points_version_by_v,
        parameters=[
            {'name': 'v', 'type': 'integer', 'required': True, 'description': '版本id'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_pscpu_aoes",
        description="更新当前应用的AOE。参数：data (object) - 请求体数据，字段：data.aoes (array[AoeModel], 必填) - AOE列表；data.aoes[].actions (array[ActionEdge], 必填) - 动作列表；data.aoes[].actions[].action (string, 必填) - 无动作；data.aoes[].actions[].aoe_id (integer, 必填) - AOE id；data.aoes[].actions[].failure_mode (string, 必填) - 失败模式；data.aoes[].actions[].name (string, 必填) - 动作名称；data.aoes[].actions[].source_node (integer, 必填) - 源节点；data.aoes[].actions[].target_node (integer, 必填) - 目标节点；data.aoes[].events (array[EventNode], 必填) - 节点列表；data.aoes[].events[].aoe_id (integer, 必填) - AOE id；data.aoes[].events[].expr (object, 必填) - 表达式对象；data.aoes[].events[].id (integer, 必填) - 节点id；data.aoes[].events[].name (string, 必填) - 节点名；data.aoes[].events[].node_type (string, 必填) - 节点类型；data.aoes[].events[].timeout (integer, 必填) - 事件还未发生时等待超时时间；data.aoes[].id (integer, 必填) - aoe id；data.aoes[].name (string, 必填) - aoe名称；data.aoes[].trigger_type (object, 必填) - 简单固定周期触发；data.aoes[].trigger_type.SimpleRepeat (object, 必填) - 时间对象；data.aoes[].variables (array[array[any]], 必填) - 用户自定义的变量：变量名和表达式；data.commit_msg (string, 必填) - 版本描述；data.version (integer, 必填) - 版本号",
        func=mems_api.add_pscpu_aoes,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.aoes (array[AoeModel], 必填) - AOE列表；data.aoes[].actions (array[ActionEdge], 必填) - 动作列表；data.aoes[].actions[].action (string, 必填) - 无动作；data.aoes[].actions[].aoe_id (integer, 必填) - AOE id；data.aoes[].actions[].failure_mode (string, 必填) - 失败模式；data.aoes[].actions[].name (string, 必填) - 动作名称；data.aoes[].actions[].source_node (integer, 必填) - 源节点；data.aoes[].actions[].target_node (integer, 必填) - 目标节点；data.aoes[].events (array[EventNode], 必填) - 节点列表；data.aoes[].events[].aoe_id (integer, 必填) - AOE id；data.aoes[].events[].expr (object, 必填) - 表达式对象；data.aoes[].events[].id (integer, 必填) - 节点id；data.aoes[].events[].name (string, 必填) - 节点名；data.aoes[].events[].node_type (string, 必填) - 节点类型；data.aoes[].events[].timeout (integer, 必填) - 事件还未发生时等待超时时间；data.aoes[].id (integer, 必填) - aoe id；data.aoes[].name (string, 必填) - aoe名称；data.aoes[].trigger_type (object, 必填) - 简单固定周期触发；data.aoes[].trigger_type.SimpleRepeat (object, 必填) - 时间对象；data.aoes[].variables (array[array[any]], 必填) - 用户自定义的变量：变量名和表达式；data.commit_msg (string, 必填) - 版本描述；data.version (integer, 必填) - 版本号', 'children': [{'name': 'aoes', 'type': 'array[AoeModel]', 'required': True, 'description': 'AOE列表', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': 'AOE列表', 'children': [{'name': 'actions', 'type': 'array[ActionEdge]', 'required': True, 'description': '动作列表', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '动作列表', 'children': [{'name': 'action', 'type': 'string', 'required': True, 'description': '无动作'}, {'name': 'aoe_id', 'type': 'integer', 'required': True, 'description': 'AOE id'}, {'name': 'failure_mode', 'type': 'string', 'required': True, 'description': '失败模式'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '动作名称'}, {'name': 'source_node', 'type': 'integer', 'required': True, 'description': '源节点'}, {'name': 'target_node', 'type': 'integer', 'required': True, 'description': '目标节点'}]}]}, {'name': 'events', 'type': 'array[EventNode]', 'required': True, 'description': '节点列表', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '节点列表', 'children': [{'name': 'aoe_id', 'type': 'integer', 'required': True, 'description': 'AOE id'}, {'name': 'expr', 'type': 'object', 'required': True, 'description': '表达式对象', 'children': [{'name': 'rpn', 'type': 'array[Token]', 'required': True, 'description': '', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '', 'children': [{'name': 'Binary', 'type': 'string', 'required': True, 'description': 'Mathematical operations.'}]}]}]}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '节点id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '节点名'}, {'name': 'node_type', 'type': 'string', 'required': True, 'description': '节点类型'}, {'name': 'timeout', 'type': 'integer', 'required': True, 'description': '事件还未发生时等待超时时间'}]}]}, {'name': 'id', 'type': 'integer', 'required': True, 'description': 'aoe id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': 'aoe名称'}, {'name': 'trigger_type', 'type': 'object', 'required': True, 'description': '简单固定周期触发', 'children': [{'name': 'SimpleRepeat', 'type': 'object', 'required': True, 'description': '时间对象', 'children': [{'name': 'nanos', 'type': 'integer', 'required': True, 'description': '剩余纳秒'}, {'name': 'secs', 'type': 'integer', 'required': True, 'description': '秒'}]}]}, {'name': 'variables', 'type': 'array[array[any]]', 'required': True, 'description': '用户自定义的变量：变量名和表达式'}]}]}, {'name': 'commit_msg', 'type': 'string', 'required': True, 'description': '版本描述'}, {'name': 'version', 'type': 'integer', 'required': True, 'description': '版本号'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_pscpu_aoes_models",
        description="查询当前应用的AOE",
        func=mems_api.get_pscpu_aoes_models,
    ))

    tools.append(ToolInfo(
        name="get_pscpu_aoes_version",
        description="查询当前应用的AOE版本号",
        func=mems_api.get_pscpu_aoes_version,
    ))

    tools.append(ToolInfo(
        name="get_pscpu_info",
        description="查询配置信息",
        func=mems_api.get_pscpu_info,
    ))

    tools.append(ToolInfo(
        name="add_pscpu_island",
        description="更新当前应用的电气岛。参数：data (object) - 请求体数据，字段：data.commit_msg (string, 必填) - 版本描述；data.island (object, 必填) - 电气岛，即集合；data.island.cns (array[CN], 必填) - 连接节点列表；data.island.cns[].id (integer, 必填) - 连接节点id；data.island.cns[].psr_id (string, 必填) - 资源id；data.island.cns[].terminals (array[integer], 必填) - 端子id数组；data.island.measures (object, 必填) - 测点，设备id->测点列表；data.island.prop_groups (object, 必填) - 属性分组，属性分组id->属性分组；data.island.resources (object, 必填) - 资源，设备id->资源对象；data.prop_defs (array[PropDefine], 必填) - 属性定义数组；data.prop_defs[].data_type (string, 必填) - 属性类型；data.prop_defs[].data_unit (string, 必填) - 数据单位；data.prop_defs[].desc (string, 必填) - 属性定义描述；data.prop_defs[].id (integer, 必填) - 属性定义id；data.prop_defs[].name (string, 必填) - 属性定义标识；data.rsr_defs (array[RsrDefine], 必填) - 设备定义数组；data.rsr_defs[].desc (string, 必填) - 设备定义的描述；data.rsr_defs[].id (integer, 必填) - 定义id；data.rsr_defs[].name (string, 必填) - 设备类别名称；data.rsr_defs[].prop_groups (array[PropGroupDefine], 必填) - 设备属性；data.rsr_defs[].prop_groups[].desc (string, 必填) - 属性定义描述；data.rsr_defs[].prop_groups[].name (string, 必填) - 属性定义标识；data.rsr_defs[].prop_groups[].prop_defines (array[integer], 必填) - 设备属性实际描述；data.rsr_defs[].rsr_type (string, 必填) - 电力设备类型；data.rsr_defs[].terminal_num (integer, 必填) - 端口数量；data.version (integer, 必填) - 版本号",
        func=mems_api.add_pscpu_island,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.commit_msg (string, 必填) - 版本描述；data.island (object, 必填) - 电气岛，即集合；data.island.cns (array[CN], 必填) - 连接节点列表；data.island.cns[].id (integer, 必填) - 连接节点id；data.island.cns[].psr_id (string, 必填) - 资源id；data.island.cns[].terminals (array[integer], 必填) - 端子id数组；data.island.measures (object, 必填) - 测点，设备id->测点列表；data.island.prop_groups (object, 必填) - 属性分组，属性分组id->属性分组；data.island.resources (object, 必填) - 资源，设备id->资源对象；data.prop_defs (array[PropDefine], 必填) - 属性定义数组；data.prop_defs[].data_type (string, 必填) - 属性类型；data.prop_defs[].data_unit (string, 必填) - 数据单位；data.prop_defs[].desc (string, 必填) - 属性定义描述；data.prop_defs[].id (integer, 必填) - 属性定义id；data.prop_defs[].name (string, 必填) - 属性定义标识；data.rsr_defs (array[RsrDefine], 必填) - 设备定义数组；data.rsr_defs[].desc (string, 必填) - 设备定义的描述；data.rsr_defs[].id (integer, 必填) - 定义id；data.rsr_defs[].name (string, 必填) - 设备类别名称；data.rsr_defs[].prop_groups (array[PropGroupDefine], 必填) - 设备属性；data.rsr_defs[].prop_groups[].desc (string, 必填) - 属性定义描述；data.rsr_defs[].prop_groups[].name (string, 必填) - 属性定义标识；data.rsr_defs[].prop_groups[].prop_defines (array[integer], 必填) - 设备属性实际描述；data.rsr_defs[].rsr_type (string, 必填) - 电力设备类型；data.rsr_defs[].terminal_num (integer, 必填) - 端口数量；data.version (integer, 必填) - 版本号', 'children': [{'name': 'commit_msg', 'type': 'string', 'required': True, 'description': '版本描述'}, {'name': 'island', 'type': 'object', 'required': True, 'description': '电气岛，即集合', 'children': [{'name': 'cns', 'type': 'array[CN]', 'required': True, 'description': '连接节点列表', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '连接节点列表', 'children': [{'name': 'id', 'type': 'integer', 'required': True, 'description': '连接节点id'}, {'name': 'psr_id', 'type': 'string', 'required': True, 'description': '资源id'}, {'name': 'terminals', 'type': 'array[integer]', 'required': True, 'description': '端子id数组'}]}]}, {'name': 'measures', 'type': 'object', 'required': True, 'description': '测点，设备id->测点列表'}, {'name': 'prop_groups', 'type': 'object', 'required': True, 'description': '属性分组，属性分组id->属性分组'}, {'name': 'resources', 'type': 'object', 'required': True, 'description': '资源，设备id->资源对象'}]}, {'name': 'prop_defs', 'type': 'array[PropDefine]', 'required': True, 'description': '属性定义数组', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '属性定义数组', 'children': [{'name': 'data_type', 'type': 'string', 'required': True, 'description': '属性类型'}, {'name': 'data_unit', 'type': 'string', 'required': True, 'description': '数据单位'}, {'name': 'desc', 'type': 'string', 'required': True, 'description': '属性定义描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '属性定义id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '属性定义标识'}]}]}, {'name': 'rsr_defs', 'type': 'array[RsrDefine]', 'required': True, 'description': '设备定义数组', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '设备定义数组', 'children': [{'name': 'desc', 'type': 'string', 'required': True, 'description': '设备定义的描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '定义id'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '设备类别名称'}, {'name': 'prop_groups', 'type': 'array[PropGroupDefine]', 'required': True, 'description': '设备属性', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '设备属性', 'children': [{'name': 'desc', 'type': 'string', 'required': True, 'description': '属性定义描述'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '属性定义标识'}, {'name': 'prop_defines', 'type': 'array[integer]', 'required': True, 'description': '设备属性实际描述'}]}]}, {'name': 'rsr_type', 'type': 'string', 'required': True, 'description': '电力设备类型'}, {'name': 'terminal_num', 'type': 'integer', 'required': True, 'description': '端口数量'}]}]}, {'name': 'version', 'type': 'integer', 'required': True, 'description': '版本号'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_pscpu_island_models",
        description="查询当前应用的电气岛",
        func=mems_api.get_pscpu_island_models,
    ))

    tools.append(ToolInfo(
        name="get_pscpu_island_paths",
        description="查询所有的测点路径（设备树）",
        func=mems_api.get_pscpu_island_paths,
    ))

    tools.append(ToolInfo(
        name="get_pscpu_island_point_tree",
        description="查询测点树",
        func=mems_api.get_pscpu_island_point_tree,
    ))

    tools.append(ToolInfo(
        name="get_pscpu_island_version",
        description="查询当前应用的电气岛版本号",
        func=mems_api.get_pscpu_island_version,
    ))

    tools.append(ToolInfo(
        name="add_pscpu_points",
        description="更新当前应用的测点。参数：data (object) - 请求体数据，字段：data.beeid_to_points (array[array[any]], 必填) - beeId和测点列表对应的数组，tuple格式为(beeId:String, 测点列表:u64[])；data.commit_msg (string, 必填) - 版本描述；data.points (array[Measurement], 必填) - 测点列表；data.points[].alarm_level1_expr (string, 必填) - 告警级别1的表达式；data.points[].alarm_level2_expr (string, 必填) - 告警级别2的表达式；data.points[].alias_id (string, 必填) - 字符串id；data.points[].change_expr (string, 必填) - 判断是否\\\"变化\\\"的公式，用于变化上传或储存；data.points[].data_unit (string, 必填) - 单位；data.points[].desc (string, 必填) - Description；data.points[].expression (string, 必填) - 如果是计算点，这是表达式；data.points[].init_value (integer, 必填) - 默认值存储在8个字节，需要根据is_discrete来转换成具体的值；data.points[].inv_trans_expr (string, 必填) - 逆变换公式；data.points[].is_computing_point (boolean, 必填) - 是否是计算点；data.points[].is_discrete (boolean, 必填) - 是否是离散量；data.points[].is_realtime (boolean, 必填) - 如是，则不判断是否\\\"变化\\\"，均上传；data.points[].is_soe (boolean, 必填) - 是否是soe点；data.points[].lower_limit (number, 必填) - 下限，用于坏数据辨识；data.points[].point_id (integer, 必填) - 唯一的id；data.points[].point_name (string, 必填) - 测点名；data.points[].trans_expr (string, 必填) - 变换公式；data.points[].upper_limit (number, 必填) - 上限，用于坏数据辨识；data.points[].zero_expr (string, 必填) - 判断是否为0值的公式；data.source_name (array[array[any]], 必填)；data.version (integer, 必填) - 版本号",
        func=mems_api.add_pscpu_points,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.beeid_to_points (array[array[any]], 必填) - beeId和测点列表对应的数组，tuple格式为(beeId:String, 测点列表:u64[])；data.commit_msg (string, 必填) - 版本描述；data.points (array[Measurement], 必填) - 测点列表；data.points[].alarm_level1_expr (string, 必填) - 告警级别1的表达式；data.points[].alarm_level2_expr (string, 必填) - 告警级别2的表达式；data.points[].alias_id (string, 必填) - 字符串id；data.points[].change_expr (string, 必填) - 判断是否\\"变化\\"的公式，用于变化上传或储存；data.points[].data_unit (string, 必填) - 单位；data.points[].desc (string, 必填) - Description；data.points[].expression (string, 必填) - 如果是计算点，这是表达式；data.points[].init_value (integer, 必填) - 默认值存储在8个字节，需要根据is_discrete来转换成具体的值；data.points[].inv_trans_expr (string, 必填) - 逆变换公式；data.points[].is_computing_point (boolean, 必填) - 是否是计算点；data.points[].is_discrete (boolean, 必填) - 是否是离散量；data.points[].is_realtime (boolean, 必填) - 如是，则不判断是否\\"变化\\"，均上传；data.points[].is_soe (boolean, 必填) - 是否是soe点；data.points[].lower_limit (number, 必填) - 下限，用于坏数据辨识；data.points[].point_id (integer, 必填) - 唯一的id；data.points[].point_name (string, 必填) - 测点名；data.points[].trans_expr (string, 必填) - 变换公式；data.points[].upper_limit (number, 必填) - 上限，用于坏数据辨识；data.points[].zero_expr (string, 必填) - 判断是否为0值的公式；data.source_name (array[array[any]], 必填)；data.version (integer, 必填) - 版本号', 'children': [{'name': 'beeid_to_points', 'type': 'array[array[any]]', 'required': True, 'description': 'beeId和测点列表对应的数组，tuple格式为(beeId:String, 测点列表:u64[])'}, {'name': 'commit_msg', 'type': 'string', 'required': True, 'description': '版本描述'}, {'name': 'points', 'type': 'array[Measurement]', 'required': True, 'description': '测点列表', 'children': [{'name': '[]', 'type': 'object', 'required': True, 'description': '测点列表', 'children': [{'name': 'alarm_level1_expr', 'type': 'string', 'required': True, 'description': '告警级别1的表达式'}, {'name': 'alarm_level2_expr', 'type': 'string', 'required': True, 'description': '告警级别2的表达式'}, {'name': 'alias_id', 'type': 'string', 'required': True, 'description': '字符串id'}, {'name': 'change_expr', 'type': 'string', 'required': True, 'description': '判断是否"变化"的公式，用于变化上传或储存'}, {'name': 'data_unit', 'type': 'string', 'required': True, 'description': '单位'}, {'name': 'desc', 'type': 'string', 'required': True, 'description': 'Description'}, {'name': 'expression', 'type': 'string', 'required': True, 'description': '如果是计算点，这是表达式'}, {'name': 'init_value', 'type': 'integer', 'required': True, 'description': '默认值存储在8个字节，需要根据is_discrete来转换成具体的值'}, {'name': 'inv_trans_expr', 'type': 'string', 'required': True, 'description': '逆变换公式'}, {'name': 'is_computing_point', 'type': 'boolean', 'required': True, 'description': '是否是计算点'}, {'name': 'is_discrete', 'type': 'boolean', 'required': True, 'description': '是否是离散量'}, {'name': 'is_realtime', 'type': 'boolean', 'required': True, 'description': '如是，则不判断是否"变化"，均上传'}, {'name': 'is_soe', 'type': 'boolean', 'required': True, 'description': '是否是soe点'}, {'name': 'lower_limit', 'type': 'number', 'required': True, 'description': '下限，用于坏数据辨识'}, {'name': 'point_id', 'type': 'integer', 'required': True, 'description': '唯一的id'}, {'name': 'point_name', 'type': 'string', 'required': True, 'description': '测点名'}, {'name': 'trans_expr', 'type': 'string', 'required': True, 'description': '变换公式'}, {'name': 'upper_limit', 'type': 'number', 'required': True, 'description': '上限，用于坏数据辨识'}, {'name': 'zero_expr', 'type': 'string', 'required': True, 'description': '判断是否为0值的公式'}]}]}, {'name': 'source_name', 'type': 'array[array[any]]', 'required': True, 'description': ''}, {'name': 'version', 'type': 'integer', 'required': True, 'description': '版本号'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_pscpu_points_by_dev",
        description="查询设备关联的测点。参数：dev_id (integer, 必填) - 设备id",
        func=mems_api.get_pscpu_points_by_dev,
        parameters=[
            {'name': 'dev_id', 'type': 'integer', 'required': True, 'description': '设备id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_pscpu_points_models",
        description="查询当前应用的测点。参数：id (string, 可选) - , name (string, 可选) - , is_soe (boolean, 可选) - ",
        func=mems_api.get_pscpu_points_models,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': False, 'description': ''},
            {'name': 'name', 'type': 'string', 'required': False, 'description': ''},
            {'name': 'is_soe', 'type': 'boolean', 'required': False, 'description': ''},
        ]
    ))

    tools.append(ToolInfo(
        name="get_pscpu_points_values_by_src",
        description="查询量测值。参数：src (integer, 必填) - , id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_pscpu_points_values_by_src,
        parameters=[
            {'name': 'src', 'type': 'integer', 'required': True, 'description': ''},
            {'name': 'id', 'type': 'integer', 'required': False, 'description': '测点id（优先）'},
            {'name': 'ids', 'type': 'string', 'required': False, 'description': '测点id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_pscpu_points_version",
        description="查询当前应用的测点版本号",
        func=mems_api.get_pscpu_points_version,
    ))

    tools.append(ToolInfo(
        name="add_pscpu_reset",
        description="重置pscpu",
        func=mems_api.add_pscpu_reset,
    ))

    tools.append(ToolInfo(
        name="add_pscpu_start",
        description="启动pscpu。参数：data (string) - 请求体数据，字段：data (string)",
        func=mems_api.add_pscpu_start,
        parameters=[
            {'name': 'data', 'type': 'string', 'required': True, 'description': '请求体数据；字段：data (string)'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_pscpu_stop",
        description="停止pscpu",
        func=mems_api.add_pscpu_stop,
    ))

    tools.append(ToolInfo(
        name="get_running_aoes",
        description="查询当前运行中的AOE",
        func=mems_api.get_running_aoes,
    ))

    tools.append(ToolInfo(
        name="get_script_file_by_script",
        description="查询7z脚本文件。参数：script_id (integer, 必填) - 脚本id",
        func=mems_api.get_script_file_by_script,
        parameters=[
            {'name': 'script_id', 'type': 'integer', 'required': True, 'description': '脚本id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_script_md5",
        description="查询脚本md5。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_script_md5,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': False, 'description': '测点id（优先）'},
            {'name': 'ids', 'type': 'string', 'required': False, 'description': '测点id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_script_results",
        description="查询所有脚本结果",
        func=mems_api.get_script_results,
    ))

    tools.append(ToolInfo(
        name="add_script_results",
        description="新增脚本结果。参数：data (object) - 请求体数据，字段：data.make_time (integer, 必填)；data.model_id (integer, 必填)；data.script_id (integer, 必填)；data.target (string, 必填)",
        func=mems_api.add_script_results,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.make_time (integer, 必填)；data.model_id (integer, 必填)；data.script_id (integer, 必填)；data.target (string, 必填)', 'children': [{'name': 'make_time', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'model_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'script_id', 'type': 'integer', 'required': True, 'description': ''}, {'name': 'target', 'type': 'string', 'required': True, 'description': ''}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_script_results_by",
        description="查询指定id脚本结果。参数：id (integer, 必填) - 脚本结果id",
        func=mems_api.get_script_results_by,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '脚本结果id'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_script_wasm",
        description="保存脚本对应的wasm和js文件。参数：data (object) - 请求体数据，字段：data.js_file (array[integer], 必填) - js文件内容；data.module_name (string, 必填) - 模块名称；data.script_id (integer, 必填) - 脚本id；data.wasm_file (array[integer], 必填) - wasm文件内容",
        func=mems_api.add_script_wasm,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.js_file (array[integer], 必填) - js文件内容；data.module_name (string, 必填) - 模块名称；data.script_id (integer, 必填) - 脚本id；data.wasm_file (array[integer], 必填) - wasm文件内容', 'children': [{'name': 'js_file', 'type': 'array[integer]', 'required': True, 'description': 'js文件内容'}, {'name': 'module_name', 'type': 'string', 'required': True, 'description': '模块名称'}, {'name': 'script_id', 'type': 'integer', 'required': True, 'description': '脚本id'}, {'name': 'wasm_file', 'type': 'array[integer]', 'required': True, 'description': 'wasm文件内容'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_scripts",
        description="查询指定id脚本。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_scripts,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': False, 'description': '测点id（优先）'},
            {'name': 'ids', 'type': 'string', 'required': False, 'description': '测点id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_scripts",
        description="新增脚本。参数：data (object) - 请求体数据，字段：data.desc (string, 必填) - 脚本描述；data.id (integer, 必填) - 脚本id；data.is_file_uploaded (boolean, 必填) - 文件是否已上传；data.is_js (boolean, 必填) - 是否是javascript文件；data.path (string, 必填) - 脚本路径；data.target (string, 必填) - 脚本目标；data.wasm_module_name (string, 必填) - wasm模块名称；data.wasm_update_time (integer, 必填) - wasm上传时间",
        func=mems_api.add_scripts,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.desc (string, 必填) - 脚本描述；data.id (integer, 必填) - 脚本id；data.is_file_uploaded (boolean, 必填) - 文件是否已上传；data.is_js (boolean, 必填) - 是否是javascript文件；data.path (string, 必填) - 脚本路径；data.target (string, 必填) - 脚本目标；data.wasm_module_name (string, 必填) - wasm模块名称；data.wasm_update_time (integer, 必填) - wasm上传时间', 'children': [{'name': 'desc', 'type': 'string', 'required': True, 'description': '脚本描述'}, {'name': 'id', 'type': 'integer', 'required': True, 'description': '脚本id'}, {'name': 'is_file_uploaded', 'type': 'boolean', 'required': True, 'description': '文件是否已上传'}, {'name': 'is_js', 'type': 'boolean', 'required': True, 'description': '是否是javascript文件'}, {'name': 'path', 'type': 'string', 'required': True, 'description': '脚本路径'}, {'name': 'target', 'type': 'string', 'required': True, 'description': '脚本目标'}, {'name': 'wasm_module_name', 'type': 'string', 'required': True, 'description': 'wasm模块名称'}, {'name': 'wasm_update_time', 'type': 'integer', 'required': True, 'description': 'wasm上传时间'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_scripts_by_s",
        description="删除指定id的脚本。参数：ids (string, 必填) - 脚本id列表，以,间隔",
        func=mems_api.delete_scripts_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '脚本id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_soes",
        description="查询SOE，结果按照时间排序。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_soes,
        parameters=[
            {'name': 'id', 'type': 'string', 'required': False, 'description': '测点id，多个id之间以,间隔'},
            {'name': 'start', 'type': 'integer', 'required': False, 'description': '开始时间, 13位时间戳'},
            {'name': 'end', 'type': 'integer', 'required': False, 'description': '结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end'},
            {'name': 'date', 'type': 'string', 'required': False, 'description': '时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准'},
            {'name': 'source', 'type': 'integer', 'required': False, 'description': '数据源'},
            {'name': 'last_only', 'type': 'boolean', 'required': False, 'description': '是否查询只最新的数据'},
            {'name': 'with_init', 'type': 'boolean', 'required': False, 'description': '是否查询该天初始的数据'},
            {'name': 'reverse_order', 'type': 'boolean', 'required': False, 'description': '是否时间倒序查询'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_tag_defines_by_group",
        description="查询指定分组的标签名称及id列表。参数：id (integer, 必填) - 分组id, group (integer, 必填) - ",
        func=mems_api.get_tag_defines_by_group,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '分组id'},
            {'name': 'group', 'type': 'integer', 'required': True, 'description': ''},
        ]
    ))

    tools.append(ToolInfo(
        name="update_tags_by_group",
        description="更新指定分组下标签名和测点数组关系。参数：group (integer, 必填) - 分组id, data (array[array[any]]) - 请求体数据，字段：data (array[array[any]])",
        func=mems_api.update_tags_by_group,
        parameters=[
            {'name': 'group', 'type': 'integer', 'required': True, 'description': '分组id'},
            {'name': 'data', 'type': 'array[array[any]]', 'required': True, 'description': '请求体数据；字段：data (array[array[any]])'},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_tags_by_group",
        description="删除指定分组下标签id和测点的关系。参数：group (integer, 必填) - 分组id, data (array[array[any]]) - 请求体数据，字段：data (array[array[any]])",
        func=mems_api.delete_tags_by_group,
        parameters=[
            {'name': 'group', 'type': 'integer', 'required': True, 'description': '分组id'},
            {'name': 'data', 'type': 'array[array[any]]', 'required': True, 'description': '请求体数据；字段：data (array[array[any]])'},
        ]
    ))

    tools.append(ToolInfo(
        name="add_tags_cbor_by_group",
        description="查询指定分组下标签id对应的测点数组。参数：id (integer, 必填) - 分组id, group (integer, 必填) - , data (array[integer]) - 请求体数据，字段：data (array[integer])",
        func=mems_api.add_tags_cbor_by_group,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': True, 'description': '分组id'},
            {'name': 'group', 'type': 'integer', 'required': True, 'description': ''},
            {'name': 'data', 'type': 'array[integer]', 'required': True, 'description': '请求体数据；字段：data (array[integer])'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_unrun_aoes",
        description="查询未运行的AOE",
        func=mems_api.get_unrun_aoes,
    ))

    tools.append(ToolInfo(
        name="add_webplugin_file",
        description="保存插件对应的file。参数：data (object) - 请求体数据，字段：data.plugin_id (integer, 必填) - 插件id；data.sevenz_file (array[integer], 必填) - 内容",
        func=mems_api.add_webplugin_file,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.plugin_id (integer, 必填) - 插件id；data.sevenz_file (array[integer], 必填) - 内容', 'children': [{'name': 'plugin_id', 'type': 'integer', 'required': True, 'description': '插件id'}, {'name': 'sevenz_file', 'type': 'array[integer]', 'required': True, 'description': '内容'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="get_webplugin_file_by_plugin",
        description="查询插件对应的压缩文件。参数：plugin_id (integer, 必填) - 插件id",
        func=mems_api.get_webplugin_file_by_plugin,
        parameters=[
            {'name': 'plugin_id', 'type': 'integer', 'required': True, 'description': '插件id'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_webplugin_md5",
        description="查询插件md5。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_webplugin_md5,
        parameters=[
            {'name': 'id', 'type': 'integer', 'required': False, 'description': '测点id（优先）'},
            {'name': 'ids', 'type': 'string', 'required': False, 'description': '测点id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_webplugins",
        description="查询所有界面插件",
        func=mems_api.get_webplugins,
    ))

    tools.append(ToolInfo(
        name="add_webplugins",
        description="新增插件。参数：data (object) - 请求体数据，字段：data.id (integer, 必填) - 插件id；data.is_file_uploaded (boolean, 必填) - 文件是否已经上传；data.is_monopoly (boolean, 必填) - if is only one view；data.model_name (string, 必填) - wasm或js或html文件的名称；data.name (string, 必填) - 在浏览模式下显示的名称；data.path (string, 必填) - 文件树中的路径",
        func=mems_api.add_webplugins,
        parameters=[
            {'name': 'data', 'type': 'object', 'required': True, 'description': '请求体数据；字段：data.id (integer, 必填) - 插件id；data.is_file_uploaded (boolean, 必填) - 文件是否已经上传；data.is_monopoly (boolean, 必填) - if is only one view；data.model_name (string, 必填) - wasm或js或html文件的名称；data.name (string, 必填) - 在浏览模式下显示的名称；data.path (string, 必填) - 文件树中的路径', 'children': [{'name': 'id', 'type': 'integer', 'required': True, 'description': '插件id'}, {'name': 'is_file_uploaded', 'type': 'boolean', 'required': True, 'description': '文件是否已经上传'}, {'name': 'is_monopoly', 'type': 'boolean', 'required': True, 'description': 'if is only one view'}, {'name': 'model_name', 'type': 'string', 'required': True, 'description': 'wasm或js或html文件的名称'}, {'name': 'name', 'type': 'string', 'required': True, 'description': '在浏览模式下显示的名称'}, {'name': 'path', 'type': 'string', 'required': True, 'description': '文件树中的路径'}]},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_webplugins_by_s",
        description="删除指定id的插件。参数：ids (string, 必填) - 插件id列表，以,间隔",
        func=mems_api.delete_webplugins_by_s,
        parameters=[
            {'name': 'ids', 'type': 'string', 'required': True, 'description': '插件id列表，以,间隔'},
        ]
    ))

    tools.append(ToolInfo(
        name="get_webplugins_by_plugin",
        description="查询指定id插件。参数：plugin_id (integer, 必填) - 插件id",
        func=mems_api.get_webplugins_by_plugin,
        parameters=[
            {'name': 'plugin_id', 'type': 'integer', 'required': True, 'description': '插件id'},
        ]
    ))

    return tools
