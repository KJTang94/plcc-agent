# MEMS API 文档

***

## 概述

本文档描述了MEMS应用的RESTful API接口和数据类型定义，方便AI Agent调用。

### 基础信息

- **基础URL**: `http://ip:port/api/v1/`
- **认证方式**: Access-Token（在请求头中携带）
- **Content-Type**: `application/json`

### 认证说明

所有API请求（除登录接口外）需要在请求头中携带Access-Token：

```http
Access-Token: <your_token>
```

## API 概览

共 **254** 个API接口，分为以下模块：

- **alarm**: 14 个接口
- **aoes**: 14 个接口
- **auth**: 30 个接口
- **controls**: 6 个接口
- **devices**: 34 个接口
- **ems**: 3 个接口
- **files**: 3 个接口
- **flows**: 28 个接口
- **graphs**: 11 个接口
- **lcc**: 43 个接口
- **measures**: 3 个接口
- **plans**: 10 个接口
- **points**: 14 个接口
- **pscpu**: 17 个接口
- **scripts**: 9 个接口
- **system**: 4 个接口
- **tag_defines**: 1 个接口
- **tags**: 2 个接口
- **tags_cbor**: 1 个接口
- **webplugins**: 7 个接口

***

## Alarm 模块

共 14 个接口

### 1. 查询告警通知配置信息

- **方法**: `GET`
- **路径**: `/alarm/config`
- **函数名**: `get_alarm_config`

### 2. 配置告警通知

- **方法**: `POST`
- **路径**: `/alarm/config`
- **函数名**: `add_alarm_config`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| common | object | 是 | 告警通知形式 |
| common.popup_window | boolean | 是 | 桌面弹窗 |
| common.sound_light | boolean | 是 | 声光 |
| common.text_messages | boolean | 是 | 短信 |
| emergency | object | 是 | 告警通知形式 |
| emergency.popup_window | boolean | 是 | 桌面弹窗 |
| emergency.sound_light | boolean | 是 | 声光 |
| emergency.text_messages | boolean | 是 | 短信 |
| important | object | 是 | 告警通知形式 |
| important.popup_window | boolean | 是 | 桌面弹窗 |
| important.sound_light | boolean | 是 | 声光 |
| important.text_messages | boolean | 是 | 短信 |

### 3. 确认告警

- **方法**: `POST`
- **路径**: `/alarm/confirm/{user_id}`
- **函数名**: `add_alarm_confirm_by_user`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| user_id | integer | 是 | 用户id |

**请求体**:

JSON对象

### 4. 查询已确认的告警

- **方法**: `GET`
- **路径**: `/alarm/confirm_status`
- **函数名**: `get_alarm_confirm_status`

### 5. 查询告警总数

- **方法**: `GET`
- **路径**: `/alarm/count`
- **函数名**: `get_alarm_count`

### 6. 上传单个告警定义

- **方法**: `POST`
- **路径**: `/alarm/define`
- **函数名**: `add_alarm_define`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 否 |  |
| id | integer | 否 |  |
| level | string | 否 |  |
| name | string | 否 |  |
| owners | string | 否 |  |
| rule | string | 否 |  |

### 7. 查询指定id的告警定义

- **方法**: `GET`
- **路径**: `/alarm/define/{id}`
- **函数名**: `get_alarm_define_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 告警定义id |

### 8. 查询所有的告警定义

- **方法**: `GET`
- **路径**: `/alarm/defines`
- **函数名**: `get_alarm_defines`

### 9. 上传告警定义

- **方法**: `POST`
- **路径**: `/alarm/defines`
- **函数名**: `add_alarm_defines`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defines | array[PbAlarmDefine] | 是 |  |
| defines[] | object | 是 |  |
| defines[].desc | string | 否 |  |
| defines[].id | integer | 否 |  |
| defines[].level | string | 否 |  |
| defines[].name | string | 否 |  |
| defines[].owners | string | 否 |  |
| defines[].rule | string | 否 |  |

### 10. 删除指定id的告警定义

- **方法**: `DELETE`
- **路径**: `/alarm/defines/{ids}`
- **函数名**: `delete_alarm_defines_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 告警定义id列表，以,间隔 |

### 11. 上传告警定义（文件形式）

- **方法**: `POST`
- **路径**: `/alarm/defines_file`
- **函数名**: `add_alarm_defines_file`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileContent | array[integer] | 否 |  |
| fileName | string | 否 |  |
| is_zip | boolean | 否 |  |
| op | string | 否 |  |

### 12. 查询未确认的告警数

- **方法**: `GET`
- **路径**: `/alarm/unconfirmed_number`
- **函数名**: `get_alarm_unconfirmed_number`

### 13. 查询告警，结果按照时间排序

- **方法**: `GET`
- **路径**: `/alarms`
- **函数名**: `get_alarms`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 14. 查询未确认的告警列表

- **方法**: `GET`
- **路径**: `/alarms/unconfirmed`
- **函数名**: `get_alarms_unconfirmed`

## Aoes 模块

共 14 个接口

### 1. 查询AOE执行结果

- **方法**: `GET`
- **路径**: `/aoe_results`
- **函数名**: `get_aoe_results`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 2. 查询所有AOE

- **方法**: `GET`
- **路径**: `/aoes/models`
- **函数名**: `get_aoes_models`

### 3. 保存AOE

- **方法**: `POST`
- **路径**: `/aoes/models`
- **函数名**: `add_aoes_models`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].actions | array[ActionEdge] | 是 | 动作列表 |
| [].actions[] | object | 是 | 动作列表 |
| [].actions[].action | string | 是 | 无动作 |
| [].actions[].aoe_id | integer | 是 | AOE id |
| [].actions[].failure_mode | string | 是 | 失败模式 |
| [].actions[].name | string | 是 | 动作名称 |
| [].actions[].source_node | integer | 是 | 源节点 |
| [].actions[].target_node | integer | 是 | 目标节点 |
| [].events | array[EventNode] | 是 | 节点列表 |
| [].events[] | object | 是 | 节点列表 |
| [].events[].aoe_id | integer | 是 | AOE id |
| [].events[].expr | object | 是 | 表达式对象 |
| [].events[].expr.rpn | array[Token] | 是 |  |
| [].events[].expr.rpn[] | object | 是 |  |
| [].events[].expr.rpn[].Binary | string | 是 | Mathematical operations. |
| [].events[].id | integer | 是 | 节点id |
| [].events[].name | string | 是 | 节点名 |
| [].events[].node_type | string | 是 | 节点类型 |
| [].events[].timeout | integer | 是 | 事件还未发生时等待超时时间 |
| [].id | integer | 是 | aoe id |
| [].name | string | 是 | aoe名称 |
| [].trigger_type | object | 是 | 简单固定周期触发 |
| [].trigger_type.SimpleRepeat | object | 是 | 时间对象 |
| [].trigger_type.SimpleRepeat.nanos | integer | 是 | 剩余纳秒 |
| [].trigger_type.SimpleRepeat.secs | integer | 是 | 秒 |
| [].variables | array[array[any]] | 是 | 用户自定义的变量：变量名和表达式 |

### 4. 查询指定版本的AOE

- **方法**: `GET`
- **路径**: `/aoes/models/by_version/{v}`
- **函数名**: `get_aoes_models_by_version_by_v`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | integer | 是 | 版本id |

### 5. 查询根据版本号组装的AOE应用对象

- **方法**: `GET`
- **路径**: `/aoes/models/for_apply`
- **函数名**: `get_aoes_models_for_apply`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 6. 删除指定id的AOE

- **方法**: `DELETE`
- **路径**: `/aoes/models/{ids}`
- **函数名**: `delete_aoes_models_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | AOE_id列表，以,间隔 |

### 7. 根据id查询指定的AOE

- **方法**: `GET`
- **路径**: `/aoes/models/{id}`
- **函数名**: `get_aoes_models_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | AOE_id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 8. 保存AOE（文件形式）

- **方法**: `POST`
- **路径**: `/aoes/models_file`
- **函数名**: `add_aoes_models_file`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileContent | array[integer] | 否 |  |
| fileName | string | 否 |  |
| is_zip | boolean | 否 |  |
| op | string | 否 |  |

### 9. 保存AOE（多文件形式）

- **方法**: `POST`
- **路径**: `/aoes/models_file2`
- **函数名**: `add_aoes_models_file2`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | array[string] | 是 |  |

### 10. 查询所有的AOE版本信息

- **方法**: `GET`
- **路径**: `/aoes/version`
- **函数名**: `get_aoes_version`

### 11. 新增AOE版本

- **方法**: `POST`
- **路径**: `/aoes/version`
- **函数名**: `add_aoes_version`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| note | string | 是 | 提交时的注释 |
| tree_id | string | 是 | 对应的tree_id |
| version | integer | 是 | 版本号 |

### 12. 删除某一个AOE版本

- **方法**: `DELETE`
- **路径**: `/aoes/version/{v}`
- **函数名**: `delete_aoes_version_by_v`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | integer | 是 | 版本id |

### 13. 查询当前运行中的AOE

- **方法**: `GET`
- **路径**: `/running_aoes`
- **函数名**: `get_running_aoes`

### 14. 查询未运行的AOE

- **方法**: `GET`
- **路径**: `/unrun_aoes`
- **函数名**: `get_unrun_aoes`

## Auth 模块

共 30 个接口

### 1. 查询所有权限

- **方法**: `GET`
- **路径**: `/auth/auths`
- **函数名**: `get_auth_auths`

### 2. 新增权限

- **方法**: `POST`
- **路径**: `/auth/auths`
- **函数名**: `add_auth_auths`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].desc | string | 是 | 权限描述 |
| [].id | integer | 是 | 权限ID |
| [].method | string | 是 | 请求方法 |
| [].name | string | 是 | 权限名称 |
| [].url | string | 是 | 权限可操作的url资源地址 |

### 3. 查询指定角色的所有权限

- **方法**: `GET`
- **路径**: `/auth/auths/by_role/{id}`
- **函数名**: `get_auth_auths_by_role`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 角色id |

### 4. 删除指定id的删除权限

- **方法**: `DELETE`
- **路径**: `/auth/auths/{ids}`
- **函数名**: `delete_auth_auths_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 权限id列表，以,间隔 |

### 5. 执行登录

- **方法**: `POST`
- **路径**: `/auth/login`
- **函数名**: `add_auth_login`

**请求体**:

JSON对象

### 6. 查询所有菜单

- **方法**: `GET`
- **路径**: `/auth/menus`
- **函数名**: `get_auth_menus`

### 7. 新增菜单

- **方法**: `POST`
- **路径**: `/auth/menus`
- **函数名**: `add_auth_menus`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].group | string | 是 | 分组 |
| [].id | integer | 是 | 菜单ID |
| [].name | string | 是 | 名称 |
| [].url | string | 是 | 菜单对应的url地址 |

### 8. 查询指定角色的所有菜单

- **方法**: `GET`
- **路径**: `/auth/menus/by_role/{id}`
- **函数名**: `get_auth_menus_by_role`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 角色id |

### 9. 查询指定用户的所有菜单

- **方法**: `GET`
- **路径**: `/auth/menus/by_user/{id}`
- **函数名**: `get_auth_menus_by_user`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 用户id |

### 10. 删除指定id的菜单

- **方法**: `DELETE`
- **路径**: `/auth/menus/{ids}`
- **函数名**: `delete_auth_menus_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 菜单id列表，以,间隔 |

### 11. 用户注册

- **方法**: `POST`
- **路径**: `/auth/register`
- **函数名**: `add_auth_register`

**请求体**:

JSON对象

### 12. 查询所有角色

- **方法**: `GET`
- **路径**: `/auth/roles`
- **函数名**: `get_auth_roles`

### 13. 修改角色

- **方法**: `PUT`
- **路径**: `/auth/roles`
- **函数名**: `update_auth_roles`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 角色ID |
| name | string | 是 | 角色名称 |
| role2authority | array[integer] | 是 | 角色权限关联表，一个角色可以拥有多个权限 |
| role2menu | array[integer] | 是 | 角色菜单关联表，一个角色可以拥有多个菜单 |

### 14. 新增角色

- **方法**: `POST`
- **路径**: `/auth/roles`
- **函数名**: `add_auth_roles`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].id | integer | 是 | 角色ID |
| [].name | string | 是 | 角色名称 |
| [].role2authority | array[integer] | 是 | 角色权限关联表，一个角色可以拥有多个权限 |
| [].role2menu | array[integer] | 是 | 角色菜单关联表，一个角色可以拥有多个菜单 |

### 15. 根据ids查询角色

- **方法**: `GET`
- **路径**: `/auth/roles/{ids}`
- **函数名**: `get_auth_roles_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 角色id列表，以,间隔 |

### 16. 删除指定id的删除角色

- **方法**: `DELETE`
- **路径**: `/auth/roles/{ids}`
- **函数名**: `delete_auth_roles_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 角色id列表，以,间隔 |

### 17. 查询所有用户组

- **方法**: `GET`
- **路径**: `/auth/user_groups`
- **函数名**: `get_auth_user_groups`

### 18. 修改用户组

- **方法**: `PUT`
- **路径**: `/auth/user_groups`
- **函数名**: `update_auth_user_groups`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 用户组ID |
| name | string | 是 | 用户组名称 |
| user_group2role | array[integer] | 是 | 用户组角色关联表，一个用户组可以拥有多个角色 |

### 19. 新增用户组

- **方法**: `POST`
- **路径**: `/auth/user_groups`
- **函数名**: `add_auth_user_groups`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].id | integer | 是 | 用户组ID |
| [].name | string | 是 | 用户组名称 |
| [].user_group2role | array[integer] | 是 | 用户组角色关联表，一个用户组可以拥有多个角色 |

### 20. 删除指定id的用户组

- **方法**: `DELETE`
- **路径**: `/auth/user_groups/{ids}`
- **函数名**: `delete_auth_user_groups_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 用户组id列表，以,间隔 |

### 21. 查询指定id用户组

- **方法**: `GET`
- **路径**: `/auth/user_groups/{id}`
- **函数名**: `get_auth_user_groups_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 用户组id |

### 22. 查询所有用户

- **方法**: `GET`
- **路径**: `/auth/users`
- **函数名**: `get_auth_users`

### 23. 修改用户

- **方法**: `PUT`
- **路径**: `/auth/users`
- **函数名**: `update_auth_users`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| password | array[integer] | 是 | 加密后的用户密码 |
| password_update_time | integer | 是 | 最近一次密码修改时间 |
| pub_info | object | 是 | 用户 - 公开信息 |
| pub_info.desc | string | 否 | 描述 |
| pub_info.email | string | 否 | 用户的邮箱 |
| pub_info.expiration_time | integer | 否 | 过期时间 |
| pub_info.id | integer | 是 | 用户ID |
| pub_info.name | string | 是 | 用户名称 |
| pub_info.phone_number | string | 否 | 用户的手机号 |
| pub_info.special_role | array[integer] | 是 | 特别分配的角色 |
| pub_info.user_group | integer | 是 | 所属用户组的id（用户与用户组关联表，一个用户只能属于一个用户组） |

### 24. 新增用户

