from typing import List, Dict, Any, Optional, TypedDict

class ToolInfo:
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func

def create_tools(mems_api) -> List[ToolInfo]:
    tools = []
    
    tools.append(ToolInfo(
        name="login",
        description="用户登录，获取访问令牌。在调用其他需要认证的接口之前，需要先调用此接口。",
        func=mems_api.login
    ))
    
    tools.append(ToolInfo(
        name="get_users",
        description="获取所有用户列表，返回用户信息数组。",
        func=mems_api.get_users
    ))
    
    tools.append(ToolInfo(
        name="get_user",
        description="根据用户ID获取指定用户的详细信息。参数：user_id (integer) - 用户ID",
        func=mems_api.get_user
    ))
    
    tools.append(ToolInfo(
        name="get_roles",
        description="获取所有角色列表，返回角色信息数组。",
        func=mems_api.get_roles
    ))
    
    tools.append(ToolInfo(
        name="get_alarms",
        description="获取所有告警列表，返回告警信息数组。",
        func=mems_api.get_alarms
    ))
    
    tools.append(ToolInfo(
        name="get_alarm_count",
        description="获取告警总数。",
        func=mems_api.get_alarm_count
    ))
    
    tools.append(ToolInfo(
        name="get_unconfirmed_alarm_count",
        description="获取未确认的告警数量。",
        func=mems_api.get_unconfirmed_alarm_count
    ))
    
    tools.append(ToolInfo(
        name="get_points",
        description="获取所有测点列表，返回测点信息数组。",
        func=mems_api.get_points
    ))
    
    tools.append(ToolInfo(
        name="get_devices",
        description="获取所有设备列表，返回设备信息数组。",
        func=mems_api.get_devices
    ))
    
    tools.append(ToolInfo(
        name="get_device_defines",
        description="获取所有设备定义列表。",
        func=mems_api.get_device_defines
    ))
    
    tools.append(ToolInfo(
        name="get_topology",
        description="获取设备拓扑信息。",
        func=mems_api.get_topology
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_list",
        description="获取所有LCC设备列表。",
        func=mems_api.get_lcc_list
    ))
    
    tools.append(ToolInfo(
        name="get_config",
        description="获取系统配置信息。",
        func=mems_api.get_config
    ))
    
    tools.append(ToolInfo(
        name="get_aoe_models",
        description="获取所有AOE模型列表。",
        func=mems_api.get_aoe_models
    ))
    
    tools.append(ToolInfo(
        name="get_auths",
        description="查询所有权限。",
        func=mems_api.get_auths
    ))
    
    tools.append(ToolInfo(
        name="get_auths_by_role",
        description="查询指定角色的所有权限。参数：role_id (integer) - 角色ID",
        func=mems_api.get_auths_by_role
    ))
    
    tools.append(ToolInfo(
        name="get_menus",
        description="查询所有菜单。",
        func=mems_api.get_menus
    ))
    
    tools.append(ToolInfo(
        name="get_menus_by_role",
        description="查询指定角色的所有菜单。参数：role_id (integer) - 角色ID",
        func=mems_api.get_menus_by_role
    ))
    
    tools.append(ToolInfo(
        name="get_menus_by_user",
        description="查询指定用户的所有菜单。参数：user_id (integer) - 用户ID",
        func=mems_api.get_menus_by_user
    ))
    
    tools.append(ToolInfo(
        name="register",
        description="用户注册。参数：username (string) - 用户名, password (string) - 密码",
        func=mems_api.register
    ))
    
    tools.append(ToolInfo(
        name="get_roles_by_ids",
        description="根据ids查询角色。参数：ids (string) - 角色ID列表，以逗号分隔",
        func=mems_api.get_roles_by_ids
    ))
    
    tools.append(ToolInfo(
        name="get_users_by_group",
        description="根据分组ID查询用户信息。参数：group_id (integer) - 用户组ID",
        func=mems_api.get_users_by_group
    ))
    
    tools.append(ToolInfo(
        name="get_user_groups",
        description="查询所有用户组。",
        func=mems_api.get_user_groups
    ))
    
    tools.append(ToolInfo(
        name="get_user_group",
        description="查询指定ID的用户组。参数：group_id (integer) - 用户组ID",
        func=mems_api.get_user_group
    ))
    
    tools.append(ToolInfo(
        name="get_users_by_lcc",
        description="查询指定LCC的所有用户。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_users_by_lcc
    ))
    
    tools.append(ToolInfo(
        name="get_alarm_config",
        description="查询告警通知配置信息。",
        func=mems_api.get_alarm_config
    ))
    
    tools.append(ToolInfo(
        name="get_confirmed_alarms",
        description="查询已确认的告警。",
        func=mems_api.get_confirmed_alarms
    ))
    
    tools.append(ToolInfo(
        name="confirm_alarm",
        description="确认告警。参数：user_id (integer) - 用户ID",
        func=mems_api.confirm_alarm
    ))
    
    tools.append(ToolInfo(
        name="get_alarm_define",
        description="查询指定ID的告警定义。参数：define_id (integer) - 告警定义ID",
        func=mems_api.get_alarm_define
    ))
    
    tools.append(ToolInfo(
        name="get_alarm_defines",
        description="查询所有的告警定义。",
        func=mems_api.get_alarm_defines
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_alarm_config",
        description="查询指定LCC的告警通知配置信息。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_alarm_config
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_confirmed_alarms",
        description="查询指定LCC的已确认告警。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_confirmed_alarms
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_alarm_count",
        description="查询指定LCC的告警总数。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_alarm_count
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_alarm_defines",
        description="查询指定LCC的所有告警定义。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_alarm_defines
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_alarm_define",
        description="查询指定LCC中指定ID的告警定义。参数：lcc_id (string) - LCC ID, define_id (integer) - 告警ID",
        func=mems_api.get_lcc_alarm_define
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_unconfirmed_alarm_count",
        description="查询指定LCC的未确认告警数。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_unconfirmed_alarm_count
    ))
    
    tools.append(ToolInfo(
        name="confirm_lcc_alarm",
        description="指定LCC确认告警。参数：lcc_id (string) - LCC ID, user_id (integer) - 用户ID",
        func=mems_api.confirm_lcc_alarm
    ))
    
    tools.append(ToolInfo(
        name="get_aoe",
        description="根据ID查询指定的AOE。参数：aoe_id (integer) - AOE ID",
        func=mems_api.get_aoe
    ))
    
    tools.append(ToolInfo(
        name="get_aoes_for_apply",
        description="根据版本号组装AOE应用对象。",
        func=mems_api.get_aoes_for_apply
    ))
    
    tools.append(ToolInfo(
        name="get_aoe_by_version",
        description="查询指定版本的AOE。参数：version_id (integer) - 版本ID",
        func=mems_api.get_aoe_by_version
    ))
    
    tools.append(ToolInfo(
        name="get_aoe_versions",
        description="查询所有的AOE版本信息。",
        func=mems_api.get_aoe_versions
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_aoe",
        description="查询指定LCC的AOE。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_aoe
    ))
    
    tools.append(ToolInfo(
        name="get_running_aoe",
        description="查询当前应用的AOE。",
        func=mems_api.get_running_aoe
    ))
    
    tools.append(ToolInfo(
        name="get_running_aoe_version",
        description="查询当前应用的AOE版本号。",
        func=mems_api.get_running_aoe_version
    ))
    
    tools.append(ToolInfo(
        name="get_points_for_apply",
        description="根据版本号组装测点应用对象。",
        func=mems_api.get_points_for_apply
    ))
    
    tools.append(ToolInfo(
        name="get_points_remote",
        description="查询控制器与测点的对应关系。",
        func=mems_api.get_points_remote
    ))
    
    tools.append(ToolInfo(
        name="get_point_versions",
        description="查询所有的测点版本信息。",
        func=mems_api.get_point_versions
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_points",
        description="查询指定LCC的测点信息。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_points
    ))
    
    tools.append(ToolInfo(
        name="get_points_by_dev",
        description="查询设备关联的测点。参数：dev_id (integer) - 设备ID",
        func=mems_api.get_points_by_dev
    ))
    
    tools.append(ToolInfo(
        name="get_running_points",
        description="查询当前应用的测点。",
        func=mems_api.get_running_points
    ))
    
    tools.append(ToolInfo(
        name="get_running_points_version",
        description="查询当前应用的测点版本号。",
        func=mems_api.get_running_points_version
    ))
    
    tools.append(ToolInfo(
        name="get_device_define",
        description="根据ID查询对应的设备定义。参数：define_id (integer) - 设备定义ID",
        func=mems_api.get_device_define
    ))
    
    tools.append(ToolInfo(
        name="get_device",
        description="根据ID查询设备对象。参数：device_id (integer) - 设备ID",
        func=mems_api.get_device
    ))
    
    tools.append(ToolInfo(
        name="get_islands",
        description="查询电气岛。",
        func=mems_api.get_islands
    ))
    
    tools.append(ToolInfo(
        name="get_measure_defs",
        description="查询设备测点。",
        func=mems_api.get_measure_defs
    ))
    
    tools.append(ToolInfo(
        name="get_prop_defines",
        description="查询所有设备属性定义。",
        func=mems_api.get_prop_defines
    ))
    
    tools.append(ToolInfo(
        name="get_prop_groups",
        description="查询所有设备属性分组。",
        func=mems_api.get_prop_groups
    ))
    
    tools.append(ToolInfo(
        name="get_prop_groups_by_ids",
        description="根据ID列表查看设备属性分组列表。参数：ids (string) - 设备属性分组ID列表，以逗号分隔",
        func=mems_api.get_prop_groups_by_ids
    ))
    
    tools.append(ToolInfo(
        name="get_island_versions",
        description="查询电气岛所有版本。",
        func=mems_api.get_island_versions
    ))
    
    tools.append(ToolInfo(
        name="get_lcc",
        description="查询指定ID的LCC。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_running_aoes",
        description="查询指定LCC运行中的AOE。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_running_aoes
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_unrun_aoes",
        description="查询指定LCC未运行的AOE。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_unrun_aoes
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_alarms",
        description="查询指定LCC的告警。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_alarms
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_config",
        description="查询指定LCC的配置。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_config
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_aoe_results",
        description="查询指定LCC的AOE执行结果。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_aoe_results
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_tag_defines",
        description="查询指定LCC指定分组的标签名称及ID列表。参数：lcc_id (string) - LCC ID, group (integer) - 分组ID",
        func=mems_api.get_lcc_tag_defines
    ))
    
    tools.append(ToolInfo(
        name="get_lcc_transport",
        description="查询指定LCC的通道信息。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_transport
    ))
    
    tools.append(ToolInfo(
        name="get_pscpu_running_aoes",
        description="查询当前运行中的AOE。",
        func=mems_api.get_pscpu_running_aoes
    ))
    
    tools.append(ToolInfo(
        name="get_pscpu_unrun_aoes",
        description="查询未运行的AOE。",
        func=mems_api.get_pscpu_unrun_aoes
    ))
    
    tools.append(ToolInfo(
        name="get_pscpu_info",
        description="查询配置信息。",
        func=mems_api.get_pscpu_info
    ))
    
    tools.append(ToolInfo(
        name="get_pscpu_island",
        description="查询当前应用的电气岛。",
        func=mems_api.get_pscpu_island
    ))
    
    tools.append(ToolInfo(
        name="get_pscpu_island_paths",
        description="查询当前应用的电气岛路径。",
        func=mems_api.get_pscpu_island_paths
    ))
    
    tools.append(ToolInfo(
        name="get_pscpu_island_version",
        description="查询当前应用的电气岛版本号。",
        func=mems_api.get_pscpu_island_version
    ))
    
    tools.append(ToolInfo(
        name="get_graph_apply_paths",
        description="获取应用版本的所有SVG名称。",
        func=mems_api.get_graph_apply_paths
    ))
    
    tools.append(ToolInfo(
        name="get_graph_apply_version",
        description="获取应用版本号。",
        func=mems_api.get_graph_apply_version
    ))
    
    tools.append(ToolInfo(
        name="get_graph_paths",
        description="查询所有SVG的名称。",
        func=mems_api.get_graph_paths
    ))
    
    tools.append(ToolInfo(
        name="get_graph_versions",
        description="查询所有的版本信息。",
        func=mems_api.get_graph_versions
    ))
    
    tools.append(ToolInfo(
        name="get_plans",
        description="查询所有计划。",
        func=mems_api.get_plans
    ))
    
    tools.append(ToolInfo(
        name="get_plans_by_ids",
        description="根据IDs查询计划列表。参数：ids (string) - 计划ID，多个ID以逗号分隔",
        func=mems_api.get_plans_by_ids
    ))
    
    tools.append(ToolInfo(
        name="get_plan",
        description="查询指定ID计划。参数：plan_id (integer) - 计划ID",
        func=mems_api.get_plan
    ))
    
    tools.append(ToolInfo(
        name="get_plan_paths",
        description="查询所有计划路径。",
        func=mems_api.get_plan_paths
    ))
    
    tools.append(ToolInfo(
        name="get_webplugins",
        description="查询所有界面插件。",
        func=mems_api.get_webplugins
    ))
    
    tools.append(ToolInfo(
        name="get_webplugin",
        description="查询指定ID插件。参数：plugin_id (integer) - 插件ID",
        func=mems_api.get_webplugin
    ))
    
    tools.append(ToolInfo(
        name="get_flow_result",
        description="根据ID查询报表执行结果。参数：result_id (string) - 报表ID",
        func=mems_api.get_flow_result
    ))
    
    tools.append(ToolInfo(
        name="get_flow_result_json",
        description="根据ID查询报表执行结果（Parquet格式）。参数：result_id (string) - 报表ID",
        func=mems_api.get_flow_result_json
    ))
    
    tools.append(ToolInfo(
        name="get_flow_result_json_rows",
        description="根据ID查询报表执行结果（逐行写入方式）。参数：result_id (string) - 报表ID",
        func=mems_api.get_flow_result_json_rows
    ))
    
    tools.append(ToolInfo(
        name="get_ems",
        description="查询指定ID的EMS。参数：ems_id (string) - EMS ID",
        func=mems_api.get_ems
    ))
    
    tools.append(ToolInfo(
        name="get_ems_list",
        description="查询所有的EMS。",
        func=mems_api.get_ems_list
    ))
    
    tools.append(ToolInfo(
        name="get_tag_defines",
        description="查询指定分组的标签名称及ID列表。参数：group (integer) - 分组ID",
        func=mems_api.get_tag_defines
    ))
    
    tools.append(ToolInfo(
        name="get_script_results",
        description="查询所有脚本结果。",
        func=mems_api.get_script_results
    ))
    
    tools.append(ToolInfo(
        name="get_script_result",
        description="查询指定ID脚本结果。参数：result_id (integer) - 脚本结果ID",
        func=mems_api.get_script_result
    ))
    
    tools.append(ToolInfo(
        name="reset_pscpu",
        description="重置PSCPU。",
        func=mems_api.reset_pscpu
    ))
    
    tools.append(ToolInfo(
        name="start_pscpu",
        description="启动PSCPU。",
        func=mems_api.start_pscpu
    ))
    
    tools.append(ToolInfo(
        name="stop_pscpu",
        description="停止PSCPU。",
        func=mems_api.stop_pscpu
    ))
    

    tools.append(ToolInfo(
        name="add_alarm_define",
        description="新增告警定义。参数：data (dict) - 请求体数据",
        func=mems_api.add_alarm_define
    ))

    tools.append(ToolInfo(
        name="add_alarm_defines",
        description="新增告警定义。参数：data (dict) - 请求体数据",
        func=mems_api.add_alarm_defines
    ))

    tools.append(ToolInfo(
        name="add_aoe",
        description="新增AOE模型。参数：data (dict) - 请求体数据",
        func=mems_api.add_aoe
    ))

    tools.append(ToolInfo(
        name="add_aoe_version",
        description="新增AOE版本。参数：data (dict) - 请求体数据",
        func=mems_api.add_aoe_version
    ))

    tools.append(ToolInfo(
        name="add_auth",
        description="新增权限。参数：data (dict) - 请求体数据",
        func=mems_api.add_auth
    ))

    tools.append(ToolInfo(
        name="add_device",
        description="新增设备。参数：data (dict) - 请求体数据",
        func=mems_api.add_device
    ))

    tools.append(ToolInfo(
        name="add_device_define",
        description="新增设备定义。参数：data (dict) - 请求体数据",
        func=mems_api.add_device_define
    ))

    tools.append(ToolInfo(
        name="add_graph_model",
        description="新增图表模型。参数：data (dict) - 请求体数据",
        func=mems_api.add_graph_model
    ))

    tools.append(ToolInfo(
        name="add_island_version",
        description="新增电气岛版本。参数：data (dict) - 请求体数据",
        func=mems_api.add_island_version
    ))

    tools.append(ToolInfo(
        name="add_lcc_alarm_define",
        description="新增LCC告警定义。参数：lcc_id (string) - LCC ID, data (dict) - 请求体数据",
        func=mems_api.add_lcc_alarm_define
    ))

    tools.append(ToolInfo(
        name="add_lcc_alarm_defines",
        description="新增LCC告警定义。参数：lcc_id (string) - LCC ID, data (dict) - 请求体数据",
        func=mems_api.add_lcc_alarm_defines
    ))

    tools.append(ToolInfo(
        name="add_lcc_aoe",
        description="新增LCC AOE。参数：lcc_id (string) - LCC ID, data (dict) - 请求体数据",
        func=mems_api.add_lcc_aoe
    ))

    tools.append(ToolInfo(
        name="add_lcc_point",
        description="新增LCC测点。参数：lcc_id (string) - LCC ID, data (dict) - 请求体数据",
        func=mems_api.add_lcc_point
    ))

    tools.append(ToolInfo(
        name="add_measure_def",
        description="新增测点定义。参数：data (dict) - 请求体数据",
        func=mems_api.add_measure_def
    ))

    tools.append(ToolInfo(
        name="add_menu",
        description="新增菜单。参数：data (dict) - 请求体数据",
        func=mems_api.add_menu
    ))

    tools.append(ToolInfo(
        name="add_plan",
        description="新增计划。参数：data (dict) - 请求体数据",
        func=mems_api.add_plan
    ))

    tools.append(ToolInfo(
        name="add_plan_path",
        description="新增计划路径。参数：data (dict) - 请求体数据",
        func=mems_api.add_plan_path
    ))

    tools.append(ToolInfo(
        name="add_point",
        description="新增测点。参数：data (dict) - 请求体数据",
        func=mems_api.add_point
    ))

    tools.append(ToolInfo(
        name="add_point_version",
        description="新增测点版本。参数：data (dict) - 请求体数据",
        func=mems_api.add_point_version
    ))

    tools.append(ToolInfo(
        name="add_prop_define",
        description="新增属性定义。参数：data (dict) - 请求体数据",
        func=mems_api.add_prop_define
    ))

    tools.append(ToolInfo(
        name="add_prop_group",
        description="新增属性分组。参数：data (dict) - 请求体数据",
        func=mems_api.add_prop_group
    ))

    tools.append(ToolInfo(
        name="add_role",
        description="新增角色。参数：data (dict) - 请求体数据",
        func=mems_api.add_role
    ))

    tools.append(ToolInfo(
        name="add_script",
        description="新增脚本。参数：data (dict) - 请求体数据",
        func=mems_api.add_script
    ))

    tools.append(ToolInfo(
        name="add_script_result",
        description="新增脚本结果。参数：data (dict) - 请求体数据",
        func=mems_api.add_script_result
    ))

    tools.append(ToolInfo(
        name="add_topology",
        description="新增拓扑。参数：data (dict) - 请求体数据",
        func=mems_api.add_topology
    ))

    tools.append(ToolInfo(
        name="add_user",
        description="新增用户。参数：data (dict) - 请求体数据",
        func=mems_api.add_user
    ))

    tools.append(ToolInfo(
        name="add_user_group",
        description="新增用户组。参数：data (dict) - 请求体数据",
        func=mems_api.add_user_group
    ))

    tools.append(ToolInfo(
        name="add_webplugin",
        description="新增界面插件。参数：data (dict) - 请求体数据",
        func=mems_api.add_webplugin
    ))

    tools.append(ToolInfo(
        name="add_webplugin_file",
        description="新增界面插件文件。参数：data (dict) - 请求体数据",
        func=mems_api.add_webplugin_file
    ))

    tools.append(ToolInfo(
        name="apply_graph_version",
        description="应用图表版本。参数：data (dict) - 请求体数据",
        func=mems_api.apply_graph_version
    ))

    tools.append(ToolInfo(
        name="apply_islands",
        description="应用电气岛。参数：data (dict) - 请求体数据",
        func=mems_api.apply_islands
    ))

    tools.append(ToolInfo(
        name="bind_user_roles",
        description="绑定user_roles。参数：user_id (integer) - 用户ID, data (dict) - 请求体数据",
        func=mems_api.bind_user_roles
    ))

    tools.append(ToolInfo(
        name="change_password",
        description="修改密码。参数：user_id (integer) - 用户ID, data (dict) - 请求体数据",
        func=mems_api.change_password
    ))

    tools.append(ToolInfo(
        name="clear_resources",
        description="清除resources",
        func=mems_api.clear_resources
    ))

    tools.append(ToolInfo(
        name="commit_file_tree_version",
        description="提交file_tree_version。参数：tree_id (string) - 树ID, data (dict) - 请求体数据",
        func=mems_api.commit_file_tree_version
    ))

    tools.append(ToolInfo(
        name="commit_graph_version",
        description="提交图表版本。参数：data (dict) - 请求体数据",
        func=mems_api.commit_graph_version
    ))

    tools.append(ToolInfo(
        name="control_point_by_alias",
        description="控制测点（按别名）。参数：data (dict) - 请求体数据",
        func=mems_api.control_point_by_alias
    ))

    tools.append(ToolInfo(
        name="control_pscpu_aoes",
        description="控制PSCPU AOE。参数：data (dict) - 请求体数据",
        func=mems_api.control_pscpu_aoes
    ))

    tools.append(ToolInfo(
        name="control_pscpu_points",
        description="控制PSCPU测点。参数：data (dict) - 请求体数据",
        func=mems_api.control_pscpu_points
    ))

    tools.append(ToolInfo(
        name="delete_alarm_defines",
        description="删除告警定义。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_alarm_defines
    ))

    tools.append(ToolInfo(
        name="delete_aoe",
        description="删除AOE模型。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_aoe
    ))

    tools.append(ToolInfo(
        name="delete_aoe_version",
        description="删除AOE版本。参数：version_id (integer) - 版本ID",
        func=mems_api.delete_aoe_version
    ))

    tools.append(ToolInfo(
        name="delete_auths",
        description="删除auths。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_auths
    ))

    tools.append(ToolInfo(
        name="delete_device",
        description="删除设备。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_device
    ))

    tools.append(ToolInfo(
        name="delete_device_defines",
        description="删除device_defines。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_device_defines
    ))

    tools.append(ToolInfo(
        name="delete_graph_model",
        description="删除图表模型。参数：path (string) - 路径",
        func=mems_api.delete_graph_model
    ))

    tools.append(ToolInfo(
        name="delete_graph_version",
        description="删除图表版本。参数：version_id (integer) - 版本ID",
        func=mems_api.delete_graph_version
    ))

    tools.append(ToolInfo(
        name="delete_island_version",
        description="删除电气岛版本。参数：version_id (integer) - 版本ID",
        func=mems_api.delete_island_version
    ))

    tools.append(ToolInfo(
        name="delete_lcc_alarm_defines",
        description="删除LCC告警定义。参数：lcc_id (string) - LCC ID, ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_lcc_alarm_defines
    ))

    tools.append(ToolInfo(
        name="delete_lcc_aoe",
        description="删除LCC AOE。参数：lcc_id (string) - LCC ID, ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_lcc_aoe
    ))

    tools.append(ToolInfo(
        name="delete_lcc_point",
        description="删除LCC测点。参数：lcc_id (string) - LCC ID, point_id (integer) - 测点ID",
        func=mems_api.delete_lcc_point
    ))

    tools.append(ToolInfo(
        name="delete_lcc_transport",
        description="删除LCC通道。参数：lcc_id (string) - LCC ID, ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_lcc_transport
    ))

    tools.append(ToolInfo(
        name="delete_measure_defs",
        description="删除measure_defs",
        func=mems_api.delete_measure_defs
    ))

    tools.append(ToolInfo(
        name="delete_menus",
        description="删除menus。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_menus
    ))

    tools.append(ToolInfo(
        name="delete_plan",
        description="删除计划。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_plan
    ))

    tools.append(ToolInfo(
        name="delete_plan_paths",
        description="删除plan_paths",
        func=mems_api.delete_plan_paths
    ))

    tools.append(ToolInfo(
        name="delete_point",
        description="删除测点。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_point
    ))

    tools.append(ToolInfo(
        name="delete_point_version",
        description="删除测点版本。参数：version_id (integer) - 版本ID",
        func=mems_api.delete_point_version
    ))

    tools.append(ToolInfo(
        name="delete_prop_defines",
        description="删除prop_defines。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_prop_defines
    ))

    tools.append(ToolInfo(
        name="delete_prop_groups",
        description="删除prop_groups。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_prop_groups
    ))

    tools.append(ToolInfo(
        name="delete_roles",
        description="删除roles。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_roles
    ))

    tools.append(ToolInfo(
        name="delete_script",
        description="删除脚本。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_script
    ))

    tools.append(ToolInfo(
        name="delete_tag",
        description="删除标签。参数：group (integer) - 分组ID",
        func=mems_api.delete_tag
    ))

    tools.append(ToolInfo(
        name="delete_user_groups",
        description="删除user_groups。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_user_groups
    ))

    tools.append(ToolInfo(
        name="delete_users",
        description="删除users。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_users
    ))

    tools.append(ToolInfo(
        name="delete_webplugin",
        description="删除界面插件。参数：ids (string) - ID列表，以逗号分隔",
        func=mems_api.delete_webplugin
    ))

    tools.append(ToolInfo(
        name="execute_common_map",
        description="执行通用映射。参数：data (dict) - 请求体数据",
        func=mems_api.execute_common_map
    ))

    tools.append(ToolInfo(
        name="execute_ems_request",
        description="执行EMS请求。参数：ems_id (string) - EMS ID, data (dict) - 请求体数据",
        func=mems_api.execute_ems_request
    ))

    tools.append(ToolInfo(
        name="execute_file_tree",
        description="执行文件树。参数：data (dict) - 请求体数据",
        func=mems_api.execute_file_tree
    ))

    tools.append(ToolInfo(
        name="execute_lcc_control",
        description="执行LCC控制。参数：lcc_id (string) - LCC ID, data (dict) - 请求体数据",
        func=mems_api.execute_lcc_control
    ))

    tools.append(ToolInfo(
        name="execute_lcc_map",
        description="执行LCC映射。参数：lcc_id (string) - LCC ID, data (dict) - 请求体数据",
        func=mems_api.execute_lcc_map
    ))

    tools.append(ToolInfo(
        name="export_lcc_models",
        description="导出LCC模型。参数：lcc_id (string) - LCC ID, lang (string) - 语言",
        func=mems_api.export_lcc_models
    ))

    tools.append(ToolInfo(
        name="get_graph_apply_model",
        description="查询图表模型。参数：path (string) - 路径",
        func=mems_api.get_graph_apply_model
    ))

    tools.append(ToolInfo(
        name="get_graph_model",
        description="查询图表模型。参数：path (string) - 路径",
        func=mems_api.get_graph_model
    ))

    tools.append(ToolInfo(
        name="get_lcc_logs",
        description="查询LCC日志。参数：lcc_id (string) - LCC ID",
        func=mems_api.get_lcc_logs
    ))

    tools.append(ToolInfo(
        name="get_lcc_tags",
        description="查询LCC标签。参数：lcc_id (string) - LCC ID, group (integer) - 分组ID",
        func=mems_api.get_lcc_tags
    ))

    tools.append(ToolInfo(
        name="get_script",
        description="查询脚本。参数：script_id - 参数",
        func=mems_api.get_script
    ))

    tools.append(ToolInfo(
        name="get_tags",
        description="查询标签。参数：group (integer) - 分组ID",
        func=mems_api.get_tags
    ))

    tools.append(ToolInfo(
        name="get_webplugin_file",
        description="查询界面插件文件。参数：plugin_id - 参数",
        func=mems_api.get_webplugin_file
    ))

    tools.append(ToolInfo(
        name="import_lcc_models",
        description="导入LCC模型。参数：lcc_id (string) - LCC ID, data (dict) - 请求体数据",
        func=mems_api.import_lcc_models
    ))

    tools.append(ToolInfo(
        name="import_lcc_points",
        description="导入lcc_points。参数：lcc_id (string) - LCC ID",
        func=mems_api.import_lcc_points
    ))

    tools.append(ToolInfo(
        name="import_models_bytes",
        description="导入模型文件。参数：data (dict) - 请求体数据",
        func=mems_api.import_models_bytes
    ))

    tools.append(ToolInfo(
        name="reset_password",
        description="重置repassword。参数：user_id (integer) - 用户ID",
        func=mems_api.reset_password
    ))

    tools.append(ToolInfo(
        name="save_config",
        description="保存配置。参数：data (dict) - 请求体数据",
        func=mems_api.save_config
    ))

    tools.append(ToolInfo(
        name="save_file_tree_node",
        description="保存文件树节点。参数：tree_id (string) - 树ID, data (dict) - 请求体数据",
        func=mems_api.save_file_tree_node
    ))

    tools.append(ToolInfo(
        name="save_script_wasm",
        description="保存脚本WASM。参数：data (dict) - 请求体数据",
        func=mems_api.save_script_wasm
    ))

    tools.append(ToolInfo(
        name="set_alarm_config",
        description="设置告警配置。参数：data (dict) - 请求体数据",
        func=mems_api.set_alarm_config
    ))

    tools.append(ToolInfo(
        name="set_lcc_alarm_config",
        description="设置LCC告警配置。参数：lcc_id (string) - LCC ID, data (dict) - 请求体数据",
        func=mems_api.set_lcc_alarm_config
    ))

    tools.append(ToolInfo(
        name="set_lcc_config",
        description="设置LCC配置。参数：lcc_id (string) - LCC ID, data (dict) - 请求体数据",
        func=mems_api.set_lcc_config
    ))

    tools.append(ToolInfo(
        name="update_device",
        description="更新设备。参数：data (dict) - 请求体数据",
        func=mems_api.update_device
    ))

    tools.append(ToolInfo(
        name="update_device_define",
        description="更新设备定义。参数：data (dict) - 请求体数据",
        func=mems_api.update_device_define
    ))

    tools.append(ToolInfo(
        name="update_lcc_tags",
        description="更新LCC标签。参数：lcc_id (string) - LCC ID, group (integer) - 分组ID, data (dict) - 请求体数据",
        func=mems_api.update_lcc_tags
    ))

    tools.append(ToolInfo(
        name="update_measure_def",
        description="更新测点定义。参数：data (dict) - 请求体数据",
        func=mems_api.update_measure_def
    ))

    tools.append(ToolInfo(
        name="update_plan",
        description="更新计划。参数：data (dict) - 请求体数据",
        func=mems_api.update_plan
    ))

    tools.append(ToolInfo(
        name="update_plan_path",
        description="更新计划路径。参数：data (dict) - 请求体数据",
        func=mems_api.update_plan_path
    ))

    tools.append(ToolInfo(
        name="update_points_remote",
        description="更新远程测点。参数：data (dict) - 请求体数据",
        func=mems_api.update_points_remote
    ))

    tools.append(ToolInfo(
        name="update_prop_define",
        description="更新属性定义。参数：data (dict) - 请求体数据",
        func=mems_api.update_prop_define
    ))

    tools.append(ToolInfo(
        name="update_prop_group",
        description="更新属性分组。参数：data (dict) - 请求体数据",
        func=mems_api.update_prop_group
    ))

    tools.append(ToolInfo(
        name="update_pscpu_aoes",
        description="更新PSCPU AOE。参数：data (dict) - 请求体数据",
        func=mems_api.update_pscpu_aoes
    ))

    tools.append(ToolInfo(
        name="update_pscpu_island",
        description="更新PSCPU电气岛。参数：data (dict) - 请求体数据",
        func=mems_api.update_pscpu_island
    ))

    tools.append(ToolInfo(
        name="update_pscpu_points",
        description="更新PSCPU测点。参数：data (dict) - 请求体数据",
        func=mems_api.update_pscpu_points
    ))

    tools.append(ToolInfo(
        name="update_role",
        description="更新角色。参数：data (dict) - 请求体数据",
        func=mems_api.update_role
    ))

    tools.append(ToolInfo(
        name="update_tags",
        description="更新标签。参数：group (integer) - 分组ID, data (dict) - 请求体数据",
        func=mems_api.update_tags
    ))

    tools.append(ToolInfo(
        name="update_user",
        description="更新用户。参数：data (dict) - 请求体数据",
        func=mems_api.update_user
    ))

    tools.append(ToolInfo(
        name="update_user_group",
        description="更新用户组。参数：data (dict) - 请求体数据",
        func=mems_api.update_user_group
    ))

    return tools