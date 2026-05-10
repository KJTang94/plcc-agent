from typing import List, Dict, Any, Optional, TypedDict


class ParameterInfo(TypedDict):
    name: str
    type: str
    required: bool
    description: str


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
        description="配置告警通知。参数：data (dict) - 请求体数据",
        func=mems_api.add_alarm_config,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_alarm_confirm_by_user",
        description="确认告警。参数：user_id (integer, 必填) - 用户id, data (dict) - 请求体数据",
        func=mems_api.add_alarm_confirm_by_user,
        parameters=[
            {"name": "user_id", "type": "integer", "required": True, "description": "用户id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
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
        description="上传单个告警定义。参数：data (dict) - 请求体数据",
        func=mems_api.add_alarm_define,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_alarm_define_by",
        description="查询指定id的告警定义。参数：id (integer, 必填) - 告警定义id",
        func=mems_api.get_alarm_define_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "告警定义id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_alarm_defines",
        description="查询所有的告警定义",
        func=mems_api.get_alarm_defines,
    ))

    tools.append(ToolInfo(
        name="add_alarm_defines",
        description="上传告警定义。参数：data (dict) - 请求体数据",
        func=mems_api.add_alarm_defines,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_alarm_defines_by_s",
        description="删除指定id的告警定义。参数：ids (string, 必填) - 告警定义id列表，以,间隔",
        func=mems_api.delete_alarm_defines_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "告警定义id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_alarm_defines_file",
        description="上传告警定义（文件形式）。参数：data (dict) - 请求体数据",
        func=mems_api.add_alarm_defines_file,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
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
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
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
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_aoes_models",
        description="查询所有AOE",
        func=mems_api.get_aoes_models,
    ))

    tools.append(ToolInfo(
        name="add_aoes_models",
        description="保存AOE。参数：data (dict) - 请求体数据",
        func=mems_api.add_aoes_models,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_aoes_models_by_version_by_v",
        description="查询指定版本的AOE。参数：v (integer, 必填) - 版本id",
        func=mems_api.get_aoes_models_by_version_by_v,
        parameters=[
            {"name": "v", "type": "integer", "required": True, "description": "版本id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_aoes_models_for_apply",
        description="查询根据版本号组装的AOE应用对象。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_aoes_models_for_apply,
        parameters=[
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_aoes_models_by_s",
        description="删除指定id的AOE。参数：ids (string, 必填) - AOE_id列表，以,间隔",
        func=mems_api.delete_aoes_models_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "AOE_id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_aoes_models_by",
        description="根据id查询指定的AOE。参数：id (integer, 必填) - AOE_id, version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_aoes_models_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "AOE_id"},
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_aoes_models_file",
        description="保存AOE（文件形式）。参数：data (dict) - 请求体数据",
        func=mems_api.add_aoes_models_file,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_aoes_models_file2",
        description="保存AOE（多文件形式）。参数：data (dict) - 请求体数据",
        func=mems_api.add_aoes_models_file2,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_aoes_version",
        description="查询所有的AOE版本信息",
        func=mems_api.get_aoes_version,
    ))

    tools.append(ToolInfo(
        name="add_aoes_version",
        description="新增AOE版本。参数：data (dict) - 请求体数据",
        func=mems_api.add_aoes_version,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_aoes_version_by_v",
        description="删除某一个AOE版本。参数：v (integer, 必填) - 版本id",
        func=mems_api.delete_aoes_version_by_v,
        parameters=[
            {"name": "v", "type": "integer", "required": True, "description": "版本id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_auths",
        description="查询所有权限",
        func=mems_api.get_auth_auths,
    ))

    tools.append(ToolInfo(
        name="add_auth_auths",
        description="新增权限。参数：data (dict) - 请求体数据",
        func=mems_api.add_auth_auths,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_auths_by_role",
        description="查询指定角色的所有权限。参数：id (integer, 必填) - 角色id",
        func=mems_api.get_auth_auths_by_role,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "角色id"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_auth_auths_by_s",
        description="删除指定id的删除权限。参数：ids (string, 必填) - 权限id列表，以,间隔",
        func=mems_api.delete_auth_auths_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "权限id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_auth_login",
        description="执行登录。参数：data (dict) - 请求体数据",
        func=mems_api.add_auth_login,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_menus",
        description="查询所有菜单",
        func=mems_api.get_auth_menus,
    ))

    tools.append(ToolInfo(
        name="add_auth_menus",
        description="新增菜单。参数：data (dict) - 请求体数据",
        func=mems_api.add_auth_menus,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_menus_by_role",
        description="查询指定角色的所有菜单。参数：id (integer, 必填) - 角色id",
        func=mems_api.get_auth_menus_by_role,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "角色id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_menus_by_user",
        description="查询指定用户的所有菜单。参数：id (integer, 必填) - 用户id",
        func=mems_api.get_auth_menus_by_user,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "用户id"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_auth_menus_by_s",
        description="删除指定id的菜单。参数：ids (string, 必填) - 菜单id列表，以,间隔",
        func=mems_api.delete_auth_menus_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "菜单id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_auth_register",
        description="用户注册。参数：data (dict) - 请求体数据",
        func=mems_api.add_auth_register,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_roles",
        description="查询所有角色",
        func=mems_api.get_auth_roles,
    ))

    tools.append(ToolInfo(
        name="update_auth_roles",
        description="修改角色。参数：data (dict) - 请求体数据",
        func=mems_api.update_auth_roles,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_auth_roles",
        description="新增角色。参数：data (dict) - 请求体数据",
        func=mems_api.add_auth_roles,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_roles_by_s",
        description="根据ids查询角色。参数：ids (string, 必填) - 角色id列表，以,间隔",
        func=mems_api.get_auth_roles_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "角色id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_auth_roles_by_s",
        description="删除指定id的删除角色。参数：ids (string, 必填) - 角色id列表，以,间隔",
        func=mems_api.delete_auth_roles_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "角色id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_user_groups",
        description="查询所有用户组",
        func=mems_api.get_auth_user_groups,
    ))

    tools.append(ToolInfo(
        name="update_auth_user_groups",
        description="修改用户组。参数：data (dict) - 请求体数据",
        func=mems_api.update_auth_user_groups,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_auth_user_groups",
        description="新增用户组。参数：data (dict) - 请求体数据",
        func=mems_api.add_auth_user_groups,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_auth_user_groups_by_s",
        description="删除指定id的用户组。参数：ids (string, 必填) - 用户组id列表，以,间隔",
        func=mems_api.delete_auth_user_groups_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "用户组id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_user_groups_by",
        description="查询指定id用户组。参数：id (integer, 必填) - 用户组id",
        func=mems_api.get_auth_user_groups_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "用户组id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_users",
        description="查询所有用户",
        func=mems_api.get_auth_users,
    ))

    tools.append(ToolInfo(
        name="update_auth_users",
        description="修改用户。参数：data (dict) - 请求体数据",
        func=mems_api.update_auth_users,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_auth_users",
        description="新增用户。参数：data (dict) - 请求体数据",
        func=mems_api.add_auth_users,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_users_by_user_group",
        description="根据分组id查询用户信息。参数：id (integer, 必填) - 分组id",
        func=mems_api.get_auth_users_by_user_group,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "分组id"},
        ]
    ))

    tools.append(ToolInfo(
        name="update_auth_users_password_by",
        description="更改用户密码。参数：id (integer, 必填) - 用户id, data (dict) - 请求体数据",
        func=mems_api.update_auth_users_password_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "用户id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="update_auth_users_reset_password_by",
        description="重置用户密码。参数：id (integer, 必填) - 用户id",
        func=mems_api.update_auth_users_reset_password_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "用户id"},
        ]
    ))

    tools.append(ToolInfo(
        name="update_auth_users_roles_by",
        description="绑定已有用户的角色信息。参数：id (integer, 必填) - 用户id, data (dict) - 请求体数据",
        func=mems_api.update_auth_users_roles_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "用户id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_auth_users_by_s",
        description="删除指定id的用户。参数：ids (string, 必填) - 用户id列表，以,间隔",
        func=mems_api.delete_auth_users_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "用户id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_auth_users_by",
        description="查询指定id用户。参数：id (integer, 必填) - 用户id",
        func=mems_api.get_auth_users_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "用户id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_commands",
        description="查询历史设点执行结果。参数：sender_id (integer, 可选) - , point_id (integer, 可选) - 测点id, start (integer, 可选) - 开始时间, end (integer, 可选) - 结束时间, date (string, 可选) - 时间字符串，yyyy-MM-dd, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_commands,
        parameters=[
            {"name": "sender_id", "type": "integer", "required": False, "description": ""},
            {"name": "point_id", "type": "integer", "required": False, "description": "测点id"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_common_map",
        description="执行map映射操作。参数：data (dict) - 请求体数据",
        func=mems_api.add_common_map,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_config",
        description="查询Eig配置",
        func=mems_api.get_config,
    ))

    tools.append(ToolInfo(
        name="add_config",
        description="保存Eig配置。参数：data (dict) - 请求体数据",
        func=mems_api.add_config,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_controls_aoes",
        description="对指定id的AOE采取指定动作，启动/停止/更新。参数：data (dict) - 请求体数据",
        func=mems_api.add_controls_aoes,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_controls_points",
        description="执行测点控制。参数：data (dict) - 请求体数据",
        func=mems_api.add_controls_points,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_controls_points_by_alias",
        description="执行测点控制（通过别名）。参数：data (dict) - 请求体数据",
        func=mems_api.add_controls_points_by_alias,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_controls_points_by_expr",
        description="执行测点控制（通过公式）。参数：data (dict) - 请求体数据",
        func=mems_api.add_controls_points_by_expr,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_controls_points_with_source_by_source",
        description="执行测点控制（通过其他数据源）。参数：source (integer, 必填) - 数据源id, data (dict) - 请求体数据",
        func=mems_api.add_controls_points_with_source_by_source,
        parameters=[
            {"name": "source", "type": "integer", "required": True, "description": "数据源id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_cns",
        description="查询拓扑。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_cns,
        parameters=[
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_cns",
        description="新增拓扑。参数：data (dict) - 请求体数据",
        func=mems_api.add_devices_cns,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_defines",
        description="查询所有设备定义",
        func=mems_api.get_devices_defines,
    ))

    tools.append(ToolInfo(
        name="update_devices_defines",
        description="修改设备定义。参数：data (dict) - 请求体数据",
        func=mems_api.update_devices_defines,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_defines",
        description="新增设备定义。参数：data (dict) - 请求体数据",
        func=mems_api.add_devices_defines,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_defines_by_s",
        description="删除指定id的设备定义。参数：ids (string, 必填) - 设备定义id列表，以,间隔",
        func=mems_api.delete_devices_defines_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "设备定义id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_defines_by",
        description="根据id查询对应的设备定义。参数：id (integer, 必填) - 设备定义id",
        func=mems_api.get_devices_defines_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "设备定义id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_devs",
        description="查询所有设备列表。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_devs,
        parameters=[
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="update_devices_devs",
        description="修改设备。参数：data (dict) - 请求体数据",
        func=mems_api.update_devices_devs,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_devs",
        description="新增设备。参数：data (dict) - 请求体数据",
        func=mems_api.add_devices_devs,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_devs_by_s",
        description="删除指定id的设备。参数：ids (string, 必填) - 设备id列表，以,间隔",
        func=mems_api.delete_devices_devs_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "设备id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_devs_by",
        description="根据ID查询设备对象。参数：id (integer, 必填) - 设备id, version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_devs_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "设备id"},
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_islands",
        description="查询电气岛。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_islands,
        parameters=[
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_islands",
        description="根据版本号apply电气岛。参数：data (dict) - 请求体数据",
        func=mems_api.add_devices_islands,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_measure_defs",
        description="查询设备测点。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_measure_defs,
        parameters=[
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="update_devices_measure_defs",
        description="修改设备测点。参数：data (dict) - 请求体数据",
        func=mems_api.update_devices_measure_defs,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_measure_defs",
        description="新增设备测点。参数：data (dict) - 请求体数据",
        func=mems_api.add_devices_measure_defs,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_measure_defs",
        description="删除指定id的设备测点。参数：data (dict) - 请求体数据",
        func=mems_api.delete_devices_measure_defs,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_point_tree",
        description="查询测点树（测点在设备树中的路径）。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_point_tree,
        parameters=[
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_prop_defines",
        description="查询所有设备属性定义",
        func=mems_api.get_devices_prop_defines,
    ))

    tools.append(ToolInfo(
        name="update_devices_prop_defines",
        description="修改设备属性定义。参数：data (dict) - 请求体数据",
        func=mems_api.update_devices_prop_defines,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_prop_defines",
        description="新增设备属性定义。参数：data (dict) - 请求体数据",
        func=mems_api.add_devices_prop_defines,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_prop_defines_by_s",
        description="删除指定id的设备属性定义。参数：ids (string, 必填) - 设备属性定义id列表，以,间隔",
        func=mems_api.delete_devices_prop_defines_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "设备属性定义id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_prop_groups",
        description="查询所有设备属性分组。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_prop_groups,
        parameters=[
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="update_devices_prop_groups",
        description="修改设备属性分组。参数：data (dict) - 请求体数据",
        func=mems_api.update_devices_prop_groups,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_devices_prop_groups",
        description="新增设备属性分组。参数：data (dict) - 请求体数据",
        func=mems_api.add_devices_prop_groups,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_devices_prop_groups_by_s",
        description="根据id列表查看设备属性分组列表。参数：ids (string, 必填) - 设备属性分组id列表，以,间隔, version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_devices_prop_groups_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "设备属性分组id列表，以,间隔"},
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_prop_groups_by_s",
        description="删除指定id的设备属性分组。参数：ids (string, 必填) - 设备属性分组id列表，以,间隔",
        func=mems_api.delete_devices_prop_groups_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "设备属性分组id列表，以,间隔"},
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
        description="新增电气岛版本。参数：data (dict) - 请求体数据",
        func=mems_api.add_devices_version,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_devices_version_by",
        description="删除指定id的电气岛版本。参数：id (integer, 必填) - 版本id",
        func=mems_api.delete_devices_version_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "版本id"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_ems_request_by_ems",
        description="对指定id的ems执行请求。参数：ems_id (string, 必填) - ems_id, data (dict) - 请求体数据",
        func=mems_api.add_ems_request_by_ems,
        parameters=[
            {"name": "ems_id", "type": "string", "required": True, "description": "ems_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_ems_by",
        description="查询指定id的ems。参数：id (string, 必填) - ems_id",
        func=mems_api.get_ems_by,
        parameters=[
            {"name": "id", "type": "string", "required": True, "description": "ems_id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_ems_list",
        description="查询所有的ems",
        func=mems_api.get_ems_list,
    ))

    tools.append(ToolInfo(
        name="add_file_tree",
        description="执行filetree的操作。参数：data (dict) - 请求体数据",
        func=mems_api.add_file_tree,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_file_tree_by",
        description="保存filetree的一个节点。参数：id (string, 必填) - tree_id, data (dict) - 请求体数据",
        func=mems_api.add_file_tree_by,
        parameters=[
            {"name": "id", "type": "string", "required": True, "description": "tree_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_file_tree_version",
        description="提交filetree版本。参数：data (dict) - 请求体数据",
        func=mems_api.add_file_tree_version,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_brief_results",
        description="查询报表结果（简洁模式）。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_flows_brief_results,
        parameters=[
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_controls",
        description="执行报表动作。参数：data (dict) - 请求体数据",
        func=mems_api.add_flows_controls,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_debug",
        description="报表节点测试。参数：data (dict) - 请求体数据",
        func=mems_api.add_flows_debug,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_models",
        description="查询报表。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_flows_models,
        parameters=[
            {"name": "id", "type": "integer", "required": False, "description": "测点id（优先）"},
            {"name": "ids", "type": "string", "required": False, "description": "测点id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="update_flows_models",
        description="修改报表。参数：data (dict) - 请求体数据",
        func=mems_api.update_flows_models,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_models",
        description="新增报表。参数：data (dict) - 请求体数据",
        func=mems_api.add_flows_models,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_flows_models_by_s",
        description="删除指定id的报表。参数：ids (string, 必填) - 报表id列表，以,间隔",
        func=mems_api.delete_flows_models_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "报表id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_models_file2",
        description="新增报表（多文件形式）。参数：data (dict) - 请求体数据",
        func=mems_api.add_flows_models_file2,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_models_json",
        description="查询报表（自定义JSON格式）。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_flows_models_json,
        parameters=[
            {"name": "id", "type": "integer", "required": False, "description": "测点id（优先）"},
            {"name": "ids", "type": "string", "required": False, "description": "测点id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_prog_file2",
        description="解析prog（多文件形式）。参数：data (dict) - 请求体数据",
        func=mems_api.add_flows_prog_file2,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_reload_dff_by_flow",
        description="重新加载报表。参数：flow_id (string, 必填) - 报表id",
        func=mems_api.add_flows_reload_dff_by_flow,
        parameters=[
            {"name": "flow_id", "type": "string", "required": True, "description": "报表id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_result_keys",
        description="查询报表结果keys。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_flows_result_keys,
        parameters=[
            {"name": "id", "type": "integer", "required": False, "description": "测点id（优先）"},
            {"name": "ids", "type": "string", "required": False, "description": "测点id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_results",
        description="根据id查询报表执行结果。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_flows_results,
        parameters=[
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_flows_results",
        description="删除指定报表id指定key的报表结果。参数：data (dict) - 请求体数据",
        func=mems_api.delete_flows_results,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_results_rename",
        description="重命名报表结果（简洁模式）。参数：data (dict) - 请求体数据",
        func=mems_api.add_flows_results_rename,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="update_flows_results_by_by_key",
        description="query_flows_result_and_eval。参数：id (string, 必填) - 报表id, key (string, 必填) - key, data (dict) - 请求体数据",
        func=mems_api.update_flows_results_by_by_key,
        parameters=[
            {"name": "id", "type": "string", "required": True, "description": "报表id"},
            {"name": "key", "type": "string", "required": True, "description": "key"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_results_by_by_key_by_view",
        description="query_flows_result_in_view。参数：id (string, 必填) - 报表id, key (string, 必填) - key, view (string, 必填) - view, data (dict) - 请求体数据",
        func=mems_api.get_flows_results_by_by_key_by_view,
        parameters=[
            {"name": "id", "type": "string", "required": True, "description": "报表id"},
            {"name": "key", "type": "string", "required": True, "description": "key"},
            {"name": "view", "type": "string", "required": True, "description": "view"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_results_json",
        description="根据id查询报表执行结果（Parquet格式）。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_flows_results_json,
        parameters=[
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_flows_results_json_rows",
        description="根据id查询报表执行结果（逐行写入方式）。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_flows_results_json_rows,
        parameters=[
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
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
            {"name": "id", "type": "integer", "required": False, "description": "测点id（优先）"},
            {"name": "ids", "type": "string", "required": False, "description": "测点id列表，以,间隔"},
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
            {"name": "id", "type": "string", "required": False, "description": "展示模型id"},
            {"name": "flow_id", "type": "integer", "required": False, "description": "报表id"},
        ]
    ))

    tools.append(ToolInfo(
        name="update_flows_view",
        description="修改报表展示模型。参数：data (dict) - 请求体数据",
        func=mems_api.update_flows_view,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_flows_view",
        description="新增报表展示模型。参数：data (dict) - 请求体数据",
        func=mems_api.add_flows_view,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_flows_view_by_s",
        description="删除指定id的报表展示模型。参数：ids (string, 必填) - 报表展示模型id列表，以,间隔",
        func=mems_api.delete_flows_view_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "报表展示模型id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_graphs_apply_additional",
        description="设置svg是否显示。参数：data (dict) - 请求体数据",
        func=mems_api.add_graphs_apply_additional,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_graphs_apply_models_by_path",
        description="获取应用版本某个名称的svg。参数：path (string, 必填) - svg名称",
        func=mems_api.get_graphs_apply_models_by_path,
        parameters=[
            {"name": "path", "type": "string", "required": True, "description": "svg名称"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_graphs_apply_paths",
        description="获取应用版本的所有svg名称",
        func=mems_api.get_graphs_apply_paths,
    ))

    tools.append(ToolInfo(
        name="add_graphs_apply_version",
        description="应用一个svg版本。参数：data (dict) - 请求体数据",
        func=mems_api.add_graphs_apply_version,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_graphs_models",
        description="新增svg。参数：data (dict) - 请求体数据",
        func=mems_api.add_graphs_models,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_graphs_models_by_path",
        description="根据path查询指定的svg内容。参数：path (string, 必填) - svg名称, version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_graphs_models_by_path,
        parameters=[
            {"name": "path", "type": "string", "required": True, "description": "svg名称"},
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_graphs_models_by_path",
        description="删除指定名称的svg。参数：path (string, 必填) - svg名称列表，以,间隔",
        func=mems_api.delete_graphs_models_by_path,
        parameters=[
            {"name": "path", "type": "string", "required": True, "description": "svg名称列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_graphs_paths",
        description="查询所有svg的名称。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_graphs_paths,
        parameters=[
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_graphs_version",
        description="查询所有的svg版本信息",
        func=mems_api.get_graphs_version,
    ))

    tools.append(ToolInfo(
        name="add_graphs_version",
        description="提交svg版本。参数：data (dict) - 请求体数据",
        func=mems_api.add_graphs_version,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_graphs_version_by_v",
        description="删除指定svg版本。参数：v (integer, 必填) - 版本id",
        func=mems_api.delete_graphs_version_by_v,
        parameters=[
            {"name": "v", "type": "integer", "required": True, "description": "版本id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_config_by_lcc",
        description="查询指定lcc的告警通知配置信息。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarm_config_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_alarm_config_by_lcc",
        description="配置指定lcc的告警通知格式。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_alarm_config_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_alarm_confirm_by_lcc_by_user",
        description="指定lcc确认告警。参数：lcc_id (string, 必填) - lcc_id, user_id (integer, 必填) - 用户id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_alarm_confirm_by_lcc_by_user,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "user_id", "type": "integer", "required": True, "description": "用户id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_confirm_status_by_lcc",
        description="查询指定lcc的已确认告警。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarm_confirm_status_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_count_by_lcc",
        description="查询指定lcc的告警总数。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarm_count_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_alarm_define_by_lcc",
        description="上传指定lcc的单个告警定义。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_alarm_define_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_define_by_lcc_by",
        description="查询指定lcc中指定id的告警定义。参数：lcc_id (string, 必填) - lcc_id, id (integer, 必填) - 告警id",
        func=mems_api.get_lcc_alarm_define_by_lcc_by,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "id", "type": "integer", "required": True, "description": "告警id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_defines_by_lcc",
        description="查询指定lcc的所有告警定义。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarm_defines_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_alarm_defines_by_lcc",
        description="上传指定lcc的告警定义。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_alarm_defines_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_lcc_alarm_defines_by_lcc_by_s",
        description="删除指定lcc的指定id们的告警定义。参数：lcc_id (string, 必填) - lcc_id, ids (string, 必填) - 告警定义id列表，以,间隔",
        func=mems_api.delete_lcc_alarm_defines_by_lcc_by_s,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "ids", "type": "string", "required": True, "description": "告警定义id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarm_unconfirmed_number_by_lcc",
        description="查询指定lcc的未确认告警数。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarm_unconfirmed_number_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarms_unconfirmed_by_lcc",
        description="查询指定lcc的未确认告警列表。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_alarms_unconfirmed_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_alarms_by_lcc",
        description="查询指定lcc的告警结果 查询告警，结果按照时间排序。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_lcc_alarms_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_allmodels_bytes_by_lcc",
        description="导出指定lcc的所有模型字节数组。参数：lcc_id (string, 必填) - lcc_id, lang (string, 必填) - 语言",
        func=mems_api.get_lcc_allmodels_bytes_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "lang", "type": "string", "required": True, "description": "语言"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_allmodels_bytes_by_lcc",
        description="导入指定lcc的所有模型字节数组。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_allmodels_bytes_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_aoe_results_by_lcc",
        description="查询指定lcc的AOE执行结果。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_lcc_aoe_results_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_aoes_models_by_lcc",
        description="查询指定lcc的AOE。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - aoe id列表，以,间隔",
        func=mems_api.get_lcc_aoes_models_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "id", "type": "string", "required": False, "description": "aoe id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_aoes_models_by_lcc",
        description="保存指定lcc的AOE。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_aoes_models_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_lcc_aoes_models_by_lcc_by_s",
        description="删除指定lcc指定id的AOE。参数：lcc_id (string, 必填) - lcc_id, ids (string, 必填) - AOE_id列表，以,间隔",
        func=mems_api.delete_lcc_aoes_models_by_lcc_by_s,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "ids", "type": "string", "required": True, "description": "AOE_id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_auth_users_by_lcc",
        description="查询指定lcc的所有用户。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_auth_users_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_commands_by_lcc",
        description="查询指定lcc的历史设点执行结果。参数：lcc_id (string, 必填) - lcc_id, sender_id (integer, 可选) - , point_id (integer, 可选) - 测点id, start (integer, 可选) - 开始时间, end (integer, 可选) - 结束时间, date (string, 可选) - 时间字符串，yyyy-MM-dd, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_lcc_commands_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "sender_id", "type": "integer", "required": False, "description": ""},
            {"name": "point_id", "type": "integer", "required": False, "description": "测点id"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_common_map_by_lcc",
        description="执行指定lcc的map映射操作。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_common_map_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_config_by_lcc",
        description="查询指定lcc的配置。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_config_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_config_by_lcc",
        description="保存指定lcc的配置。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_config_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_controls_by_lcc",
        description="执行Lcc操作。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_controls_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_logs_bytes_by_lcc",
        description="查询指定lcc的日志。参数：lcc_id (string, 必填) - lcc_id, is_query_size (boolean, 可选) - 是否限制文件大小",
        func=mems_api.get_lcc_logs_bytes_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "is_query_size", "type": "boolean", "required": False, "description": "是否限制文件大小"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_measures_by_lcc",
        description="查询指定lcc的历史量测。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_lcc_measures_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_points_import_str_by_lcc",
        description="加载LCC的测点到base服务。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_points_import_str_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_points_models_by_lcc",
        description="查询指定lcc的测点信息。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - , name (string, 可选) - , is_soe (boolean, 可选) - ",
        func=mems_api.get_lcc_points_models_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "id", "type": "string", "required": False, "description": ""},
            {"name": "name", "type": "string", "required": False, "description": ""},
            {"name": "is_soe", "type": "boolean", "required": False, "description": ""},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_points_models_by_lcc",
        description="保存指定lcc的测点信息。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_points_models_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_lcc_points_models_by_lcc",
        description="删除指定lcc的测点。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.delete_lcc_points_models_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_running_aoes_by_lcc",
        description="查询指定lcc运行中的AOE。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_running_aoes_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_soes_by_lcc",
        description="查询指定lcc的SOE。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_lcc_soes_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_tag_defines_by_lcc_by_group",
        description="查询指定lcc指定分组的标签名称及id列表。参数：lcc_id (string, 必填) - lcc_id, group (integer, 必填) - 分组id",
        func=mems_api.get_lcc_tag_defines_by_lcc_by_group,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "group", "type": "integer", "required": True, "description": "分组id"},
        ]
    ))

    tools.append(ToolInfo(
        name="update_lcc_tags_by_lcc_by_group",
        description="更新指定lcc指定分组下标签名和测点数组关系。参数：lcc_id (string, 必填) - lcc_id, group (integer, 必填) - 分组id, data (dict) - 请求体数据",
        func=mems_api.update_lcc_tags_by_lcc_by_group,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "group", "type": "integer", "required": True, "description": "分组id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_tags_by_lcc_by_group",
        description="查询指定lcc指定分组下标签id对应的测点数组。参数：lcc_id (string, 必填) - lcc_id, group (integer, 必填) - 分组id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_tags_by_lcc_by_group,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "group", "type": "integer", "required": True, "description": "分组id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_lcc_tags_by_lcc_by_group",
        description="删除指定lcc指定分组下标签id和测点的关系。参数：lcc_id (string, 必填) - lcc_id, group (integer, 必填) - 分组id, data (dict) - 请求体数据",
        func=mems_api.delete_lcc_tags_by_lcc_by_group,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "group", "type": "integer", "required": True, "description": "分组id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_transports_models_by_lcc",
        description="查询指定lcc的通道信息。参数：lcc_id (string, 必填) - lcc_id, id (string, 可选) - 通道id列表，以,间隔, transport_type (string, 可选) - 通道类型",
        func=mems_api.get_lcc_transports_models_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "id", "type": "string", "required": False, "description": "通道id列表，以,间隔"},
            {"name": "transport_type", "type": "string", "required": False, "description": "通道类型"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_lcc_transports_models_by_lcc",
        description="保存指定lcc的通道信息。参数：lcc_id (string, 必填) - lcc_id, data (dict) - 请求体数据",
        func=mems_api.add_lcc_transports_models_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_lcc_transports_models_by_lcc_by_s",
        description="删除指定lcc指定id的通道。参数：lcc_id (string, 必填) - lcc_id, ids (string, 必填) - 通道id列表，以,间隔",
        func=mems_api.delete_lcc_transports_models_by_lcc_by_s,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
            {"name": "ids", "type": "string", "required": True, "description": "通道id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_unrun_aoes_by_lcc",
        description="查询指定lcc未运行的AOE。参数：lcc_id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_unrun_aoes_by_lcc,
        parameters=[
            {"name": "lcc_id", "type": "string", "required": True, "description": "lcc_id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_lcc_by",
        description="查询指定id的lcc。参数：id (string, 必填) - lcc_id",
        func=mems_api.get_lcc_by,
        parameters=[
            {"name": "id", "type": "string", "required": True, "description": "lcc_id"},
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
            {"name": "is_query_size", "type": "boolean", "required": False, "description": "是否限制文件大小"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_measureinits_by_day",
        description="量测值初始化。参数：day (integer, 必填) - 时间戳",
        func=mems_api.add_measureinits_by_day,
        parameters=[
            {"name": "day", "type": "integer", "required": True, "description": "时间戳"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_measures",
        description="查询历史量测。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_measures,
        parameters=[
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_multi_import_bytes",
        description="导入所有模型字节数组。参数：data (dict) - 请求体数据",
        func=mems_api.add_multi_import_bytes,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_north_dataframe_by_flow_by_node",
        description="加载其他mems来的Dataframe。参数：flow (integer, 必填) - 报表id, node (integer, 必填) - 节点id, data (dict) - 请求体数据",
        func=mems_api.add_north_dataframe_by_flow_by_node,
        parameters=[
            {"name": "flow", "type": "integer", "required": True, "description": "报表id"},
            {"name": "node", "type": "integer", "required": True, "description": "节点id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
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
        description="修改计划。参数：data (dict) - 请求体数据",
        func=mems_api.update_plans_models,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_plans_models",
        description="新增计划。参数：data (dict) - 请求体数据",
        func=mems_api.add_plans_models,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_plans_models_by_ids",
        description="查询指定id的计划列表。参数：ids (string, 必填) - 计划id列表，以,间隔",
        func=mems_api.get_plans_models_by_ids,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "计划id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_plans_models_by_s",
        description="删除指定id的计划。参数：ids (string, 必填) - 计划id列表，以,间隔",
        func=mems_api.delete_plans_models_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "计划id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_plans_models_by",
        description="查询指定id的计划。参数：id (integer, 必填) - 计划id",
        func=mems_api.get_plans_models_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "计划id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_plans_paths",
        description="查询所有计划路径",
        func=mems_api.get_plans_paths,
    ))

    tools.append(ToolInfo(
        name="update_plans_paths",
        description="修改计划路径。参数：data (dict) - 请求体数据",
        func=mems_api.update_plans_paths,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_plans_paths",
        description="新增计划路径。参数：data (dict) - 请求体数据",
        func=mems_api.add_plans_paths,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_plans_paths",
        description="删除指定的计划路径。参数：data (dict) - 请求体数据",
        func=mems_api.delete_plans_paths,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_points_models",
        description="查询所有测点",
        func=mems_api.get_points_models,
    ))

    tools.append(ToolInfo(
        name="add_points_models",
        description="保存测点。参数：data (dict) - 请求体数据",
        func=mems_api.add_points_models,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_points_models",
        description="删除指定id的测点（body形式）。参数：data (dict) - 请求体数据",
        func=mems_api.delete_points_models,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_points_models_for_apply",
        description="获取根据版本号组装的测点应用对象。参数：version (integer, 可选) - 版本号，可选，若为空则默认0号版本",
        func=mems_api.get_points_models_for_apply,
        parameters=[
            {"name": "version", "type": "integer", "required": False, "description": "版本号，可选，若为空则默认0号版本"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_points_models_by_s",
        description="删除指定id的测点。参数：ids (string, 必填) - 测点id列表，以,间隔",
        func=mems_api.delete_points_models_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "测点id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_points_models_file",
        description="保存测点（文件形式）。参数：data (dict) - 请求体数据",
        func=mems_api.add_points_models_file,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_points_models_file2",
        description="保存测点（多文件形式）。参数：data (dict) - 请求体数据",
        func=mems_api.add_points_models_file2,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_points_remote",
        description="查询控制器与测点的对应关系",
        func=mems_api.get_points_remote,
    ))

    tools.append(ToolInfo(
        name="add_points_remote",
        description="更新控制器与测点的关系。参数：data (dict) - 请求体数据",
        func=mems_api.add_points_remote,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_points_source",
        description="查询所有测点数据源",
        func=mems_api.get_points_source,
    ))

    tools.append(ToolInfo(
        name="add_points_source",
        description="保存测点数据源。参数：data (dict) - 请求体数据",
        func=mems_api.add_points_source,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_points_version",
        description="查询所有的测点版本信息",
        func=mems_api.get_points_version,
    ))

    tools.append(ToolInfo(
        name="add_points_version",
        description="新增测点版本。参数：data (dict) - 请求体数据",
        func=mems_api.add_points_version,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_points_version_by_v",
        description="删除某一个测点版本。参数：v (integer, 必填) - 版本id",
        func=mems_api.delete_points_version_by_v,
        parameters=[
            {"name": "v", "type": "integer", "required": True, "description": "版本id"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_pscpu_aoes",
        description="更新当前应用的AOE。参数：data (dict) - 请求体数据",
        func=mems_api.add_pscpu_aoes,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
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
        description="更新当前应用的电气岛。参数：data (dict) - 请求体数据",
        func=mems_api.add_pscpu_island,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
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
        description="更新当前应用的测点。参数：data (dict) - 请求体数据",
        func=mems_api.add_pscpu_points,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_pscpu_points_by_dev",
        description="查询设备关联的测点。参数：dev_id (integer, 必填) - 设备id",
        func=mems_api.get_pscpu_points_by_dev,
        parameters=[
            {"name": "dev_id", "type": "integer", "required": True, "description": "设备id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_pscpu_points_models",
        description="查询当前应用的测点。参数：id (string, 可选) - , name (string, 可选) - , is_soe (boolean, 可选) - ",
        func=mems_api.get_pscpu_points_models,
        parameters=[
            {"name": "id", "type": "string", "required": False, "description": ""},
            {"name": "name", "type": "string", "required": False, "description": ""},
            {"name": "is_soe", "type": "boolean", "required": False, "description": ""},
        ]
    ))

    tools.append(ToolInfo(
        name="get_pscpu_points_values_by_src",
        description="查询量测值。参数：src (integer, 必填) - , id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_pscpu_points_values_by_src,
        parameters=[
            {"name": "src", "type": "integer", "required": True, "description": ""},
            {"name": "id", "type": "integer", "required": False, "description": "测点id（优先）"},
            {"name": "ids", "type": "string", "required": False, "description": "测点id列表，以,间隔"},
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
        description="启动pscpu。参数：data (dict) - 请求体数据",
        func=mems_api.add_pscpu_start,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
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
            {"name": "script_id", "type": "integer", "required": True, "description": "脚本id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_script_md5",
        description="查询脚本md5。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_script_md5,
        parameters=[
            {"name": "id", "type": "integer", "required": False, "description": "测点id（优先）"},
            {"name": "ids", "type": "string", "required": False, "description": "测点id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_script_results",
        description="查询所有脚本结果",
        func=mems_api.get_script_results,
    ))

    tools.append(ToolInfo(
        name="add_script_results",
        description="新增脚本结果。参数：data (dict) - 请求体数据",
        func=mems_api.add_script_results,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_script_results_by",
        description="查询指定id脚本结果。参数：id (integer, 必填) - 脚本结果id",
        func=mems_api.get_script_results_by,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "脚本结果id"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_script_wasm",
        description="保存脚本对应的wasm和js文件。参数：data (dict) - 请求体数据",
        func=mems_api.add_script_wasm,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_scripts",
        description="查询指定id脚本。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_scripts,
        parameters=[
            {"name": "id", "type": "integer", "required": False, "description": "测点id（优先）"},
            {"name": "ids", "type": "string", "required": False, "description": "测点id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_scripts",
        description="新增脚本。参数：data (dict) - 请求体数据",
        func=mems_api.add_scripts,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_scripts_by_s",
        description="删除指定id的脚本。参数：ids (string, 必填) - 脚本id列表，以,间隔",
        func=mems_api.delete_scripts_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "脚本id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_soes",
        description="查询SOE，结果按照时间排序。参数：id (string, 可选) - 测点id，多个id之间以,间隔, start (integer, 可选) - 开始时间, 13位时间戳, end (integer, 可选) - 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end, date (string, 可选) - 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准, source (integer, 可选) - 数据源, last_only (boolean, 可选) - 是否查询只最新的数据, with_init (boolean, 可选) - 是否查询该天初始的数据, reverse_order (boolean, 可选) - 是否时间倒序查询",
        func=mems_api.get_soes,
        parameters=[
            {"name": "id", "type": "string", "required": False, "description": "测点id，多个id之间以,间隔"},
            {"name": "start", "type": "integer", "required": False, "description": "开始时间, 13位时间戳"},
            {"name": "end", "type": "integer", "required": False, "description": "结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end"},
            {"name": "date", "type": "string", "required": False, "description": "时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准"},
            {"name": "source", "type": "integer", "required": False, "description": "数据源"},
            {"name": "last_only", "type": "boolean", "required": False, "description": "是否查询只最新的数据"},
            {"name": "with_init", "type": "boolean", "required": False, "description": "是否查询该天初始的数据"},
            {"name": "reverse_order", "type": "boolean", "required": False, "description": "是否时间倒序查询"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_tag_defines_by_group",
        description="查询指定分组的标签名称及id列表。参数：id (integer, 必填) - 分组id, group (integer, 必填) - ",
        func=mems_api.get_tag_defines_by_group,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "分组id"},
            {"name": "group", "type": "integer", "required": True, "description": ""},
        ]
    ))

    tools.append(ToolInfo(
        name="update_tags_by_group",
        description="更新指定分组下标签名和测点数组关系。参数：group (integer, 必填) - 分组id, data (dict) - 请求体数据",
        func=mems_api.update_tags_by_group,
        parameters=[
            {"name": "group", "type": "integer", "required": True, "description": "分组id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_tags_by_group",
        description="删除指定分组下标签id和测点的关系。参数：group (integer, 必填) - 分组id, data (dict) - 请求体数据",
        func=mems_api.delete_tags_by_group,
        parameters=[
            {"name": "group", "type": "integer", "required": True, "description": "分组id"},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="add_tags_cbor_by_group",
        description="查询指定分组下标签id对应的测点数组。参数：id (integer, 必填) - 分组id, group (integer, 必填) - , data (dict) - 请求体数据",
        func=mems_api.add_tags_cbor_by_group,
        parameters=[
            {"name": "id", "type": "integer", "required": True, "description": "分组id"},
            {"name": "group", "type": "integer", "required": True, "description": ""},
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_unrun_aoes",
        description="查询未运行的AOE",
        func=mems_api.get_unrun_aoes,
    ))

    tools.append(ToolInfo(
        name="add_webplugin_file",
        description="保存插件对应的file。参数：data (dict) - 请求体数据",
        func=mems_api.add_webplugin_file,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_webplugin_file_by_plugin",
        description="查询插件对应的压缩文件。参数：plugin_id (integer, 必填) - 插件id",
        func=mems_api.get_webplugin_file_by_plugin,
        parameters=[
            {"name": "plugin_id", "type": "integer", "required": True, "description": "插件id"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_webplugin_md5",
        description="查询插件md5。参数：id (integer, 可选) - 测点id（优先）, ids (string, 可选) - 测点id列表，以,间隔",
        func=mems_api.get_webplugin_md5,
        parameters=[
            {"name": "id", "type": "integer", "required": False, "description": "测点id（优先）"},
            {"name": "ids", "type": "string", "required": False, "description": "测点id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_webplugins",
        description="查询所有界面插件",
        func=mems_api.get_webplugins,
    ))

    tools.append(ToolInfo(
        name="add_webplugins",
        description="新增插件。参数：data (dict) - 请求体数据",
        func=mems_api.add_webplugins,
        parameters=[
            {"name": "data", "type": "dict", "required": True, "description": "请求体数据"},
        ]
    ))

    tools.append(ToolInfo(
        name="delete_webplugins_by_s",
        description="删除指定id的插件。参数：ids (string, 必填) - 插件id列表，以,间隔",
        func=mems_api.delete_webplugins_by_s,
        parameters=[
            {"name": "ids", "type": "string", "required": True, "description": "插件id列表，以,间隔"},
        ]
    ))

    tools.append(ToolInfo(
        name="get_webplugins_by_plugin",
        description="查询指定id插件。参数：plugin_id (integer, 必填) - 插件id",
        func=mems_api.get_webplugins_by_plugin,
        parameters=[
            {"name": "plugin_id", "type": "integer", "required": True, "description": "插件id"},
        ]
    ))

    return tools