- **方法**: `POST`
- **路径**: `/auth/users`
- **函数名**: `add_auth_users`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| password | array[integer] | 是 | 加密后的用户密码 |
| password_update_time | integer | 是 | 最近一次密码修改时间 |
| pub_info | object | 是 | 用户 - 公开信息 |
| pub_info.desc | string | 否 | 描述 |
| pub_info.email | string | 否 | 用户的邮箱 |
| pub_info.expiration_time | integer | 否 | 过期时间 |
| pub_info.id | integer | 是 | 用户ID |
| pub_info.name | string | 是 | 用户名称 |
| pub_info.phone_number | string | 否 | 用户的手机号 |
| pub_info.special_role | array[integer] | 是 | 特别分配的角色 |
| pub_info.user_group | integer | 是 | 所属用户组的id（用户与用户组关联表，一个用户只能属于一个用户组） |

### 25. 根据分组id查询用户信息

- **方法**: `GET`
- **路径**: `/auth/users/by_user_group/{id}`
- **函数名**: `get_auth_users_by_user_group`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 分组id |

### 26. 更改用户密码

- **方法**: `PUT`
- **路径**: `/auth/users/password/{id}`
- **函数名**: `update_auth_users_password_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 用户id |

**请求体**:

JSON对象

### 27. 重置用户密码

- **方法**: `PUT`
- **路径**: `/auth/users/reset_password/{id}`
- **函数名**: `update_auth_users_reset_password_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 用户id |

### 28. 绑定已有用户的角色信息

- **方法**: `PUT`
- **路径**: `/auth/users/roles/{id}`
- **函数名**: `update_auth_users_roles_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 用户id |

**请求体**:

JSON对象

### 29. 删除指定id的用户

- **方法**: `DELETE`
- **路径**: `/auth/users/{ids}`
- **函数名**: `delete_auth_users_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 用户id列表，以,间隔 |

### 30. 查询指定id用户

- **方法**: `GET`
- **路径**: `/auth/users/{id}`
- **函数名**: `get_auth_users_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 用户id |

## Controls 模块

共 6 个接口

### 1. 查询历史设点执行结果

- **方法**: `GET`
- **路径**: `/commands`
- **函数名**: `get_commands`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sender_id | integer | 否 |  |
| point_id | integer | 否 | 测点id |
| start | integer | 否 | 开始时间 |
| end | integer | 否 | 结束时间 |
| date | string | 否 | 时间字符串，yyyy-MM-dd |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 2. 对指定id的AOE采取指定动作，启动/停止/更新

- **方法**: `POST`
- **路径**: `/controls/aoes`
- **函数名**: `add_controls_aoes`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| AoeActions | array[AoeAction] | 是 | AOE指令列表 |
| AoeActions[] | object | 是 | AOE指令列表 |
| AoeActions[].StartAoe | integer | 是 | 开始AOE |

### 3. 执行测点控制

- **方法**: `POST`
- **路径**: `/controls/points`
- **函数名**: `add_controls_points`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| analogs | array[SetFloatValue] | 是 |  |
| analogs[] | object | 是 |  |
| analogs[].point_id | integer | 是 |  |
| analogs[].sender_id | integer | 是 |  |
| analogs[].timestamp | integer | 是 |  |
| analogs[].yt_command | number | 是 |  |
| discretes | array[SetIntValue] | 是 |  |
| discretes[] | object | 是 |  |
| discretes[].point_id | integer | 是 |  |
| discretes[].sender_id | integer | 是 |  |
| discretes[].timestamp | integer | 是 |  |
| discretes[].yk_command | integer | 是 |  |

### 4. 执行测点控制（通过别名）

- **方法**: `POST`
- **路径**: `/controls/points_by_alias`
- **函数名**: `add_controls_points_by_alias`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| analogs | array[SetFloatValue2] | 是 |  |
| analogs[] | object | 是 |  |
| analogs[].point_alias | string | 是 |  |
| analogs[].sender_id | integer | 是 |  |
| analogs[].timestamp | integer | 是 |  |
| analogs[].yt_command | number | 是 |  |
| discretes | array[SetIntValue2] | 是 |  |
| discretes[] | object | 是 |  |
| discretes[].point_alias | string | 是 |  |
| discretes[].sender_id | integer | 是 |  |
| discretes[].timestamp | integer | 是 |  |
| discretes[].yk_command | integer | 是 |  |

### 5. 执行测点控制（通过公式）

- **方法**: `POST`
- **路径**: `/controls/points_by_expr`
- **函数名**: `add_controls_points_by_expr`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commands | array[SetPointValue] | 是 |  |
| commands[] | object | 是 |  |
| commands[].command | object | 是 | 表达式对象 |
| commands[].command.rpn | array[Token] | 是 |  |
| commands[].command.rpn[] | object | 是 |  |
| commands[].command.rpn[].Binary | string | 是 | Mathematical operations. |
| commands[].point_id | integer | 是 |  |
| commands[].sender_id | integer | 是 |  |
| commands[].timestamp | integer | 是 |  |

### 6. 执行测点控制（通过其他数据源）

- **方法**: `POST`
- **路径**: `/controls/points_with_source/{source}`
- **函数名**: `add_controls_points_with_source_by_source`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | integer | 是 | 数据源id |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].analog_value | number | 是 | 模拟量值 |
| [].discrete_value | integer | 是 | 离散量值 |
| [].is_discrete | boolean | 是 | 是否离散量 |
| [].is_transformed | boolean | 是 | 是否已经变换 |
| [].point_id | integer | 是 | 对应的测点 |
| [].timestamp | integer | 是 | 时间戳 |
| [].transformed_analog | number | 是 | 变换后的模拟量值 |
| [].transformed_discrete | integer | 是 | 变换后的离散量值 |

## Devices 模块

共 34 个接口

### 1. 查询拓扑

- **方法**: `GET`
- **路径**: `/devices/cns`
- **函数名**: `get_devices_cns`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 2. 新增拓扑

- **方法**: `POST`
- **路径**: `/devices/cns`
- **函数名**: `add_devices_cns`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].id | integer | 是 | 连接节点id |
| [].psr_id | string | 是 | 资源id |
| [].terminals | array[integer] | 是 | 端子id数组 |

### 3. 查询所有设备定义

- **方法**: `GET`
- **路径**: `/devices/defines`
- **函数名**: `get_devices_defines`

### 4. 修改设备定义

- **方法**: `PUT`
- **路径**: `/devices/defines`
- **函数名**: `update_devices_defines`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 是 | 设备定义的描述 |
| id | integer | 是 | 定义id |
| name | string | 是 | 设备类别名称 |
| prop_groups | array[PropGroupDefine] | 是 | 设备属性 |
| prop_groups[] | object | 是 | 设备属性 |
| prop_groups[].desc | string | 是 | 属性定义描述 |
| prop_groups[].name | string | 是 | 属性定义标识 |
| prop_groups[].prop_defines | array[integer] | 是 | 设备属性实际描述 |
| rsr_type | string | 是 | 电力设备类型 |
| terminal_num | integer | 是 | 端口数量 |

### 5. 新增设备定义

- **方法**: `POST`
- **路径**: `/devices/defines`
- **函数名**: `add_devices_defines`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].desc | string | 是 | 设备定义的描述 |
| [].id | integer | 是 | 定义id |
| [].name | string | 是 | 设备类别名称 |
| [].prop_groups | array[PropGroupDefine] | 是 | 设备属性 |
| [].prop_groups[] | object | 是 | 设备属性 |
| [].prop_groups[].desc | string | 是 | 属性定义描述 |
| [].prop_groups[].name | string | 是 | 属性定义标识 |
| [].prop_groups[].prop_defines | array[integer] | 是 | 设备属性实际描述 |
| [].rsr_type | string | 是 | 电力设备类型 |
| [].terminal_num | integer | 是 | 端口数量 |

### 6. 删除指定id的设备定义

- **方法**: `DELETE`
- **路径**: `/devices/defines/{ids}`
- **函数名**: `delete_devices_defines_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 设备定义id列表，以,间隔 |

### 7. 根据id查询对应的设备定义

- **方法**: `GET`
- **路径**: `/devices/defines/{id}`
- **函数名**: `get_devices_defines_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 设备定义id |

### 8. 查询所有设备列表

- **方法**: `GET`
- **路径**: `/devices/devs`
- **函数名**: `get_devices_devs`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 9. 修改设备

- **方法**: `PUT`
- **路径**: `/devices/devs`
- **函数名**: `update_devices_devs`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| container_id | integer | 否 |  |
| define_id | integer | 是 | 设备定义id |
| desc | string | 是 | 设备描述 |
| id | integer | 是 | 设备id |
| name | string | 是 | 设备名称 |
| prop_group_ids | array[integer] | 是 | 设备属性分组id列表 |
| terminals | array[Terminal] | 是 | 设备的端口 |
| terminals[] | object | 是 | 设备的端口 |
| terminals[].device | integer | 是 | 设备id |
| terminals[].id | integer | 是 | 端口id |

### 10. 新增设备

- **方法**: `POST`
- **路径**: `/devices/devs`
- **函数名**: `add_devices_devs`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].container_id | integer | 否 |  |
| [].define_id | integer | 是 | 设备定义id |
| [].desc | string | 是 | 设备描述 |
| [].id | integer | 是 | 设备id |
| [].name | string | 是 | 设备名称 |
| [].prop_group_ids | array[integer] | 是 | 设备属性分组id列表 |
| [].terminals | array[Terminal] | 是 | 设备的端口 |
| [].terminals[] | object | 是 | 设备的端口 |
| [].terminals[].device | integer | 是 | 设备id |
| [].terminals[].id | integer | 是 | 端口id |

### 11. 删除指定id的设备

- **方法**: `DELETE`
- **路径**: `/devices/devs/{ids}`
- **函数名**: `delete_devices_devs_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 设备id列表，以,间隔 |

### 12. 根据ID查询设备对象

- **方法**: `GET`
- **路径**: `/devices/devs/{id}`
- **函数名**: `get_devices_devs_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 设备id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 13. 查询电气岛

- **方法**: `GET`
- **路径**: `/devices/islands`
- **函数名**: `get_devices_islands`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 14. 根据版本号apply电气岛

- **方法**: `POST`
- **路径**: `/devices/islands`
- **函数名**: `add_devices_islands`

**请求体**:

JSON对象

### 15. 查询设备测点

- **方法**: `GET`
- **路径**: `/devices/measure_defs`
- **函数名**: `get_devices_measure_defs`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 16. 修改设备测点

- **方法**: `PUT`
- **路径**: `/devices/measure_defs`
- **函数名**: `update_devices_measure_defs`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].dev_id | integer | 是 |  |
| [].id | integer | 是 |  |
| [].phase | string | 是 | 量测相位 |
| [].point_id | integer | 是 |  |
| [].terminal_id | integer | 是 |  |

### 17. 新增设备测点

- **方法**: `POST`
- **路径**: `/devices/measure_defs`
- **函数名**: `add_devices_measure_defs`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].dev_id | integer | 是 |  |
| [].id | integer | 是 |  |
| [].phase | string | 是 | 量测相位 |
| [].point_id | integer | 是 |  |
| [].terminal_id | integer | 是 |  |

### 18. 删除指定id的设备测点

- **方法**: `DELETE`
- **路径**: `/devices/measure_defs`
- **函数名**: `delete_devices_measure_defs`

**请求体**:

JSON对象

### 19. 查询测点树（测点在设备树中的路径）

- **方法**: `GET`
- **路径**: `/devices/point_tree`
- **函数名**: `get_devices_point_tree`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 20. 查询所有设备属性定义

- **方法**: `GET`
- **路径**: `/devices/prop_defines`
- **函数名**: `get_devices_prop_defines`

### 21. 修改设备属性定义

- **方法**: `PUT`
- **路径**: `/devices/prop_defines`
- **函数名**: `update_devices_prop_defines`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data_type | string | 是 | 属性类型 |
| data_unit | string | 是 | 数据单位 |
| desc | string | 是 | 属性定义描述 |
| id | integer | 是 | 属性定义id |
| name | string | 是 | 属性定义标识 |

### 22. 新增设备属性定义

- **方法**: `POST`
- **路径**: `/devices/prop_defines`
- **函数名**: `add_devices_prop_defines`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].data_type | string | 是 | 属性类型 |
| [].data_unit | string | 是 | 数据单位 |
| [].desc | string | 是 | 属性定义描述 |
| [].id | integer | 是 | 属性定义id |
| [].name | string | 是 | 属性定义标识 |

### 23. 删除指定id的设备属性定义

- **方法**: `DELETE`
- **路径**: `/devices/prop_defines/{ids}`
- **函数名**: `delete_devices_prop_defines_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 设备属性定义id列表，以,间隔 |

### 24. 查询所有设备属性分组

- **方法**: `GET`
- **路径**: `/devices/prop_groups`
- **函数名**: `get_devices_prop_groups`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 25. 修改设备属性分组

- **方法**: `PUT`
- **路径**: `/devices/prop_groups`
- **函数名**: `update_devices_prop_groups`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].defines | array[integer] | 是 | 设备属性定义列表 |
| [].id | integer | 是 |  |
| [].name | string | 是 | 分组名称，用于显示，以及匹配PropGroupDefine |
| [].props | array[PropValue] | 是 | 设备属性实际描述 |
| [].props[] | object | 是 | 设备属性实际描述 |
| [].props[].U8 | integer | 是 |  |
| [].rsr_id | integer | 是 | resource id |

### 26. 新增设备属性分组

- **方法**: `POST`
- **路径**: `/devices/prop_groups`
- **函数名**: `add_devices_prop_groups`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].defines | array[integer] | 是 | 设备属性定义列表 |
| [].id | integer | 是 |  |
| [].name | string | 是 | 分组名称，用于显示，以及匹配PropGroupDefine |
| [].props | array[PropValue] | 是 | 设备属性实际描述 |
| [].props[] | object | 是 | 设备属性实际描述 |
| [].props[].U8 | integer | 是 |  |
| [].rsr_id | integer | 是 | resource id |

### 27. 根据id列表查看设备属性分组列表

- **方法**: `GET`
- **路径**: `/devices/prop_groups/{ids}`
- **函数名**: `get_devices_prop_groups_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 设备属性分组id列表，以,间隔 |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 28. 删除指定id的设备属性分组

- **方法**: `DELETE`
- **路径**: `/devices/prop_groups/{ids}`
- **函数名**: `delete_devices_prop_groups_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 设备属性分组id列表，以,间隔 |

### 29. 清空资源

- **方法**: `DELETE`
- **路径**: `/devices/resources_clear`
- **函数名**: `delete_devices_resources_clear`

### 30. 查询电气岛所有版本

- **方法**: `GET`
- **路径**: `/devices/version`
- **函数名**: `get_devices_version`

### 31. 新增电气岛版本

- **方法**: `POST`
- **路径**: `/devices/version`
- **函数名**: `add_devices_version`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| note | string | 是 | 提交时的注释 |
| tree_id | string | 是 | 对应的tree_id |
| version | integer | 是 | 版本号 |

### 32. 删除指定id的电气岛版本

- **方法**: `DELETE`
- **路径**: `/devices/version/{id}`
- **函数名**: `delete_devices_version_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 版本id |

### 33. 查询日志字节数组

- **方法**: `GET`
- **路径**: `/logs_bytes`
- **函数名**: `get_logs_bytes`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| is_query_size | boolean | 否 | 是否限制文件大小 |

### 34. 导入所有模型字节数组

- **方法**: `POST`
- **路径**: `/multi_import_bytes`
- **函数名**: `add_multi_import_bytes`

**请求体**:

JSON对象

## Ems 模块

共 3 个接口

### 1. 对指定id的ems执行请求

- **方法**: `POST`
- **路径**: `/ems/request/{ems_id}`
- **函数名**: `add_ems_request_by_ems`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ems_id | string | 是 | ems_id |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 否 |  |
| function | string | 否 |  |
| header_keys | array[string] | 是 |  |
| header_values | array[string] | 是 |  |
| id | integer | 否 |  |
| url | string | 否 |  |

### 2. 查询指定id的ems

- **方法**: `GET`
- **路径**: `/ems/{id}`
- **函数名**: `get_ems_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | ems_id |

### 3. 查询所有的ems

- **方法**: `GET`
- **路径**: `/ems_list`
- **函数名**: `get_ems_list`

## Files 模块

共 3 个接口

### 1. 执行filetree的操作

- **方法**: `POST`
- **路径**: `/file_tree`
- **函数名**: `add_file_tree`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| op | string | 是 | 文件树的操作类型 |
| op_paths | array[string] | 是 |  |
| path | string | 否 |  |
| tree_id | string | 是 |  |
| version | integer | 否 |  |

### 2. 保存filetree的一个节点

- **方法**: `POST`
- **路径**: `/file_tree/{id}`
- **函数名**: `add_file_tree_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | tree_id |

**请求体**:

JSON对象

### 3. 提交filetree版本

- **方法**: `POST`
- **路径**: `/file_tree_version`
- **函数名**: `add_file_tree_version`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| note | string | 是 | 提交时的注释 |
| tree_id | string | 是 | 对应的tree_id |
| version | integer | 是 | 版本号 |

## Flows 模块

共 28 个接口

### 1. 查询报表结果（简洁模式）

- **方法**: `GET`
- **路径**: `/flows/brief_results`
- **函数名**: `get_flows_brief_results`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 2. 执行报表动作

- **方法**: `POST`
- **路径**: `/flows/controls`
- **函数名**: `add_flows_controls`

**请求体**:

JSON对象

### 3. 报表节点测试

- **方法**: `POST`
- **路径**: `/flows/debug`
- **函数名**: `add_flows_debug`

**请求体**:

JSON对象

### 4. 查询报表

- **方法**: `GET`
- **路径**: `/flows/models`
- **函数名**: `get_flows_models`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 否 | 测点id（优先） |
| ids | string | 否 | 测点id列表，以,间隔 |

### 5. 修改报表

- **方法**: `PUT`
- **路径**: `/flows/models`
- **函数名**: `update_flows_models`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].actions | array[DfActionEdge] | 是 | 边 |
| [].actions[] | object | 是 | 边 |
| [].actions[].action | object | 是 | 对单个Dataframe进行运算 |
| [].actions[].action.Eval | array[Expr] | 是 | 对单个Dataframe进行运算 |
| [].actions[].action.Eval[] | object | 是 | 对单个Dataframe进行运算 |
| [].actions[].action.Eval[].rpn | array[Token] | 是 |  |
| [].actions[].action.Eval[].rpn[] | object | 是 |  |
| [].actions[].action.Eval[].rpn[].Binary | string | 是 | Mathematical operations. |
| [].actions[].desc | string | 是 |  |
| [].actions[].flow_id | integer | 是 |  |
| [].actions[].name | string | 是 |  |
| [].actions[].source_node | integer | 是 |  |
| [].actions[].target_node | integer | 是 |  |
| [].aoe_var | array[any] | 否 | destination of aoe variable |
| [].id | integer | 是 | dff id |
| [].is_on | boolean | 是 | should schedule |
| [].name | string | 是 | dff name |
| [].nodes | array[DfNode] | 是 | 节点 |
| [].nodes[] | object | 是 | 节点 |
| [].nodes[].flow_id | integer | 是 |  |
| [].nodes[].id | integer | 是 |  |
| [].nodes[].name | string | 是 |  |
| [].nodes[].node_type | object | 是 | query data source |
| [].nodes[].node_type.Source | object | 是 | 直接导入数据 |
| [].nodes[].node_type.Source.Data | any | 是 | 直接导入数据 |
| [].save_mode | string | 是 | Data frame save mode |
| [].trigger_type | object | 是 | Dataframe flow 启动的方式 |
| [].trigger_type.SimpleRepeat | object | 是 | 时间对象 |
| [].trigger_type.SimpleRepeat.nanos | integer | 是 | 剩余纳秒 |
| [].trigger_type.SimpleRepeat.secs | integer | 是 | 秒 |

### 6. 新增报表

- **方法**: `POST`
- **路径**: `/flows/models`
- **函数名**: `add_flows_models`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].actions | array[DfActionEdge] | 是 | 边 |
| [].actions[] | object | 是 | 边 |
| [].actions[].action | object | 是 | 对单个Dataframe进行运算 |
| [].actions[].action.Eval | array[Expr] | 是 | 对单个Dataframe进行运算 |
| [].actions[].action.Eval[] | object | 是 | 对单个Dataframe进行运算 |
| [].actions[].action.Eval[].rpn | array[Token] | 是 |  |
| [].actions[].action.Eval[].rpn[] | object | 是 |  |
| [].actions[].action.Eval[].rpn[].Binary | string | 是 | Mathematical operations. |
| [].actions[].desc | string | 是 |  |
| [].actions[].flow_id | integer | 是 |  |
| [].actions[].name | string | 是 |  |
| [].actions[].source_node | integer | 是 |  |
| [].actions[].target_node | integer | 是 |  |
| [].aoe_var | array[any] | 否 | destination of aoe variable |
| [].id | integer | 是 | dff id |
| [].is_on | boolean | 是 | should schedule |
| [].name | string | 是 | dff name |
| [].nodes | array[DfNode] | 是 | 节点 |
| [].nodes[] | object | 是 | 节点 |
| [].nodes[].flow_id | integer | 是 |  |
| [].nodes[].id | integer | 是 |  |
| [].nodes[].name | string | 是 |  |
| [].nodes[].node_type | object | 是 | query data source |
| [].nodes[].node_type.Source | object | 是 | 直接导入数据 |
| [].nodes[].node_type.Source.Data | any | 是 | 直接导入数据 |
| [].save_mode | string | 是 | Data frame save mode |
| [].trigger_type | object | 是 | Dataframe flow 启动的方式 |
| [].trigger_type.SimpleRepeat | object | 是 | 时间对象 |
| [].trigger_type.SimpleRepeat.nanos | integer | 是 | 剩余纳秒 |
| [].trigger_type.SimpleRepeat.secs | integer | 是 | 秒 |

### 7. 删除指定id的报表

- **方法**: `DELETE`
- **路径**: `/flows/models/{ids}`
- **函数名**: `delete_flows_models_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 报表id列表，以,间隔 |

### 8. 新增报表（多文件形式）

- **方法**: `POST`
- **路径**: `/flows/models_file2`
- **函数名**: `add_flows_models_file2`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | array[string] | 是 |  |

### 9. 查询报表（自定义JSON格式）

- **方法**: `GET`
- **路径**: `/flows/models_json`
- **函数名**: `get_flows_models_json`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 否 | 测点id（优先） |
| ids | string | 否 | 测点id列表，以,间隔 |

### 10. 解析prog（多文件形式）

- **方法**: `POST`
- **路径**: `/flows/prog_file2`
- **函数名**: `add_flows_prog_file2`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | array[string] | 是 |  |

### 11. 重新加载报表

- **方法**: `POST`
- **路径**: `/flows/reload_dff/{flow_id}`
- **函数名**: `add_flows_reload_dff_by_flow`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flow_id | string | 是 | 报表id |

### 12. 查询报表结果keys

- **方法**: `GET`
- **路径**: `/flows/result_keys`
- **函数名**: `get_flows_result_keys`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 否 | 测点id（优先） |
| ids | string | 否 | 测点id列表，以,间隔 |

### 13. 根据id查询报表执行结果

- **方法**: `GET`
- **路径**: `/flows/results`
- **函数名**: `get_flows_results`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 14. 删除指定报表id指定key的报表结果

- **方法**: `DELETE`
- **路径**: `/flows/results`
- **函数名**: `delete_flows_results`

**请求体**:

JSON对象

### 15. 重命名报表结果（简洁模式）

- **方法**: `POST`
- **路径**: `/flows/results/rename`
- **函数名**: `add_flows_results_rename`

**请求体**:

JSON对象

### 16. query_flows_result_and_eval

- **方法**: `PUT`
- **路径**: `/flows/results/{id}/{key}`
- **函数名**: `update_flows_results_by_by_key`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 报表id |
| key | string | 是 | key |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].rpn | array[Token] | 是 |  |
| [].rpn[] | object | 是 |  |
| [].rpn[].Binary | string | 是 | Mathematical operations. |

### 17. query_flows_result_in_view

- **方法**: `GET`
- **路径**: `/flows/results/{id}/{key}/{view}`
- **函数名**: `get_flows_results_by_by_key_by_view`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 报表id |
| key | string | 是 | key |
| view | string | 是 | view |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].rpn | array[Token] | 是 |  |
| [].rpn[] | object | 是 |  |
| [].rpn[].Binary | string | 是 | Mathematical operations. |

### 18. 根据id查询报表执行结果（Parquet格式）

- **方法**: `GET`
- **路径**: `/flows/results_json`
- **函数名**: `get_flows_results_json`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 19. 根据id查询报表执行结果（逐行写入方式）

- **方法**: `GET`
- **路径**: `/flows/results_json_rows`
- **函数名**: `get_flows_results_json_rows`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 20. 查询运行中的报表

- **方法**: `GET`
- **路径**: `/flows/running`
- **函数名**: `get_flows_running`

### 21. 查询报表（不包含Dataframe）

- **方法**: `GET`
- **路径**: `/flows/simple_models`
- **函数名**: `get_flows_simple_models`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 否 | 测点id（优先） |
| ids | string | 否 | 测点id列表，以,间隔 |

### 22. 查询未运行的报表

- **方法**: `GET`
- **路径**: `/flows/unrun`
- **函数名**: `get_flows_unrun`

### 23. 查询报表展示模型

- **方法**: `GET`
- **路径**: `/flows/view`
- **函数名**: `get_flows_view`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 展示模型id |
| flow_id | integer | 否 | 报表id |

### 24. 修改报表展示模型

- **方法**: `PUT`
- **路径**: `/flows/view`
- **函数名**: `update_flows_view`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | any | 是 |  |
| echart_js | string | 否 |  |
| exprs | string | 是 |  |
| flow_id | integer | 是 |  |
| id | integer | 是 |  |
| is_show | boolean | 是 |  |
| layout | any | 是 |  |
| name | string | 是 |  |
| plot_template | string | 是 |  |
| plot_type | string | 是 |  |
| refresh_interval | integer | 否 |  |
| series_style | any | 是 |  |

### 25. 新增报表展示模型

- **方法**: `POST`
- **路径**: `/flows/view`
- **函数名**: `add_flows_view`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | any | 是 |  |
| echart_js | string | 否 |  |
| exprs | string | 是 |  |
| flow_id | integer | 是 |  |
| id | integer | 是 |  |
| is_show | boolean | 是 |  |
| layout | any | 是 |  |
| name | string | 是 |  |
| plot_template | string | 是 |  |
| plot_type | string | 是 |  |
| refresh_interval | integer | 否 |  |
| series_style | any | 是 |  |

### 26. 删除指定id的报表展示模型

- **方法**: `DELETE`
- **路径**: `/flows/view/{ids}`
- **函数名**: `delete_flows_view_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 报表展示模型id列表，以,间隔 |

### 27. 加载其他mems来的Dataframe

- **方法**: `POST`
- **路径**: `/north/dataframe/{flow}/{node}`
- **函数名**: `add_north_dataframe_by_flow_by_node`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flow | integer | 是 | 报表id |
| node | integer | 是 | 节点id |

**请求体**:

JSON对象

### 28. 重启北向服务

- **方法**: `POST`
- **路径**: `/north/restart`
- **函数名**: `add_north_restart`

## Graphs 模块

共 11 个接口

### 1. 设置svg是否显示

- **方法**: `POST`
- **路径**: `/graphs/apply/additional`
- **函数名**: `add_graphs_apply_additional`

**请求体**:

JSON对象

### 2. 获取应用版本某个名称的svg

- **方法**: `GET`
- **路径**: `/graphs/apply/models/{path}`
- **函数名**: `get_graphs_apply_models_by_path`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | svg名称 |

### 3. 获取应用版本的所有svg名称

- **方法**: `GET`
- **路径**: `/graphs/apply/paths`
- **函数名**: `get_graphs_apply_paths`

### 4. 应用一个svg版本

- **方法**: `POST`
- **路径**: `/graphs/apply/version`
- **函数名**: `add_graphs_apply_version`

**请求体**:

JSON对象

### 5. 新增svg

- **方法**: `POST`
- **路径**: `/graphs/models`
- **函数名**: `add_graphs_models`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].fileContent | array[integer] | 否 |  |
| [].fileName | string | 否 |  |
| [].is_zip | boolean | 否 |  |
| [].op | string | 否 |  |

### 6. 根据path查询指定的svg内容

- **方法**: `GET`
- **路径**: `/graphs/models/{path}`
- **函数名**: `get_graphs_models_by_path`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | svg名称 |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 7. 删除指定名称的svg

- **方法**: `DELETE`
- **路径**: `/graphs/models/{path}`
- **函数名**: `delete_graphs_models_by_path`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | svg名称列表，以,间隔 |

### 8. 查询所有svg的名称

- **方法**: `GET`
- **路径**: `/graphs/paths`
- **函数名**: `get_graphs_paths`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 9. 查询所有的svg版本信息

- **方法**: `GET`
- **路径**: `/graphs/version`
- **函数名**: `get_graphs_version`

### 10. 提交svg版本

- **方法**: `POST`
- **路径**: `/graphs/version`
- **函数名**: `add_graphs_version`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| note | string | 是 | 提交时的注释 |
| tree_id | string | 是 | 对应的tree_id |
| version | integer | 是 | 版本号 |

### 11. 删除指定svg版本

- **方法**: `DELETE`
- **路径**: `/graphs/version/{v}`
- **函数名**: `delete_graphs_version_by_v`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | integer | 是 | 版本id |

## Lcc 模块

共 43 个接口

### 1. 查询指定lcc的告警通知配置信息

- **方法**: `GET`
- **路径**: `/lcc/alarm/config/{lcc_id}`
- **函数名**: `get_lcc_alarm_config_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

### 2. 配置指定lcc的告警通知格式

- **方法**: `POST`
- **路径**: `/lcc/alarm/config/{lcc_id}`
- **函数名**: `add_lcc_alarm_config_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| common | object | 是 | 告警通知形式 |
| common.popup_window | boolean | 是 | 桌面弹窗 |
| common.sound_light | boolean | 是 | 声光 |
| common.text_messages | boolean | 是 | 短信 |
| emergency | object | 是 | 告警通知形式 |
| emergency.popup_window | boolean | 是 | 桌面弹窗 |
| emergency.sound_light | boolean | 是 | 声光 |
| emergency.text_messages | boolean | 是 | 短信 |
| important | object | 是 | 告警通知形式 |
| important.popup_window | boolean | 是 | 桌面弹窗 |
| important.sound_light | boolean | 是 | 声光 |
| important.text_messages | boolean | 是 | 短信 |

### 3. 指定lcc确认告警

- **方法**: `POST`
- **路径**: `/lcc/alarm/confirm/{lcc_id}/{user_id}`
- **函数名**: `add_lcc_alarm_confirm_by_lcc_by_user`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |
| user_id | integer | 是 | 用户id |

**请求体**:

JSON对象

### 4. 查询指定lcc的已确认告警

- **方法**: `GET`
- **路径**: `/lcc/alarm/confirm_status/{lcc_id}`
- **函数名**: `get_lcc_alarm_confirm_status_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

### 5. 查询指定lcc的告警总数

- **方法**: `GET`
- **路径**: `/lcc/alarm/count/{lcc_id}`
- **函数名**: `get_lcc_alarm_count_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

### 6. 上传指定lcc的单个告警定义

- **方法**: `POST`
- **路径**: `/lcc/alarm/define/{lcc_id}`
- **函数名**: `add_lcc_alarm_define_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 否 |  |
| id | integer | 否 |  |
| level | string | 否 |  |
| name | string | 否 |  |
| owners | string | 否 |  |
| rule | string | 否 |  |

### 7. 查询指定lcc中指定id的告警定义

- **方法**: `GET`
- **路径**: `/lcc/alarm/define/{lcc_id}/{id}`
- **函数名**: `get_lcc_alarm_define_by_lcc_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |
| id | integer | 是 | 告警id |

### 8. 查询指定lcc的所有告警定义

- **方法**: `GET`
- **路径**: `/lcc/alarm/defines/{lcc_id}`
- **函数名**: `get_lcc_alarm_defines_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

### 9. 上传指定lcc的告警定义

- **方法**: `POST`
- **路径**: `/lcc/alarm/defines/{lcc_id}`
- **函数名**: `add_lcc_alarm_defines_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defines | array[PbAlarmDefine] | 是 |  |
| defines[] | object | 是 |  |
| defines[].desc | string | 否 |  |
| defines[].id | integer | 否 |  |
| defines[].level | string | 否 |  |
| defines[].name | string | 否 |  |
| defines[].owners | string | 否 |  |
| defines[].rule | string | 否 |  |

### 10. 删除指定lcc的指定id们的告警定义

- **方法**: `DELETE`
- **路径**: `/lcc/alarm/defines/{lcc_id}/{ids}`
- **函数名**: `delete_lcc_alarm_defines_by_lcc_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |
| ids | string | 是 | 告警定义id列表，以,间隔 |

### 11. 查询指定lcc的未确认告警数

- **方法**: `GET`
- **路径**: `/lcc/alarm/unconfirmed_number/{lcc_id}`
- **函数名**: `get_lcc_alarm_unconfirmed_number_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

### 12. 查询指定lcc的未确认告警列表

- **方法**: `GET`
- **路径**: `/lcc/alarms/unconfirmed/{lcc_id}`
- **函数名**: `get_lcc_alarms_unconfirmed_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

### 13. 查询指定lcc的告警结果
查询告警，结果按照时间排序

- **方法**: `GET`
- **路径**: `/lcc/alarms/{lcc_id}`
- **函数名**: `get_lcc_alarms_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 14. 导出指定lcc的所有模型字节数组

- **方法**: `GET`
- **路径**: `/lcc/allmodels_bytes/{lcc_id}`
- **函数名**: `get_lcc_allmodels_bytes_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lang | string | 是 | 语言 |

### 15. 导入指定lcc的所有模型字节数组

- **方法**: `POST`
- **路径**: `/lcc/allmodels_bytes/{lcc_id}`
- **函数名**: `add_lcc_allmodels_bytes_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

JSON对象

### 16. 查询指定lcc的AOE执行结果

- **方法**: `GET`
- **路径**: `/lcc/aoe_results/{lcc_id}`
- **函数名**: `get_lcc_aoe_results_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 17. 查询指定lcc的AOE

- **方法**: `GET`
- **路径**: `/lcc/aoes/models/{lcc_id}`
- **函数名**: `get_lcc_aoes_models_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | aoe id列表，以,间隔 |

### 18. 保存指定lcc的AOE

- **方法**: `POST`
- **路径**: `/lcc/aoes/models/{lcc_id}`
- **函数名**: `add_lcc_aoes_models_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].actions | array[ActionEdge] | 是 | 动作列表 |
| [].actions[] | object | 是 | 动作列表 |
| [].actions[].action | string | 是 | 无动作 |
| [].actions[].aoe_id | integer | 是 | AOE id |
| [].actions[].failure_mode | string | 是 | 失败模式 |
| [].actions[].name | string | 是 | 动作名称 |
| [].actions[].source_node | integer | 是 | 源节点 |
| [].actions[].target_node | integer | 是 | 目标节点 |
| [].events | array[EventNode] | 是 | 节点列表 |
| [].events[] | object | 是 | 节点列表 |
| [].events[].aoe_id | integer | 是 | AOE id |
| [].events[].expr | object | 是 | 表达式对象 |
| [].events[].expr.rpn | array[Token] | 是 |  |
| [].events[].expr.rpn[] | object | 是 |  |
| [].events[].expr.rpn[].Binary | string | 是 | Mathematical operations. |
| [].events[].id | integer | 是 | 节点id |
| [].events[].name | string | 是 | 节点名 |
| [].events[].node_type | string | 是 | 节点类型 |
| [].events[].timeout | integer | 是 | 事件还未发生时等待超时时间 |
| [].id | integer | 是 | aoe id |
| [].name | string | 是 | aoe名称 |
| [].trigger_type | object | 是 | 简单固定周期触发 |
| [].trigger_type.SimpleRepeat | object | 是 | 时间对象 |
| [].trigger_type.SimpleRepeat.nanos | integer | 是 | 剩余纳秒 |
| [].trigger_type.SimpleRepeat.secs | integer | 是 | 秒 |
| [].variables | array[array[any]] | 是 | 用户自定义的变量：变量名和表达式 |

### 19. 删除指定lcc指定id的AOE

- **方法**: `DELETE`
- **路径**: `/lcc/aoes/models/{lcc_id}/{ids}`
- **函数名**: `delete_lcc_aoes_models_by_lcc_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |
| ids | string | 是 | AOE_id列表，以,间隔 |

### 20. 查询指定lcc的所有用户

- **方法**: `GET`
- **路径**: `/lcc/auth/users/{lcc_id}`
- **函数名**: `get_lcc_auth_users_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

### 21. 查询指定lcc的历史设点执行结果

- **方法**: `GET`
- **路径**: `/lcc/commands/{lcc_id}`
- **函数名**: `get_lcc_commands_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sender_id | integer | 否 |  |
| point_id | integer | 否 | 测点id |
| start | integer | 否 | 开始时间 |
| end | integer | 否 | 结束时间 |
| date | string | 否 | 时间字符串，yyyy-MM-dd |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 22. 执行指定lcc的map映射操作

- **方法**: `POST`
- **路径**: `/lcc/common_map/{lcc_id}`
- **函数名**: `add_lcc_common_map_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| Query | array[integer] | 是 | 查询 |

### 23. 查询指定lcc的配置

- **方法**: `GET`
- **路径**: `/lcc/config/{lcc_id}`
- **函数名**: `get_lcc_config_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

### 24. 保存指定lcc的配置

- **方法**: `POST`
- **路径**: `/lcc/config/{lcc_id}`
- **函数名**: `add_lcc_config_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| properties | object | 是 | 主要配置属性 |
| properties2 | object | 是 | 次要配置属性 |

### 25. 执行Lcc操作

- **方法**: `POST`
- **路径**: `/lcc/controls/{lcc_id}`
- **函数名**: `add_lcc_controls_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

JSON对象

### 26. 查询指定lcc的日志

- **方法**: `GET`
- **路径**: `/lcc/logs_bytes/{lcc_id}`
- **函数名**: `get_lcc_logs_bytes_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| is_query_size | boolean | 否 | 是否限制文件大小 |

### 27. 查询指定lcc的历史量测

- **方法**: `GET`
- **路径**: `/lcc/measures/{lcc_id}`
- **函数名**: `get_lcc_measures_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 28. 加载LCC的测点到base服务

- **方法**: `POST`
- **路径**: `/lcc/points/import_str/{lcc_id}`
- **函数名**: `add_lcc_points_import_str_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

JSON对象

### 29. 查询指定lcc的测点信息

- **方法**: `GET`
- **路径**: `/lcc/points/models/{lcc_id}`
- **函数名**: `get_lcc_points_models_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 |  |
| name | string | 否 |  |
| is_soe | boolean | 否 |  |

### 30. 保存指定lcc的测点信息

- **方法**: `POST`
- **路径**: `/lcc/points/models/{lcc_id}`
- **函数名**: `add_lcc_points_models_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].alarm_level1_expr | string | 是 | 告警级别1的表达式 |
| [].alarm_level2_expr | string | 是 | 告警级别2的表达式 |
| [].alias_id | string | 是 | 字符串id |
| [].change_expr | string | 是 | 判断是否"变化"的公式，用于变化上传或储存 |
| [].data_unit | string | 是 | 单位 |
| [].desc | string | 是 | Description |
| [].expression | string | 是 | 如果是计算点，这是表达式 |
| [].init_value | integer | 是 | 默认值存储在8个字节，需要根据is_discrete来转换成具体的值 |
| [].inv_trans_expr | string | 是 | 逆变换公式 |
| [].is_computing_point | boolean | 是 | 是否是计算点 |
| [].is_discrete | boolean | 是 | 是否是离散量 |
| [].is_realtime | boolean | 是 | 如是，则不判断是否"变化"，均上传 |
| [].is_soe | boolean | 是 | 是否是soe点 |
| [].lower_limit | number | 是 | 下限，用于坏数据辨识 |
| [].point_id | integer | 是 | 唯一的id |
| [].point_name | string | 是 | 测点名 |
| [].trans_expr | string | 是 | 变换公式 |
| [].upper_limit | number | 是 | 上限，用于坏数据辨识 |
| [].zero_expr | string | 是 | 判断是否为0值的公式 |

### 31. 删除指定lcc的测点

- **方法**: `DELETE`
- **路径**: `/lcc/points/models/{lcc_id}`
- **函数名**: `delete_lcc_points_models_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

JSON对象

### 32. 查询指定lcc运行中的AOE

- **方法**: `GET`
- **路径**: `/lcc/running_aoes/{lcc_id}`
- **函数名**: `get_lcc_running_aoes_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

### 33. 查询指定lcc的SOE

- **方法**: `GET`
- **路径**: `/lcc/soes/{lcc_id}`
- **函数名**: `get_lcc_soes_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 34. 查询指定lcc指定分组的标签名称及id列表

- **方法**: `GET`
- **路径**: `/lcc/tag_defines/{lcc_id}/{group}`
- **函数名**: `get_lcc_tag_defines_by_lcc_by_group`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |
| group | integer | 是 | 分组id |

### 35. 更新指定lcc指定分组下标签名和测点数组关系

- **方法**: `PUT`
- **路径**: `/lcc/tags/{lcc_id}/{group}`
- **函数名**: `update_lcc_tags_by_lcc_by_group`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |
| group | integer | 是 | 分组id |

**请求体**:

JSON对象

### 36. 查询指定lcc指定分组下标签id对应的测点数组

- **方法**: `POST`
- **路径**: `/lcc/tags/{lcc_id}/{group}`
- **函数名**: `add_lcc_tags_by_lcc_by_group`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |
| group | integer | 是 | 分组id |

**请求体**:

JSON对象

### 37. 删除指定lcc指定分组下标签id和测点的关系

- **方法**: `DELETE`
- **路径**: `/lcc/tags/{lcc_id}/{group}`
- **函数名**: `delete_lcc_tags_by_lcc_by_group`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |
| group | integer | 是 | 分组id |

**请求体**:

JSON对象

### 38. 查询指定lcc的通道信息

- **方法**: `GET`
- **路径**: `/lcc/transports/models/{lcc_id}`
- **函数名**: `get_lcc_transports_models_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 通道id列表，以,间隔 |
| transport_type | string | 否 | 通道类型 |

### 39. 保存指定lcc的通道信息

- **方法**: `POST`
- **路径**: `/lcc/transports/models/{lcc_id}`
- **函数名**: `add_lcc_transports_models_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].MbcTcp | object | 是 | ModbusTcp客户端通道信息 |
| [].MbcTcp.connections | array[MbConnection] | 是 | Modbus通道连接信息 |
| [].MbcTcp.connections[] | object | 是 | Modbus通道连接信息 |
| [].MbcTcp.connections[].coil_write_code | integer | 否 |  |
| [].MbcTcp.connections[].default_polling_period_in_milli | integer | 是 |  |
| [].MbcTcp.connections[].delay_between_requests | integer | 是 | 两条请求直接的间隔 |
| [].MbcTcp.connections[].holding_write_code | integer | 否 |  |
| [].MbcTcp.connections[].max_read_bit_count | integer | 是 |  |
| [].MbcTcp.connections[].max_read_register_count | integer | 是 |  |
| [].MbcTcp.connections[].max_write_bit_count | integer | 是 |  |
| [].MbcTcp.connections[].max_write_register_count | integer | 是 |  |
| [].MbcTcp.connections[].mb_data_configure | array[RegisterData] | 是 | register settings |
| [].MbcTcp.connections[].mb_data_configure[] | object | 是 | register settings |
| [].MbcTcp.connections[].mb_data_configure[].data_id | integer | 是 | 数据标识 |
| [].MbcTcp.connections[].mb_data_configure[].point_ids | array[integer] | 是 | 对应的测点Id |
| [].MbcTcp.connections[].mb_data_configure[].polling_period_in_milli | integer | 是 | 轮询周期，毫秒 |
| [].MbcTcp.connections[].name | string | 是 |  |
| [].MbcTcp.connections[].point_id | integer | 是 | 通道状态对应的测点号 |
| [].MbcTcp.connections[].point_id_to_rd | object | 是 | key is point id, value is position of register data |
| [].MbcTcp.connections[].polling_period_to_data | object | 是 | 轮询周期不同的数据, key is period in milli, value is position. |
| [].MbcTcp.connections[].protocol_type | string | 是 | Modbus协议类型 |
| [].MbcTcp.connections[].register_addr_to_rd | object | 是 | key:寄存器地址,value:setting中vec<RegisterData>的位置 |
| [].MbcTcp.connections[].slave_id | integer | 是 |  |
| [].MbcTcp.connections[].timeout_in_milli | integer | 是 | 超时设置 |
| [].MbcTcp.id | integer | 是 | 通道id |
| [].MbcTcp.name | string | 是 | 通道名称 |
| [].MbcTcp.tcp_server | array[any] | 是 | 服务端的ip和port |

### 40. 删除指定lcc指定id的通道

- **方法**: `DELETE`
- **路径**: `/lcc/transports/models/{lcc_id}/{ids}`
- **函数名**: `delete_lcc_transports_models_by_lcc_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |
| ids | string | 是 | 通道id列表，以,间隔 |

### 41. 查询指定lcc未运行的AOE

- **方法**: `GET`
- **路径**: `/lcc/unrun_aoes/{lcc_id}`
- **函数名**: `get_lcc_unrun_aoes_by_lcc`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lcc_id | string | 是 | lcc_id |

### 42. 查询指定id的lcc

- **方法**: `GET`
- **路径**: `/lcc/{id}`
- **函数名**: `get_lcc_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | lcc_id |

### 43. 查询所有的lcc

- **方法**: `GET`
- **路径**: `/lcc_list`
- **函数名**: `get_lcc_list`

## Measures 模块

共 3 个接口

### 1. 量测值初始化

- **方法**: `POST`
- **路径**: `/measureinits/{day}`
- **函数名**: `add_measureinits_by_day`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| day | integer | 是 | 时间戳 |

### 2. 查询历史量测

- **方法**: `GET`
- **路径**: `/measures`
- **函数名**: `get_measures`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

### 3. 查询SOE，结果按照时间排序

- **方法**: `GET`
- **路径**: `/soes`
- **函数名**: `get_soes`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 | 测点id，多个id之间以,间隔 |
| start | integer | 否 | 开始时间, 13位时间戳 |
| end | integer | 否 | 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end |
| date | string | 否 | 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准 |
| source | integer | 否 | 数据源 |
| last_only | boolean | 否 | 是否查询只最新的数据 |
| with_init | boolean | 否 | 是否查询该天初始的数据 |
| reverse_order | boolean | 否 | 是否时间倒序查询 |

## Plans 模块

共 10 个接口

### 1. 查询所有计划

- **方法**: `GET`
- **路径**: `/plans/models`
- **函数名**: `get_plans_models`

### 2. 修改计划

- **方法**: `PUT`
- **路径**: `/plans/models`
- **函数名**: `update_plans_models`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 是 | 计划描述 |
| id | integer | 是 | 计划id |
| name | string | 是 | 计划名称 |
| plan | array[array[any]] | 是 | 计划内容数组，tuple格式为(开始时间:u64, 结束时间:u64, 功率值:f64) |

### 3. 新增计划

- **方法**: `POST`
- **路径**: `/plans/models`
- **函数名**: `add_plans_models`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 是 | 计划描述 |
| id | integer | 是 | 计划id |
| name | string | 是 | 计划名称 |
| plan | array[array[any]] | 是 | 计划内容数组，tuple格式为(开始时间:u64, 结束时间:u64, 功率值:f64) |

### 4. 查询指定id的计划列表

- **方法**: `GET`
- **路径**: `/plans/models/by_ids/{ids}`
- **函数名**: `get_plans_models_by_ids`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 计划id列表，以,间隔 |

### 5. 删除指定id的计划

- **方法**: `DELETE`
- **路径**: `/plans/models/{ids}`
- **函数名**: `delete_plans_models_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 计划id列表，以,间隔 |

### 6. 查询指定id的计划

- **方法**: `GET`
- **路径**: `/plans/models/{id}`
- **函数名**: `get_plans_models_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 计划id |

### 7. 查询所有计划路径

- **方法**: `GET`
- **路径**: `/plans/paths`
- **函数名**: `get_plans_paths`

### 8. 修改计划路径

- **方法**: `PUT`
- **路径**: `/plans/paths`
- **函数名**: `update_plans_paths`

**请求体**:

JSON对象

### 9. 新增计划路径

- **方法**: `POST`
- **路径**: `/plans/paths`
- **函数名**: `add_plans_paths`

**请求体**:

JSON对象

### 10. 删除指定的计划路径

- **方法**: `DELETE`
- **路径**: `/plans/paths`
- **函数名**: `delete_plans_paths`

**请求体**:

JSON对象

## Points 模块

共 14 个接口

### 1. 查询所有测点

- **方法**: `GET`
- **路径**: `/points/models`
- **函数名**: `get_points_models`

### 2. 保存测点

- **方法**: `POST`
- **路径**: `/points/models`
- **函数名**: `add_points_models`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].alarm_level1_expr | string | 是 | 告警级别1的表达式 |
| [].alarm_level2_expr | string | 是 | 告警级别2的表达式 |
| [].alias_id | string | 是 | 字符串id |
| [].change_expr | string | 是 | 判断是否"变化"的公式，用于变化上传或储存 |
| [].data_unit | string | 是 | 单位 |
| [].desc | string | 是 | Description |
| [].expression | string | 是 | 如果是计算点，这是表达式 |
| [].init_value | integer | 是 | 默认值存储在8个字节，需要根据is_discrete来转换成具体的值 |
| [].inv_trans_expr | string | 是 | 逆变换公式 |
| [].is_computing_point | boolean | 是 | 是否是计算点 |
| [].is_discrete | boolean | 是 | 是否是离散量 |
| [].is_realtime | boolean | 是 | 如是，则不判断是否"变化"，均上传 |
| [].is_soe | boolean | 是 | 是否是soe点 |
| [].lower_limit | number | 是 | 下限，用于坏数据辨识 |
| [].point_id | integer | 是 | 唯一的id |
| [].point_name | string | 是 | 测点名 |
| [].trans_expr | string | 是 | 变换公式 |
| [].upper_limit | number | 是 | 上限，用于坏数据辨识 |
| [].zero_expr | string | 是 | 判断是否为0值的公式 |

### 3. 删除指定id的测点（body形式）

- **方法**: `DELETE`
- **路径**: `/points/models`
- **函数名**: `delete_points_models`

**请求体**:

JSON对象

### 4. 获取根据版本号组装的测点应用对象

- **方法**: `GET`
- **路径**: `/points/models/for_apply`
- **函数名**: `get_points_models_for_apply`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | integer | 否 | 版本号，可选，若为空则默认0号版本 |

### 5. 删除指定id的测点

- **方法**: `DELETE`
- **路径**: `/points/models/{ids}`
- **函数名**: `delete_points_models_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 测点id列表，以,间隔 |

### 6. 保存测点（文件形式）

- **方法**: `POST`
- **路径**: `/points/models_file`
- **函数名**: `add_points_models_file`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileContent | array[integer] | 否 |  |
| fileName | string | 否 |  |
| is_zip | boolean | 否 |  |
| op | string | 否 |  |

### 7. 保存测点（多文件形式）

- **方法**: `POST`
- **路径**: `/points/models_file2`
- **函数名**: `add_points_models_file2`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | array[string] | 是 |  |

### 8. 查询控制器与测点的对应关系

- **方法**: `GET`
- **路径**: `/points/remote`
- **函数名**: `get_points_remote`

### 9. 更新控制器与测点的关系

- **方法**: `POST`
- **路径**: `/points/remote`
- **函数名**: `add_points_remote`

**请求体**:

JSON对象

### 10. 查询所有测点数据源

- **方法**: `GET`
- **路径**: `/points/source`
- **函数名**: `get_points_source`

### 11. 保存测点数据源

- **方法**: `POST`
- **路径**: `/points/source`
- **函数名**: `add_points_source`

**请求体**:

JSON对象

### 12. 查询所有的测点版本信息

- **方法**: `GET`
- **路径**: `/points/version`
- **函数名**: `get_points_version`

### 13. 新增测点版本

- **方法**: `POST`
- **路径**: `/points/version`
- **函数名**: `add_points_version`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| note | string | 是 | 提交时的注释 |
| tree_id | string | 是 | 对应的tree_id |
| version | integer | 是 | 版本号 |

### 14. 删除某一个测点版本

- **方法**: `DELETE`
- **路径**: `/points/version/{v}`
- **函数名**: `delete_points_version_by_v`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | integer | 是 | 版本id |

## Pscpu 模块

共 17 个接口

### 1. 更新当前应用的AOE

- **方法**: `POST`
- **路径**: `/pscpu/aoes`
- **函数名**: `add_pscpu_aoes`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aoes | array[AoeModel] | 是 | AOE列表 |
| aoes[] | object | 是 | AOE列表 |
| aoes[].actions | array[ActionEdge] | 是 | 动作列表 |
| aoes[].actions[] | object | 是 | 动作列表 |
| aoes[].actions[].action | string | 是 | 无动作 |
| aoes[].actions[].aoe_id | integer | 是 | AOE id |
| aoes[].actions[].failure_mode | string | 是 | 失败模式 |
| aoes[].actions[].name | string | 是 | 动作名称 |
| aoes[].actions[].source_node | integer | 是 | 源节点 |
| aoes[].actions[].target_node | integer | 是 | 目标节点 |
| aoes[].events | array[EventNode] | 是 | 节点列表 |
| aoes[].events[] | object | 是 | 节点列表 |
| aoes[].events[].aoe_id | integer | 是 | AOE id |
| aoes[].events[].expr | object | 是 | 表达式对象 |
| aoes[].events[].expr.rpn | array[Token] | 是 |  |
| aoes[].events[].expr.rpn[] | object | 是 |  |
| aoes[].events[].expr.rpn[].Binary | string | 是 | Mathematical operations. |
| aoes[].events[].id | integer | 是 | 节点id |
| aoes[].events[].name | string | 是 | 节点名 |
| aoes[].events[].node_type | string | 是 | 节点类型 |
| aoes[].events[].timeout | integer | 是 | 事件还未发生时等待超时时间 |
| aoes[].id | integer | 是 | aoe id |
| aoes[].name | string | 是 | aoe名称 |
| aoes[].trigger_type | object | 是 | 简单固定周期触发 |
| aoes[].trigger_type.SimpleRepeat | object | 是 | 时间对象 |
| aoes[].trigger_type.SimpleRepeat.nanos | integer | 是 | 剩余纳秒 |
| aoes[].trigger_type.SimpleRepeat.secs | integer | 是 | 秒 |
| aoes[].variables | array[array[any]] | 是 | 用户自定义的变量：变量名和表达式 |
| commit_msg | string | 是 | 版本描述 |
| version | integer | 是 | 版本号 |

### 2. 查询当前应用的AOE

- **方法**: `GET`
- **路径**: `/pscpu/aoes/models`
- **函数名**: `get_pscpu_aoes_models`

### 3. 查询当前应用的AOE版本号

- **方法**: `GET`
- **路径**: `/pscpu/aoes/version`
- **函数名**: `get_pscpu_aoes_version`

### 4. 查询配置信息

- **方法**: `GET`
- **路径**: `/pscpu/info`
- **函数名**: `get_pscpu_info`

### 5. 更新当前应用的电气岛

- **方法**: `POST`
- **路径**: `/pscpu/island`
- **函数名**: `add_pscpu_island`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commit_msg | string | 是 | 版本描述 |
| island | object | 是 | 电气岛，即集合 |
| island.cns | array[CN] | 是 | 连接节点列表 |
| island.cns[] | object | 是 | 连接节点列表 |
| island.cns[].id | integer | 是 | 连接节点id |
| island.cns[].psr_id | string | 是 | 资源id |
| island.cns[].terminals | array[integer] | 是 | 端子id数组 |
| island.measures | object | 是 | 测点，设备id->测点列表 |
| island.prop_groups | object | 是 | 属性分组，属性分组id->属性分组 |
| island.resources | object | 是 | 资源，设备id->资源对象 |
| prop_defs | array[PropDefine] | 是 | 属性定义数组 |
| prop_defs[] | object | 是 | 属性定义数组 |
| prop_defs[].data_type | string | 是 | 属性类型 |
| prop_defs[].data_unit | string | 是 | 数据单位 |
| prop_defs[].desc | string | 是 | 属性定义描述 |
| prop_defs[].id | integer | 是 | 属性定义id |
| prop_defs[].name | string | 是 | 属性定义标识 |
| rsr_defs | array[RsrDefine] | 是 | 设备定义数组 |
| rsr_defs[] | object | 是 | 设备定义数组 |
| rsr_defs[].desc | string | 是 | 设备定义的描述 |
| rsr_defs[].id | integer | 是 | 定义id |
| rsr_defs[].name | string | 是 | 设备类别名称 |
| rsr_defs[].prop_groups | array[PropGroupDefine] | 是 | 设备属性 |
| rsr_defs[].prop_groups[] | object | 是 | 设备属性 |
| rsr_defs[].prop_groups[].desc | string | 是 | 属性定义描述 |
| rsr_defs[].prop_groups[].name | string | 是 | 属性定义标识 |
| rsr_defs[].prop_groups[].prop_defines | array[integer] | 是 | 设备属性实际描述 |
| rsr_defs[].rsr_type | string | 是 | 电力设备类型 |
| rsr_defs[].terminal_num | integer | 是 | 端口数量 |
| version | integer | 是 | 版本号 |

### 6. 查询当前应用的电气岛

- **方法**: `GET`
- **路径**: `/pscpu/island/models`
- **函数名**: `get_pscpu_island_models`

### 7. 查询所有的测点路径（设备树）

- **方法**: `GET`
- **路径**: `/pscpu/island/paths`
- **函数名**: `get_pscpu_island_paths`

### 8. 查询测点树

- **方法**: `GET`
- **路径**: `/pscpu/island/point_tree`
- **函数名**: `get_pscpu_island_point_tree`

### 9. 查询当前应用的电气岛版本号

- **方法**: `GET`
- **路径**: `/pscpu/island/version`
- **函数名**: `get_pscpu_island_version`

### 10. 更新当前应用的测点

- **方法**: `POST`
- **路径**: `/pscpu/points`
- **函数名**: `add_pscpu_points`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| beeid_to_points | array[array[any]] | 是 | beeId和测点列表对应的数组，tuple格式为(beeId:String, 测点列表:u64[]) |
| commit_msg | string | 是 | 版本描述 |
| points | array[Measurement] | 是 | 测点列表 |
| points[] | object | 是 | 测点列表 |
| points[].alarm_level1_expr | string | 是 | 告警级别1的表达式 |
| points[].alarm_level2_expr | string | 是 | 告警级别2的表达式 |
| points[].alias_id | string | 是 | 字符串id |
| points[].change_expr | string | 是 | 判断是否"变化"的公式，用于变化上传或储存 |
| points[].data_unit | string | 是 | 单位 |
| points[].desc | string | 是 | Description |
| points[].expression | string | 是 | 如果是计算点，这是表达式 |
| points[].init_value | integer | 是 | 默认值存储在8个字节，需要根据is_discrete来转换成具体的值 |
| points[].inv_trans_expr | string | 是 | 逆变换公式 |
| points[].is_computing_point | boolean | 是 | 是否是计算点 |
| points[].is_discrete | boolean | 是 | 是否是离散量 |
| points[].is_realtime | boolean | 是 | 如是，则不判断是否"变化"，均上传 |
| points[].is_soe | boolean | 是 | 是否是soe点 |
| points[].lower_limit | number | 是 | 下限，用于坏数据辨识 |
| points[].point_id | integer | 是 | 唯一的id |
| points[].point_name | string | 是 | 测点名 |
| points[].trans_expr | string | 是 | 变换公式 |
| points[].upper_limit | number | 是 | 上限，用于坏数据辨识 |
| points[].zero_expr | string | 是 | 判断是否为0值的公式 |
| source_name | array[array[any]] | 是 |  |
| version | integer | 是 | 版本号 |

### 11. 查询设备关联的测点

- **方法**: `GET`
- **路径**: `/pscpu/points/by_dev/{dev_id}`
- **函数名**: `get_pscpu_points_by_dev`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dev_id | integer | 是 | 设备id |

### 12. 查询当前应用的测点

- **方法**: `GET`
- **路径**: `/pscpu/points/models`
- **函数名**: `get_pscpu_points_models`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 否 |  |
| name | string | 否 |  |
| is_soe | boolean | 否 |  |

### 13. 查询量测值

- **方法**: `GET`
- **路径**: `/pscpu/points/values/{src}`
- **函数名**: `get_pscpu_points_values_by_src`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | integer | 是 |  |

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 否 | 测点id（优先） |
| ids | string | 否 | 测点id列表，以,间隔 |

### 14. 查询当前应用的测点版本号

- **方法**: `GET`
- **路径**: `/pscpu/points/version`
- **函数名**: `get_pscpu_points_version`

### 15. 重置pscpu

- **方法**: `POST`
- **路径**: `/pscpu/reset`
- **函数名**: `add_pscpu_reset`

### 16. 启动pscpu

- **方法**: `POST`
- **路径**: `/pscpu/start`
- **函数名**: `add_pscpu_start`

**请求体**:

JSON对象

### 17. 停止pscpu

- **方法**: `POST`
- **路径**: `/pscpu/stop`
- **函数名**: `add_pscpu_stop`

## Scripts 模块

共 9 个接口

### 1. 查询7z脚本文件

- **方法**: `GET`
- **路径**: `/script_file/{script_id}`
- **函数名**: `get_script_file_by_script`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| script_id | integer | 是 | 脚本id |

### 2. 查询脚本md5

- **方法**: `GET`
- **路径**: `/script_md5`
- **函数名**: `get_script_md5`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 否 | 测点id（优先） |
| ids | string | 否 | 测点id列表，以,间隔 |

### 3. 查询所有脚本结果

- **方法**: `GET`
- **路径**: `/script_results`
- **函数名**: `get_script_results`

### 4. 新增脚本结果

- **方法**: `POST`
- **路径**: `/script_results`
- **函数名**: `add_script_results`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| make_time | integer | 是 |  |
| model_id | integer | 是 |  |
| script_id | integer | 是 |  |
| target | string | 是 |  |

### 5. 查询指定id脚本结果

- **方法**: `GET`
- **路径**: `/script_results/{id}`
- **函数名**: `get_script_results_by`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 脚本结果id |

### 6. 保存脚本对应的wasm和js文件

- **方法**: `POST`
- **路径**: `/script_wasm`
- **函数名**: `add_script_wasm`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| js_file | array[integer] | 是 | js文件内容 |
| module_name | string | 是 | 模块名称 |
| script_id | integer | 是 | 脚本id |
| wasm_file | array[integer] | 是 | wasm文件内容 |

### 7. 查询指定id脚本

- **方法**: `GET`
- **路径**: `/scripts`
- **函数名**: `get_scripts`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 否 | 测点id（优先） |
| ids | string | 否 | 测点id列表，以,间隔 |

### 8. 新增脚本

- **方法**: `POST`
- **路径**: `/scripts`
- **函数名**: `add_scripts`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 是 | 脚本描述 |
| id | integer | 是 | 脚本id |
| is_file_uploaded | boolean | 是 | 文件是否已上传 |
| is_js | boolean | 是 | 是否是javascript文件 |
| path | string | 是 | 脚本路径 |
| target | string | 是 | 脚本目标 |
| wasm_module_name | string | 是 | wasm模块名称 |
| wasm_update_time | integer | 是 | wasm上传时间 |

### 9. 删除指定id的脚本

- **方法**: `DELETE`
- **路径**: `/scripts/{ids}`
- **函数名**: `delete_scripts_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 脚本id列表，以,间隔 |

## System 模块

共 4 个接口

### 1. 执行map映射操作

- **方法**: `POST`
- **路径**: `/common_map`
- **函数名**: `add_common_map`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| Query | array[integer] | 是 | 查询 |

### 2. 查询Eig配置

- **方法**: `GET`
- **路径**: `/config`
- **函数名**: `get_config`

### 3. 保存Eig配置

- **方法**: `POST`
- **路径**: `/config`
- **函数名**: `add_config`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| properties | object | 是 | 主要配置属性 |
| properties2 | object | 是 | 次要配置属性 |

### 4. 查看ping结果

- **方法**: `GET`
- **路径**: `/ping`
- **函数名**: `get_ping`

## Tag_defines 模块

共 1 个接口

### 1. 查询指定分组的标签名称及id列表

- **方法**: `GET`
- **路径**: `/tag_defines/{group}`
- **函数名**: `get_tag_defines_by_group`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 分组id |
| group | integer | 是 |  |

## Tags 模块

共 2 个接口

### 1. 更新指定分组下标签名和测点数组关系

- **方法**: `PUT`
- **路径**: `/tags/{group}`
- **函数名**: `update_tags_by_group`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| group | integer | 是 | 分组id |

**请求体**:

JSON对象

### 2. 删除指定分组下标签id和测点的关系

- **方法**: `DELETE`
- **路径**: `/tags/{group}`
- **函数名**: `delete_tags_by_group`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| group | integer | 是 | 分组id |

**请求体**:

JSON对象

## Tags_cbor 模块

共 1 个接口

### 1. 查询指定分组下标签id对应的测点数组

- **方法**: `POST`
- **路径**: `/tags_cbor/{group}`
- **函数名**: `add_tags_cbor_by_group`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 分组id |
| group | integer | 是 |  |

**请求体**:

JSON对象

## Webplugins 模块

共 7 个接口

### 1. 保存插件对应的file

- **方法**: `POST`
- **路径**: `/webplugin_file`
- **函数名**: `add_webplugin_file`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| plugin_id | integer | 是 | 插件id |
| sevenz_file | array[integer] | 是 | 内容 |

### 2. 查询插件对应的压缩文件

- **方法**: `GET`
- **路径**: `/webplugin_file/{plugin_id}`
- **函数名**: `get_webplugin_file_by_plugin`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| plugin_id | integer | 是 | 插件id |

### 3. 查询插件md5

- **方法**: `GET`
- **路径**: `/webplugin_md5`
- **函数名**: `get_webplugin_md5`

**查询参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 否 | 测点id（优先） |
| ids | string | 否 | 测点id列表，以,间隔 |

### 4. 查询所有界面插件

- **方法**: `GET`
- **路径**: `/webplugins`
- **函数名**: `get_webplugins`

### 5. 新增插件

- **方法**: `POST`
- **路径**: `/webplugins`
- **函数名**: `add_webplugins`

**请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 插件id |
| is_file_uploaded | boolean | 是 | 文件是否已经上传 |
| is_monopoly | boolean | 是 | if is only one view |
| model_name | string | 是 | wasm或js或html文件的名称 |
| name | string | 是 | 在浏览模式下显示的名称 |
| path | string | 是 | 文件树中的路径 |

### 6. 删除指定id的插件

- **方法**: `DELETE`
- **路径**: `/webplugins/{ids}`
- **函数名**: `delete_webplugins_by_s`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ids | string | 是 | 插件id列表，以,间隔 |

### 7. 查询指定id插件

- **方法**: `GET`
- **路径**: `/webplugins/{plugin_id}`
- **函数名**: `get_webplugins_by_plugin`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| plugin_id | integer | 是 | 插件id |

## 枚举类型定义

共 24 个枚举类型

### 1. ActionExeResult

- **可选值**: NotRun, Success, Failed

### 2. AlarmLevel

- **可选值**: Common, Important, Emergency

### 3. AlarmStatus

- **可选值**: occur, disappear

### 4. AlarmType

- **可选值**: invalidPoints, invalidTransport, invalidAOE, alarmLevel1, alarmLevel2, badData, userDefine

### 5. DataType

- **描述**: 采集数据类型
- **可选值**: Binary, OneByteIntSigned, OneByteIntSignedLower, OneByteIntSignedUpper, OneByteIntUnsigned, OneByteIntUnsignedLower, OneByteIntUnsignedUpper, TwoByteIntUnsigned, TwoByteIntUnsignedSwapped, TwoByteIntSigned, TwoByteIntSignedSwapped, TwoByteBcd, FourByteIntUnsigned, FourByteIntSigned, FourByteIntUnsignedSwapped, FourByteIntSignedSwapped, FourByteIntUnsignedSwappedSwapped, FourByteIntSignedSwappedSwapped, FourByteFloat, FourByteFloatSwapped, FourByteFloatSwappedSwapped, FourByteBcd, FourByteBcdSwapped, FourByteMod10k, FourByteMod10kSwapped, SixByteMod10k, SixByteMod10kSwapped, EightByteIntUnsigned, EightByteIntSigned, EightByteIntUnsignedSwapped, EightByteIntSignedSwapped, EightByteIntUnsignedSwappedSwapped, EightByteIntSignedSwappedSwapped, EightByteFloat, EightByteFloatSwapped, EightByteFloatSwappedSwapped, EightByteMod10kSwapped, EightByteMod10k

### 6. DataUnit

- **描述**: 数据单位
- **可选值**: OnOrOff, A, V, kV, W, kW, MW, Var, kVar, MVar, VA, kVA, MVA, H, mH, Ah, mAh, kWh, Celsius, feet, km, meter, mm2, degree, rad, UnitOne, Percent, bit, B, kB, MB, GB, TB, PB, Unknown

### 7. DfSaveMode

- **可选值**: EveryTime, Once, Memory, Never

### 8. EventEvalResult

- **可选值**: Happen, NotHappen, Canceled, Error

### 9. FailureMode

- **描述**: 失败模式
- **可选值**: Default, Ignore, StopAll, StopFailed

### 10. FileOperation

- **可选值**: UPDATE, DELETE, RENAME

### 11. FileTreeOp

- **描述**: 文件树的操作类型
- **可选值**: Query, Add, Delete, Change, Apply, QueryApply

### 12. MbProtocolType

- **描述**: Modbus协议类型
- **可选值**: ENCAP, XA, RTU

### 13. MeasPhase

- **描述**: 量测相位
- **可选值**: Unknown, Total, A, B, C, A0, B0, C0, AB, BC, CA

### 14. NodeType

- **描述**: 节点类型
- **可选值**: ConditionNode, SwitchNode, SwitchOfActionResult

### 15. Operation

- **描述**: Mathematical operations.
- **可选值**: Plus, Minus, Times, Div, Rem, Pow, Fact, Equal, Unequal, LessThan, GreatThan, LtOrEqual, GtOrEqual, And, Or, Not, BitAnd, BitOr, BitXor, BitShl, BitShr, BitAt, BitNot, DotTimes, DotDiv, LeftDiv, DotPow, Transpose

### 16. PlotType

- **可选值**: Bar, BarPolar, Box, Candlestick, Contour, Carpet, Graph, Heatmap, Histogram, Histogram2d, Histogram2dContour, Indicator, IsoSurface, Mesh3d, Ohlc, Pie, Sankey, Scatter, Scatter3d, ScatterPolar, Sunburst, Surface, Table, Violin, EChart, Undefined

### 17. PropType

- **描述**: 属性类型
- **可选值**: U8, U16, U32, U64, I8, I16, I32, I64, F32, F64, Str, Complex32, Complex64, TensorF32, TensorF64, TensorC32, TensorC64, Unknown

### 18. PsRsrType

- **描述**: 电力设备类型
- **可选值**: Switch, Busbar, ACline, DCline, Winding, SyncGenerator, ESS, PCS, Transformer, Load, ShuntCompensator, SerialCompensator, ShuntReactor, ShuntCapacitor, SeriesReactor, SeriesCapacitor, Breaker, Disconnector, GroundDisconnector, SVC, SVG, Feeder, PWBusbar, Cable, Regulator, Connector, Measurement, Company, SubIsland, LoadArea, Substation, PowerPlant, VoltageLevel, BaseVoltage, HvdcSys, HvdcPoleSys, DCPole, DCLineDot, TLineDot, Converter, TLine, ACLineDot, TNode, Convergenceline, SeriesPowerTransformer, SeriesTransformerWinding, Acfilter, Synccondenser, DCBreaker, DCDisconnector, Signal, Combined, Composite, Section, SectionType, Bus, Branch, UserDefine1, UserDefine2, UserDefine3, UserDefine4, UserDefine5, UserDefine6, UserDefine7, UserDefine8, UserDefine9, UserDefine10, Unknown

### 19. RegisterType

- **描述**: 注册类型
- **可选值**: COILS, DISCRETE, INPUT, HOLDING

### 20. RequestType

- **可选值**: Get, Post, Put, Delete, Test

### 21. ScriptTarget

- **可选值**: Aoe, Dff

### 22. SerialParity

- **描述**: 奇偶校验位
- **可选值**: None, Odd, Even, Mark, Space

### 23. SetPointStatus

- **可选值**: YkCreated, YtCreated, YkSuccess, YtSuccess, YkFailTimeout, YtFailTimeout, YkFailTooBusy, YtFailTooBusy, YkFailProtocol, YtFailProtocol, YkFailBadData, YtFailBadData

### 24. TimeUnit

- **可选值**: Nanoseconds, Microseconds, Milliseconds

## 对象类型定义

共 114 个对象类型

### 1. ActionEdge

- **描述**: 边对象

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| action | EigAction | 动作定义 |
| aoe_id | integer | AOE id |
| failure_mode | FailureMode | action失败时的处理方式 |
| name | string | 动作名称 |
| source_node | integer | 源节点 |
| target_node | integer | 目标节点 |

### 2. AlarmConfig

- **描述**: 告警通知配置

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| common | AlarmNoticeSetting | 普通 |
| emergency | AlarmNoticeSetting | 紧急 |
| important | AlarmNoticeSetting | 严重 |

### 3. AlarmNoticeSetting

- **描述**: 告警通知形式

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| popup_window | boolean | 桌面弹窗 |
| sound_light | boolean | 声光 |
| text_messages | boolean | 短信 |

### 4. AoeControl

- **描述**: AOE指令集

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| AoeActions | array | AOE指令列表 |

### 5. AoeModel

- **描述**: aoe模型

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| actions | array | 动作列表 |
| events | array | 节点列表 |
| id | integer | aoe id |
| name | string | aoe名称 |
| trigger_type | TriggerType | 触发类型 |
| variables | array | 用户自定义的变量：变量名和表达式 |

### 6. Authority

- **描述**: 权限

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| desc | string | 权限描述 |
| id | integer | 权限ID |
| method | string | 请求方法 |
| name | string | 权限名称 |
| url | string | 权限可操作的url资源地址 |

### 7. BiViewModel


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| config | any |  |
| echart_js | ['string', 'null'] |  |
| exprs | string |  |
| flow_id | integer |  |
| id | integer |  |
| is_show | boolean |  |
| layout | any |  |
| name | string |  |
| plot_template | string |  |
| plot_type | PlotType |  |
| refresh_interval | ['integer', 'null'] |  |
| series_style | any |  |

### 8. CN

- **描述**: 连接节点

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| id | integer | 连接节点id |
| psr_id | string | 资源id |
| terminals | array | 端子id数组 |

### 9. CommitNote

- **描述**: 版本信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| note | string | 提交时的注释 |
| tree_id | string | 对应的tree_id |
| version | integer | 版本号 |

### 10. Complex32


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| im | number |  |
| re | number |  |

### 11. Complex64


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| im | number |  |
| re | number |  |

### 12. DayPlan

- **描述**: 计划对象

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| desc | string | 计划描述 |
| id | integer | 计划id |
| name | string | 计划名称 |
| plan | array | 计划内容数组，tuple格式为(开始时间:u64, 结束时间:u64, 功率值:f64) |

### 13. DfActionEdge


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| action | DfAction |  |
| desc | string |  |
| flow_id | integer |  |
| name | string |  |
| source_node | integer |  |
| target_node | integer |  |

### 14. DfNode


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| flow_id | integer |  |
| id | integer |  |
| name | string |  |
| node_type | DfNodeType |  |

### 15. DffBriefResult


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| end_time | integer |  |
| flow_id | integer |  |
| height | integer |  |
| length | integer |  |
| name | ['string', 'null'] |  |
| series_dtypes | array |  |
| series_names | array |  |
| start_time | integer |  |

### 16. DffModel


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| actions | array | 边 |
| aoe_var | ['array', 'null'] | destination of aoe variable |
| id | integer | dff id |
| is_on | boolean | should schedule |
| name | string | dff name |
| nodes | array | 节点 |
| save_mode | DfSaveMode | Data frame save mode |
| trigger_type | DfTriggerType | Dataframe flow 启动的方式 |

### 17. DffResult


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| end_time | integer |  |
| flow_id | integer |  |
| result | any |  |
| start_time | integer |  |

### 18. Dlt645ClientTp

- **描述**: Dlt645客户端通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| connections | array | 通道连接信息 |
| id | integer | 通道id |
| name | string | 通道名称 |
| para | Dlt645Para | 参数 |

### 19. Dlt645Connection

- **描述**: Dlt645通道连接信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| data_configure | array | register settings |
| data_id_to_rd | object | key:寄存器地址,value:setting中vec<RegisterData>的位置 |
| default_polling_period_in_milli | integer | 默认的轮询周期 |
| name | string | 连接名称 |
| point_id | integer | 通道状态对应的测点号 |
| point_id_to_rd | object | key is point id, value is position of register data |
| polling_period_to_data | object | 轮询周期不同的数据, key is period in milli, value is position. |
| slave_id | integer |  |
| timeout_in_milli | integer | 超时设置 |

### 20. Duration

- **描述**: 时间对象

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| nanos | integer | 剩余纳秒 |
| secs | integer | 秒 |

### 21. EcConnection

- **描述**: EtherCAT通道连接信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| cycle_time_in_micro | integer |  |
| data | array |  |
| dc_sync | boolean | is DC sync |
| index | integer |  |
| module_name | string |  |
| name | string |  |
| point_id | integer |  |
| point_to_pos | object |  |
| watchdog_multi | ['integer', 'null'] | defaukt to 2498 |
| watchdog_pdi | ['integer', 'null'] | 1/25M*(multi_watchdog+2)*pdi_watchdog |
| watchdog_sm | ['integer', 'null'] | 1/25M*(multi_watchdog+2)*sm_watchdog, defaukt to 1000 |

### 22. EcMasterTp

- **描述**: EtherCAT通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| connections | array | 连接信息 |
| eth | string |  |
| id | integer | 通道id |
| name | string | 通道名称 |

### 23. EigConfig

- **描述**: EIG 配置对象
用于存储和管理 EIG 相关的配置信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| properties | object | 主要配置属性 |
| properties2 | object | 次要配置属性 |

### 24. EventNode

- **描述**: 节点对象

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| aoe_id | integer | AOE id |
| expr | Expr | 事件是否发生判断的bool表达式 |
| id | integer | 节点id |
| name | string | 节点名 |
| node_type | NodeType | 节点类型 |
| timeout | integer | 事件还未发生时等待超时时间 |

### 25. Expr

- **描述**: 表达式对象

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| rpn | array |  |

### 26. FileTreeNote

- **描述**: 文件树的上传结构

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| op | FileTreeOp |  |
| op_paths | array |  |
| path | ['string', 'null'] |  |
| tree_id | string |  |
| version | ['integer', 'null'] |  |

### 27. HYDevice

- **描述**: 华云台区智能融合终端模型

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| dev_uuid | ['string', 'null'] |  |
| device_id | integer |  |
| device_info | HYDeviceInfo |  |
| need_register | boolean |  |
| points_pos | array |  |
| poll_period | integer |  |

### 28. HYDeviceInfo

- **描述**: 华云-台区智能融合终端模型

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| ProType | string | 协议类型 |
| addr | string | 地址 |
| desc | string | 描述 |
| deviceType | string | 设备型号 |
| isReport | string | 上报标志 0不需要上报，1需要上报 |
| manuID | string | 厂商ID 1234 名 |
| manuName | string | 厂商名称 |
| model | string | 模型名称 |
| nodeID | string | 节点ID |
| port | string | RS485-1、RS485-2、RS485-3、RS485-4、PLC、UMW |
| productID | string | 产品ID |

### 29. HYMqttTransport

- **描述**: 华云Mqtt通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| app_name | string | APP的名称，用于生成topic |
| data_configure | array | 测点列表 |
| device_configure | object | 设备key is 设备序号, value is (dev,设备的信息) |
| id | integer | 通道id |
| is_new | boolean | 版本，false是配电物联2020版本，true是2021版本，该参数会导致topic不同 |
| is_poll | boolean |  |
| model_to_pos | object | 模型列表key is model, value is 测点索引 |
| mqtt_broker | array | 服务端的ip和por |
| name | string | 通道名称 |
| point_id | integer | 通道状态对应的测点号 |
| point_id_to_pos | object | key is point id, value is information object address(data_configure的索引) |
| poll_time | integer | 轮询周期，单位毫秒 |
| read_topic | string | 读测点的主题 |
| user_name | ['string', 'null'] | 用户名，可选 |
| user_password | ['string', 'null'] | 用户密码，可选 |
| write_topic | string | 写测点的主题 |

### 30. HYPoint

- **描述**: 华云-台区智能融合终端测点

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| device_id | integer | 测点归属的设备序号 |
| not_realtime | boolean | 暂时无用 |
| point_id | integer | 对应的测点Id |
| point_info | HYPointInfo | 测点信息 |

### 31. HYPointInfo

- **描述**: 华云台区智能融合终端测点信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| deadzone | string |  |
| isReport | string |  |
| name | string |  |
| ratio | string |  |
| type | string |  |
| unit | string |  |
| userdefine | string | 名字不能改！！！ |

### 32. Iec104ClientTp

- **描述**: Iec104客户端通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| connection | Iec104Connection | 连接信息 |
| id | integer | 通道id |
| name | string | 通道名称 |
| tcp_server | array | 服务端的ip和port |
| yc_data_type | integer | 遥测点号的数据类型 |
| yx_data_type | integer | 遥信点号的数据类型 |

### 33. Iec104Connection

- **描述**: Iec104通道连接信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| call_counter_time | ['integer', 'null'] | 点度量总召时间间隔 |
| call_time | ['integer', 'null'] | 总召时间间隔 |
| common_address | integer | 公共地址 |
| common_address_field_length | integer | 公共地址字节个数 |
| cot_field_length | integer | 传输原因字节个数 |
| data_configure | array | register settings |
| direct_yk | boolean | 遥控遥调是否为直控，默认为false |
| direct_yt | boolean |  |
| extension_config | array | 扩展配置 |
| ioa_field_length | integer | 信息体地址字节个数 |
| ioa_to_pos | object | key:Point地址,value:data_configure中的位置 |
| is_client | boolean | 是否为客户端 |
| is_control_with_time | boolean | 控制方向是否带时标 |
| max_idle_time | integer | t3 |
| max_time_no_ack_received | integer | t1 |
| max_time_no_ack_sent | integer | t2 |
| max_unconfirmed_apdus_received | integer | w，接收方收到w个I格式报文后发送确认 |
| max_unconfirmed_apdus_sent | integer | k，发送方发送k条连续的未被确认的I格式报文，停止发送 |
| name | string | 连接名称 |
| originator_address | integer | 源发地址 |
| point_id | integer | 通道状态对应的测点号 |
| point_id_to_ioa | object | key is point id, value is information object address |

### 34. Iec104Point

- **描述**: Iec104测点信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| control_ioa | ['integer', 'null'] | 控制点地址，若进行配置控制点地址，则说明该点可写 |
| ioa | integer | 协议地址 |
| is_yx | boolean | 是否是遥信量 |
| point_id | integer | 对应的测点Id |

### 35. Iec104ServerTp

- **描述**: Iec104服务端通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| connections | array | 连接信息 |
| id | integer | 通道id |
| name | string | 通道名称 |
| tcp_server_port | integer | 服务的port |
| yc_data_type | integer | 遥测点号的数据类型 |
| yx_data_type | integer | 遥信点号的数据类型 |

### 36. ImageDfFilter


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| color_type | string |  |
| filter_type | string |  |
| height | integer |  |
| is_url | boolean |  |
| url_or_path | string |  |
| width | integer |  |

### 37. Island

- **描述**: 电气岛，即集合

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| cns | array | 连接节点列表 |
| measures | object | 测点，设备id->测点列表 |
| prop_groups | object | 属性分组，属性分组id->属性分组 |
| resources | object | 资源，设备id->资源对象 |

### 38. LccDevice

- **描述**: Lcc设备信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| desc | string | lcc描述 |
| ip | string | lcc ip |
| is_ems | boolean | 是否是ems |
| lcc_id | string | lcc id |
| name | string | lcc名称 |

### 39. MILP

- **描述**: 混合整数线性规划求解器

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| a | Mat | Ax >=/<= b |
| b | array |  |
| binary_int_float | array | 整数变量在x中的位置 |
| c | array | min/max c^T*x |
| constraint_type | array |  |
| min_or_max | boolean | min: true, max: false |
| parameters | object | 求解器参数：参数名、参数值 |
| x_lower | array | 变量的下界约束：变量位置、约束表达式 |
| x_name | array | 变量名称 |
| x_upper | array |  |

### 40. Mat

- **描述**: 由表达式组成的矩阵

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| m | integer | 行数 |
| n | integer | 列数 |
| v | array | 值 |

### 41. MbConnection

- **描述**: Modbus通道连接信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| coil_write_code | ['integer', 'null'] |  |
| default_polling_period_in_milli | integer |  |
| delay_between_requests | integer | 两条请求直接的间隔 |
| holding_write_code | ['integer', 'null'] |  |
| max_read_bit_count | integer |  |
| max_read_register_count | integer |  |
| max_write_bit_count | integer |  |
| max_write_register_count | integer |  |
| mb_data_configure | array | register settings |
| name | string |  |
| point_id | integer | 通道状态对应的测点号 |
| point_id_to_rd | object | key is point id, value is position of register data |
| polling_period_to_data | object | 轮询周期不同的数据, key is period in milli, value is position. |
| protocol_type | MbProtocolType | 协议类型 |
| register_addr_to_rd | object | key:寄存器地址,value:setting中vec<RegisterData>的位置 |
| slave_id | integer |  |
| timeout_in_milli | integer | 超时设置 |

### 42. MeasureDef

- **描述**: 测点定义

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| dev_id | integer |  |
| id | integer |  |
| phase | MeasPhase |  |
| point_id | integer |  |
| terminal_id | integer |  |

### 43. MeasureValue


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| analog_value | number | 模拟量值 |
| discrete_value | integer | 离散量值 |
| is_discrete | boolean | 是否离散量 |
| is_transformed | boolean | 是否已经变换 |
| point_id | integer | 对应的测点 |
| timestamp | integer | 时间戳 |
| transformed_analog | number | 变换后的模拟量值 |
| transformed_discrete | integer | 变换后的离散量值 |

### 44. Measurement

- **描述**: 测点对象

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| alarm_level1_expr | string | 告警级别1的表达式 |
| alarm_level2_expr | string | 告警级别2的表达式 |
| alias_id | string | 字符串id |
| change_expr | string | 判断是否"变化"的公式，用于变化上传或储存 |
| data_unit | string | 单位 |
| desc | string | Description |
| expression | string | 如果是计算点，这是表达式 |
| init_value | integer | 默认值存储在8个字节，需要根据is_discrete来转换成具体的值 |
| inv_trans_expr | string | 逆变换公式 |
| is_computing_point | boolean | 是否是计算点 |
| is_discrete | boolean | 是否是离散量 |
| is_realtime | boolean | 如是，则不判断是否"变化"，均上传 |
| is_soe | boolean | 是否是soe点 |
| lower_limit | number | 下限，用于坏数据辨识 |
| point_id | integer | 唯一的id |
| point_name | string | 测点名 |
| trans_expr | string | 变换公式 |
| upper_limit | number | 上限，用于坏数据辨识 |
| zero_expr | string | 判断是否为0值的公式 |

### 45. MemConnection

- **描述**: 内存通道连接信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| base_addr | integer |  |
| data | array |  |
| default_polling_period_in_milli | integer |  |
| lock_method | MemLock |  |
| mem_addr_to_pos | object | key:寄存器地址,value:setting中vec<MemData>的位置 |
| name | string |  |
| point_to_pos | object |  |
| polling_period_to_data | object | 轮询周期不同的数据, key is period in milli, value is position. |
| total_size | ['integer', 'null'] | 取决于计算机位数，如果溢出，应该报错。 |

### 46. MemData


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| data_type | DataType | 数据类型 |
| from | integer |  |
| is_writable | boolean |  |
| point_id | integer | 对应的测点Id |
| polling_period_in_milli | integer |  |

### 47. MemoryPosixTp

- **描述**: Posix内存通道

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| connections | array | 连接信息 |
| id | integer | 通道id |
| is_transfer | boolean |  |
| name | string | 通道名称 |
| path | ['string', 'null'] |  |

### 48. MemorySystemVTp

- **描述**: SystemV内存通道

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| connection | MemConnection |  |
| id | integer | 通道id |
| identifier | integer |  |
| is_transfer | boolean |  |
| name | string | 通道名称 |
| path | string |  |

### 49. MemsScript

- **描述**: 脚本

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| desc | string | 脚本描述 |
| id | integer | 脚本id |
| is_file_uploaded | boolean | 文件是否已上传 |
| is_js | boolean | 是否是javascript文件 |
| path | string | 脚本路径 |
| target | ScriptTarget | 脚本目标 |
| wasm_module_name | string | wasm模块名称 |
| wasm_update_time | integer | wasm上传时间 |

### 50. Menuitem

- **描述**: 菜单

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| group | string | 分组 |
| id | integer | 菜单ID |
| name | string | 名称 |
| url | string | 菜单对应的url地址 |

### 51. ModbusRtuClientTp

- **描述**: ModbusRtu客户端通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| connections | array | 通道连接信息 |
| id | integer | 通道id |
| name | string | 通道名称 |
| para | SerialPara | 串口参数 |

### 52. ModbusRtuServerTp

- **描述**: ModbusRtu服务端通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| connections | array | 通道连接信息 |
| id | integer | 通道id |
| name | string | 通道名称 |
| para | SerialPara | 串口参数 |

### 53. ModbusTcpClientTp

- **描述**: ModbusTcp客户端通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| connections | array | Modbus通道连接信息 |
| id | integer | 通道id |
| name | string | 通道名称 |
| tcp_server | array | 服务端的ip和port |

### 54. ModbusTcpServerTp

- **描述**: ModbusTcp服务端通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| connections | array | 通道连接信息 |
| id | integer | 通道id |
| name | string | 通道名称 |
| tcp_server_port | integer | 服务的port |

### 55. MqttTransport

- **描述**: Mqtt通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| array_filter | ['string', 'null'] | 总的提取器，有些情况测量数据作为一个数组放在json中 |
| filter_keys | ['array', 'null'] | json格式过滤器 |
| filter_values | ['array', 'null'] |  |
| id | integer | 通道id |
| is_json | boolean | 编码格式，默认是protobuf |
| is_transfer | boolean | 是否转发通道 |
| json_tags | ['object', 'null'] | json测点对应的数据标识, key是过滤器对应Array的json字符串，value是标识以及测点的索引 |
| json_write_tag | ['object', 'null'] | json写测点模板 |
| json_write_template | ['object', 'null'] | json写测点模板 |
| keep_alive | ['integer', 'null'] | 心跳时间 |
| mqtt_broker | array | 服务端的ip和por |
| name | string | 通道名称 |
| point_id | integer | 通道状态对应的测点号 |
| point_ids | array | 通过mqtt读写的测点 |
| read_topic | string | 读测点的主题 |
| user_name | ['string', 'null'] | 用户名，可选 |
| user_password | ['string', 'null'] | 用户密码，可选 |
| write_topic | string | 写测点的主题 |

### 56. NLP

- **描述**: 非整数线性规划求解器

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| g | array | 等式约束式 g(x) == b |
| g_lower | array | 不等式约束式 g(x) <= b |
| g_upper | array | 不等式约束式 g(x) >= b |
| min_or_max | boolean | min: true, max: false |
| obj_expr | Expr | 目标函数表达式 min obj |
| parameters | object | 求解器参数：参数名、参数值 |
| x_init | array | 变量初始值x0 |
| x_lower | array | 整数变量在x中的位置 |
| x_name | array | 变量名称 |
| x_upper | array |  |

### 57. NetworkRsr

- **描述**: 设备对象

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| container_id | ['integer', 'null'] |  |
| define_id | integer | 设备定义id |
| desc | string | 设备描述 |
| id | integer | 设备id |
| name | string | 设备名称 |
| prop_group_ids | array | 设备属性分组id列表 |
| terminals | array | 设备的端口 |

### 58. NewtonSolver

- **描述**: 非线性方程f(x)=b求解器

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| f | array |  |
| parameters | object |  |
| x_init | array |  |
| x_init_cx | array |  |
| x_name | array |  |

### 59. NodeInfo


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| node_id | NodeIdentifier |  |
| node_ns | integer |  |

### 60. OpcuaClientTp

- **描述**: Opcua客户端通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| certificate | ['array', 'null'] | certificate |
| id | integer | 通道id |
| is_writable | array |  |
| name | string | 通道名称 |
| node_ids | array | corresponding node ids in opc ua server |
| point_id | integer | 通道状态对应的测点号 |
| point_ids | array | 通过opcua读写的测点 |
| poll_period | array |  |
| private_key | ['array', 'null'] | private_key |
| server | array | 服务端的ip和port |
| sub_properties | object | subscribe properties |
| user_name | ['string', 'null'] | 用户名，可选 |
| user_password | ['string', 'null'] | 用户密码，可选 |

### 61. OpcuaServerTp

- **描述**: Opcua服务端通道信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| browse_name | array |  |
| certificate | ['array', 'null'] | certificate |
| id | integer | 通道id |
| is_writable | array |  |
| name | string | 通道名称 |
| node_ids | array |  |
| point_ids | array | register settings |
| private_key | ['array', 'null'] | private_key |
| server_port | integer | 服务端的ip和port |
| users | ['array', 'null'] | 用户 |

### 62. PbActionResult


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| end_time | ['integer', 'null'] |  |
| fail_code | ['integer', 'null'] |  |
| final_result | any |  |
| source_id | ['integer', 'null'] |  |
| start_time | ['integer', 'null'] |  |
| target_id | ['integer', 'null'] |  |
| var_values | array |  |
| variables | array |  |
| yk_points | array |  |
| yk_values | array |  |
| yt_points | array |  |
| yt_values | array |  |

### 63. PbAlarmDefine


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| desc | ['string', 'null'] |  |
| id | ['integer', 'null'] |  |
| level | any |  |
| name | ['string', 'null'] |  |
| owners | ['string', 'null'] |  |
| rule | ['string', 'null'] |  |

### 64. PbAlarmDefines


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| defines | array |  |

### 65. PbAnalogValue


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| change_init | ['boolean', 'null'] |  |
| measValue | ['number', 'null'] |  |
| origValue | ['number', 'null'] |  |
| pointId | ['integer', 'null'] |  |
| source | ['integer', 'null'] |  |
| timestamp | ['integer', 'null'] |  |

### 66. PbAoeResult


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| action_results | array |  |
| aoe_id | ['integer', 'null'] |  |
| end_time | ['integer', 'null'] |  |
| event_results | array |  |
| start_time | ['integer', 'null'] |  |

### 67. PbAoeResults


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| results | array |  |

### 68. PbDiscreteValue


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| change_init | ['boolean', 'null'] |  |
| measValue | ['integer', 'null'] |  |
| origValue | ['integer', 'null'] |  |
| pointId | ['integer', 'null'] |  |
| source | ['integer', 'null'] |  |
| timestamp | ['integer', 'null'] |  |

### 69. PbEigAlarm


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| alarm_type | any |  |
| content | ['string', 'null'] |  |
| define_id | ['integer', 'null'] |  |
| id | ['integer', 'null'] |  |
| status | any |  |
| timestamp | ['integer', 'null'] |  |

### 70. PbEigAlarms


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| alarms | array |  |

### 71. PbEigPingRes


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| desc | ['string', 'null'] |  |
| id | ['string', 'null'] |  |
| ip | ['string', 'null'] |  |
| is_ems | ['boolean', 'null'] |  |
| is_standby | ['boolean', 'null'] |  |
| name | ['string', 'null'] |  |

### 72. PbEventResult


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| end_time | ['integer', 'null'] |  |
| final_result | any |  |
| id | ['integer', 'null'] |  |
| start_time | ['integer', 'null'] |  |

### 73. PbFile


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| fileContent | ['array', 'null'] |  |
| fileName | ['string', 'null'] |  |
| is_zip | ['boolean', 'null'] |  |
| op | any |  |

### 74. PbPointValues

- **描述**: 测点值对象

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| aValues | array |  |
| dValues | array |  |

### 75. PbRequest


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| content | ['string', 'null'] |  |
| function | any |  |
| header_keys | array |  |
| header_values | array |  |
| id | ['integer', 'null'] |  |
| url | ['string', 'null'] |  |

### 76. PbResponse


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| content | ['string', 'null'] |  |
| is_ok | ['boolean', 'null'] |  |
| is_zip | ['boolean', 'null'] |  |
| request_id | ['integer', 'null'] |  |

### 77. PbSetPointResult


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| command | ['integer', 'null'] |  |
| create_time | ['integer', 'null'] |  |
| finish_time | ['integer', 'null'] |  |
| point_id | ['integer', 'null'] |  |
| sender_id | ['integer', 'null'] |  |
| status | any |  |

### 78. PbSetPointResults


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| results | array |  |

### 79. PdiData


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| data_type | DataType | 数据类型 |
| from | integer |  |
| is_writable | boolean | 是否可写 |
| point_id | integer | 对应的测点Id |

### 80. PlanTreeNode

- **描述**: 计划树节点

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| desc | ['string', 'null'] | 描述 |
| name | string | 名称 |
| path | string | 路径 |
| ref_id | ['integer', 'null'] |  |

### 81. PointControl


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| analogs | array |  |
| discretes | array |  |

### 82. PointControl2


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| analogs | array |  |
| discretes | array |  |

### 83. PointControl3


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| commands | array |  |

### 84. PointsToExp


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| expr | Expr | 表达式 |
| ids | array | id列表 |

### 85. PropDefine

- **描述**: 设备属性

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| data_type | PropType | 属性类型 |
| data_unit | DataUnit | 属性单位 |
| desc | string | 属性定义描述 |
| id | integer | 属性定义id |
| name | string | 属性定义标识 |

### 86. PropGroupDefine

- **描述**: 属性分组定义

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| desc | string | 属性定义描述 |
| name | string | 属性定义标识 |
| prop_defines | array | 设备属性实际描述 |

### 87. PscpuInfo


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| aoe_info | ['array', 'null'] |  |
| is_start | boolean |  |
| island_info | ['array', 'null'] |  |
| point_info | ['array', 'null'] |  |

### 88. RegisterData

- **描述**: Dlt645注册信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| data_id | integer | 数据标识 |
| point_ids | array | 对应的测点Id |
| polling_period_in_milli | integer | 轮询周期，毫秒 |

### 89. Role

- **描述**: 角色

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| id | integer | 角色ID |
| name | string | 角色名称 |
| role2authority | array | 角色权限关联表，一个角色可以拥有多个权限 |
| role2menu | array | 角色菜单关联表，一个角色可以拥有多个菜单 |

### 90. RsrDefine

- **描述**: 设备定义

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| desc | string | 设备定义的描述 |
| id | integer | 定义id |
| name | string | 设备类别名称 |
| prop_groups | array | 设备属性 |
| rsr_type | PsRsrType | 设备所属类型 |
| terminal_num | integer | 端口数量 |

### 91. RsrPropGroup

- **描述**: 设备属性分组

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| defines | array | 设备属性定义列表 |
| id | integer |  |
| name | string | 分组名称，用于显示，以及匹配PropGroupDefine |
| props | array | 设备属性实际描述 |
| rsr_id | integer | resource id |

### 92. ScriptResult

- **描述**: 脚本结果

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| make_time | integer |  |
| model_id | integer |  |
| script_id | integer |  |
| target | ScriptTarget |  |

### 93. ScriptWasmFile

- **描述**: 脚本Wasm文件

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| js_file | array | js文件内容 |
| module_name | string | 模块名称 |
| script_id | integer | 脚本id |
| wasm_file | array | wasm文件内容 |

### 94. SerialPara

- **描述**: 串口通道参数

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| baud_rate | integer |  |
| data_bits | integer |  |
| delay_between_requests | integer |  |
| file_path | string |  |
| parity | SerialParity |  |
| stop_bits | integer |  |

### 95. SetFloatValue

- **描述**: 浮点型指令数据

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| point_id | integer |  |
| sender_id | integer |  |
| timestamp | integer |  |
| yt_command | number |  |

### 96. SetFloatValue2

- **描述**: 浮点型指令数据

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| point_alias | string |  |
| sender_id | integer |  |
| timestamp | integer |  |
| yt_command | number |  |

### 97. SetIntValue

- **描述**: 整型指令数据

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| point_id | integer |  |
| sender_id | integer |  |
| timestamp | integer |  |
| yk_command | integer |  |

### 98. SetIntValue2

- **描述**: 整型指令数据

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| point_alias | string |  |
| sender_id | integer |  |
| timestamp | integer |  |
| yk_command | integer |  |

### 99. SetPointValue

- **描述**: 公式型指令数据

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| command | Expr |  |
| point_id | integer |  |
| sender_id | integer |  |
| timestamp | integer |  |

### 100. SetPoints

- **描述**: 设点

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| analog_id | array |  |
| analog_v | array |  |
| discrete_id | array |  |
| discrete_v | array |  |

### 101. SetPoints2

- **描述**: 设点2（包含张量）

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| analogs | array |  |
| discretes | array |  |

### 102. SparseMILP

- **描述**: 混合整数线性规划求解器，矩阵用稀疏矩阵

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| a | SparseMat | Ax >=/<= b |
| b | array |  |
| binary_int_float | array | 整数变量在x中的位置 |
| c | array | min/max c^T*x |
| constraint_type | array |  |
| min_or_max | boolean | min: true, max: false |
| parameters | object | 求解器参数：参数名、参数值 |
| x_lower | array | 变量的下界约束：变量位置、约束表达式 |
| x_name | array | 变量名称 |
| x_upper | array | 变量的上界约束：变量位置、约束表达式 |

### 103. SparseMat

- **描述**: 由表达式组成的稀疏矩阵

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| m | integer | 行数 |
| n | integer | 列数 |
| v | array |  |

### 104. SparseSolver

- **描述**: 稀疏线性方程组Ax=b求解器

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| a | SparseMat | A矩阵 |
| b | array | b向量 |
| parameters | object | 求解器参数：参数名、参数值 |
| x_init | array | 变量初始值 |
| x_name | array | 变量名称 |

### 105. SysAoes

- **描述**: 当前应用AOE信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| aoes | array | AOE列表 |
| commit_msg | string | 版本描述 |
| version | integer | 版本号 |

### 106. SysIsland

- **描述**: 当前应用的电气岛信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| commit_msg | string | 版本描述 |
| island | Island | 电气岛 |
| prop_defs | array | 属性定义数组 |
| rsr_defs | array | 设备定义数组 |
| version | integer | 版本号 |

### 107. SysPoints

- **描述**: 当前应用测点信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| beeid_to_points | array | beeId和测点列表对应的数组，tuple格式为(beeId:String, 测点列表:u64[]) |
| commit_msg | string | 版本描述 |
| points | array | 测点列表 |
| source_name | array |  |
| version | integer | 版本号 |

### 108. Terminal

- **描述**: 端口

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| device | integer | 设备id |
| id | integer | 端口id |

### 109. UploadForm


**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| file | array |  |

### 110. User

- **描述**: 用户 - 全部信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| password | array | 加密后的用户密码 |
| password_update_time | integer | 最近一次密码修改时间 |
| pub_info | UserPub | 可查询的用户公开信息 |

### 111. UserGroup

- **描述**: 用户组

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| id | integer | 用户组ID |
| name | string | 用户组名称 |
| user_group2role | array | 用户组角色关联表，一个用户组可以拥有多个角色 |

### 112. UserPub

- **描述**: 用户 - 公开信息

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| desc | ['string', 'null'] | 描述 |
| email | ['string', 'null'] | 用户的邮箱 |
| expiration_time | ['integer', 'null'] | 过期时间 |
| id | integer | 用户ID |
| name | string | 用户名称 |
| phone_number | ['string', 'null'] | 用户的手机号 |
| special_role | array | 特别分配的角色 |
| user_group | integer | 所属用户组的id（用户与用户组关联表，一个用户只能属于一个用户组） |

### 113. WebPlugin

- **描述**: Web插件

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| id | integer | 插件id |
| is_file_uploaded | boolean | 文件是否已经上传 |
| is_monopoly | boolean | if is only one view |
| model_name | string | wasm或js或html文件的名称 |
| name | string | 在浏览模式下显示的名称 |
| path | string | 文件树中的路径 |

### 114. WebPluginFile

- **描述**: 插件文件内容

**字段**:

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| plugin_id | integer | 插件id |
| sevenz_file | array | 内容 |

