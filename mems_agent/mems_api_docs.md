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

## ALARM 模块

### 查询告警通知配置信息

- **方法**: `GET`
- **路径**: `/alarm/config`
- **工具名**: `get_alarm_config`

### 配置告警通知

- **方法**: `POST`
- **路径**: `/alarm/config`
- **工具名**: `add_alarm_config`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| common | object | 是 | 普通 |
| common.popup_window | boolean | 是 | 桌面弹窗 |
| common.sound_light | boolean | 是 | 声光 |
| common.text_messages | boolean | 是 | 短信 |
| emergency | object | 是 | 紧急 |
| emergency.popup_window | boolean | 是 | 桌面弹窗 |
| emergency.sound_light | boolean | 是 | 声光 |
| emergency.text_messages | boolean | 是 | 短信 |
| important | object | 是 | 严重 |
| important.popup_window | boolean | 是 | 桌面弹窗 |
| important.sound_light | boolean | 是 | 声光 |
| important.text_messages | boolean | 是 | 短信 |


### 确认告警

- **方法**: `POST`
- **路径**: `/alarm/confirm/{user_id}`
- **工具名**: `add_alarm_confirm_by_user`
- **参数**:
  - `user_id` (path, integer, 必填): 用户id；元信息：format=int32
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | integer | 是 | 格式：int64 |


### 查询已确认的告警

- **方法**: `GET`
- **路径**: `/alarm/confirm_status`
- **工具名**: `get_alarm_confirm_status`

### 查询告警总数

- **方法**: `GET`
- **路径**: `/alarm/count`
- **工具名**: `get_alarm_count`

### 上传单个告警定义

- **方法**: `POST`
- **路径**: `/alarm/define`
- **工具名**: `add_alarm_define`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 否 | 允许空值 |
| id | integer | 否 | 格式：int32；允许空值 |
| level | oneOf[string] | 否 | 可选值：Common、Important、Emergency；可选结构：string |
| level.oneOf[1] | string | 是 | 可选值：Common、Important、Emergency |
| name | string | 否 | 允许空值 |
| owners | string | 否 | 允许空值 |
| rule | string | 否 | 允许空值 |


### 查询指定id的告警定义

- **方法**: `GET`
- **路径**: `/alarm/define/{id}`
- **工具名**: `get_alarm_define_by`
- **参数**:
  - `id` (path, integer, 必填): 告警定义id；元信息：format=int64

### 查询所有的告警定义

- **方法**: `GET`
- **路径**: `/alarm/defines`
- **工具名**: `get_alarm_defines`

### 上传告警定义

- **方法**: `POST`
- **路径**: `/alarm/defines`
- **工具名**: `add_alarm_defines`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defines | array[PbAlarmDefine] | 是 |  |
| defines[] | object | 是 |  |
| defines[].desc | string | 否 | 允许空值 |
| defines[].id | integer | 否 | 格式：int32；允许空值 |
| defines[].level | oneOf[string] | 否 | 可选值：Common、Important、Emergency；可选结构：string |
| defines[].level.oneOf[1] | string | 是 | 可选值：Common、Important、Emergency |
| defines[].name | string | 否 | 允许空值 |
| defines[].owners | string | 否 | 允许空值 |
| defines[].rule | string | 否 | 允许空值 |


### 删除指定id的告警定义

- **方法**: `DELETE`
- **路径**: `/alarm/defines/{ids}`
- **工具名**: `delete_alarm_defines_by_s`
- **参数**:
  - `ids` (path, string, 必填): 告警定义id列表，以,间隔

### 上传告警定义（文件形式）

- **方法**: `POST`
- **路径**: `/alarm/defines_file`
- **工具名**: `add_alarm_defines_file`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileContent | array[integer] | 否 | 允许空值 |
| fileContent[] | integer | 是 | 格式：int32 |
| fileName | string | 否 | 允许空值 |
| is_zip | boolean | 否 | 允许空值 |
| op | oneOf[string] | 否 | 可选值：UPDATE、DELETE、RENAME；可选结构：string |
| op.oneOf[1] | string | 是 | 可选值：UPDATE、DELETE、RENAME |


### 查询未确认的告警数

- **方法**: `GET`
- **路径**: `/alarm/unconfirmed_number`
- **工具名**: `get_alarm_unconfirmed_number`

### 查询告警，结果按照时间排序

- **方法**: `GET`
- **路径**: `/alarms`
- **工具名**: `get_alarms`
- **参数**:
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 查询未确认的告警列表

- **方法**: `GET`
- **路径**: `/alarms/unconfirmed`
- **工具名**: `get_alarms_unconfirmed`

***

## AOES 模块

### 查询AOE执行结果

- **方法**: `GET`
- **路径**: `/aoe_results`
- **工具名**: `get_aoe_results`
- **参数**:
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 查询所有AOE

- **方法**: `GET`
- **路径**: `/aoes/models`
- **工具名**: `get_aoes_models`

### 保存AOE

- **方法**: `POST`
- **路径**: `/aoes/models`
- **工具名**: `add_aoes_models`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | aoe模型 |
| [].actions | array[ActionEdge] | 是 | 动作列表 |
| [].actions[] | object | 是 | 边对象 |
| [].actions[].action | oneOf[string | object{SetPoints} | object{SetPointsWithCheck} | object{SetPoints2} | object{SetPointsWithCheck2} | object{Solve} | object{Nlsolve} | object{Milp} | object{SimpleMilp} | object{Nlp}] | 是 | 动作定义；可选值：None；可选结构：string | object{SetPoints} | object{SetPointsWithCheck} | object{SetPoints2} | object{SetPointsWithCheck2} | object{Solve} | object{Nlsolve} | object{Milp} | object{SimpleMilp} | object{Nlp} |
| [].actions[].action.oneOf[1] | string | 是 | 无动作；可选值：None |
| [].actions[].action.oneOf[2] | object | 是 | 设点动作 |
| [].actions[].action.oneOf[2].SetPoints | object | 是 | 设点动作 |
| [].actions[].action.oneOf[2].SetPoints.analog_id | array[string] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.analog_v | array[Expr] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.analog_v[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[2].SetPoints.discrete_id | array[string] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.discrete_v | array[Expr] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[3] | object | 是 | 设点动作 |
| [].actions[].action.oneOf[3].SetPointsWithCheck | object | 是 | 设点动作 |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_id | array[string] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v | array[Expr] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_id | array[string] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v | array[Expr] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[4] | object | 是 | 设点动作 |
| [].actions[].action.oneOf[4].SetPoints2 | object | 是 | 设点动作 |
| [].actions[].action.oneOf[4].SetPoints2.analogs | array[PointsToExp] | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.analogs[] | object | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr | object | 是 | 表达式 |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].ids | array[string] | 是 | id列表 |
| [].actions[].action.oneOf[4].SetPoints2.discretes | array[PointsToExp] | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.discretes[] | object | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr | object | 是 | 表达式 |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].ids | array[string] | 是 | id列表 |
| [].actions[].action.oneOf[5] | object | 是 | 设点动作 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2 | object | 是 | 设点动作 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs | array[PointsToExp] | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[] | object | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr | object | 是 | 表达式 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].ids | array[string] | 是 | id列表 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes | array[PointsToExp] | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[] | object | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr | object | 是 | 表达式 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].ids | array[string] | 是 | id列表 |
| [].actions[].action.oneOf[6] | object | 是 | 求方程 |
| [].actions[].action.oneOf[6].Solve | object | 是 | 求方程 |
| [].actions[].action.oneOf[6].Solve.a | object | 是 | A矩阵 |
| [].actions[].action.oneOf[6].Solve.a.m | integer | 是 | 行数 |
| [].actions[].action.oneOf[6].Solve.a.n | integer | 是 | 列数 |
| [].actions[].action.oneOf[6].Solve.a.v | array[array[any]] | 是 |  |
| [].actions[].action.oneOf[6].Solve.b | array[Expr] | 是 | b向量 |
| [].actions[].action.oneOf[6].Solve.b[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[6].Solve.b[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[6].Solve.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[6].Solve.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| [].actions[].action.oneOf[6].Solve.x_init | array[Expr] | 是 | 变量初始值 |
| [].actions[].action.oneOf[6].Solve.x_init[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[6].Solve.x_name | array[string] | 是 | 变量名称 |
| [].actions[].action.oneOf[7] | object | 是 | 求非线性方程组 |
| [].actions[].action.oneOf[7].Nlsolve | object | 是 | 求非线性方程组 |
| [].actions[].action.oneOf[7].Nlsolve.f | array[Expr] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.f[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.parameters | object[string, string] | 是 | 额外属性：string |
| [].actions[].action.oneOf[7].Nlsolve.x_init | array[Expr] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx | array[Expr] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.x_name | array[string] | 是 |  |
| [].actions[].action.oneOf[8] | object | 是 | 混合整数线性规划稀疏表示 |
| [].actions[].action.oneOf[8].Milp | object | 是 | 混合整数线性规划稀疏表示 |
| [].actions[].action.oneOf[8].Milp.a | object | 是 | Ax >=/<= b |
| [].actions[].action.oneOf[8].Milp.a.m | integer | 是 | 行数 |
| [].actions[].action.oneOf[8].Milp.a.n | integer | 是 | 列数 |
| [].actions[].action.oneOf[8].Milp.a.v | array[array[any]] | 是 |  |
| [].actions[].action.oneOf[8].Milp.b | array[Expr] | 是 |  |
| [].actions[].action.oneOf[8].Milp.b[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[8].Milp.b[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[8].Milp.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[8].Milp.binary_int_float | array[integer] | 是 | 整数变量在x中的位置 |
| [].actions[].action.oneOf[8].Milp.binary_int_float[] | integer | 是 | 整数变量在x中的位置；格式：int32 |
| [].actions[].action.oneOf[8].Milp.c | array[array[any]] | 是 | min/max c^T*x |
| [].actions[].action.oneOf[8].Milp.constraint_type | array[Operation] | 是 |  |
| [].actions[].action.oneOf[8].Milp.constraint_type[] | string | 是 | Mathematical operations.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[8].Milp.min_or_max | boolean | 是 | min: true, max: false |
| [].actions[].action.oneOf[8].Milp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| [].actions[].action.oneOf[8].Milp.x_lower | array[array[any]] | 是 | 变量的下界约束：变量位置、约束表达式 |
| [].actions[].action.oneOf[8].Milp.x_name | array[string] | 是 | 变量名称 |
| [].actions[].action.oneOf[8].Milp.x_upper | array[array[any]] | 是 | 变量的上界约束：变量位置、约束表达式 |
| [].actions[].action.oneOf[9] | object | 是 | 混合整数线性规划稠密表示 |
| [].actions[].action.oneOf[9].SimpleMilp | object | 是 | 混合整数线性规划稠密表示 |
| [].actions[].action.oneOf[9].SimpleMilp.a | object | 是 | Ax >=/<= b |
| [].actions[].action.oneOf[9].SimpleMilp.a.m | integer | 是 | 行数 |
| [].actions[].action.oneOf[9].SimpleMilp.a.n | integer | 是 | 列数 |
| [].actions[].action.oneOf[9].SimpleMilp.a.v | array[Expr] | 是 | 值 |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.b | array[Expr] | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.b[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.binary_int_float | array[integer] | 是 | 整数变量在x中的位置 |
| [].actions[].action.oneOf[9].SimpleMilp.binary_int_float[] | integer | 是 | 整数变量在x中的位置；格式：int32 |
| [].actions[].action.oneOf[9].SimpleMilp.c | array[Expr] | 是 | min/max c^T*x |
| [].actions[].action.oneOf[9].SimpleMilp.c[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.constraint_type | array[Operation] | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.constraint_type[] | string | 是 | Mathematical operations.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.min_or_max | boolean | 是 | min: true, max: false |
| [].actions[].action.oneOf[9].SimpleMilp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| [].actions[].action.oneOf[9].SimpleMilp.x_lower | array[array[any]] | 是 | 变量的下界约束：变量位置、约束表达式 |
| [].actions[].action.oneOf[9].SimpleMilp.x_name | array[string] | 是 | 变量名称 |
| [].actions[].action.oneOf[9].SimpleMilp.x_upper | array[array[any]] | 是 |  |
| [].actions[].action.oneOf[10] | object | 是 | 非整数线性规划 |
| [].actions[].action.oneOf[10].Nlp | object | 是 | 非整数线性规划 |
| [].actions[].action.oneOf[10].Nlp.g | array[Expr] | 是 | 等式约束式 g(x) == b |
| [].actions[].action.oneOf[10].Nlp.g[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.g[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.g_lower | array[Expr] | 是 | 不等式约束式 g(x) <= b |
| [].actions[].action.oneOf[10].Nlp.g_lower[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.g_upper | array[Expr] | 是 | 不等式约束式 g(x) >= b |
| [].actions[].action.oneOf[10].Nlp.g_upper[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.min_or_max | boolean | 是 | min: true, max: false |
| [].actions[].action.oneOf[10].Nlp.obj_expr | object | 是 | 目标函数表达式 min obj |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| [].actions[].action.oneOf[10].Nlp.x_init | array[Expr] | 是 | 变量初始值x0 |
| [].actions[].action.oneOf[10].Nlp.x_init[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.x_lower | array[Expr] | 是 | 整数变量在x中的位置 |
| [].actions[].action.oneOf[10].Nlp.x_lower[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.x_name | array[string] | 是 | 变量名称 |
| [].actions[].action.oneOf[10].Nlp.x_upper | array[Expr] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_upper[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].aoe_id | integer | 是 | AOE id；格式：int64 |
| [].actions[].failure_mode | string | 是 | action失败时的处理方式；可选值：Default、Ignore、StopAll、StopFailed |
| [].actions[].name | string | 是 | 动作名称 |
| [].actions[].source_node | integer | 是 | 源节点；格式：int64 |
| [].actions[].target_node | integer | 是 | 目标节点；格式：int64 |
| [].events | array[EventNode] | 是 | 节点列表 |
| [].events[] | object | 是 | 节点对象 |
| [].events[].aoe_id | integer | 是 | AOE id；格式：int64 |
| [].events[].expr | object | 是 | 事件是否发生判断的bool表达式 |
| [].events[].expr.rpn | array[Token] | 是 |  |
| [].events[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].events[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].events[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].events[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].events[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].events[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].events[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].events[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].events[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].events[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].events[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].events[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].events[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].events[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].events[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].events[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].events[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].events[].expr.rpn[].oneOf[12] | object | 是 |  |
| [].events[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].events[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].events[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].events[].id | integer | 是 | 节点id；格式：int64 |
| [].events[].name | string | 是 | 节点名 |
| [].events[].node_type | string | 是 | 节点类型；可选值：ConditionNode、SwitchNode、SwitchOfActionResult |
| [].events[].timeout | integer | 是 | 事件还未发生时等待超时时间；格式：int64 |
| [].id | integer | 是 | aoe id；格式：int64 |
| [].name | string | 是 | aoe名称 |
| [].trigger_type | oneOf[object{SimpleRepeat} | object{TimeDrive} | string | object{EventRepeatMix} | object{EventTimeMix}] | 是 | 触发类型；可选值：EventDrive；可选结构：object{SimpleRepeat} | object{TimeDrive} | string | object{EventRepeatMix} | object{EventTimeMix} |
| [].trigger_type.oneOf[1] | object | 是 | 简单固定周期触发 |
| [].trigger_type.oneOf[1].SimpleRepeat | object | 是 | 简单固定周期触发 |
| [].trigger_type.oneOf[1].SimpleRepeat.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| [].trigger_type.oneOf[1].SimpleRepeat.secs | integer | 是 | 秒；格式：int64 |
| [].trigger_type.oneOf[2] | object | 是 | cron表达式 |
| [].trigger_type.oneOf[2].TimeDrive | string | 是 | cron表达式 |
| [].trigger_type.oneOf[3] | string | 是 | 事件驱动，AOE开始节点条件满足即触发；可选值：EventDrive |
| [].trigger_type.oneOf[4] | object | 是 | 事件驱动 && 简单固定周期 联合 |
| [].trigger_type.oneOf[4].EventRepeatMix | object | 是 | 事件驱动 && 简单固定周期 联合 |
| [].trigger_type.oneOf[4].EventRepeatMix.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| [].trigger_type.oneOf[4].EventRepeatMix.secs | integer | 是 | 秒；格式：int64 |
| [].trigger_type.oneOf[5] | object | 是 | 事件驱动 && cron表达式 联合 |
| [].trigger_type.oneOf[5].EventTimeMix | string | 是 | 事件驱动 && cron表达式 联合 |
| [].variables | array[array[any]] | 是 | 用户自定义的变量：变量名和表达式 |


### 查询指定版本的AOE

- **方法**: `GET`
- **路径**: `/aoes/models/by_version/{v}`
- **工具名**: `get_aoes_models_by_version_by_v`
- **参数**:
  - `v` (path, integer, 必填): 版本id；元信息：format=int32

### 查询根据版本号组装的AOE应用对象

- **方法**: `GET`
- **路径**: `/aoes/models/for_apply`
- **工具名**: `get_aoes_models_for_apply`
- **参数**:
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 删除指定id的AOE

- **方法**: `DELETE`
- **路径**: `/aoes/models/{ids}`
- **工具名**: `delete_aoes_models_by_s`
- **参数**:
  - `ids` (path, string, 必填): AOE_id列表，以,间隔

### 根据id查询指定的AOE

- **方法**: `GET`
- **路径**: `/aoes/models/{id}`
- **工具名**: `get_aoes_models_by`
- **参数**:
  - `id` (path, integer, 必填): AOE_id；元信息：format=int64
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 保存AOE（文件形式）

- **方法**: `POST`
- **路径**: `/aoes/models_file`
- **工具名**: `add_aoes_models_file`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileContent | array[integer] | 否 | 允许空值 |
| fileContent[] | integer | 是 | 格式：int32 |
| fileName | string | 否 | 允许空值 |
| is_zip | boolean | 否 | 允许空值 |
| op | oneOf[string] | 否 | 可选值：UPDATE、DELETE、RENAME；可选结构：string |
| op.oneOf[1] | string | 是 | 可选值：UPDATE、DELETE、RENAME |


### 保存AOE（多文件形式）

- **方法**: `POST`
- **路径**: `/aoes/models_file2`
- **工具名**: `add_aoes_models_file2`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | array[string] | 是 |  |
| file[] | string | 是 | 格式：binary |


### 查询所有的AOE版本信息

- **方法**: `GET`
- **路径**: `/aoes/version`
- **工具名**: `get_aoes_version`

### 新增AOE版本

- **方法**: `POST`
- **路径**: `/aoes/version`
- **工具名**: `add_aoes_version`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| note | string | 是 | 提交时的注释 |
| tree_id | string | 是 | 对应的tree_id |
| version | integer | 是 | 版本号；格式：int32 |


### 删除某一个AOE版本

- **方法**: `DELETE`
- **路径**: `/aoes/version/{v}`
- **工具名**: `delete_aoes_version_by_v`
- **参数**:
  - `v` (path, integer, 必填): 版本id；元信息：format=int32

### 查询当前运行中的AOE

- **方法**: `GET`
- **路径**: `/running_aoes`
- **工具名**: `get_running_aoes`

### 查询未运行的AOE

- **方法**: `GET`
- **路径**: `/unrun_aoes`
- **工具名**: `get_unrun_aoes`

***

## AUTH 模块

### 查询所有权限

- **方法**: `GET`
- **路径**: `/auth/auths`
- **工具名**: `get_auth_auths`

### 新增权限

- **方法**: `POST`
- **路径**: `/auth/auths`
- **工具名**: `add_auth_auths`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 权限 |
| [].desc | string | 是 | 权限描述 |
| [].id | integer | 是 | 权限ID；格式：int32 |
| [].method | string | 是 | 请求方法 |
| [].name | string | 是 | 权限名称 |
| [].url | string | 是 | 权限可操作的url资源地址 |


### 查询指定角色的所有权限

- **方法**: `GET`
- **路径**: `/auth/auths/by_role/{id}`
- **工具名**: `get_auth_auths_by_role`
- **参数**:
  - `id` (path, integer, 必填): 角色id；元信息：format=int32

### 删除指定id的删除权限

- **方法**: `DELETE`
- **路径**: `/auth/auths/{ids}`
- **工具名**: `delete_auth_auths_by_s`
- **参数**:
  - `ids` (path, string, 必填): 权限id列表，以,间隔

### 执行登录

- **方法**: `POST`
- **路径**: `/auth/login`
- **工具名**: `add_auth_login`
- **请求体**:

  - 无法解析请求体结构


### 查询所有菜单

- **方法**: `GET`
- **路径**: `/auth/menus`
- **工具名**: `get_auth_menus`

### 新增菜单

- **方法**: `POST`
- **路径**: `/auth/menus`
- **工具名**: `add_auth_menus`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 菜单 |
| [].group | string | 是 | 分组 |
| [].id | integer | 是 | 菜单ID；格式：int32 |
| [].name | string | 是 | 名称 |
| [].url | string | 是 | 菜单对应的url地址 |


### 查询指定角色的所有菜单

- **方法**: `GET`
- **路径**: `/auth/menus/by_role/{id}`
- **工具名**: `get_auth_menus_by_role`
- **参数**:
  - `id` (path, integer, 必填): 角色id；元信息：format=int32

### 查询指定用户的所有菜单

- **方法**: `GET`
- **路径**: `/auth/menus/by_user/{id}`
- **工具名**: `get_auth_menus_by_user`
- **参数**:
  - `id` (path, integer, 必填): 用户id；元信息：format=int32

### 删除指定id的菜单

- **方法**: `DELETE`
- **路径**: `/auth/menus/{ids}`
- **工具名**: `delete_auth_menus_by_s`
- **参数**:
  - `ids` (path, string, 必填): 菜单id列表，以,间隔

### 用户注册

- **方法**: `POST`
- **路径**: `/auth/register`
- **工具名**: `add_auth_register`
- **请求体**:

  - 无法解析请求体结构


### 查询所有角色

- **方法**: `GET`
- **路径**: `/auth/roles`
- **工具名**: `get_auth_roles`

### 新增角色

- **方法**: `POST`
- **路径**: `/auth/roles`
- **工具名**: `add_auth_roles`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 角色 |
| [].id | integer | 是 | 角色ID；格式：int32 |
| [].name | string | 是 | 角色名称 |
| [].role2authority | array[integer] | 是 | 角色权限关联表，一个角色可以拥有多个权限 |
| [].role2authority[] | integer | 是 | 角色权限关联表，一个角色可以拥有多个权限；格式：int32 |
| [].role2menu | array[integer] | 是 | 角色菜单关联表，一个角色可以拥有多个菜单 |
| [].role2menu[] | integer | 是 | 角色菜单关联表，一个角色可以拥有多个菜单；格式：int32 |


### 修改角色

- **方法**: `PUT`
- **路径**: `/auth/roles`
- **工具名**: `update_auth_roles`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 角色ID；格式：int32 |
| name | string | 是 | 角色名称 |
| role2authority | array[integer] | 是 | 角色权限关联表，一个角色可以拥有多个权限 |
| role2authority[] | integer | 是 | 角色权限关联表，一个角色可以拥有多个权限；格式：int32 |
| role2menu | array[integer] | 是 | 角色菜单关联表，一个角色可以拥有多个菜单 |
| role2menu[] | integer | 是 | 角色菜单关联表，一个角色可以拥有多个菜单；格式：int32 |


### 根据ids查询角色

- **方法**: `GET`
- **路径**: `/auth/roles/{ids}`
- **工具名**: `get_auth_roles_by_s`
- **参数**:
  - `ids` (path, string, 必填): 角色id列表，以,间隔

### 删除指定id的删除角色

- **方法**: `DELETE`
- **路径**: `/auth/roles/{ids}`
- **工具名**: `delete_auth_roles_by_s`
- **参数**:
  - `ids` (path, string, 必填): 角色id列表，以,间隔

### 查询所有用户组

- **方法**: `GET`
- **路径**: `/auth/user_groups`
- **工具名**: `get_auth_user_groups`

### 新增用户组

- **方法**: `POST`
- **路径**: `/auth/user_groups`
- **工具名**: `add_auth_user_groups`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 用户组 |
| [].id | integer | 是 | 用户组ID；格式：int32 |
| [].name | string | 是 | 用户组名称 |
| [].user_group2role | array[integer] | 是 | 用户组角色关联表，一个用户组可以拥有多个角色 |
| [].user_group2role[] | integer | 是 | 用户组角色关联表，一个用户组可以拥有多个角色；格式：int32 |


### 修改用户组

- **方法**: `PUT`
- **路径**: `/auth/user_groups`
- **工具名**: `update_auth_user_groups`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 用户组ID；格式：int32 |
| name | string | 是 | 用户组名称 |
| user_group2role | array[integer] | 是 | 用户组角色关联表，一个用户组可以拥有多个角色 |
| user_group2role[] | integer | 是 | 用户组角色关联表，一个用户组可以拥有多个角色；格式：int32 |


### 删除指定id的用户组

- **方法**: `DELETE`
- **路径**: `/auth/user_groups/{ids}`
- **工具名**: `delete_auth_user_groups_by_s`
- **参数**:
  - `ids` (path, string, 必填): 用户组id列表，以,间隔

### 查询指定id用户组

- **方法**: `GET`
- **路径**: `/auth/user_groups/{id}`
- **工具名**: `get_auth_user_groups_by`
- **参数**:
  - `id` (path, integer, 必填): 用户组id；元信息：format=int32

### 查询所有用户

- **方法**: `GET`
- **路径**: `/auth/users`
- **工具名**: `get_auth_users`

### 新增用户

- **方法**: `POST`
- **路径**: `/auth/users`
- **工具名**: `add_auth_users`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| password | array[integer] | 是 | 加密后的用户密码 |
| password[] | integer | 是 | 加密后的用户密码；格式：int32 |
| password_update_time | integer | 是 | 最近一次密码修改时间；格式：int64 |
| pub_info | object | 是 | 可查询的用户公开信息 |
| pub_info.desc | string | 否 | 描述；允许空值 |
| pub_info.email | string | 否 | 用户的邮箱；允许空值 |
| pub_info.expiration_time | integer | 否 | 过期时间；格式：int64；允许空值 |
| pub_info.id | integer | 是 | 用户ID；格式：int32 |
| pub_info.name | string | 是 | 用户名称 |
| pub_info.phone_number | string | 否 | 用户的手机号；允许空值 |
| pub_info.special_role | array[integer] | 是 | 特别分配的角色 |
| pub_info.special_role[] | integer | 是 | 特别分配的角色；格式：int32 |
| pub_info.user_group | integer | 是 | 所属用户组的id（用户与用户组关联表，一个用户只能属于一个用户组）；格式：int32 |


### 修改用户

- **方法**: `PUT`
- **路径**: `/auth/users`
- **工具名**: `update_auth_users`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| password | array[integer] | 是 | 加密后的用户密码 |
| password[] | integer | 是 | 加密后的用户密码；格式：int32 |
| password_update_time | integer | 是 | 最近一次密码修改时间；格式：int64 |
| pub_info | object | 是 | 可查询的用户公开信息 |
| pub_info.desc | string | 否 | 描述；允许空值 |
| pub_info.email | string | 否 | 用户的邮箱；允许空值 |
| pub_info.expiration_time | integer | 否 | 过期时间；格式：int64；允许空值 |
| pub_info.id | integer | 是 | 用户ID；格式：int32 |
| pub_info.name | string | 是 | 用户名称 |
| pub_info.phone_number | string | 否 | 用户的手机号；允许空值 |
| pub_info.special_role | array[integer] | 是 | 特别分配的角色 |
| pub_info.special_role[] | integer | 是 | 特别分配的角色；格式：int32 |
| pub_info.user_group | integer | 是 | 所属用户组的id（用户与用户组关联表，一个用户只能属于一个用户组）；格式：int32 |


### 根据分组id查询用户信息

- **方法**: `GET`
- **路径**: `/auth/users/by_user_group/{id}`
- **工具名**: `get_auth_users_by_user_group`
- **参数**:
  - `id` (path, integer, 必填): 分组id；元信息：format=int32

### 更改用户密码

- **方法**: `PUT`
- **路径**: `/auth/users/password/{id}`
- **工具名**: `update_auth_users_password_by`
- **参数**:
  - `id` (path, integer, 必填): 用户id；元信息：format=int32
- **请求体**:

  - 无法解析请求体结构


### 重置用户密码

- **方法**: `PUT`
- **路径**: `/auth/users/reset_password/{id}`
- **工具名**: `update_auth_users_reset_password_by`
- **参数**:
  - `id` (path, integer, 必填): 用户id；元信息：format=int32

### 绑定已有用户的角色信息

- **方法**: `PUT`
- **路径**: `/auth/users/roles/{id}`
- **工具名**: `update_auth_users_roles_by`
- **参数**:
  - `id` (path, integer, 必填): 用户id；元信息：format=int32
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | integer | 是 | 格式：int32 |


### 删除指定id的用户

- **方法**: `DELETE`
- **路径**: `/auth/users/{ids}`
- **工具名**: `delete_auth_users_by_s`
- **参数**:
  - `ids` (path, string, 必填): 用户id列表，以,间隔

### 查询指定id用户

- **方法**: `GET`
- **路径**: `/auth/users/{id}`
- **工具名**: `get_auth_users_by`
- **参数**:
  - `id` (path, integer, 必填): 用户id；元信息：format=int32

***

## CONTROLS 模块

### 查询历史设点执行结果

- **方法**: `GET`
- **路径**: `/commands`
- **工具名**: `get_commands`
- **参数**:
  - `sender_id` (query, integer, 可选): 元信息：format=int64, nullable=true
  - `point_id` (query, integer, 可选): 测点id；元信息：format=int64, nullable=true
  - `start` (query, integer, 可选): 开始时间；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 对指定id的AOE采取指定动作，启动/停止/更新

- **方法**: `POST`
- **路径**: `/controls/aoes`
- **工具名**: `add_controls_aoes`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| AoeActions | array[AoeAction] | 是 | AOE指令列表 |
| AoeActions[] | oneOf[object{StartAoe} | object{StopAoe} | object{UpdateAoe} | object{UpdateAoeCsv}] | 是 | AOE指令对象；可选结构：object{StartAoe} | object{StopAoe} | object{UpdateAoe} | object{UpdateAoeCsv} |
| AoeActions[].oneOf[1] | object | 是 | 开始AOE |
| AoeActions[].oneOf[1].StartAoe | integer | 是 | 开始AOE；格式：int64 |
| AoeActions[].oneOf[2] | object | 是 | 停止AOE |
| AoeActions[].oneOf[2].StopAoe | integer | 是 | 停止AOE；格式：int64 |
| AoeActions[].oneOf[3] | object | 是 | 更新AOE |
| AoeActions[].oneOf[3].UpdateAoe | object | 是 | 更新AOE |
| AoeActions[].oneOf[3].UpdateAoe.actions | array[ActionEdge] | 是 | 动作列表 |
| AoeActions[].oneOf[3].UpdateAoe.actions[] | object | 是 | 边对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action | oneOf[string | object{SetPoints} | object{SetPointsWithCheck} | object{SetPoints2} | object{SetPointsWithCheck2} | object{Solve} | object{Nlsolve} | object{Milp} | object{SimpleMilp} | object{Nlp}] | 是 | 动作定义；可选值：None；可选结构：string | object{SetPoints} | object{SetPointsWithCheck} | object{SetPoints2} | object{SetPointsWithCheck2} | object{Solve} | object{Nlsolve} | object{Milp} | object{SimpleMilp} | object{Nlp} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[1] | string | 是 | 无动作；可选值：None |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2] | object | 是 | 设点动作 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints | object | 是 | 设点动作 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_id | array[string] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v | array[Expr] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_id | array[string] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v | array[Expr] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3] | object | 是 | 设点动作 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck | object | 是 | 设点动作 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_id | array[string] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v | array[Expr] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_id | array[string] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v | array[Expr] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4] | object | 是 | 设点动作 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2 | object | 是 | 设点动作 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs | array[PointsToExp] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr | object | 是 | 表达式 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].ids | array[string] | 是 | id列表 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes | array[PointsToExp] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr | object | 是 | 表达式 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].ids | array[string] | 是 | id列表 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5] | object | 是 | 设点动作 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2 | object | 是 | 设点动作 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs | array[PointsToExp] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr | object | 是 | 表达式 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].ids | array[string] | 是 | id列表 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes | array[PointsToExp] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr | object | 是 | 表达式 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].ids | array[string] | 是 | id列表 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6] | object | 是 | 求方程 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve | object | 是 | 求方程 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.a | object | 是 | A矩阵 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.a.m | integer | 是 | 行数 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.a.n | integer | 是 | 列数 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.a.v | array[array[any]] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b | array[Expr] | 是 | b向量 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init | array[Expr] | 是 | 变量初始值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_name | array[string] | 是 | 变量名称 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7] | object | 是 | 求非线性方程组 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve | object | 是 | 求非线性方程组 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f | array[Expr] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.parameters | object[string, string] | 是 | 额外属性：string |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init | array[Expr] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx | array[Expr] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_name | array[string] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8] | object | 是 | 混合整数线性规划稀疏表示 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp | object | 是 | 混合整数线性规划稀疏表示 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.a | object | 是 | Ax >=/<= b |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.a.m | integer | 是 | 行数 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.a.n | integer | 是 | 列数 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.a.v | array[array[any]] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b | array[Expr] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.binary_int_float | array[integer] | 是 | 整数变量在x中的位置 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.binary_int_float[] | integer | 是 | 整数变量在x中的位置；格式：int32 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.c | array[array[any]] | 是 | min/max c^T*x |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.constraint_type | array[Operation] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.constraint_type[] | string | 是 | Mathematical operations.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.min_or_max | boolean | 是 | min: true, max: false |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.x_lower | array[array[any]] | 是 | 变量的下界约束：变量位置、约束表达式 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.x_name | array[string] | 是 | 变量名称 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.x_upper | array[array[any]] | 是 | 变量的上界约束：变量位置、约束表达式 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9] | object | 是 | 混合整数线性规划稠密表示 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp | object | 是 | 混合整数线性规划稠密表示 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a | object | 是 | Ax >=/<= b |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.m | integer | 是 | 行数 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.n | integer | 是 | 列数 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v | array[Expr] | 是 | 值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b | array[Expr] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.binary_int_float | array[integer] | 是 | 整数变量在x中的位置 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.binary_int_float[] | integer | 是 | 整数变量在x中的位置；格式：int32 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c | array[Expr] | 是 | min/max c^T*x |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.constraint_type | array[Operation] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.constraint_type[] | string | 是 | Mathematical operations.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.min_or_max | boolean | 是 | min: true, max: false |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.x_lower | array[array[any]] | 是 | 变量的下界约束：变量位置、约束表达式 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.x_name | array[string] | 是 | 变量名称 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.x_upper | array[array[any]] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10] | object | 是 | 非整数线性规划 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp | object | 是 | 非整数线性规划 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g | array[Expr] | 是 | 等式约束式 g(x) == b |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower | array[Expr] | 是 | 不等式约束式 g(x) <= b |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper | array[Expr] | 是 | 不等式约束式 g(x) >= b |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.min_or_max | boolean | 是 | min: true, max: false |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr | object | 是 | 目标函数表达式 min obj |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init | array[Expr] | 是 | 变量初始值x0 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower | array[Expr] | 是 | 整数变量在x中的位置 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_name | array[string] | 是 | 变量名称 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper | array[Expr] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[] | object | 是 | 表达式对象 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.actions[].aoe_id | integer | 是 | AOE id；格式：int64 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].failure_mode | string | 是 | action失败时的处理方式；可选值：Default、Ignore、StopAll、StopFailed |
| AoeActions[].oneOf[3].UpdateAoe.actions[].name | string | 是 | 动作名称 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].source_node | integer | 是 | 源节点；格式：int64 |
| AoeActions[].oneOf[3].UpdateAoe.actions[].target_node | integer | 是 | 目标节点；格式：int64 |
| AoeActions[].oneOf[3].UpdateAoe.events | array[EventNode] | 是 | 节点列表 |
| AoeActions[].oneOf[3].UpdateAoe.events[] | object | 是 | 节点对象 |
| AoeActions[].oneOf[3].UpdateAoe.events[].aoe_id | integer | 是 | AOE id；格式：int64 |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr | object | 是 | 事件是否发生判断的bool表达式 |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn | array[Token] | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[12] | object | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| AoeActions[].oneOf[3].UpdateAoe.events[].id | integer | 是 | 节点id；格式：int64 |
| AoeActions[].oneOf[3].UpdateAoe.events[].name | string | 是 | 节点名 |
| AoeActions[].oneOf[3].UpdateAoe.events[].node_type | string | 是 | 节点类型；可选值：ConditionNode、SwitchNode、SwitchOfActionResult |
| AoeActions[].oneOf[3].UpdateAoe.events[].timeout | integer | 是 | 事件还未发生时等待超时时间；格式：int64 |
| AoeActions[].oneOf[3].UpdateAoe.id | integer | 是 | aoe id；格式：int64 |
| AoeActions[].oneOf[3].UpdateAoe.name | string | 是 | aoe名称 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type | oneOf[object{SimpleRepeat} | object{TimeDrive} | string | object{EventRepeatMix} | object{EventTimeMix}] | 是 | 触发类型；可选值：EventDrive；可选结构：object{SimpleRepeat} | object{TimeDrive} | string | object{EventRepeatMix} | object{EventTimeMix} |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[1] | object | 是 | 简单固定周期触发 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[1].SimpleRepeat | object | 是 | 简单固定周期触发 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[1].SimpleRepeat.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[1].SimpleRepeat.secs | integer | 是 | 秒；格式：int64 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[2] | object | 是 | cron表达式 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[2].TimeDrive | string | 是 | cron表达式 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[3] | string | 是 | 事件驱动，AOE开始节点条件满足即触发；可选值：EventDrive |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[4] | object | 是 | 事件驱动 && 简单固定周期 联合 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[4].EventRepeatMix | object | 是 | 事件驱动 && 简单固定周期 联合 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[4].EventRepeatMix.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[4].EventRepeatMix.secs | integer | 是 | 秒；格式：int64 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[5] | object | 是 | 事件驱动 && cron表达式 联合 |
| AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[5].EventTimeMix | string | 是 | 事件驱动 && cron表达式 联合 |
| AoeActions[].oneOf[3].UpdateAoe.variables | array[array[any]] | 是 | 用户自定义的变量：变量名和表达式 |
| AoeActions[].oneOf[4] | object | 是 | 更新AOE（字节数组） |
| AoeActions[].oneOf[4].UpdateAoeCsv | array[integer] | 是 | 更新AOE（字节数组） |
| AoeActions[].oneOf[4].UpdateAoeCsv[] | integer | 是 | 更新AOE（字节数组）；格式：int32 |


### 执行测点控制

- **方法**: `POST`
- **路径**: `/controls/points`
- **工具名**: `add_controls_points`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| analogs | array[SetFloatValue] | 是 |  |
| analogs[] | object | 是 | 浮点型指令数据 |
| analogs[].point_id | integer | 是 | 格式：int64 |
| analogs[].sender_id | integer | 是 | 格式：int64 |
| analogs[].timestamp | integer | 是 | 格式：int64 |
| analogs[].yt_command | number | 是 | 格式：double |
| discretes | array[SetIntValue] | 是 |  |
| discretes[] | object | 是 | 整型指令数据 |
| discretes[].point_id | integer | 是 | 格式：int64 |
| discretes[].sender_id | integer | 是 | 格式：int64 |
| discretes[].timestamp | integer | 是 | 格式：int64 |
| discretes[].yk_command | integer | 是 | 格式：int64 |


### 执行测点控制（通过别名）

- **方法**: `POST`
- **路径**: `/controls/points_by_alias`
- **工具名**: `add_controls_points_by_alias`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| analogs | array[SetFloatValue2] | 是 |  |
| analogs[] | object | 是 | 浮点型指令数据 |
| analogs[].point_alias | string | 是 |  |
| analogs[].sender_id | integer | 是 | 格式：int64 |
| analogs[].timestamp | integer | 是 | 格式：int64 |
| analogs[].yt_command | number | 是 | 格式：double |
| discretes | array[SetIntValue2] | 是 |  |
| discretes[] | object | 是 | 整型指令数据 |
| discretes[].point_alias | string | 是 |  |
| discretes[].sender_id | integer | 是 | 格式：int64 |
| discretes[].timestamp | integer | 是 | 格式：int64 |
| discretes[].yk_command | integer | 是 | 格式：int64 |


### 执行测点控制（通过公式）

- **方法**: `POST`
- **路径**: `/controls/points_by_expr`
- **工具名**: `add_controls_points_by_expr`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commands | array[SetPointValue] | 是 |  |
| commands[] | object | 是 | 公式型指令数据 |
| commands[].command | object | 是 | 表达式对象 |
| commands[].command.rpn | array[Token] | 是 |  |
| commands[].command.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| commands[].command.rpn[].oneOf[1] | object | 是 | Binary operation. |
| commands[].command.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| commands[].command.rpn[].oneOf[2] | object | 是 | Unary operation. |
| commands[].command.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| commands[].command.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| commands[].command.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| commands[].command.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| commands[].command.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| commands[].command.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| commands[].command.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| commands[].command.rpn[].oneOf[9] | object | 是 | A number. |
| commands[].command.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| commands[].command.rpn[].oneOf[10] | object | 是 | A tensor. |
| commands[].command.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| commands[].command.rpn[].oneOf[11] | object | 是 | A variable. |
| commands[].command.rpn[].oneOf[11].Var | string | 是 | A variable. |
| commands[].command.rpn[].oneOf[12] | object | 是 |  |
| commands[].command.rpn[].oneOf[12].Str | string | 是 |  |
| commands[].command.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| commands[].command.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| commands[].point_id | integer | 是 | 格式：int64 |
| commands[].sender_id | integer | 是 | 格式：int64 |
| commands[].timestamp | integer | 是 | 格式：int64 |


### 执行测点控制（通过其他数据源）

- **方法**: `POST`
- **路径**: `/controls/points_with_source/{source}`
- **工具名**: `add_controls_points_with_source_by_source`
- **参数**:
  - `source` (path, integer, 必填): 数据源id；元信息：format=int32
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].analog_value | number | 是 | 模拟量值；格式：double |
| [].discrete_value | integer | 是 | 离散量值；格式：int64 |
| [].is_discrete | boolean | 是 | 是否离散量 |
| [].is_transformed | boolean | 是 | 是否已经变换 |
| [].point_id | integer | 是 | 对应的测点；格式：int64 |
| [].timestamp | integer | 是 | 时间戳；格式：int64 |
| [].transformed_analog | number | 是 | 变换后的模拟量值；格式：double |
| [].transformed_discrete | integer | 是 | 变换后的离散量值；格式：int64 |


***

## DEVICES 模块

### 查询拓扑

- **方法**: `GET`
- **路径**: `/devices/cns`
- **工具名**: `get_devices_cns`
- **参数**:
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 新增拓扑

- **方法**: `POST`
- **路径**: `/devices/cns`
- **工具名**: `add_devices_cns`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 连接节点 |
| [].id | integer | 是 | 连接节点id；格式：int64 |
| [].psr_id | string | 是 | 资源id |
| [].terminals | array[integer] | 是 | 端子id数组 |
| [].terminals[] | integer | 是 | 端子id数组；格式：int64 |


### 查询所有设备定义

- **方法**: `GET`
- **路径**: `/devices/defines`
- **工具名**: `get_devices_defines`

### 新增设备定义

- **方法**: `POST`
- **路径**: `/devices/defines`
- **工具名**: `add_devices_defines`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 设备定义 |
| [].desc | string | 是 | 设备定义的描述 |
| [].id | integer | 是 | 定义id；格式：int64 |
| [].name | string | 是 | 设备类别名称 |
| [].prop_groups | array[PropGroupDefine] | 是 | 设备属性 |
| [].prop_groups[] | object | 是 | 属性分组定义 |
| [].prop_groups[].desc | string | 是 | 属性定义描述 |
| [].prop_groups[].name | string | 是 | 属性定义标识 |
| [].prop_groups[].prop_defines | array[integer] | 是 | 设备属性实际描述 |
| [].prop_groups[].prop_defines[] | integer | 是 | 设备属性实际描述；格式：int64 |
| [].rsr_type | string | 是 | 设备所属类型；可选值：Switch、Busbar、ACline、DCline、Winding、SyncGenerator、ESS、PCS、Transformer、Load、ShuntCompensator、SerialCompensator、ShuntReactor、ShuntCapacitor、SeriesReactor、SeriesCapacitor、Breaker、Disconnector、GroundDisconnector、SVC、SVG、Feeder、PWBusbar、Cable、Regulator、Connector、Measurement、Company、SubIsland、LoadArea、Substation、PowerPlant、VoltageLevel、BaseVoltage、HvdcSys、HvdcPoleSys、DCPole、DCLineDot、TLineDot、Converter、TLine、ACLineDot、TNode、Convergenceline、SeriesPowerTransformer、SeriesTransformerWinding、Acfilter、Synccondenser、DCBreaker、DCDisconnector、Signal、Combined、Composite、Section、SectionType、Bus、Branch、UserDefine1、UserDefine2、UserDefine3、UserDefine4、UserDefine5、UserDefine6、UserDefine7、UserDefine8、UserDefine9、UserDefine10、Unknown |
| [].terminal_num | integer | 是 | 端口数量；格式：int32 |


### 修改设备定义

- **方法**: `PUT`
- **路径**: `/devices/defines`
- **工具名**: `update_devices_defines`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 是 | 设备定义的描述 |
| id | integer | 是 | 定义id；格式：int64 |
| name | string | 是 | 设备类别名称 |
| prop_groups | array[PropGroupDefine] | 是 | 设备属性 |
| prop_groups[] | object | 是 | 属性分组定义 |
| prop_groups[].desc | string | 是 | 属性定义描述 |
| prop_groups[].name | string | 是 | 属性定义标识 |
| prop_groups[].prop_defines | array[integer] | 是 | 设备属性实际描述 |
| prop_groups[].prop_defines[] | integer | 是 | 设备属性实际描述；格式：int64 |
| rsr_type | string | 是 | 设备所属类型；可选值：Switch、Busbar、ACline、DCline、Winding、SyncGenerator、ESS、PCS、Transformer、Load、ShuntCompensator、SerialCompensator、ShuntReactor、ShuntCapacitor、SeriesReactor、SeriesCapacitor、Breaker、Disconnector、GroundDisconnector、SVC、SVG、Feeder、PWBusbar、Cable、Regulator、Connector、Measurement、Company、SubIsland、LoadArea、Substation、PowerPlant、VoltageLevel、BaseVoltage、HvdcSys、HvdcPoleSys、DCPole、DCLineDot、TLineDot、Converter、TLine、ACLineDot、TNode、Convergenceline、SeriesPowerTransformer、SeriesTransformerWinding、Acfilter、Synccondenser、DCBreaker、DCDisconnector、Signal、Combined、Composite、Section、SectionType、Bus、Branch、UserDefine1、UserDefine2、UserDefine3、UserDefine4、UserDefine5、UserDefine6、UserDefine7、UserDefine8、UserDefine9、UserDefine10、Unknown |
| terminal_num | integer | 是 | 端口数量；格式：int32 |


### 删除指定id的设备定义

- **方法**: `DELETE`
- **路径**: `/devices/defines/{ids}`
- **工具名**: `delete_devices_defines_by_s`
- **参数**:
  - `ids` (path, string, 必填): 设备定义id列表，以,间隔

### 根据id查询对应的设备定义

- **方法**: `GET`
- **路径**: `/devices/defines/{id}`
- **工具名**: `get_devices_defines_by`
- **参数**:
  - `id` (path, integer, 必填): 设备定义id；元信息：format=int64

### 查询所有设备列表

- **方法**: `GET`
- **路径**: `/devices/devs`
- **工具名**: `get_devices_devs`
- **参数**:
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 新增设备

- **方法**: `POST`
- **路径**: `/devices/devs`
- **工具名**: `add_devices_devs`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 设备对象 |
| [].container_id | integer | 否 | 格式：int64；允许空值 |
| [].define_id | integer | 是 | 设备定义id；格式：int64 |
| [].desc | string | 是 | 设备描述 |
| [].id | integer | 是 | 设备id；格式：int64 |
| [].name | string | 是 | 设备名称 |
| [].prop_group_ids | array[integer] | 是 | 设备属性分组id列表 |
| [].prop_group_ids[] | integer | 是 | 设备属性分组id列表；格式：int64 |
| [].terminals | array[Terminal] | 是 | 设备的端口 |
| [].terminals[] | object | 是 | 端口 |
| [].terminals[].device | integer | 是 | 设备id；格式：int64 |
| [].terminals[].id | integer | 是 | 端口id；格式：int64 |


### 修改设备

- **方法**: `PUT`
- **路径**: `/devices/devs`
- **工具名**: `update_devices_devs`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| container_id | integer | 否 | 格式：int64；允许空值 |
| define_id | integer | 是 | 设备定义id；格式：int64 |
| desc | string | 是 | 设备描述 |
| id | integer | 是 | 设备id；格式：int64 |
| name | string | 是 | 设备名称 |
| prop_group_ids | array[integer] | 是 | 设备属性分组id列表 |
| prop_group_ids[] | integer | 是 | 设备属性分组id列表；格式：int64 |
| terminals | array[Terminal] | 是 | 设备的端口 |
| terminals[] | object | 是 | 端口 |
| terminals[].device | integer | 是 | 设备id；格式：int64 |
| terminals[].id | integer | 是 | 端口id；格式：int64 |


### 删除指定id的设备

- **方法**: `DELETE`
- **路径**: `/devices/devs/{ids}`
- **工具名**: `delete_devices_devs_by_s`
- **参数**:
  - `ids` (path, string, 必填): 设备id列表，以,间隔

### 根据ID查询设备对象

- **方法**: `GET`
- **路径**: `/devices/devs/{id}`
- **工具名**: `get_devices_devs_by`
- **参数**:
  - `id` (path, integer, 必填): 设备id；元信息：format=int64
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 查询电气岛

- **方法**: `GET`
- **路径**: `/devices/islands`
- **工具名**: `get_devices_islands`
- **参数**:
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 根据版本号apply电气岛

- **方法**: `POST`
- **路径**: `/devices/islands`
- **工具名**: `add_devices_islands`
- **请求体**:

  - 无法解析请求体结构


### 查询设备测点

- **方法**: `GET`
- **路径**: `/devices/measure_defs`
- **工具名**: `get_devices_measure_defs`
- **参数**:
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 新增设备测点

- **方法**: `POST`
- **路径**: `/devices/measure_defs`
- **工具名**: `add_devices_measure_defs`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 测点定义 |
| [].dev_id | integer | 是 | 格式：int64 |
| [].id | integer | 是 | 格式：int64 |
| [].phase | string | 是 | 量测相位；可选值：Unknown、Total、A、B、C、A0、B0、C0、AB、BC、CA |
| [].point_id | integer | 是 | 格式：int64 |
| [].terminal_id | integer | 是 | 格式：int64 |


### 修改设备测点

- **方法**: `PUT`
- **路径**: `/devices/measure_defs`
- **工具名**: `update_devices_measure_defs`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 测点定义 |
| [].dev_id | integer | 是 | 格式：int64 |
| [].id | integer | 是 | 格式：int64 |
| [].phase | string | 是 | 量测相位；可选值：Unknown、Total、A、B、C、A0、B0、C0、AB、BC、CA |
| [].point_id | integer | 是 | 格式：int64 |
| [].terminal_id | integer | 是 | 格式：int64 |


### 删除指定id的设备测点

- **方法**: `DELETE`
- **路径**: `/devices/measure_defs`
- **工具名**: `delete_devices_measure_defs`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | integer | 是 | 格式：int64 |


### 查询测点树（测点在设备树中的路径）

- **方法**: `GET`
- **路径**: `/devices/point_tree`
- **工具名**: `get_devices_point_tree`
- **参数**:
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 查询所有设备属性定义

- **方法**: `GET`
- **路径**: `/devices/prop_defines`
- **工具名**: `get_devices_prop_defines`

### 新增设备属性定义

- **方法**: `POST`
- **路径**: `/devices/prop_defines`
- **工具名**: `add_devices_prop_defines`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 设备属性 |
| [].data_type | string | 是 | 属性类型；可选值：U8、U16、U32、U64、I8、I16、I32、I64、F32、F64、Str、Complex32、Complex64、TensorF32、TensorF64、TensorC32、TensorC64、Unknown |
| [].data_unit | string | 是 | 属性单位；可选值：OnOrOff、A、V、kV、W、kW、MW、Var、kVar、MVar、VA、kVA、MVA、H、mH、Ah、mAh、kWh、Celsius、feet、km、meter、mm2、degree、rad、UnitOne、Percent、bit、B、kB、MB、GB、TB、PB、Unknown |
| [].desc | string | 是 | 属性定义描述 |
| [].id | integer | 是 | 属性定义id；格式：int64 |
| [].name | string | 是 | 属性定义标识 |


### 修改设备属性定义

- **方法**: `PUT`
- **路径**: `/devices/prop_defines`
- **工具名**: `update_devices_prop_defines`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data_type | string | 是 | 属性类型；可选值：U8、U16、U32、U64、I8、I16、I32、I64、F32、F64、Str、Complex32、Complex64、TensorF32、TensorF64、TensorC32、TensorC64、Unknown |
| data_unit | string | 是 | 属性单位；可选值：OnOrOff、A、V、kV、W、kW、MW、Var、kVar、MVar、VA、kVA、MVA、H、mH、Ah、mAh、kWh、Celsius、feet、km、meter、mm2、degree、rad、UnitOne、Percent、bit、B、kB、MB、GB、TB、PB、Unknown |
| desc | string | 是 | 属性定义描述 |
| id | integer | 是 | 属性定义id；格式：int64 |
| name | string | 是 | 属性定义标识 |


### 删除指定id的设备属性定义

- **方法**: `DELETE`
- **路径**: `/devices/prop_defines/{ids}`
- **工具名**: `delete_devices_prop_defines_by_s`
- **参数**:
  - `ids` (path, string, 必填): 设备属性定义id列表，以,间隔

### 查询所有设备属性分组

- **方法**: `GET`
- **路径**: `/devices/prop_groups`
- **工具名**: `get_devices_prop_groups`
- **参数**:
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 新增设备属性分组

- **方法**: `POST`
- **路径**: `/devices/prop_groups`
- **工具名**: `add_devices_prop_groups`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 设备属性分组 |
| [].defines | array[integer] | 是 | 设备属性定义列表 |
| [].defines[] | integer | 是 | 设备属性定义列表；格式：int64 |
| [].id | integer | 是 | 格式：int64 |
| [].name | string | 是 | 分组名称，用于显示，以及匹配PropGroupDefine |
| [].props | array[PropValue] | 是 | 设备属性实际描述 |
| [].props[] | oneOf[object{U8} | object{U16} | object{U32} | object{U64} | object{I8} | object{I16} | object{I32} | object{I64} | object{F32} | object{F64} | object{Str} | object{Complex32} | object{Complex64} | object{TensorF32} | object{TensorF64} | object{TensorC32} | object{TensorC64} | string] | 是 | 设备属性值；可选值：Unknown；可选结构：object{U8} | object{U16} | object{U32} | object{U64} | object{I8} | object{I16} | object{I32} | object{I64} | object{F32} | object{F64} | object{Str} | object{Complex32} | object{Complex64} | object{TensorF32} | object{TensorF64} | object{TensorC32} | object{TensorC64} | string |
| [].props[].oneOf[1] | object | 是 |  |
| [].props[].oneOf[1].U8 | integer | 是 | 格式：int32 |
| [].props[].oneOf[2] | object | 是 |  |
| [].props[].oneOf[2].U16 | integer | 是 | 格式：int32 |
| [].props[].oneOf[3] | object | 是 |  |
| [].props[].oneOf[3].U32 | integer | 是 | 格式：int32 |
| [].props[].oneOf[4] | object | 是 |  |
| [].props[].oneOf[4].U64 | integer | 是 | 格式：int64 |
| [].props[].oneOf[5] | object | 是 |  |
| [].props[].oneOf[5].I8 | integer | 是 | 格式：int32 |
| [].props[].oneOf[6] | object | 是 |  |
| [].props[].oneOf[6].I16 | integer | 是 | 格式：int32 |
| [].props[].oneOf[7] | object | 是 |  |
| [].props[].oneOf[7].I32 | integer | 是 | 格式：int32 |
| [].props[].oneOf[8] | object | 是 |  |
| [].props[].oneOf[8].I64 | integer | 是 | 格式：int64 |
| [].props[].oneOf[9] | object | 是 |  |
| [].props[].oneOf[9].F32 | number | 是 | 格式：float |
| [].props[].oneOf[10] | object | 是 |  |
| [].props[].oneOf[10].F64 | number | 是 | 格式：double |
| [].props[].oneOf[11] | object | 是 |  |
| [].props[].oneOf[11].Str | string | 是 |  |
| [].props[].oneOf[12] | object | 是 | f32类型复数 |
| [].props[].oneOf[12].Complex32 | object | 是 | f32类型复数 |
| [].props[].oneOf[12].Complex32.im | number | 是 | 格式：float |
| [].props[].oneOf[12].Complex32.re | number | 是 | 格式：float |
| [].props[].oneOf[13] | object | 是 | f64类型复数 |
| [].props[].oneOf[13].Complex64 | object | 是 | f64类型复数 |
| [].props[].oneOf[13].Complex64.im | number | 是 | 格式：double |
| [].props[].oneOf[13].Complex64.re | number | 是 | 格式：double |
| [].props[].oneOf[14] | object | 是 | f32类型向量 |
| [].props[].oneOf[14].TensorF32 | array[object] | 是 | f32类型向量 |
| [].props[].oneOf[15] | object | 是 | f64类型向量 |
| [].props[].oneOf[15].TensorF64 | array[object] | 是 | f64类型向量 |
| [].props[].oneOf[16] | object | 是 | f32类型复数向量 |
| [].props[].oneOf[16].TensorC32 | array[object] | 是 | f32类型复数向量 |
| [].props[].oneOf[17] | object | 是 | f64类型复数向量 |
| [].props[].oneOf[17].TensorC64 | array[object] | 是 | f64类型复数向量 |
| [].props[].oneOf[18] | string | 是 | 可选值：Unknown |
| [].rsr_id | integer | 是 | resource id；格式：int64 |


### 修改设备属性分组

- **方法**: `PUT`
- **路径**: `/devices/prop_groups`
- **工具名**: `update_devices_prop_groups`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 设备属性分组 |
| [].defines | array[integer] | 是 | 设备属性定义列表 |
| [].defines[] | integer | 是 | 设备属性定义列表；格式：int64 |
| [].id | integer | 是 | 格式：int64 |
| [].name | string | 是 | 分组名称，用于显示，以及匹配PropGroupDefine |
| [].props | array[PropValue] | 是 | 设备属性实际描述 |
| [].props[] | oneOf[object{U8} | object{U16} | object{U32} | object{U64} | object{I8} | object{I16} | object{I32} | object{I64} | object{F32} | object{F64} | object{Str} | object{Complex32} | object{Complex64} | object{TensorF32} | object{TensorF64} | object{TensorC32} | object{TensorC64} | string] | 是 | 设备属性值；可选值：Unknown；可选结构：object{U8} | object{U16} | object{U32} | object{U64} | object{I8} | object{I16} | object{I32} | object{I64} | object{F32} | object{F64} | object{Str} | object{Complex32} | object{Complex64} | object{TensorF32} | object{TensorF64} | object{TensorC32} | object{TensorC64} | string |
| [].props[].oneOf[1] | object | 是 |  |
| [].props[].oneOf[1].U8 | integer | 是 | 格式：int32 |
| [].props[].oneOf[2] | object | 是 |  |
| [].props[].oneOf[2].U16 | integer | 是 | 格式：int32 |
| [].props[].oneOf[3] | object | 是 |  |
| [].props[].oneOf[3].U32 | integer | 是 | 格式：int32 |
| [].props[].oneOf[4] | object | 是 |  |
| [].props[].oneOf[4].U64 | integer | 是 | 格式：int64 |
| [].props[].oneOf[5] | object | 是 |  |
| [].props[].oneOf[5].I8 | integer | 是 | 格式：int32 |
| [].props[].oneOf[6] | object | 是 |  |
| [].props[].oneOf[6].I16 | integer | 是 | 格式：int32 |
| [].props[].oneOf[7] | object | 是 |  |
| [].props[].oneOf[7].I32 | integer | 是 | 格式：int32 |
| [].props[].oneOf[8] | object | 是 |  |
| [].props[].oneOf[8].I64 | integer | 是 | 格式：int64 |
| [].props[].oneOf[9] | object | 是 |  |
| [].props[].oneOf[9].F32 | number | 是 | 格式：float |
| [].props[].oneOf[10] | object | 是 |  |
| [].props[].oneOf[10].F64 | number | 是 | 格式：double |
| [].props[].oneOf[11] | object | 是 |  |
| [].props[].oneOf[11].Str | string | 是 |  |
| [].props[].oneOf[12] | object | 是 | f32类型复数 |
| [].props[].oneOf[12].Complex32 | object | 是 | f32类型复数 |
| [].props[].oneOf[12].Complex32.im | number | 是 | 格式：float |
| [].props[].oneOf[12].Complex32.re | number | 是 | 格式：float |
| [].props[].oneOf[13] | object | 是 | f64类型复数 |
| [].props[].oneOf[13].Complex64 | object | 是 | f64类型复数 |
| [].props[].oneOf[13].Complex64.im | number | 是 | 格式：double |
| [].props[].oneOf[13].Complex64.re | number | 是 | 格式：double |
| [].props[].oneOf[14] | object | 是 | f32类型向量 |
| [].props[].oneOf[14].TensorF32 | array[object] | 是 | f32类型向量 |
| [].props[].oneOf[15] | object | 是 | f64类型向量 |
| [].props[].oneOf[15].TensorF64 | array[object] | 是 | f64类型向量 |
| [].props[].oneOf[16] | object | 是 | f32类型复数向量 |
| [].props[].oneOf[16].TensorC32 | array[object] | 是 | f32类型复数向量 |
| [].props[].oneOf[17] | object | 是 | f64类型复数向量 |
| [].props[].oneOf[17].TensorC64 | array[object] | 是 | f64类型复数向量 |
| [].props[].oneOf[18] | string | 是 | 可选值：Unknown |
| [].rsr_id | integer | 是 | resource id；格式：int64 |


### 根据id列表查看设备属性分组列表

- **方法**: `GET`
- **路径**: `/devices/prop_groups/{ids}`
- **工具名**: `get_devices_prop_groups_by_s`
- **参数**:
  - `ids` (path, string, 必填): 设备属性分组id列表，以,间隔
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 删除指定id的设备属性分组

- **方法**: `DELETE`
- **路径**: `/devices/prop_groups/{ids}`
- **工具名**: `delete_devices_prop_groups_by_s`
- **参数**:
  - `ids` (path, string, 必填): 设备属性分组id列表，以,间隔

### 清空资源

- **方法**: `DELETE`
- **路径**: `/devices/resources_clear`
- **工具名**: `delete_devices_resources_clear`

### 查询电气岛所有版本

- **方法**: `GET`
- **路径**: `/devices/version`
- **工具名**: `get_devices_version`

### 新增电气岛版本

- **方法**: `POST`
- **路径**: `/devices/version`
- **工具名**: `add_devices_version`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| note | string | 是 | 提交时的注释 |
| tree_id | string | 是 | 对应的tree_id |
| version | integer | 是 | 版本号；格式：int32 |


### 删除指定id的电气岛版本

- **方法**: `DELETE`
- **路径**: `/devices/version/{id}`
- **工具名**: `delete_devices_version_by`
- **参数**:
  - `id` (path, integer, 必填): 版本id；元信息：format=int32

### 查询日志字节数组

- **方法**: `GET`
- **路径**: `/logs_bytes`
- **工具名**: `get_logs_bytes`
- **参数**:
  - `is_query_size` (query, boolean, 可选): 是否限制文件大小；元信息：nullable=true

### 导入所有模型字节数组

- **方法**: `POST`
- **路径**: `/multi_import_bytes`
- **工具名**: `add_multi_import_bytes`
- **请求体**:

  - 无法解析请求体结构


***

## EMS 模块

### 对指定id的ems执行请求

- **方法**: `POST`
- **路径**: `/ems/request/{ems_id}`
- **工具名**: `add_ems_request_by_ems`
- **参数**:
  - `ems_id` (path, string, 必填): ems_id
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | string | 否 | 允许空值 |
| function | oneOf[string] | 否 | 可选值：Get、Post、Put、Delete、Test；可选结构：string |
| function.oneOf[1] | string | 是 | 可选值：Get、Post、Put、Delete、Test |
| header_keys | array[string] | 是 |  |
| header_values | array[string] | 是 |  |
| id | integer | 否 | 格式：int64；允许空值 |
| url | string | 否 | 允许空值 |


### 查询指定id的ems

- **方法**: `GET`
- **路径**: `/ems/{id}`
- **工具名**: `get_ems_by`
- **参数**:
  - `id` (path, string, 必填): ems_id

### 查询所有的ems

- **方法**: `GET`
- **路径**: `/ems_list`
- **工具名**: `get_ems_list`

***

## FILES 模块

### 执行filetree的操作

- **方法**: `POST`
- **路径**: `/file_tree`
- **工具名**: `add_file_tree`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| op | string | 是 | 文件树的操作类型；可选值：Query、Add、Delete、Change、Apply、QueryApply |
| op_paths | array[string] | 是 |  |
| path | string | 否 | 允许空值 |
| tree_id | string | 是 |  |
| version | integer | 否 | 格式：int32；允许空值 |


### 保存filetree的一个节点

- **方法**: `POST`
- **路径**: `/file_tree/{id}`
- **工具名**: `add_file_tree_by`
- **参数**:
  - `id` (path, string, 必填): tree_id
- **请求体**:

  - 无法解析请求体结构


### 提交filetree版本

- **方法**: `POST`
- **路径**: `/file_tree_version`
- **工具名**: `add_file_tree_version`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| note | string | 是 | 提交时的注释 |
| tree_id | string | 是 | 对应的tree_id |
| version | integer | 是 | 版本号；格式：int32 |


***

## FLOWS 模块

### 查询报表结果（简洁模式）

- **方法**: `GET`
- **路径**: `/flows/brief_results`
- **工具名**: `get_flows_brief_results`
- **参数**:
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 执行报表动作

- **方法**: `POST`
- **路径**: `/flows/controls`
- **工具名**: `add_flows_controls`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oneOf[1] | string | 是 | 开始；可选值：Start |
| oneOf[2] | string | 是 | 停止；可选值：Stop |
| oneOf[3] | object | 是 | 开始某个报表 |
| oneOf[3].StartFlow | integer | 是 | 开始某个报表；格式：int64 |
| oneOf[4] | object | 是 | 开始某些报表 |
| oneOf[4].StartFlows | array[integer] | 是 | 开始某些报表 |
| oneOf[4].StartFlows[] | integer | 是 | 开始某些报表；格式：int64 |
| oneOf[5] | object | 是 | 停止某个报表 |
| oneOf[5].StopFlow | integer | 是 | 停止某个报表；格式：int64 |
| oneOf[6] | object | 是 | 停止某些报表 |
| oneOf[6].StopFlows | array[integer] | 是 | 停止某些报表 |
| oneOf[6].StopFlows[] | integer | 是 | 停止某些报表；格式：int64 |
| oneOf[7] | string | 是 | 退出；可选值：QuitDb |


### 报表节点测试

- **方法**: `POST`
- **路径**: `/flows/debug`
- **工具名**: `add_flows_debug`
- **请求体**:

  - 无法解析请求体结构


### 查询报表

- **方法**: `GET`
- **路径**: `/flows/models`
- **工具名**: `get_flows_models`
- **参数**:
  - `id` (query, integer, 可选): 测点id（优先）；元信息：format=int64, nullable=true
  - `ids` (query, string, 可选): 测点id列表，以,间隔；元信息：nullable=true

### 新增报表

- **方法**: `POST`
- **路径**: `/flows/models`
- **工具名**: `add_flows_models`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].actions | array[DfActionEdge] | 是 | 边 |
| [].actions[] | object | 是 | 边 |
| [].actions[].action | oneOf[object{Eval} | object{Sql} | object{Onnx} | object{OnnxUrl} | object{Nnef} | object{NnefUrl} | object{WriteFile} | object{WriteSql} | string] | 是 | 可选值：None；可选结构：object{Eval} | object{Sql} | object{Onnx} | object{OnnxUrl} | object{Nnef} | object{NnefUrl} | object{WriteFile} | object{WriteSql} | string |
| [].actions[].action.oneOf[1] | object | 是 | 对单个Dataframe进行运算 |
| [].actions[].action.oneOf[1].Eval | array[Expr] | 是 | 对单个Dataframe进行运算 |
| [].actions[].action.oneOf[1].Eval[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[1].Eval[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[1].Eval[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[2] | object | 是 | 从DataFrame中进行sql查询 |
| [].actions[].action.oneOf[2].Sql | string | 是 | 从DataFrame中进行sql查询 |
| [].actions[].action.oneOf[3] | object | 是 | 用onnx表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[3].Onnx | array[integer] | 是 | 用onnx表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[3].Onnx[] | integer | 是 | 用onnx表达的神经网络对DataFrame进行运行；格式：int32 |
| [].actions[].action.oneOf[4] | object | 是 | 用onnx表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[4].OnnxUrl | string | 是 | 用onnx表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[5] | object | 是 | 用nnef表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[5].Nnef | array[integer] | 是 | 用nnef表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[5].Nnef[] | integer | 是 | 用nnef表达的神经网络对DataFrame进行运行；格式：int32 |
| [].actions[].action.oneOf[6] | object | 是 | 用nnef表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[6].NnefUrl | string | 是 | 用nnef表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[7] | object | 是 | 写到文件 |
| [].actions[].action.oneOf[7].WriteFile | string | 是 | 写到文件 |
| [].actions[].action.oneOf[8] | object | 是 | 写到数据库 |
| [].actions[].action.oneOf[8].WriteSql | array[object] | 是 | 写到数据库 |
| [].actions[].action.oneOf[9] | string | 是 | 不做任何操作；可选值：None |
| [].actions[].desc | string | 是 |  |
| [].actions[].flow_id | integer | 是 | 格式：int64 |
| [].actions[].name | string | 是 |  |
| [].actions[].source_node | integer | 是 | 格式：int64 |
| [].actions[].target_node | integer | 是 | 格式：int64 |
| [].aoe_var | array[any] | 否 | destination of aoe variable；允许空值 |
| [].id | integer | 是 | dff id；格式：int64 |
| [].is_on | boolean | 是 | should schedule |
| [].name | string | 是 | dff name |
| [].nodes | array[DfNode] | 是 | 节点 |
| [].nodes[] | object | 是 | 节点 |
| [].nodes[].flow_id | integer | 是 | 格式：int64 |
| [].nodes[].id | integer | 是 | 格式：int64 |
| [].nodes[].name | string | 是 |  |
| [].nodes[].node_type | oneOf[object{Source} | object{Transform} | object{TensorEval} | object{Sql} | object{Solve} | string | object{MILP} | object{NLP} | object{Wasm}] | 是 | 可选值：NLSolve、None；可选结构：object{Source} | object{Transform} | object{TensorEval} | object{Sql} | object{Solve} | string | object{MILP} | object{NLP} | object{Wasm} |
| [].nodes[].node_type.oneOf[1] | object | 是 | query data source |
| [].nodes[].node_type.oneOf[1].Source | oneOf[object{Data} | object{File} | object{Url} | object{Image} | object{Sql} | object{OtherFlow} | object{Dev} | object{Points} | object{Meas} | object{Plan} | object{PointsEval} | object{MeasEval}] | 是 | query data source；可选结构：object{Data} | object{File} | object{Url} | object{Image} | object{Sql} | object{OtherFlow} | object{Dev} | object{Points} | object{Meas} | object{Plan} | object{PointsEval} | object{MeasEval} |
| [].nodes[].node_type.oneOf[1].Source.oneOf[1] | object | 是 | 直接导入数据 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[1].Data | string | 是 | 直接导入数据 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[2] | object | 是 | 根据文件后缀parquet/xlsx/csv自动判断，如果没有后缀默认用csv |
| [].nodes[].node_type.oneOf[1].Source.oneOf[2].File | string | 是 | 根据文件后缀parquet/xlsx/csv自动判断，如果没有后缀默认用csv |
| [].nodes[].node_type.oneOf[1].Source.oneOf[3] | object | 是 | 根据url后缀parquet/xlsx/csv自动判断，如果没有后缀默认用csv |
| [].nodes[].node_type.oneOf[1].Source.oneOf[3].Url | string | 是 | 根据url后缀parquet/xlsx/csv自动判断，如果没有后缀默认用csv |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4] | object | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image | object | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.color_type | string | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.filter_type | string | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.height | integer | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.is_url | boolean | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.url_or_path | string | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.width | integer | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[5] | object | 是 | 数据库 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[5].Sql | array[object] | 是 | 数据库 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[6] | object | 是 | 其他Flow |
| [].nodes[].node_type.oneOf[1].Source.oneOf[6].OtherFlow | integer | 是 | 其他Flow；格式：int64 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[7] | object | 是 | 内置的设备列表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[7].Dev | string | 是 | 内置的设备列表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[8] | object | 是 | 内置的测点表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[8].Points | string | 是 | 内置的测点表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[9] | object | 是 | 内置的量测表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[9].Meas | array[string] | 是 | 内置的量测表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[10] | object | 是 | 计划数据表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[10].Plan | string | 是 | 计划数据表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11] | object | 是 | 筛选测点，功能与DfSource::Points一样，参数是表达式而不是sql |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval | array[Expr] | 是 | 筛选测点，功能与DfSource::Points一样，参数是表达式而不是sql |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[] | object | 是 | 表达式对象 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn | array[Token] | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[9] | object | 是 | A number. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[12] | object | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[12].Str | string | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[12] | object | 是 | 筛选量测，功能与DfSource::Meas一样，参数是表达式而不是sql |
| [].nodes[].node_type.oneOf[1].Source.oneOf[12].MeasEval | array[object] | 是 | 筛选量测，功能与DfSource::Meas一样，参数是表达式而不是sql |
| [].nodes[].node_type.oneOf[2] | object | 是 | transformation |
| [].nodes[].node_type.oneOf[2].Transform | object | 是 | transformation |
| [].nodes[].node_type.oneOf[2].Transform.rpn | array[Token] | 是 |  |
| [].nodes[].node_type.oneOf[2].Transform.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[9] | object | 是 | A number. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[11] | object | 是 | A variable. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[12] | object | 是 |  |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[12].Str | string | 是 |  |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].nodes[].node_type.oneOf[3] | object | 是 | tensor eval script |
| [].nodes[].node_type.oneOf[3].TensorEval | array[object] | 是 | tensor eval script |
| [].nodes[].node_type.oneOf[4] | object | 是 | sql execute |
| [].nodes[].node_type.oneOf[4].Sql | string | 是 | sql execute |
| [].nodes[].node_type.oneOf[5] | object | 是 | linear equations |
| [].nodes[].node_type.oneOf[5].Solve | boolean | 是 | linear equations |
| [].nodes[].node_type.oneOf[6] | string | 是 | nonlinear equations；可选值：NLSolve |
| [].nodes[].node_type.oneOf[7] | object | 是 | mixed integer linear programming, objective function related DF name, constraint related DF name |
| [].nodes[].node_type.oneOf[7].MILP | array[object] | 是 | mixed integer linear programming, objective function related DF name, constraint related DF name |
| [].nodes[].node_type.oneOf[8] | object | 是 | nonlinear programming |
| [].nodes[].node_type.oneOf[8].NLP | array[string] | 是 | nonlinear programming |
| [].nodes[].node_type.oneOf[9] | object | 是 | 脚本 |
| [].nodes[].node_type.oneOf[9].Wasm | array[object] | 是 | 脚本 |
| [].nodes[].node_type.oneOf[10] | string | 是 | end；可选值：None |
| [].save_mode | string | 是 | Data frame save mode；可选值：EveryTime、Once、Memory、Never |
| [].trigger_type | oneOf[object{SimpleRepeat} | object{TimeDrive} | object{EventDrive} | object{DataSource} | string] | 是 | Dataframe flow 启动的方式；可选值：Manual；可选结构：object{SimpleRepeat} | object{TimeDrive} | object{EventDrive} | object{DataSource} | string |
| [].trigger_type.oneOf[1] | object | 是 |  |
| [].trigger_type.oneOf[1].SimpleRepeat | object | 是 | 时间对象 |
| [].trigger_type.oneOf[1].SimpleRepeat.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| [].trigger_type.oneOf[1].SimpleRepeat.secs | integer | 是 | 秒；格式：int64 |
| [].trigger_type.oneOf[2] | object | 是 |  |
| [].trigger_type.oneOf[2].TimeDrive | string | 是 |  |
| [].trigger_type.oneOf[3] | object | 是 |  |
| [].trigger_type.oneOf[3].EventDrive | object | 是 | 表达式对象 |
| [].trigger_type.oneOf[3].EventDrive.rpn | array[Token] | 是 |  |
| [].trigger_type.oneOf[3].EventDrive.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[9] | object | 是 | A number. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[11] | object | 是 | A variable. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[12] | object | 是 |  |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[12].Str | string | 是 |  |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].trigger_type.oneOf[4] | object | 是 |  |
| [].trigger_type.oneOf[4].DataSource | array[integer] | 是 |  |
| [].trigger_type.oneOf[4].DataSource[] | integer | 是 | 格式：int64 |
| [].trigger_type.oneOf[5] | string | 是 | 可选值：Manual |


### 修改报表

- **方法**: `PUT`
- **路径**: `/flows/models`
- **工具名**: `update_flows_models`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].actions | array[DfActionEdge] | 是 | 边 |
| [].actions[] | object | 是 | 边 |
| [].actions[].action | oneOf[object{Eval} | object{Sql} | object{Onnx} | object{OnnxUrl} | object{Nnef} | object{NnefUrl} | object{WriteFile} | object{WriteSql} | string] | 是 | 可选值：None；可选结构：object{Eval} | object{Sql} | object{Onnx} | object{OnnxUrl} | object{Nnef} | object{NnefUrl} | object{WriteFile} | object{WriteSql} | string |
| [].actions[].action.oneOf[1] | object | 是 | 对单个Dataframe进行运算 |
| [].actions[].action.oneOf[1].Eval | array[Expr] | 是 | 对单个Dataframe进行运算 |
| [].actions[].action.oneOf[1].Eval[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[1].Eval[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[1].Eval[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[1].Eval[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[2] | object | 是 | 从DataFrame中进行sql查询 |
| [].actions[].action.oneOf[2].Sql | string | 是 | 从DataFrame中进行sql查询 |
| [].actions[].action.oneOf[3] | object | 是 | 用onnx表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[3].Onnx | array[integer] | 是 | 用onnx表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[3].Onnx[] | integer | 是 | 用onnx表达的神经网络对DataFrame进行运行；格式：int32 |
| [].actions[].action.oneOf[4] | object | 是 | 用onnx表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[4].OnnxUrl | string | 是 | 用onnx表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[5] | object | 是 | 用nnef表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[5].Nnef | array[integer] | 是 | 用nnef表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[5].Nnef[] | integer | 是 | 用nnef表达的神经网络对DataFrame进行运行；格式：int32 |
| [].actions[].action.oneOf[6] | object | 是 | 用nnef表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[6].NnefUrl | string | 是 | 用nnef表达的神经网络对DataFrame进行运行 |
| [].actions[].action.oneOf[7] | object | 是 | 写到文件 |
| [].actions[].action.oneOf[7].WriteFile | string | 是 | 写到文件 |
| [].actions[].action.oneOf[8] | object | 是 | 写到数据库 |
| [].actions[].action.oneOf[8].WriteSql | array[object] | 是 | 写到数据库 |
| [].actions[].action.oneOf[9] | string | 是 | 不做任何操作；可选值：None |
| [].actions[].desc | string | 是 |  |
| [].actions[].flow_id | integer | 是 | 格式：int64 |
| [].actions[].name | string | 是 |  |
| [].actions[].source_node | integer | 是 | 格式：int64 |
| [].actions[].target_node | integer | 是 | 格式：int64 |
| [].aoe_var | array[any] | 否 | destination of aoe variable；允许空值 |
| [].id | integer | 是 | dff id；格式：int64 |
| [].is_on | boolean | 是 | should schedule |
| [].name | string | 是 | dff name |
| [].nodes | array[DfNode] | 是 | 节点 |
| [].nodes[] | object | 是 | 节点 |
| [].nodes[].flow_id | integer | 是 | 格式：int64 |
| [].nodes[].id | integer | 是 | 格式：int64 |
| [].nodes[].name | string | 是 |  |
| [].nodes[].node_type | oneOf[object{Source} | object{Transform} | object{TensorEval} | object{Sql} | object{Solve} | string | object{MILP} | object{NLP} | object{Wasm}] | 是 | 可选值：NLSolve、None；可选结构：object{Source} | object{Transform} | object{TensorEval} | object{Sql} | object{Solve} | string | object{MILP} | object{NLP} | object{Wasm} |
| [].nodes[].node_type.oneOf[1] | object | 是 | query data source |
| [].nodes[].node_type.oneOf[1].Source | oneOf[object{Data} | object{File} | object{Url} | object{Image} | object{Sql} | object{OtherFlow} | object{Dev} | object{Points} | object{Meas} | object{Plan} | object{PointsEval} | object{MeasEval}] | 是 | query data source；可选结构：object{Data} | object{File} | object{Url} | object{Image} | object{Sql} | object{OtherFlow} | object{Dev} | object{Points} | object{Meas} | object{Plan} | object{PointsEval} | object{MeasEval} |
| [].nodes[].node_type.oneOf[1].Source.oneOf[1] | object | 是 | 直接导入数据 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[1].Data | string | 是 | 直接导入数据 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[2] | object | 是 | 根据文件后缀parquet/xlsx/csv自动判断，如果没有后缀默认用csv |
| [].nodes[].node_type.oneOf[1].Source.oneOf[2].File | string | 是 | 根据文件后缀parquet/xlsx/csv自动判断，如果没有后缀默认用csv |
| [].nodes[].node_type.oneOf[1].Source.oneOf[3] | object | 是 | 根据url后缀parquet/xlsx/csv自动判断，如果没有后缀默认用csv |
| [].nodes[].node_type.oneOf[1].Source.oneOf[3].Url | string | 是 | 根据url后缀parquet/xlsx/csv自动判断，如果没有后缀默认用csv |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4] | object | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image | object | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.color_type | string | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.filter_type | string | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.height | integer | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.is_url | boolean | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.url_or_path | string | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[4].Image.width | integer | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[5] | object | 是 | 数据库 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[5].Sql | array[object] | 是 | 数据库 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[6] | object | 是 | 其他Flow |
| [].nodes[].node_type.oneOf[1].Source.oneOf[6].OtherFlow | integer | 是 | 其他Flow；格式：int64 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[7] | object | 是 | 内置的设备列表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[7].Dev | string | 是 | 内置的设备列表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[8] | object | 是 | 内置的测点表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[8].Points | string | 是 | 内置的测点表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[9] | object | 是 | 内置的量测表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[9].Meas | array[string] | 是 | 内置的量测表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[10] | object | 是 | 计划数据表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[10].Plan | string | 是 | 计划数据表 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11] | object | 是 | 筛选测点，功能与DfSource::Points一样，参数是表达式而不是sql |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval | array[Expr] | 是 | 筛选测点，功能与DfSource::Points一样，参数是表达式而不是sql |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[] | object | 是 | 表达式对象 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn | array[Token] | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[9] | object | 是 | A number. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[12] | object | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[12].Str | string | 是 |  |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[11].PointsEval[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].nodes[].node_type.oneOf[1].Source.oneOf[12] | object | 是 | 筛选量测，功能与DfSource::Meas一样，参数是表达式而不是sql |
| [].nodes[].node_type.oneOf[1].Source.oneOf[12].MeasEval | array[object] | 是 | 筛选量测，功能与DfSource::Meas一样，参数是表达式而不是sql |
| [].nodes[].node_type.oneOf[2] | object | 是 | transformation |
| [].nodes[].node_type.oneOf[2].Transform | object | 是 | transformation |
| [].nodes[].node_type.oneOf[2].Transform.rpn | array[Token] | 是 |  |
| [].nodes[].node_type.oneOf[2].Transform.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[9] | object | 是 | A number. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[11] | object | 是 | A variable. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[12] | object | 是 |  |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[12].Str | string | 是 |  |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].nodes[].node_type.oneOf[2].Transform.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].nodes[].node_type.oneOf[3] | object | 是 | tensor eval script |
| [].nodes[].node_type.oneOf[3].TensorEval | array[object] | 是 | tensor eval script |
| [].nodes[].node_type.oneOf[4] | object | 是 | sql execute |
| [].nodes[].node_type.oneOf[4].Sql | string | 是 | sql execute |
| [].nodes[].node_type.oneOf[5] | object | 是 | linear equations |
| [].nodes[].node_type.oneOf[5].Solve | boolean | 是 | linear equations |
| [].nodes[].node_type.oneOf[6] | string | 是 | nonlinear equations；可选值：NLSolve |
| [].nodes[].node_type.oneOf[7] | object | 是 | mixed integer linear programming, objective function related DF name, constraint related DF name |
| [].nodes[].node_type.oneOf[7].MILP | array[object] | 是 | mixed integer linear programming, objective function related DF name, constraint related DF name |
| [].nodes[].node_type.oneOf[8] | object | 是 | nonlinear programming |
| [].nodes[].node_type.oneOf[8].NLP | array[string] | 是 | nonlinear programming |
| [].nodes[].node_type.oneOf[9] | object | 是 | 脚本 |
| [].nodes[].node_type.oneOf[9].Wasm | array[object] | 是 | 脚本 |
| [].nodes[].node_type.oneOf[10] | string | 是 | end；可选值：None |
| [].save_mode | string | 是 | Data frame save mode；可选值：EveryTime、Once、Memory、Never |
| [].trigger_type | oneOf[object{SimpleRepeat} | object{TimeDrive} | object{EventDrive} | object{DataSource} | string] | 是 | Dataframe flow 启动的方式；可选值：Manual；可选结构：object{SimpleRepeat} | object{TimeDrive} | object{EventDrive} | object{DataSource} | string |
| [].trigger_type.oneOf[1] | object | 是 |  |
| [].trigger_type.oneOf[1].SimpleRepeat | object | 是 | 时间对象 |
| [].trigger_type.oneOf[1].SimpleRepeat.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| [].trigger_type.oneOf[1].SimpleRepeat.secs | integer | 是 | 秒；格式：int64 |
| [].trigger_type.oneOf[2] | object | 是 |  |
| [].trigger_type.oneOf[2].TimeDrive | string | 是 |  |
| [].trigger_type.oneOf[3] | object | 是 |  |
| [].trigger_type.oneOf[3].EventDrive | object | 是 | 表达式对象 |
| [].trigger_type.oneOf[3].EventDrive.rpn | array[Token] | 是 |  |
| [].trigger_type.oneOf[3].EventDrive.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[9] | object | 是 | A number. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[11] | object | 是 | A variable. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[12] | object | 是 |  |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[12].Str | string | 是 |  |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].trigger_type.oneOf[3].EventDrive.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].trigger_type.oneOf[4] | object | 是 |  |
| [].trigger_type.oneOf[4].DataSource | array[integer] | 是 |  |
| [].trigger_type.oneOf[4].DataSource[] | integer | 是 | 格式：int64 |
| [].trigger_type.oneOf[5] | string | 是 | 可选值：Manual |


### 删除指定id的报表

- **方法**: `DELETE`
- **路径**: `/flows/models/{ids}`
- **工具名**: `delete_flows_models_by_s`
- **参数**:
  - `ids` (path, string, 必填): 报表id列表，以,间隔

### 新增报表（多文件形式）

- **方法**: `POST`
- **路径**: `/flows/models_file2`
- **工具名**: `add_flows_models_file2`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | array[string] | 是 |  |
| file[] | string | 是 | 格式：binary |


### 查询报表（自定义JSON格式）

- **方法**: `GET`
- **路径**: `/flows/models_json`
- **工具名**: `get_flows_models_json`
- **参数**:
  - `id` (query, integer, 可选): 测点id（优先）；元信息：format=int64, nullable=true
  - `ids` (query, string, 可选): 测点id列表，以,间隔；元信息：nullable=true

### 解析prog（多文件形式）

- **方法**: `POST`
- **路径**: `/flows/prog_file2`
- **工具名**: `add_flows_prog_file2`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | array[string] | 是 |  |
| file[] | string | 是 | 格式：binary |


### 重新加载报表

- **方法**: `POST`
- **路径**: `/flows/reload_dff/{flow_id}`
- **工具名**: `add_flows_reload_dff_by_flow`
- **参数**:
  - `flow_id` (path, string, 必填): 报表id

### 查询报表结果keys

- **方法**: `GET`
- **路径**: `/flows/result_keys`
- **工具名**: `get_flows_result_keys`
- **参数**:
  - `id` (query, integer, 可选): 测点id（优先）；元信息：format=int64, nullable=true
  - `ids` (query, string, 可选): 测点id列表，以,间隔；元信息：nullable=true

### 根据id查询报表执行结果

- **方法**: `GET`
- **路径**: `/flows/results`
- **工具名**: `get_flows_results`
- **参数**:
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 删除指定报表id指定key的报表结果

- **方法**: `DELETE`
- **路径**: `/flows/results`
- **工具名**: `delete_flows_results`
- **请求体**:

  - 无法解析请求体结构


### 重命名报表结果（简洁模式）

- **方法**: `POST`
- **路径**: `/flows/results/rename`
- **工具名**: `add_flows_results_rename`
- **请求体**:

  - 无法解析请求体结构


### query_flows_result_and_eval

- **方法**: `PUT`
- **路径**: `/flows/results/{id}/{key}`
- **工具名**: `update_flows_results_by_by_key`
- **参数**:
  - `id` (path, string, 必填): 报表id
  - `key` (path, string, 必填): key
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 表达式对象 |
| [].rpn | array[Token] | 是 |  |
| [].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].rpn[].oneOf[9] | object | 是 | A number. |
| [].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].rpn[].oneOf[11] | object | 是 | A variable. |
| [].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].rpn[].oneOf[12] | object | 是 |  |
| [].rpn[].oneOf[12].Str | string | 是 |  |
| [].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |


### query_flows_result_in_view

- **方法**: `GET`
- **路径**: `/flows/results/{id}/{key}/{view}`
- **工具名**: `get_flows_results_by_by_key_by_view`
- **参数**:
  - `id` (path, string, 必填): 报表id
  - `key` (path, string, 必填): key
  - `view` (path, string, 必填): view
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 表达式对象 |
| [].rpn | array[Token] | 是 |  |
| [].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].rpn[].oneOf[9] | object | 是 | A number. |
| [].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].rpn[].oneOf[11] | object | 是 | A variable. |
| [].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].rpn[].oneOf[12] | object | 是 |  |
| [].rpn[].oneOf[12].Str | string | 是 |  |
| [].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |


### 根据id查询报表执行结果（Parquet格式）

- **方法**: `GET`
- **路径**: `/flows/results_json`
- **工具名**: `get_flows_results_json`
- **参数**:
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 根据id查询报表执行结果（逐行写入方式）

- **方法**: `GET`
- **路径**: `/flows/results_json_rows`
- **工具名**: `get_flows_results_json_rows`
- **参数**:
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 查询运行中的报表

- **方法**: `GET`
- **路径**: `/flows/running`
- **工具名**: `get_flows_running`

### 查询报表（不包含Dataframe）

- **方法**: `GET`
- **路径**: `/flows/simple_models`
- **工具名**: `get_flows_simple_models`
- **参数**:
  - `id` (query, integer, 可选): 测点id（优先）；元信息：format=int64, nullable=true
  - `ids` (query, string, 可选): 测点id列表，以,间隔；元信息：nullable=true

### 查询未运行的报表

- **方法**: `GET`
- **路径**: `/flows/unrun`
- **工具名**: `get_flows_unrun`

### 查询报表展示模型

- **方法**: `GET`
- **路径**: `/flows/view`
- **工具名**: `get_flows_view`
- **参数**:
  - `id` (query, string, 可选): 展示模型id；元信息：nullable=true
  - `flow_id` (query, integer, 可选): 报表id；元信息：format=int64, nullable=true

### 新增报表展示模型

- **方法**: `POST`
- **路径**: `/flows/view`
- **工具名**: `add_flows_view`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | string | 是 |  |
| echart_js | string | 否 | 允许空值 |
| exprs | string | 是 |  |
| flow_id | integer | 是 | 格式：int64 |
| id | integer | 是 | 格式：int64 |
| is_show | boolean | 是 |  |
| layout | string | 是 |  |
| name | string | 是 |  |
| plot_template | string | 是 |  |
| plot_type | string | 是 | 可选值：Bar、BarPolar、Box、Candlestick、Contour、Carpet、Graph、Heatmap、Histogram、Histogram2d、Histogram2dContour、Indicator、IsoSurface、Mesh3d、Ohlc、Pie、Sankey、Scatter、Scatter3d、ScatterPolar、Sunburst、Surface、Table、Violin、EChart、Undefined |
| refresh_interval | integer | 否 | 格式：int32；允许空值 |
| series_style | string | 是 |  |


### 修改报表展示模型

- **方法**: `PUT`
- **路径**: `/flows/view`
- **工具名**: `update_flows_view`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | string | 是 |  |
| echart_js | string | 否 | 允许空值 |
| exprs | string | 是 |  |
| flow_id | integer | 是 | 格式：int64 |
| id | integer | 是 | 格式：int64 |
| is_show | boolean | 是 |  |
| layout | string | 是 |  |
| name | string | 是 |  |
| plot_template | string | 是 |  |
| plot_type | string | 是 | 可选值：Bar、BarPolar、Box、Candlestick、Contour、Carpet、Graph、Heatmap、Histogram、Histogram2d、Histogram2dContour、Indicator、IsoSurface、Mesh3d、Ohlc、Pie、Sankey、Scatter、Scatter3d、ScatterPolar、Sunburst、Surface、Table、Violin、EChart、Undefined |
| refresh_interval | integer | 否 | 格式：int32；允许空值 |
| series_style | string | 是 |  |


### 删除指定id的报表展示模型

- **方法**: `DELETE`
- **路径**: `/flows/view/{ids}`
- **工具名**: `delete_flows_view_by_s`
- **参数**:
  - `ids` (path, string, 必填): 报表展示模型id列表，以,间隔

### 加载其他mems来的Dataframe

- **方法**: `POST`
- **路径**: `/north/dataframe/{flow}/{node}`
- **工具名**: `add_north_dataframe_by_flow_by_node`
- **参数**:
  - `flow` (path, integer, 必填): 报表id；元信息：format=int64
  - `node` (path, integer, 必填): 节点id；元信息：format=int64
- **请求体**:

  - 无法解析请求体结构


### 重启北向服务

- **方法**: `POST`
- **路径**: `/north/restart`
- **工具名**: `add_north_restart`

***

## GRAPHS 模块

### 设置svg是否显示

- **方法**: `POST`
- **路径**: `/graphs/apply/additional`
- **工具名**: `add_graphs_apply_additional`
- **请求体**:

  - 无法解析请求体结构


### 获取应用版本某个名称的svg

- **方法**: `GET`
- **路径**: `/graphs/apply/models/{path}`
- **工具名**: `get_graphs_apply_models_by_path`
- **参数**:
  - `path` (path, string, 必填): svg名称

### 获取应用版本的所有svg名称

- **方法**: `GET`
- **路径**: `/graphs/apply/paths`
- **工具名**: `get_graphs_apply_paths`

### 应用一个svg版本

- **方法**: `POST`
- **路径**: `/graphs/apply/version`
- **工具名**: `add_graphs_apply_version`
- **请求体**:

  - 无法解析请求体结构


### 新增svg

- **方法**: `POST`
- **路径**: `/graphs/models`
- **工具名**: `add_graphs_models`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 |  |
| [].fileContent | array[integer] | 否 | 允许空值 |
| [].fileContent[] | integer | 是 | 格式：int32 |
| [].fileName | string | 否 | 允许空值 |
| [].is_zip | boolean | 否 | 允许空值 |
| [].op | oneOf[string] | 否 | 可选值：UPDATE、DELETE、RENAME；可选结构：string |
| [].op.oneOf[1] | string | 是 | 可选值：UPDATE、DELETE、RENAME |


### 根据path查询指定的svg内容

- **方法**: `GET`
- **路径**: `/graphs/models/{path}`
- **工具名**: `get_graphs_models_by_path`
- **参数**:
  - `path` (path, string, 必填): svg名称
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 删除指定名称的svg

- **方法**: `DELETE`
- **路径**: `/graphs/models/{path}`
- **工具名**: `delete_graphs_models_by_path`
- **参数**:
  - `path` (path, string, 必填): svg名称列表，以,间隔

### 查询所有svg的名称

- **方法**: `GET`
- **路径**: `/graphs/paths`
- **工具名**: `get_graphs_paths`
- **参数**:
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 查询所有的svg版本信息

- **方法**: `GET`
- **路径**: `/graphs/version`
- **工具名**: `get_graphs_version`

### 提交svg版本

- **方法**: `POST`
- **路径**: `/graphs/version`
- **工具名**: `add_graphs_version`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| note | string | 是 | 提交时的注释 |
| tree_id | string | 是 | 对应的tree_id |
| version | integer | 是 | 版本号；格式：int32 |


### 删除指定svg版本

- **方法**: `DELETE`
- **路径**: `/graphs/version/{v}`
- **工具名**: `delete_graphs_version_by_v`
- **参数**:
  - `v` (path, integer, 必填): 版本id；元信息：format=int32

***

## LCC 模块

### 查询指定lcc的告警通知配置信息

- **方法**: `GET`
- **路径**: `/lcc/alarm/config/{lcc_id}`
- **工具名**: `get_lcc_alarm_config_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id

### 配置指定lcc的告警通知格式

- **方法**: `POST`
- **路径**: `/lcc/alarm/config/{lcc_id}`
- **工具名**: `add_lcc_alarm_config_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| common | object | 是 | 普通 |
| common.popup_window | boolean | 是 | 桌面弹窗 |
| common.sound_light | boolean | 是 | 声光 |
| common.text_messages | boolean | 是 | 短信 |
| emergency | object | 是 | 紧急 |
| emergency.popup_window | boolean | 是 | 桌面弹窗 |
| emergency.sound_light | boolean | 是 | 声光 |
| emergency.text_messages | boolean | 是 | 短信 |
| important | object | 是 | 严重 |
| important.popup_window | boolean | 是 | 桌面弹窗 |
| important.sound_light | boolean | 是 | 声光 |
| important.text_messages | boolean | 是 | 短信 |


### 指定lcc确认告警

- **方法**: `POST`
- **路径**: `/lcc/alarm/confirm/{lcc_id}/{user_id}`
- **工具名**: `add_lcc_alarm_confirm_by_lcc_by_user`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `user_id` (path, integer, 必填): 用户id；元信息：format=int32
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | integer | 是 | 格式：int64 |


### 查询指定lcc的已确认告警

- **方法**: `GET`
- **路径**: `/lcc/alarm/confirm_status/{lcc_id}`
- **工具名**: `get_lcc_alarm_confirm_status_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id

### 查询指定lcc的告警总数

- **方法**: `GET`
- **路径**: `/lcc/alarm/count/{lcc_id}`
- **工具名**: `get_lcc_alarm_count_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id

### 上传指定lcc的单个告警定义

- **方法**: `POST`
- **路径**: `/lcc/alarm/define/{lcc_id}`
- **工具名**: `add_lcc_alarm_define_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 否 | 允许空值 |
| id | integer | 否 | 格式：int32；允许空值 |
| level | oneOf[string] | 否 | 可选值：Common、Important、Emergency；可选结构：string |
| level.oneOf[1] | string | 是 | 可选值：Common、Important、Emergency |
| name | string | 否 | 允许空值 |
| owners | string | 否 | 允许空值 |
| rule | string | 否 | 允许空值 |


### 查询指定lcc中指定id的告警定义

- **方法**: `GET`
- **路径**: `/lcc/alarm/define/{lcc_id}/{id}`
- **工具名**: `get_lcc_alarm_define_by_lcc_by`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `id` (path, integer, 必填): 告警id；元信息：format=int32

### 查询指定lcc的所有告警定义

- **方法**: `GET`
- **路径**: `/lcc/alarm/defines/{lcc_id}`
- **工具名**: `get_lcc_alarm_defines_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id

### 上传指定lcc的告警定义

- **方法**: `POST`
- **路径**: `/lcc/alarm/defines/{lcc_id}`
- **工具名**: `add_lcc_alarm_defines_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defines | array[PbAlarmDefine] | 是 |  |
| defines[] | object | 是 |  |
| defines[].desc | string | 否 | 允许空值 |
| defines[].id | integer | 否 | 格式：int32；允许空值 |
| defines[].level | oneOf[string] | 否 | 可选值：Common、Important、Emergency；可选结构：string |
| defines[].level.oneOf[1] | string | 是 | 可选值：Common、Important、Emergency |
| defines[].name | string | 否 | 允许空值 |
| defines[].owners | string | 否 | 允许空值 |
| defines[].rule | string | 否 | 允许空值 |


### 删除指定lcc的指定id们的告警定义

- **方法**: `DELETE`
- **路径**: `/lcc/alarm/defines/{lcc_id}/{ids}`
- **工具名**: `delete_lcc_alarm_defines_by_lcc_by_s`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `ids` (path, string, 必填): 告警定义id列表，以,间隔

### 查询指定lcc的未确认告警数

- **方法**: `GET`
- **路径**: `/lcc/alarm/unconfirmed_number/{lcc_id}`
- **工具名**: `get_lcc_alarm_unconfirmed_number_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id

### 查询指定lcc的未确认告警列表

- **方法**: `GET`
- **路径**: `/lcc/alarms/unconfirmed/{lcc_id}`
- **工具名**: `get_lcc_alarms_unconfirmed_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id

### 查询指定lcc的告警结果
查询告警，结果按照时间排序

- **方法**: `GET`
- **路径**: `/lcc/alarms/{lcc_id}`
- **工具名**: `get_lcc_alarms_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 导出指定lcc的所有模型字节数组

- **方法**: `GET`
- **路径**: `/lcc/allmodels_bytes/{lcc_id}`
- **工具名**: `get_lcc_allmodels_bytes_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `lang` (query, string, 必填): 语言

### 导入指定lcc的所有模型字节数组

- **方法**: `POST`
- **路径**: `/lcc/allmodels_bytes/{lcc_id}`
- **工具名**: `add_lcc_allmodels_bytes_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

  - 无法解析请求体结构


### 查询指定lcc的AOE执行结果

- **方法**: `GET`
- **路径**: `/lcc/aoe_results/{lcc_id}`
- **工具名**: `get_lcc_aoe_results_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 查询指定lcc的AOE

- **方法**: `GET`
- **路径**: `/lcc/aoes/models/{lcc_id}`
- **工具名**: `get_lcc_aoes_models_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `id` (query, string, 可选): aoe id列表，以,间隔；元信息：nullable=true

### 保存指定lcc的AOE

- **方法**: `POST`
- **路径**: `/lcc/aoes/models/{lcc_id}`
- **工具名**: `add_lcc_aoes_models_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | aoe模型 |
| [].actions | array[ActionEdge] | 是 | 动作列表 |
| [].actions[] | object | 是 | 边对象 |
| [].actions[].action | oneOf[string | object{SetPoints} | object{SetPointsWithCheck} | object{SetPoints2} | object{SetPointsWithCheck2} | object{Solve} | object{Nlsolve} | object{Milp} | object{SimpleMilp} | object{Nlp}] | 是 | 动作定义；可选值：None；可选结构：string | object{SetPoints} | object{SetPointsWithCheck} | object{SetPoints2} | object{SetPointsWithCheck2} | object{Solve} | object{Nlsolve} | object{Milp} | object{SimpleMilp} | object{Nlp} |
| [].actions[].action.oneOf[1] | string | 是 | 无动作；可选值：None |
| [].actions[].action.oneOf[2] | object | 是 | 设点动作 |
| [].actions[].action.oneOf[2].SetPoints | object | 是 | 设点动作 |
| [].actions[].action.oneOf[2].SetPoints.analog_id | array[string] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.analog_v | array[Expr] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.analog_v[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[2].SetPoints.discrete_id | array[string] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.discrete_v | array[Expr] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[3] | object | 是 | 设点动作 |
| [].actions[].action.oneOf[3].SetPointsWithCheck | object | 是 | 设点动作 |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_id | array[string] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v | array[Expr] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_id | array[string] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v | array[Expr] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[4] | object | 是 | 设点动作 |
| [].actions[].action.oneOf[4].SetPoints2 | object | 是 | 设点动作 |
| [].actions[].action.oneOf[4].SetPoints2.analogs | array[PointsToExp] | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.analogs[] | object | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr | object | 是 | 表达式 |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[4].SetPoints2.analogs[].ids | array[string] | 是 | id列表 |
| [].actions[].action.oneOf[4].SetPoints2.discretes | array[PointsToExp] | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.discretes[] | object | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr | object | 是 | 表达式 |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[4].SetPoints2.discretes[].ids | array[string] | 是 | id列表 |
| [].actions[].action.oneOf[5] | object | 是 | 设点动作 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2 | object | 是 | 设点动作 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs | array[PointsToExp] | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[] | object | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr | object | 是 | 表达式 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].ids | array[string] | 是 | id列表 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes | array[PointsToExp] | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[] | object | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr | object | 是 | 表达式 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].ids | array[string] | 是 | id列表 |
| [].actions[].action.oneOf[6] | object | 是 | 求方程 |
| [].actions[].action.oneOf[6].Solve | object | 是 | 求方程 |
| [].actions[].action.oneOf[6].Solve.a | object | 是 | A矩阵 |
| [].actions[].action.oneOf[6].Solve.a.m | integer | 是 | 行数 |
| [].actions[].action.oneOf[6].Solve.a.n | integer | 是 | 列数 |
| [].actions[].action.oneOf[6].Solve.a.v | array[array[any]] | 是 |  |
| [].actions[].action.oneOf[6].Solve.b | array[Expr] | 是 | b向量 |
| [].actions[].action.oneOf[6].Solve.b[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[6].Solve.b[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[6].Solve.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[6].Solve.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| [].actions[].action.oneOf[6].Solve.x_init | array[Expr] | 是 | 变量初始值 |
| [].actions[].action.oneOf[6].Solve.x_init[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[6].Solve.x_name | array[string] | 是 | 变量名称 |
| [].actions[].action.oneOf[7] | object | 是 | 求非线性方程组 |
| [].actions[].action.oneOf[7].Nlsolve | object | 是 | 求非线性方程组 |
| [].actions[].action.oneOf[7].Nlsolve.f | array[Expr] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.f[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.parameters | object[string, string] | 是 | 额外属性：string |
| [].actions[].action.oneOf[7].Nlsolve.x_init | array[Expr] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx | array[Expr] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[7].Nlsolve.x_name | array[string] | 是 |  |
| [].actions[].action.oneOf[8] | object | 是 | 混合整数线性规划稀疏表示 |
| [].actions[].action.oneOf[8].Milp | object | 是 | 混合整数线性规划稀疏表示 |
| [].actions[].action.oneOf[8].Milp.a | object | 是 | Ax >=/<= b |
| [].actions[].action.oneOf[8].Milp.a.m | integer | 是 | 行数 |
| [].actions[].action.oneOf[8].Milp.a.n | integer | 是 | 列数 |
| [].actions[].action.oneOf[8].Milp.a.v | array[array[any]] | 是 |  |
| [].actions[].action.oneOf[8].Milp.b | array[Expr] | 是 |  |
| [].actions[].action.oneOf[8].Milp.b[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[8].Milp.b[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[8].Milp.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[8].Milp.binary_int_float | array[integer] | 是 | 整数变量在x中的位置 |
| [].actions[].action.oneOf[8].Milp.binary_int_float[] | integer | 是 | 整数变量在x中的位置；格式：int32 |
| [].actions[].action.oneOf[8].Milp.c | array[array[any]] | 是 | min/max c^T*x |
| [].actions[].action.oneOf[8].Milp.constraint_type | array[Operation] | 是 |  |
| [].actions[].action.oneOf[8].Milp.constraint_type[] | string | 是 | Mathematical operations.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[8].Milp.min_or_max | boolean | 是 | min: true, max: false |
| [].actions[].action.oneOf[8].Milp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| [].actions[].action.oneOf[8].Milp.x_lower | array[array[any]] | 是 | 变量的下界约束：变量位置、约束表达式 |
| [].actions[].action.oneOf[8].Milp.x_name | array[string] | 是 | 变量名称 |
| [].actions[].action.oneOf[8].Milp.x_upper | array[array[any]] | 是 | 变量的上界约束：变量位置、约束表达式 |
| [].actions[].action.oneOf[9] | object | 是 | 混合整数线性规划稠密表示 |
| [].actions[].action.oneOf[9].SimpleMilp | object | 是 | 混合整数线性规划稠密表示 |
| [].actions[].action.oneOf[9].SimpleMilp.a | object | 是 | Ax >=/<= b |
| [].actions[].action.oneOf[9].SimpleMilp.a.m | integer | 是 | 行数 |
| [].actions[].action.oneOf[9].SimpleMilp.a.n | integer | 是 | 列数 |
| [].actions[].action.oneOf[9].SimpleMilp.a.v | array[Expr] | 是 | 值 |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.b | array[Expr] | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.b[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.binary_int_float | array[integer] | 是 | 整数变量在x中的位置 |
| [].actions[].action.oneOf[9].SimpleMilp.binary_int_float[] | integer | 是 | 整数变量在x中的位置；格式：int32 |
| [].actions[].action.oneOf[9].SimpleMilp.c | array[Expr] | 是 | min/max c^T*x |
| [].actions[].action.oneOf[9].SimpleMilp.c[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[9].SimpleMilp.constraint_type | array[Operation] | 是 |  |
| [].actions[].action.oneOf[9].SimpleMilp.constraint_type[] | string | 是 | Mathematical operations.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[9].SimpleMilp.min_or_max | boolean | 是 | min: true, max: false |
| [].actions[].action.oneOf[9].SimpleMilp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| [].actions[].action.oneOf[9].SimpleMilp.x_lower | array[array[any]] | 是 | 变量的下界约束：变量位置、约束表达式 |
| [].actions[].action.oneOf[9].SimpleMilp.x_name | array[string] | 是 | 变量名称 |
| [].actions[].action.oneOf[9].SimpleMilp.x_upper | array[array[any]] | 是 |  |
| [].actions[].action.oneOf[10] | object | 是 | 非整数线性规划 |
| [].actions[].action.oneOf[10].Nlp | object | 是 | 非整数线性规划 |
| [].actions[].action.oneOf[10].Nlp.g | array[Expr] | 是 | 等式约束式 g(x) == b |
| [].actions[].action.oneOf[10].Nlp.g[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.g[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.g_lower | array[Expr] | 是 | 不等式约束式 g(x) <= b |
| [].actions[].action.oneOf[10].Nlp.g_lower[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.g_upper | array[Expr] | 是 | 不等式约束式 g(x) >= b |
| [].actions[].action.oneOf[10].Nlp.g_upper[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.min_or_max | boolean | 是 | min: true, max: false |
| [].actions[].action.oneOf[10].Nlp.obj_expr | object | 是 | 目标函数表达式 min obj |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| [].actions[].action.oneOf[10].Nlp.x_init | array[Expr] | 是 | 变量初始值x0 |
| [].actions[].action.oneOf[10].Nlp.x_init[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.x_lower | array[Expr] | 是 | 整数变量在x中的位置 |
| [].actions[].action.oneOf[10].Nlp.x_lower[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.x_name | array[string] | 是 | 变量名称 |
| [].actions[].action.oneOf[10].Nlp.x_upper | array[Expr] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_upper[] | object | 是 | 表达式对象 |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn | array[Token] | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[9] | object | 是 | A number. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[10] | object | 是 | A tensor. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[11] | object | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[12] | object | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[12].Str | string | 是 |  |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].actions[].aoe_id | integer | 是 | AOE id；格式：int64 |
| [].actions[].failure_mode | string | 是 | action失败时的处理方式；可选值：Default、Ignore、StopAll、StopFailed |
| [].actions[].name | string | 是 | 动作名称 |
| [].actions[].source_node | integer | 是 | 源节点；格式：int64 |
| [].actions[].target_node | integer | 是 | 目标节点；格式：int64 |
| [].events | array[EventNode] | 是 | 节点列表 |
| [].events[] | object | 是 | 节点对象 |
| [].events[].aoe_id | integer | 是 | AOE id；格式：int64 |
| [].events[].expr | object | 是 | 事件是否发生判断的bool表达式 |
| [].events[].expr.rpn | array[Token] | 是 |  |
| [].events[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| [].events[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| [].events[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].events[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| [].events[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| [].events[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| [].events[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| [].events[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| [].events[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| [].events[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| [].events[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| [].events[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| [].events[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| [].events[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| [].events[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| [].events[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| [].events[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| [].events[].expr.rpn[].oneOf[12] | object | 是 |  |
| [].events[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| [].events[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| [].events[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| [].events[].id | integer | 是 | 节点id；格式：int64 |
| [].events[].name | string | 是 | 节点名 |
| [].events[].node_type | string | 是 | 节点类型；可选值：ConditionNode、SwitchNode、SwitchOfActionResult |
| [].events[].timeout | integer | 是 | 事件还未发生时等待超时时间；格式：int64 |
| [].id | integer | 是 | aoe id；格式：int64 |
| [].name | string | 是 | aoe名称 |
| [].trigger_type | oneOf[object{SimpleRepeat} | object{TimeDrive} | string | object{EventRepeatMix} | object{EventTimeMix}] | 是 | 触发类型；可选值：EventDrive；可选结构：object{SimpleRepeat} | object{TimeDrive} | string | object{EventRepeatMix} | object{EventTimeMix} |
| [].trigger_type.oneOf[1] | object | 是 | 简单固定周期触发 |
| [].trigger_type.oneOf[1].SimpleRepeat | object | 是 | 简单固定周期触发 |
| [].trigger_type.oneOf[1].SimpleRepeat.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| [].trigger_type.oneOf[1].SimpleRepeat.secs | integer | 是 | 秒；格式：int64 |
| [].trigger_type.oneOf[2] | object | 是 | cron表达式 |
| [].trigger_type.oneOf[2].TimeDrive | string | 是 | cron表达式 |
| [].trigger_type.oneOf[3] | string | 是 | 事件驱动，AOE开始节点条件满足即触发；可选值：EventDrive |
| [].trigger_type.oneOf[4] | object | 是 | 事件驱动 && 简单固定周期 联合 |
| [].trigger_type.oneOf[4].EventRepeatMix | object | 是 | 事件驱动 && 简单固定周期 联合 |
| [].trigger_type.oneOf[4].EventRepeatMix.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| [].trigger_type.oneOf[4].EventRepeatMix.secs | integer | 是 | 秒；格式：int64 |
| [].trigger_type.oneOf[5] | object | 是 | 事件驱动 && cron表达式 联合 |
| [].trigger_type.oneOf[5].EventTimeMix | string | 是 | 事件驱动 && cron表达式 联合 |
| [].variables | array[array[any]] | 是 | 用户自定义的变量：变量名和表达式 |


### 删除指定lcc指定id的AOE

- **方法**: `DELETE`
- **路径**: `/lcc/aoes/models/{lcc_id}/{ids}`
- **工具名**: `delete_lcc_aoes_models_by_lcc_by_s`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `ids` (path, string, 必填): AOE_id列表，以,间隔

### 查询指定lcc的所有用户

- **方法**: `GET`
- **路径**: `/lcc/auth/users/{lcc_id}`
- **工具名**: `get_lcc_auth_users_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id

### 查询指定lcc的历史设点执行结果

- **方法**: `GET`
- **路径**: `/lcc/commands/{lcc_id}`
- **工具名**: `get_lcc_commands_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `sender_id` (query, integer, 可选): 元信息：format=int64, nullable=true
  - `point_id` (query, integer, 可选): 测点id；元信息：format=int64, nullable=true
  - `start` (query, integer, 可选): 开始时间；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 执行指定lcc的map映射操作

- **方法**: `POST`
- **路径**: `/lcc/common_map/{lcc_id}`
- **工具名**: `add_lcc_common_map_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oneOf[1] | object | 是 | 查询 |
| oneOf[1].Query | array[integer] | 是 | 查询 |
| oneOf[1].Query[] | integer | 是 | 查询；格式：int32 |
| oneOf[2] | object | 是 | 增加 |
| oneOf[2].Update | array[array[integer]] | 是 | 增加 |
| oneOf[2].Update[] | array[integer] | 是 | 增加 |
| oneOf[2].Update[][] | integer | 是 | 增加；格式：int32 |
| oneOf[3] | object | 是 |  |
| oneOf[3].Update2 | array[array[integer]] | 是 |  |
| oneOf[3].Update2[] | array[integer] | 是 |  |
| oneOf[3].Update2[][] | integer | 是 | 格式：int32 |
| oneOf[4] | object | 是 | 删除 |
| oneOf[4].Delete | array[integer] | 是 | 删除 |
| oneOf[4].Delete[] | integer | 是 | 删除；格式：int32 |


### 查询指定lcc的配置

- **方法**: `GET`
- **路径**: `/lcc/config/{lcc_id}`
- **工具名**: `get_lcc_config_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id

### 保存指定lcc的配置

- **方法**: `POST`
- **路径**: `/lcc/config/{lcc_id}`
- **工具名**: `add_lcc_config_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| properties | object[string, string] | 是 | 主要配置属性；额外属性：string |
| properties2 | object[string, string] | 是 | 次要配置属性；额外属性：string |


### 执行Lcc操作

- **方法**: `POST`
- **路径**: `/lcc/controls/{lcc_id}`
- **工具名**: `add_lcc_controls_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oneOf[1] | string | 是 | 强制退出；可选值：QuitForce |
| oneOf[2] | string | 是 | 重启；可选值：Restart |
| oneOf[3] | string | 是 | 重置；可选值：Reset |
| oneOf[4] | string | 是 | 可选值：Recover |
| oneOf[5] | object | 是 | 控制AOE启动，停止或更新 |
| oneOf[5].AoeControl | object | 是 | 控制AOE启动，停止或更新 |
| oneOf[5].AoeControl.AoeActions | array[AoeAction] | 是 | AOE指令列表 |
| oneOf[5].AoeControl.AoeActions[] | oneOf[object{StartAoe} | object{StopAoe} | object{UpdateAoe} | object{UpdateAoeCsv}] | 是 | AOE指令对象；可选结构：object{StartAoe} | object{StopAoe} | object{UpdateAoe} | object{UpdateAoeCsv} |
| oneOf[5].AoeControl.AoeActions[].oneOf[1] | object | 是 | 开始AOE |
| oneOf[5].AoeControl.AoeActions[].oneOf[1].StartAoe | integer | 是 | 开始AOE；格式：int64 |
| oneOf[5].AoeControl.AoeActions[].oneOf[2] | object | 是 | 停止AOE |
| oneOf[5].AoeControl.AoeActions[].oneOf[2].StopAoe | integer | 是 | 停止AOE；格式：int64 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3] | object | 是 | 更新AOE |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe | object | 是 | 更新AOE |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions | array[ActionEdge] | 是 | 动作列表 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[] | object | 是 | 边对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action | oneOf[string | object{SetPoints} | object{SetPointsWithCheck} | object{SetPoints2} | object{SetPointsWithCheck2} | object{Solve} | object{Nlsolve} | object{Milp} | object{SimpleMilp} | object{Nlp}] | 是 | 动作定义；可选值：None；可选结构：string | object{SetPoints} | object{SetPointsWithCheck} | object{SetPoints2} | object{SetPointsWithCheck2} | object{Solve} | object{Nlsolve} | object{Milp} | object{SimpleMilp} | object{Nlp} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[1] | string | 是 | 无动作；可选值：None |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2] | object | 是 | 设点动作 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints | object | 是 | 设点动作 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_id | array[string] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v | array[Expr] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_id | array[string] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v | array[Expr] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3] | object | 是 | 设点动作 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck | object | 是 | 设点动作 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_id | array[string] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v | array[Expr] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_id | array[string] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v | array[Expr] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4] | object | 是 | 设点动作 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2 | object | 是 | 设点动作 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs | array[PointsToExp] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr | object | 是 | 表达式 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.analogs[].ids | array[string] | 是 | id列表 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes | array[PointsToExp] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr | object | 是 | 表达式 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[4].SetPoints2.discretes[].ids | array[string] | 是 | id列表 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5] | object | 是 | 设点动作 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2 | object | 是 | 设点动作 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs | array[PointsToExp] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr | object | 是 | 表达式 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].ids | array[string] | 是 | id列表 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes | array[PointsToExp] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr | object | 是 | 表达式 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].ids | array[string] | 是 | id列表 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6] | object | 是 | 求方程 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve | object | 是 | 求方程 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.a | object | 是 | A矩阵 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.a.m | integer | 是 | 行数 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.a.n | integer | 是 | 列数 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.a.v | array[array[any]] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b | array[Expr] | 是 | b向量 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init | array[Expr] | 是 | 变量初始值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[6].Solve.x_name | array[string] | 是 | 变量名称 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7] | object | 是 | 求非线性方程组 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve | object | 是 | 求非线性方程组 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f | array[Expr] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.parameters | object[string, string] | 是 | 额外属性：string |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init | array[Expr] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx | array[Expr] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[7].Nlsolve.x_name | array[string] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8] | object | 是 | 混合整数线性规划稀疏表示 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp | object | 是 | 混合整数线性规划稀疏表示 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.a | object | 是 | Ax >=/<= b |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.a.m | integer | 是 | 行数 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.a.n | integer | 是 | 列数 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.a.v | array[array[any]] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b | array[Expr] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.binary_int_float | array[integer] | 是 | 整数变量在x中的位置 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.binary_int_float[] | integer | 是 | 整数变量在x中的位置；格式：int32 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.c | array[array[any]] | 是 | min/max c^T*x |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.constraint_type | array[Operation] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.constraint_type[] | string | 是 | Mathematical operations.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.min_or_max | boolean | 是 | min: true, max: false |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.x_lower | array[array[any]] | 是 | 变量的下界约束：变量位置、约束表达式 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.x_name | array[string] | 是 | 变量名称 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[8].Milp.x_upper | array[array[any]] | 是 | 变量的上界约束：变量位置、约束表达式 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9] | object | 是 | 混合整数线性规划稠密表示 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp | object | 是 | 混合整数线性规划稠密表示 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a | object | 是 | Ax >=/<= b |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.m | integer | 是 | 行数 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.n | integer | 是 | 列数 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v | array[Expr] | 是 | 值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b | array[Expr] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.binary_int_float | array[integer] | 是 | 整数变量在x中的位置 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.binary_int_float[] | integer | 是 | 整数变量在x中的位置；格式：int32 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c | array[Expr] | 是 | min/max c^T*x |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.constraint_type | array[Operation] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.constraint_type[] | string | 是 | Mathematical operations.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.min_or_max | boolean | 是 | min: true, max: false |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.x_lower | array[array[any]] | 是 | 变量的下界约束：变量位置、约束表达式 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.x_name | array[string] | 是 | 变量名称 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[9].SimpleMilp.x_upper | array[array[any]] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10] | object | 是 | 非整数线性规划 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp | object | 是 | 非整数线性规划 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g | array[Expr] | 是 | 等式约束式 g(x) == b |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower | array[Expr] | 是 | 不等式约束式 g(x) <= b |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper | array[Expr] | 是 | 不等式约束式 g(x) >= b |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.min_or_max | boolean | 是 | min: true, max: false |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr | object | 是 | 目标函数表达式 min obj |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init | array[Expr] | 是 | 变量初始值x0 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower | array[Expr] | 是 | 整数变量在x中的位置 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_name | array[string] | 是 | 变量名称 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper | array[Expr] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[] | object | 是 | 表达式对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].aoe_id | integer | 是 | AOE id；格式：int64 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].failure_mode | string | 是 | action失败时的处理方式；可选值：Default、Ignore、StopAll、StopFailed |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].name | string | 是 | 动作名称 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].source_node | integer | 是 | 源节点；格式：int64 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.actions[].target_node | integer | 是 | 目标节点；格式：int64 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events | array[EventNode] | 是 | 节点列表 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[] | object | 是 | 节点对象 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].aoe_id | integer | 是 | AOE id；格式：int64 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr | object | 是 | 事件是否发生判断的bool表达式 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn | array[Token] | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[12] | object | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].id | integer | 是 | 节点id；格式：int64 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].name | string | 是 | 节点名 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].node_type | string | 是 | 节点类型；可选值：ConditionNode、SwitchNode、SwitchOfActionResult |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.events[].timeout | integer | 是 | 事件还未发生时等待超时时间；格式：int64 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.id | integer | 是 | aoe id；格式：int64 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.name | string | 是 | aoe名称 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type | oneOf[object{SimpleRepeat} | object{TimeDrive} | string | object{EventRepeatMix} | object{EventTimeMix}] | 是 | 触发类型；可选值：EventDrive；可选结构：object{SimpleRepeat} | object{TimeDrive} | string | object{EventRepeatMix} | object{EventTimeMix} |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[1] | object | 是 | 简单固定周期触发 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[1].SimpleRepeat | object | 是 | 简单固定周期触发 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[1].SimpleRepeat.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[1].SimpleRepeat.secs | integer | 是 | 秒；格式：int64 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[2] | object | 是 | cron表达式 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[2].TimeDrive | string | 是 | cron表达式 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[3] | string | 是 | 事件驱动，AOE开始节点条件满足即触发；可选值：EventDrive |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[4] | object | 是 | 事件驱动 && 简单固定周期 联合 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[4].EventRepeatMix | object | 是 | 事件驱动 && 简单固定周期 联合 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[4].EventRepeatMix.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[4].EventRepeatMix.secs | integer | 是 | 秒；格式：int64 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[5] | object | 是 | 事件驱动 && cron表达式 联合 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.trigger_type.oneOf[5].EventTimeMix | string | 是 | 事件驱动 && cron表达式 联合 |
| oneOf[5].AoeControl.AoeActions[].oneOf[3].UpdateAoe.variables | array[array[any]] | 是 | 用户自定义的变量：变量名和表达式 |
| oneOf[5].AoeControl.AoeActions[].oneOf[4] | object | 是 | 更新AOE（字节数组） |
| oneOf[5].AoeControl.AoeActions[].oneOf[4].UpdateAoeCsv | array[integer] | 是 | 更新AOE（字节数组） |
| oneOf[5].AoeControl.AoeActions[].oneOf[4].UpdateAoeCsv[] | integer | 是 | 更新AOE（字节数组）；格式：int32 |
| oneOf[6] | object | 是 | 设置测点 |
| oneOf[6].PointControl | object | 是 | 设置测点 |
| oneOf[6].PointControl.analogs | array[SetFloatValue] | 是 |  |
| oneOf[6].PointControl.analogs[] | object | 是 | 浮点型指令数据 |
| oneOf[6].PointControl.analogs[].point_id | integer | 是 | 格式：int64 |
| oneOf[6].PointControl.analogs[].sender_id | integer | 是 | 格式：int64 |
| oneOf[6].PointControl.analogs[].timestamp | integer | 是 | 格式：int64 |
| oneOf[6].PointControl.analogs[].yt_command | number | 是 | 格式：double |
| oneOf[6].PointControl.discretes | array[SetIntValue] | 是 |  |
| oneOf[6].PointControl.discretes[] | object | 是 | 整型指令数据 |
| oneOf[6].PointControl.discretes[].point_id | integer | 是 | 格式：int64 |
| oneOf[6].PointControl.discretes[].sender_id | integer | 是 | 格式：int64 |
| oneOf[6].PointControl.discretes[].timestamp | integer | 是 | 格式：int64 |
| oneOf[6].PointControl.discretes[].yk_command | integer | 是 | 格式：int64 |


### 查询指定lcc的日志

- **方法**: `GET`
- **路径**: `/lcc/logs_bytes/{lcc_id}`
- **工具名**: `get_lcc_logs_bytes_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `is_query_size` (query, boolean, 可选): 是否限制文件大小；元信息：nullable=true

### 查询指定lcc的历史量测

- **方法**: `GET`
- **路径**: `/lcc/measures/{lcc_id}`
- **工具名**: `get_lcc_measures_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 加载LCC的测点到base服务

- **方法**: `POST`
- **路径**: `/lcc/points/import_str/{lcc_id}`
- **工具名**: `add_lcc_points_import_str_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

  - 无法解析请求体结构


### 查询指定lcc的测点信息

- **方法**: `GET`
- **路径**: `/lcc/points/models/{lcc_id}`
- **工具名**: `get_lcc_points_models_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `id` (query, string, 可选): 元信息：nullable=true
  - `name` (query, string, 可选): 元信息：nullable=true
  - `is_soe` (query, boolean, 可选): 元信息：nullable=true

### 保存指定lcc的测点信息

- **方法**: `POST`
- **路径**: `/lcc/points/models/{lcc_id}`
- **工具名**: `add_lcc_points_models_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 测点对象 |
| [].alarm_level1_expr | string | 是 | 告警级别1的表达式 |
| [].alarm_level2_expr | string | 是 | 告警级别2的表达式 |
| [].alias_id | string | 是 | 字符串id |
| [].change_expr | string | 是 | 判断是否"变化"的公式，用于变化上传或储存 |
| [].data_unit | string | 是 | 单位 |
| [].desc | string | 是 | Description |
| [].expression | string | 是 | 如果是计算点，这是表达式 |
| [].init_value | integer | 是 | 默认值存储在8个字节，需要根据is_discrete来转换成具体的值；格式：int64 |
| [].inv_trans_expr | string | 是 | 逆变换公式 |
| [].is_computing_point | boolean | 是 | 是否是计算点 |
| [].is_discrete | boolean | 是 | 是否是离散量 |
| [].is_realtime | boolean | 是 | 如是，则不判断是否"变化"，均上传 |
| [].is_soe | boolean | 是 | 是否是soe点 |
| [].lower_limit | number | 是 | 下限，用于坏数据辨识；格式：double |
| [].point_id | integer | 是 | 唯一的id；格式：int64 |
| [].point_name | string | 是 | 测点名 |
| [].trans_expr | string | 是 | 变换公式 |
| [].upper_limit | number | 是 | 上限，用于坏数据辨识；格式：double |
| [].zero_expr | string | 是 | 判断是否为0值的公式 |


### 删除指定lcc的测点

- **方法**: `DELETE`
- **路径**: `/lcc/points/models/{lcc_id}`
- **工具名**: `delete_lcc_points_models_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | integer | 是 | 格式：int64 |


### 查询指定lcc运行中的AOE

- **方法**: `GET`
- **路径**: `/lcc/running_aoes/{lcc_id}`
- **工具名**: `get_lcc_running_aoes_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id

### 查询指定lcc的SOE

- **方法**: `GET`
- **路径**: `/lcc/soes/{lcc_id}`
- **工具名**: `get_lcc_soes_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 查询指定lcc指定分组的标签名称及id列表

- **方法**: `GET`
- **路径**: `/lcc/tag_defines/{lcc_id}/{group}`
- **工具名**: `get_lcc_tag_defines_by_lcc_by_group`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `group` (path, integer, 必填): 分组id；元信息：format=int32

### 查询指定lcc指定分组下标签id对应的测点数组

- **方法**: `POST`
- **路径**: `/lcc/tags/{lcc_id}/{group}`
- **工具名**: `add_lcc_tags_by_lcc_by_group`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `group` (path, integer, 必填): 分组id；元信息：format=int32
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | integer | 是 | 格式：int32 |


### 更新指定lcc指定分组下标签名和测点数组关系

- **方法**: `PUT`
- **路径**: `/lcc/tags/{lcc_id}/{group}`
- **工具名**: `update_lcc_tags_by_lcc_by_group`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `group` (path, integer, 必填): 分组id；元信息：format=int32
- **请求体**:

  - 无法解析请求体结构


### 删除指定lcc指定分组下标签id和测点的关系

- **方法**: `DELETE`
- **路径**: `/lcc/tags/{lcc_id}/{group}`
- **工具名**: `delete_lcc_tags_by_lcc_by_group`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `group` (path, integer, 必填): 分组id；元信息：format=int32
- **请求体**:

  - 无法解析请求体结构


### 查询指定lcc的通道信息

- **方法**: `GET`
- **路径**: `/lcc/transports/models/{lcc_id}`
- **工具名**: `get_lcc_transports_models_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `id` (query, string, 可选): 通道id列表，以,间隔；元信息：nullable=true
  - `transport_type` (query, string, 可选): 通道类型；元信息：oneOf=TransportType；可选结构：TransportType

### 保存指定lcc的通道信息

- **方法**: `POST`
- **路径**: `/lcc/transports/models/{lcc_id}`
- **工具名**: `add_lcc_transports_models_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | oneOf[object{MbcTcp} | object{MbdTcp} | object{MbcRtu} | object{MbdRtu} | object{DLT645c} | object{Mqtt} | object{Iec104c} | object{Iec104d} | object{HYMqtt} | object{EtherCAT} | object{MemoryPosix} | object{MemorySystemV} | object{OpcuaClient} | object{OpcuaServer}] | 是 | 通道对象；可选结构：object{MbcTcp} | object{MbdTcp} | object{MbcRtu} | object{MbdRtu} | object{DLT645c} | object{Mqtt} | object{Iec104c} | object{Iec104d} | object{HYMqtt} | object{EtherCAT} | object{MemoryPosix} | object{MemorySystemV} | object{OpcuaClient} | object{OpcuaServer} |
| [].oneOf[1] | object | 是 |  |
| [].oneOf[1].MbcTcp | object | 是 | ModbusTcp客户端通道信息 |
| [].oneOf[1].MbcTcp.connections | array[MbConnection] | 是 | Modbus通道连接信息 |
| [].oneOf[1].MbcTcp.connections[] | object | 是 | Modbus通道连接信息 |
| [].oneOf[1].MbcTcp.connections[].coil_write_code | integer | 否 | 格式：int32；允许空值 |
| [].oneOf[1].MbcTcp.connections[].default_polling_period_in_milli | integer | 是 | 格式：int64 |
| [].oneOf[1].MbcTcp.connections[].delay_between_requests | integer | 是 | 两条请求直接的间隔；格式：int64 |
| [].oneOf[1].MbcTcp.connections[].holding_write_code | integer | 否 | 格式：int32；允许空值 |
| [].oneOf[1].MbcTcp.connections[].max_read_bit_count | integer | 是 | 格式：int32 |
| [].oneOf[1].MbcTcp.connections[].max_read_register_count | integer | 是 | 格式：int32 |
| [].oneOf[1].MbcTcp.connections[].max_write_bit_count | integer | 是 | 格式：int32 |
| [].oneOf[1].MbcTcp.connections[].max_write_register_count | integer | 是 | 格式：int32 |
| [].oneOf[1].MbcTcp.connections[].mb_data_configure | array[RegisterData] | 是 | register settings |
| [].oneOf[1].MbcTcp.connections[].mb_data_configure[] | object | 是 | Dlt645注册信息 |
| [].oneOf[1].MbcTcp.connections[].mb_data_configure[].data_id | integer | 是 | 数据标识；格式：int32 |
| [].oneOf[1].MbcTcp.connections[].mb_data_configure[].point_ids | array[integer] | 是 | 对应的测点Id |
| [].oneOf[1].MbcTcp.connections[].mb_data_configure[].point_ids[] | integer | 是 | 对应的测点Id；格式：int64 |
| [].oneOf[1].MbcTcp.connections[].mb_data_configure[].polling_period_in_milli | integer | 是 | 轮询周期，毫秒；格式：int64 |
| [].oneOf[1].MbcTcp.connections[].name | string | 是 |  |
| [].oneOf[1].MbcTcp.connections[].point_id | integer | 是 | 通道状态对应的测点号；格式：int64 |
| [].oneOf[1].MbcTcp.connections[].point_id_to_rd | object[string, integer] | 是 | key is point id, value is position of register data；额外属性：integer |
| [].oneOf[1].MbcTcp.connections[].polling_period_to_data | object[string, array[integer]] | 是 | 轮询周期不同的数据, key is period in milli, value is position.；额外属性：array[integer] |
| [].oneOf[1].MbcTcp.connections[].protocol_type | string | 是 | 协议类型；可选值：ENCAP、XA、RTU |
| [].oneOf[1].MbcTcp.connections[].register_addr_to_rd | object[string, integer] | 是 | key:寄存器地址,value:setting中vec<RegisterData>的位置；额外属性：integer |
| [].oneOf[1].MbcTcp.connections[].slave_id | integer | 是 | 格式：int32 |
| [].oneOf[1].MbcTcp.connections[].timeout_in_milli | integer | 是 | 超时设置；格式：int64 |
| [].oneOf[1].MbcTcp.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[1].MbcTcp.name | string | 是 | 通道名称 |
| [].oneOf[1].MbcTcp.tcp_server | array[any] | 是 | 服务端的ip和port |
| [].oneOf[2] | object | 是 |  |
| [].oneOf[2].MbdTcp | object | 是 | ModbusTcp服务端通道信息 |
| [].oneOf[2].MbdTcp.connections | array[array[any]] | 是 | 通道连接信息 |
| [].oneOf[2].MbdTcp.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[2].MbdTcp.name | string | 是 | 通道名称 |
| [].oneOf[2].MbdTcp.tcp_server_port | integer | 是 | 服务的port；格式：int32 |
| [].oneOf[3] | object | 是 |  |
| [].oneOf[3].MbcRtu | object | 是 | ModbusRtu客户端通道信息 |
| [].oneOf[3].MbcRtu.connections | array[MbConnection] | 是 | 通道连接信息 |
| [].oneOf[3].MbcRtu.connections[] | object | 是 | Modbus通道连接信息 |
| [].oneOf[3].MbcRtu.connections[].coil_write_code | integer | 否 | 格式：int32；允许空值 |
| [].oneOf[3].MbcRtu.connections[].default_polling_period_in_milli | integer | 是 | 格式：int64 |
| [].oneOf[3].MbcRtu.connections[].delay_between_requests | integer | 是 | 两条请求直接的间隔；格式：int64 |
| [].oneOf[3].MbcRtu.connections[].holding_write_code | integer | 否 | 格式：int32；允许空值 |
| [].oneOf[3].MbcRtu.connections[].max_read_bit_count | integer | 是 | 格式：int32 |
| [].oneOf[3].MbcRtu.connections[].max_read_register_count | integer | 是 | 格式：int32 |
| [].oneOf[3].MbcRtu.connections[].max_write_bit_count | integer | 是 | 格式：int32 |
| [].oneOf[3].MbcRtu.connections[].max_write_register_count | integer | 是 | 格式：int32 |
| [].oneOf[3].MbcRtu.connections[].mb_data_configure | array[RegisterData] | 是 | register settings |
| [].oneOf[3].MbcRtu.connections[].mb_data_configure[] | object | 是 | Dlt645注册信息 |
| [].oneOf[3].MbcRtu.connections[].mb_data_configure[].data_id | integer | 是 | 数据标识；格式：int32 |
| [].oneOf[3].MbcRtu.connections[].mb_data_configure[].point_ids | array[integer] | 是 | 对应的测点Id |
| [].oneOf[3].MbcRtu.connections[].mb_data_configure[].point_ids[] | integer | 是 | 对应的测点Id；格式：int64 |
| [].oneOf[3].MbcRtu.connections[].mb_data_configure[].polling_period_in_milli | integer | 是 | 轮询周期，毫秒；格式：int64 |
| [].oneOf[3].MbcRtu.connections[].name | string | 是 |  |
| [].oneOf[3].MbcRtu.connections[].point_id | integer | 是 | 通道状态对应的测点号；格式：int64 |
| [].oneOf[3].MbcRtu.connections[].point_id_to_rd | object[string, integer] | 是 | key is point id, value is position of register data；额外属性：integer |
| [].oneOf[3].MbcRtu.connections[].polling_period_to_data | object[string, array[integer]] | 是 | 轮询周期不同的数据, key is period in milli, value is position.；额外属性：array[integer] |
| [].oneOf[3].MbcRtu.connections[].protocol_type | string | 是 | 协议类型；可选值：ENCAP、XA、RTU |
| [].oneOf[3].MbcRtu.connections[].register_addr_to_rd | object[string, integer] | 是 | key:寄存器地址,value:setting中vec<RegisterData>的位置；额外属性：integer |
| [].oneOf[3].MbcRtu.connections[].slave_id | integer | 是 | 格式：int32 |
| [].oneOf[3].MbcRtu.connections[].timeout_in_milli | integer | 是 | 超时设置；格式：int64 |
| [].oneOf[3].MbcRtu.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[3].MbcRtu.name | string | 是 | 通道名称 |
| [].oneOf[3].MbcRtu.para | object | 是 | 串口参数 |
| [].oneOf[3].MbcRtu.para.baud_rate | integer | 是 | 格式：int32 |
| [].oneOf[3].MbcRtu.para.data_bits | integer | 是 | 格式：int32 |
| [].oneOf[3].MbcRtu.para.delay_between_requests | integer | 是 | 格式：int64 |
| [].oneOf[3].MbcRtu.para.file_path | string | 是 |  |
| [].oneOf[3].MbcRtu.para.parity | string | 是 | 奇偶校验位；可选值：None、Odd、Even、Mark、Space |
| [].oneOf[3].MbcRtu.para.stop_bits | integer | 是 | 格式：int32 |
| [].oneOf[4] | object | 是 |  |
| [].oneOf[4].MbdRtu | object | 是 | ModbusRtu服务端通道信息 |
| [].oneOf[4].MbdRtu.connections | array[MbConnection] | 是 | 通道连接信息 |
| [].oneOf[4].MbdRtu.connections[] | object | 是 | Modbus通道连接信息 |
| [].oneOf[4].MbdRtu.connections[].coil_write_code | integer | 否 | 格式：int32；允许空值 |
| [].oneOf[4].MbdRtu.connections[].default_polling_period_in_milli | integer | 是 | 格式：int64 |
| [].oneOf[4].MbdRtu.connections[].delay_between_requests | integer | 是 | 两条请求直接的间隔；格式：int64 |
| [].oneOf[4].MbdRtu.connections[].holding_write_code | integer | 否 | 格式：int32；允许空值 |
| [].oneOf[4].MbdRtu.connections[].max_read_bit_count | integer | 是 | 格式：int32 |
| [].oneOf[4].MbdRtu.connections[].max_read_register_count | integer | 是 | 格式：int32 |
| [].oneOf[4].MbdRtu.connections[].max_write_bit_count | integer | 是 | 格式：int32 |
| [].oneOf[4].MbdRtu.connections[].max_write_register_count | integer | 是 | 格式：int32 |
| [].oneOf[4].MbdRtu.connections[].mb_data_configure | array[RegisterData] | 是 | register settings |
| [].oneOf[4].MbdRtu.connections[].mb_data_configure[] | object | 是 | Dlt645注册信息 |
| [].oneOf[4].MbdRtu.connections[].mb_data_configure[].data_id | integer | 是 | 数据标识；格式：int32 |
| [].oneOf[4].MbdRtu.connections[].mb_data_configure[].point_ids | array[integer] | 是 | 对应的测点Id |
| [].oneOf[4].MbdRtu.connections[].mb_data_configure[].point_ids[] | integer | 是 | 对应的测点Id；格式：int64 |
| [].oneOf[4].MbdRtu.connections[].mb_data_configure[].polling_period_in_milli | integer | 是 | 轮询周期，毫秒；格式：int64 |
| [].oneOf[4].MbdRtu.connections[].name | string | 是 |  |
| [].oneOf[4].MbdRtu.connections[].point_id | integer | 是 | 通道状态对应的测点号；格式：int64 |
| [].oneOf[4].MbdRtu.connections[].point_id_to_rd | object[string, integer] | 是 | key is point id, value is position of register data；额外属性：integer |
| [].oneOf[4].MbdRtu.connections[].polling_period_to_data | object[string, array[integer]] | 是 | 轮询周期不同的数据, key is period in milli, value is position.；额外属性：array[integer] |
| [].oneOf[4].MbdRtu.connections[].protocol_type | string | 是 | 协议类型；可选值：ENCAP、XA、RTU |
| [].oneOf[4].MbdRtu.connections[].register_addr_to_rd | object[string, integer] | 是 | key:寄存器地址,value:setting中vec<RegisterData>的位置；额外属性：integer |
| [].oneOf[4].MbdRtu.connections[].slave_id | integer | 是 | 格式：int32 |
| [].oneOf[4].MbdRtu.connections[].timeout_in_milli | integer | 是 | 超时设置；格式：int64 |
| [].oneOf[4].MbdRtu.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[4].MbdRtu.name | string | 是 | 通道名称 |
| [].oneOf[4].MbdRtu.para | object | 是 | 串口参数 |
| [].oneOf[4].MbdRtu.para.baud_rate | integer | 是 | 格式：int32 |
| [].oneOf[4].MbdRtu.para.data_bits | integer | 是 | 格式：int32 |
| [].oneOf[4].MbdRtu.para.delay_between_requests | integer | 是 | 格式：int64 |
| [].oneOf[4].MbdRtu.para.file_path | string | 是 |  |
| [].oneOf[4].MbdRtu.para.parity | string | 是 | 奇偶校验位；可选值：None、Odd、Even、Mark、Space |
| [].oneOf[4].MbdRtu.para.stop_bits | integer | 是 | 格式：int32 |
| [].oneOf[5] | object | 是 |  |
| [].oneOf[5].DLT645c | object | 是 | Dlt645客户端通道信息 |
| [].oneOf[5].DLT645c.connections | array[Dlt645Connection] | 是 | 通道连接信息 |
| [].oneOf[5].DLT645c.connections[] | object | 是 | Dlt645通道连接信息 |
| [].oneOf[5].DLT645c.connections[].data_configure | array[RegisterData] | 是 | register settings |
| [].oneOf[5].DLT645c.connections[].data_configure[] | object | 是 | Dlt645注册信息 |
| [].oneOf[5].DLT645c.connections[].data_configure[].data_id | integer | 是 | 数据标识；格式：int32 |
| [].oneOf[5].DLT645c.connections[].data_configure[].point_ids | array[integer] | 是 | 对应的测点Id |
| [].oneOf[5].DLT645c.connections[].data_configure[].point_ids[] | integer | 是 | 对应的测点Id；格式：int64 |
| [].oneOf[5].DLT645c.connections[].data_configure[].polling_period_in_milli | integer | 是 | 轮询周期，毫秒；格式：int64 |
| [].oneOf[5].DLT645c.connections[].data_id_to_rd | object[string, integer] | 是 | key:寄存器地址,value:setting中vec<RegisterData>的位置；额外属性：integer |
| [].oneOf[5].DLT645c.connections[].default_polling_period_in_milli | integer | 是 | 默认的轮询周期；格式：int64 |
| [].oneOf[5].DLT645c.connections[].name | string | 是 | 连接名称 |
| [].oneOf[5].DLT645c.connections[].point_id | integer | 是 | 通道状态对应的测点号；格式：int64 |
| [].oneOf[5].DLT645c.connections[].point_id_to_rd | object[string, integer] | 是 | key is point id, value is position of register data；额外属性：integer |
| [].oneOf[5].DLT645c.connections[].polling_period_to_data | object[string, array[integer]] | 是 | 轮询周期不同的数据, key is period in milli, value is position.；额外属性：array[integer] |
| [].oneOf[5].DLT645c.connections[].slave_id | integer | 是 | 格式：int64 |
| [].oneOf[5].DLT645c.connections[].timeout_in_milli | integer | 是 | 超时设置；格式：int64 |
| [].oneOf[5].DLT645c.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[5].DLT645c.name | string | 是 | 通道名称 |
| [].oneOf[5].DLT645c.para | oneOf[object{Serial} | object{Socket}] | 是 | 参数；可选结构：object{Serial} | object{Socket} |
| [].oneOf[5].DLT645c.para.oneOf[1] | object | 是 |  |
| [].oneOf[5].DLT645c.para.oneOf[1].Serial | object | 是 | 串口通道参数 |
| [].oneOf[5].DLT645c.para.oneOf[1].Serial.baud_rate | integer | 是 | 格式：int32 |
| [].oneOf[5].DLT645c.para.oneOf[1].Serial.data_bits | integer | 是 | 格式：int32 |
| [].oneOf[5].DLT645c.para.oneOf[1].Serial.delay_between_requests | integer | 是 | 格式：int64 |
| [].oneOf[5].DLT645c.para.oneOf[1].Serial.file_path | string | 是 |  |
| [].oneOf[5].DLT645c.para.oneOf[1].Serial.parity | string | 是 | 奇偶校验位；可选值：None、Odd、Even、Mark、Space |
| [].oneOf[5].DLT645c.para.oneOf[1].Serial.stop_bits | integer | 是 | 格式：int32 |
| [].oneOf[5].DLT645c.para.oneOf[2] | object | 是 |  |
| [].oneOf[5].DLT645c.para.oneOf[2].Socket | array[object] | 是 |  |
| [].oneOf[6] | object | 是 |  |
| [].oneOf[6].Mqtt | object | 是 | Mqtt通道信息 |
| [].oneOf[6].Mqtt.array_filter | string | 否 | 总的提取器，有些情况测量数据作为一个数组放在json中；允许空值 |
| [].oneOf[6].Mqtt.filter_keys | array[array[string]] | 否 | json格式过滤器；允许空值 |
| [].oneOf[6].Mqtt.filter_values | array[array[string]] | 否 | 允许空值 |
| [].oneOf[6].Mqtt.filter_values[] | array[string] | 是 | 允许空值 |
| [].oneOf[6].Mqtt.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[6].Mqtt.is_json | boolean | 是 | 编码格式，默认是protobuf |
| [].oneOf[6].Mqtt.is_transfer | boolean | 是 | 是否转发通道 |
| [].oneOf[6].Mqtt.json_tags | object[string, object[string, integer]] | 否 | json测点对应的数据标识, key是过滤器对应Array的json字符串，value是标识以及测点的索引；允许空值；额外属性：object[string, integer] |
| [].oneOf[6].Mqtt.json_write_tag | object[string, string] | 否 | json写测点模板；允许空值；额外属性：string |
| [].oneOf[6].Mqtt.json_write_template | object[string, string] | 否 | json写测点模板；允许空值；额外属性：string |
| [].oneOf[6].Mqtt.keep_alive | integer | 否 | 心跳时间；格式：int32；允许空值 |
| [].oneOf[6].Mqtt.mqtt_broker | array[any] | 是 | 服务端的ip和por |
| [].oneOf[6].Mqtt.name | string | 是 | 通道名称 |
| [].oneOf[6].Mqtt.point_id | integer | 是 | 通道状态对应的测点号；格式：int64 |
| [].oneOf[6].Mqtt.point_ids | array[array[any]] | 是 | 通过mqtt读写的测点 |
| [].oneOf[6].Mqtt.read_topic | string | 是 | 读测点的主题 |
| [].oneOf[6].Mqtt.user_name | string | 否 | 用户名，可选；允许空值 |
| [].oneOf[6].Mqtt.user_password | string | 否 | 用户密码，可选；允许空值 |
| [].oneOf[6].Mqtt.write_topic | string | 是 | 写测点的主题 |
| [].oneOf[7] | object | 是 |  |
| [].oneOf[7].Iec104c | object | 是 | Iec104客户端通道信息 |
| [].oneOf[7].Iec104c.connection | object | 是 | 连接信息 |
| [].oneOf[7].Iec104c.connection.call_counter_time | integer | 否 | 点度量总召时间间隔；格式：int64；允许空值 |
| [].oneOf[7].Iec104c.connection.call_time | integer | 否 | 总召时间间隔；格式：int64；允许空值 |
| [].oneOf[7].Iec104c.connection.common_address | integer | 是 | 公共地址；格式：int32 |
| [].oneOf[7].Iec104c.connection.common_address_field_length | integer | 是 | 公共地址字节个数；格式：int32 |
| [].oneOf[7].Iec104c.connection.cot_field_length | integer | 是 | 传输原因字节个数；格式：int32 |
| [].oneOf[7].Iec104c.connection.data_configure | array[Iec104Point] | 是 | register settings |
| [].oneOf[7].Iec104c.connection.data_configure[] | object | 是 | Iec104测点信息 |
| [].oneOf[7].Iec104c.connection.data_configure[].control_ioa | integer | 否 | 控制点地址，若进行配置控制点地址，则说明该点可写；格式：int32；允许空值 |
| [].oneOf[7].Iec104c.connection.data_configure[].ioa | integer | 是 | 协议地址；格式：int32 |
| [].oneOf[7].Iec104c.connection.data_configure[].is_yx | boolean | 是 | 是否是遥信量 |
| [].oneOf[7].Iec104c.connection.data_configure[].point_id | integer | 是 | 对应的测点Id；格式：int64 |
| [].oneOf[7].Iec104c.connection.direct_yk | boolean | 否 | 遥控遥调是否为直控，默认为false |
| [].oneOf[7].Iec104c.connection.direct_yt | boolean | 否 |  |
| [].oneOf[7].Iec104c.connection.extension_config | array[array[any]] | 否 | 扩展配置 |
| [].oneOf[7].Iec104c.connection.ioa_field_length | integer | 是 | 信息体地址字节个数；格式：int32 |
| [].oneOf[7].Iec104c.connection.ioa_to_pos | object[string, integer] | 是 | key:Point地址,value:data_configure中的位置；额外属性：integer |
| [].oneOf[7].Iec104c.connection.is_client | boolean | 是 | 是否为客户端 |
| [].oneOf[7].Iec104c.connection.is_control_with_time | boolean | 是 | 控制方向是否带时标 |
| [].oneOf[7].Iec104c.connection.max_idle_time | integer | 是 | t3；格式：int64 |
| [].oneOf[7].Iec104c.connection.max_time_no_ack_received | integer | 是 | t1；格式：int64 |
| [].oneOf[7].Iec104c.connection.max_time_no_ack_sent | integer | 是 | t2；格式：int64 |
| [].oneOf[7].Iec104c.connection.max_unconfirmed_apdus_received | integer | 是 | w，接收方收到w个I格式报文后发送确认；格式：int32 |
| [].oneOf[7].Iec104c.connection.max_unconfirmed_apdus_sent | integer | 是 | k，发送方发送k条连续的未被确认的I格式报文，停止发送；格式：int32 |
| [].oneOf[7].Iec104c.connection.name | string | 是 | 连接名称 |
| [].oneOf[7].Iec104c.connection.originator_address | integer | 是 | 源发地址；格式：int32 |
| [].oneOf[7].Iec104c.connection.point_id | integer | 是 | 通道状态对应的测点号；格式：int64 |
| [].oneOf[7].Iec104c.connection.point_id_to_ioa | object[string, integer] | 是 | key is point id, value is information object address；额外属性：integer |
| [].oneOf[7].Iec104c.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[7].Iec104c.name | string | 是 | 通道名称 |
| [].oneOf[7].Iec104c.tcp_server | array[any] | 是 | 服务端的ip和port |
| [].oneOf[7].Iec104c.yc_data_type | integer | 否 | 遥测点号的数据类型；格式：int32 |
| [].oneOf[7].Iec104c.yx_data_type | integer | 否 | 遥信点号的数据类型；格式：int32 |
| [].oneOf[8] | object | 是 |  |
| [].oneOf[8].Iec104d | object | 是 | Iec104服务端通道信息 |
| [].oneOf[8].Iec104d.connections | array[array[any]] | 是 | 连接信息 |
| [].oneOf[8].Iec104d.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[8].Iec104d.name | string | 是 | 通道名称 |
| [].oneOf[8].Iec104d.tcp_server_port | integer | 是 | 服务的port；格式：int32 |
| [].oneOf[8].Iec104d.yc_data_type | integer | 是 | 遥测点号的数据类型；格式：int32 |
| [].oneOf[8].Iec104d.yx_data_type | integer | 是 | 遥信点号的数据类型；格式：int32 |
| [].oneOf[9] | object | 是 |  |
| [].oneOf[9].HYMqtt | object | 是 | 华云Mqtt通道信息 |
| [].oneOf[9].HYMqtt.app_name | string | 是 | APP的名称，用于生成topic |
| [].oneOf[9].HYMqtt.data_configure | array[HYPoint] | 是 | 测点列表 |
| [].oneOf[9].HYMqtt.data_configure[] | object | 是 | 华云-台区智能融合终端测点 |
| [].oneOf[9].HYMqtt.data_configure[].device_id | integer | 是 | 测点归属的设备序号；格式：int32 |
| [].oneOf[9].HYMqtt.data_configure[].not_realtime | boolean | 是 | 暂时无用 |
| [].oneOf[9].HYMqtt.data_configure[].point_id | integer | 是 | 对应的测点Id；格式：int64 |
| [].oneOf[9].HYMqtt.data_configure[].point_info | object | 是 | 测点信息 |
| [].oneOf[9].HYMqtt.data_configure[].point_info.deadzone | string | 是 |  |
| [].oneOf[9].HYMqtt.data_configure[].point_info.isReport | string | 是 |  |
| [].oneOf[9].HYMqtt.data_configure[].point_info.name | string | 是 |  |
| [].oneOf[9].HYMqtt.data_configure[].point_info.ratio | string | 是 |  |
| [].oneOf[9].HYMqtt.data_configure[].point_info.type | string | 是 |  |
| [].oneOf[9].HYMqtt.data_configure[].point_info.unit | string | 是 |  |
| [].oneOf[9].HYMqtt.data_configure[].point_info.userdefine | string | 是 | 名字不能改！！！ |
| [].oneOf[9].HYMqtt.device_configure | object[string, HYDevice] | 是 | 设备key is 设备序号, value is (dev,设备的信息)；额外属性：HYDevice |
| [].oneOf[9].HYMqtt.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[9].HYMqtt.is_new | boolean | 是 | 版本，false是配电物联2020版本，true是2021版本，该参数会导致topic不同 |
| [].oneOf[9].HYMqtt.is_poll | boolean | 是 |  |
| [].oneOf[9].HYMqtt.model_to_pos | object[string, array[integer]] | 是 | 模型列表key is model, value is 测点索引；额外属性：array[integer] |
| [].oneOf[9].HYMqtt.mqtt_broker | array[any] | 是 | 服务端的ip和por |
| [].oneOf[9].HYMqtt.name | string | 是 | 通道名称 |
| [].oneOf[9].HYMqtt.point_id | integer | 是 | 通道状态对应的测点号；格式：int64 |
| [].oneOf[9].HYMqtt.point_id_to_pos | object[string, integer] | 是 | key is point id, value is information object address(data_configure的索引)；额外属性：integer |
| [].oneOf[9].HYMqtt.poll_time | integer | 是 | 轮询周期，单位毫秒；格式：int64 |
| [].oneOf[9].HYMqtt.read_topic | string | 是 | 读测点的主题 |
| [].oneOf[9].HYMqtt.user_name | string | 否 | 用户名，可选；允许空值 |
| [].oneOf[9].HYMqtt.user_password | string | 否 | 用户密码，可选；允许空值 |
| [].oneOf[9].HYMqtt.write_topic | string | 是 | 写测点的主题 |
| [].oneOf[10] | object | 是 |  |
| [].oneOf[10].EtherCAT | object | 是 | EtherCAT通道信息 |
| [].oneOf[10].EtherCAT.connections | array[EcConnection] | 是 | 连接信息 |
| [].oneOf[10].EtherCAT.connections[] | object | 是 | EtherCAT通道连接信息 |
| [].oneOf[10].EtherCAT.connections[].cycle_time_in_micro | integer | 是 | 格式：int64 |
| [].oneOf[10].EtherCAT.connections[].data | array[PdiData] | 是 |  |
| [].oneOf[10].EtherCAT.connections[].data[] | object | 是 |  |
| [].oneOf[10].EtherCAT.connections[].data[].data_type | string | 是 | 数据类型；可选值：Binary、OneByteIntSigned、OneByteIntSignedLower、OneByteIntSignedUpper、OneByteIntUnsigned、OneByteIntUnsignedLower、OneByteIntUnsignedUpper、TwoByteIntUnsigned、TwoByteIntUnsignedSwapped、TwoByteIntSigned、TwoByteIntSignedSwapped、TwoByteBcd、FourByteIntUnsigned、FourByteIntSigned、FourByteIntUnsignedSwapped、FourByteIntSignedSwapped、FourByteIntUnsignedSwappedSwapped、FourByteIntSignedSwappedSwapped、FourByteFloat、FourByteFloatSwapped、FourByteFloatSwappedSwapped、FourByteBcd、FourByteBcdSwapped、FourByteMod10k、FourByteMod10kSwapped、SixByteMod10k、SixByteMod10kSwapped、EightByteIntUnsigned、EightByteIntSigned、EightByteIntUnsignedSwapped、EightByteIntSignedSwapped、EightByteIntUnsignedSwappedSwapped、EightByteIntSignedSwappedSwapped、EightByteFloat、EightByteFloatSwapped、EightByteFloatSwappedSwapped、EightByteMod10kSwapped、EightByteMod10k |
| [].oneOf[10].EtherCAT.connections[].data[].from | integer | 是 | 格式：int32 |
| [].oneOf[10].EtherCAT.connections[].data[].is_writable | boolean | 是 | 是否可写 |
| [].oneOf[10].EtherCAT.connections[].data[].point_id | integer | 是 | 对应的测点Id；格式：int64 |
| [].oneOf[10].EtherCAT.connections[].dc_sync | boolean | 是 | is DC sync |
| [].oneOf[10].EtherCAT.connections[].index | integer | 是 |  |
| [].oneOf[10].EtherCAT.connections[].module_name | string | 是 |  |
| [].oneOf[10].EtherCAT.connections[].name | string | 是 |  |
| [].oneOf[10].EtherCAT.connections[].point_id | integer | 是 | 格式：int64 |
| [].oneOf[10].EtherCAT.connections[].point_to_pos | object[string, integer] | 是 | 额外属性：integer |
| [].oneOf[10].EtherCAT.connections[].watchdog_multi | integer | 否 | defaukt to 2498；格式：int32；允许空值 |
| [].oneOf[10].EtherCAT.connections[].watchdog_pdi | integer | 否 | 1/25M*(multi_watchdog+2)*pdi_watchdog；格式：int32；允许空值 |
| [].oneOf[10].EtherCAT.connections[].watchdog_sm | integer | 否 | 1/25M*(multi_watchdog+2)*sm_watchdog, defaukt to 1000；格式：int32；允许空值 |
| [].oneOf[10].EtherCAT.eth | string | 是 |  |
| [].oneOf[10].EtherCAT.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[10].EtherCAT.name | string | 是 | 通道名称 |
| [].oneOf[11] | object | 是 |  |
| [].oneOf[11].MemoryPosix | object | 是 | Posix内存通道 |
| [].oneOf[11].MemoryPosix.connections | array[MemConnection] | 是 | 连接信息 |
| [].oneOf[11].MemoryPosix.connections[] | object | 是 | 内存通道连接信息 |
| [].oneOf[11].MemoryPosix.connections[].base_addr | integer | 是 |  |
| [].oneOf[11].MemoryPosix.connections[].data | array[MemData] | 是 |  |
| [].oneOf[11].MemoryPosix.connections[].data[] | object | 是 |  |
| [].oneOf[11].MemoryPosix.connections[].data[].data_type | string | 是 | 数据类型；可选值：Binary、OneByteIntSigned、OneByteIntSignedLower、OneByteIntSignedUpper、OneByteIntUnsigned、OneByteIntUnsignedLower、OneByteIntUnsignedUpper、TwoByteIntUnsigned、TwoByteIntUnsignedSwapped、TwoByteIntSigned、TwoByteIntSignedSwapped、TwoByteBcd、FourByteIntUnsigned、FourByteIntSigned、FourByteIntUnsignedSwapped、FourByteIntSignedSwapped、FourByteIntUnsignedSwappedSwapped、FourByteIntSignedSwappedSwapped、FourByteFloat、FourByteFloatSwapped、FourByteFloatSwappedSwapped、FourByteBcd、FourByteBcdSwapped、FourByteMod10k、FourByteMod10kSwapped、SixByteMod10k、SixByteMod10kSwapped、EightByteIntUnsigned、EightByteIntSigned、EightByteIntUnsignedSwapped、EightByteIntSignedSwapped、EightByteIntUnsignedSwappedSwapped、EightByteIntSignedSwappedSwapped、EightByteFloat、EightByteFloatSwapped、EightByteFloatSwappedSwapped、EightByteMod10kSwapped、EightByteMod10k |
| [].oneOf[11].MemoryPosix.connections[].data[].from | integer | 是 |  |
| [].oneOf[11].MemoryPosix.connections[].data[].is_writable | boolean | 是 |  |
| [].oneOf[11].MemoryPosix.connections[].data[].point_id | integer | 是 | 对应的测点Id；格式：int64 |
| [].oneOf[11].MemoryPosix.connections[].data[].polling_period_in_milli | integer | 是 | 格式：int64 |
| [].oneOf[11].MemoryPosix.connections[].default_polling_period_in_milli | integer | 是 | 格式：int64 |
| [].oneOf[11].MemoryPosix.connections[].lock_method | oneOf[string | object{Mutex}] | 是 | 可选值：None、Semaphore；可选结构：string | object{Mutex} |
| [].oneOf[11].MemoryPosix.connections[].lock_method.oneOf[1] | string | 是 | 可选值：None |
| [].oneOf[11].MemoryPosix.connections[].lock_method.oneOf[2] | object | 是 |  |
| [].oneOf[11].MemoryPosix.connections[].lock_method.oneOf[2].Mutex | integer | 是 |  |
| [].oneOf[11].MemoryPosix.connections[].lock_method.oneOf[3] | string | 是 | 可选值：Semaphore |
| [].oneOf[11].MemoryPosix.connections[].mem_addr_to_pos | object[string, integer] | 是 | key:寄存器地址,value:setting中vec<MemData>的位置；额外属性：integer |
| [].oneOf[11].MemoryPosix.connections[].name | string | 是 |  |
| [].oneOf[11].MemoryPosix.connections[].point_to_pos | object[string, integer] | 是 | 额外属性：integer |
| [].oneOf[11].MemoryPosix.connections[].polling_period_to_data | object[string, array[integer]] | 是 | 轮询周期不同的数据, key is period in milli, value is position.；额外属性：array[integer] |
| [].oneOf[11].MemoryPosix.connections[].total_size | integer | 否 | 取决于计算机位数，如果溢出，应该报错。；允许空值 |
| [].oneOf[11].MemoryPosix.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[11].MemoryPosix.is_transfer | boolean | 是 |  |
| [].oneOf[11].MemoryPosix.name | string | 是 | 通道名称 |
| [].oneOf[11].MemoryPosix.path | string | 否 | 允许空值 |
| [].oneOf[12] | object | 是 |  |
| [].oneOf[12].MemorySystemV | object | 是 | SystemV内存通道 |
| [].oneOf[12].MemorySystemV.connection | object | 是 | 内存通道连接信息 |
| [].oneOf[12].MemorySystemV.connection.base_addr | integer | 是 |  |
| [].oneOf[12].MemorySystemV.connection.data | array[MemData] | 是 |  |
| [].oneOf[12].MemorySystemV.connection.data[] | object | 是 |  |
| [].oneOf[12].MemorySystemV.connection.data[].data_type | string | 是 | 数据类型；可选值：Binary、OneByteIntSigned、OneByteIntSignedLower、OneByteIntSignedUpper、OneByteIntUnsigned、OneByteIntUnsignedLower、OneByteIntUnsignedUpper、TwoByteIntUnsigned、TwoByteIntUnsignedSwapped、TwoByteIntSigned、TwoByteIntSignedSwapped、TwoByteBcd、FourByteIntUnsigned、FourByteIntSigned、FourByteIntUnsignedSwapped、FourByteIntSignedSwapped、FourByteIntUnsignedSwappedSwapped、FourByteIntSignedSwappedSwapped、FourByteFloat、FourByteFloatSwapped、FourByteFloatSwappedSwapped、FourByteBcd、FourByteBcdSwapped、FourByteMod10k、FourByteMod10kSwapped、SixByteMod10k、SixByteMod10kSwapped、EightByteIntUnsigned、EightByteIntSigned、EightByteIntUnsignedSwapped、EightByteIntSignedSwapped、EightByteIntUnsignedSwappedSwapped、EightByteIntSignedSwappedSwapped、EightByteFloat、EightByteFloatSwapped、EightByteFloatSwappedSwapped、EightByteMod10kSwapped、EightByteMod10k |
| [].oneOf[12].MemorySystemV.connection.data[].from | integer | 是 |  |
| [].oneOf[12].MemorySystemV.connection.data[].is_writable | boolean | 是 |  |
| [].oneOf[12].MemorySystemV.connection.data[].point_id | integer | 是 | 对应的测点Id；格式：int64 |
| [].oneOf[12].MemorySystemV.connection.data[].polling_period_in_milli | integer | 是 | 格式：int64 |
| [].oneOf[12].MemorySystemV.connection.default_polling_period_in_milli | integer | 是 | 格式：int64 |
| [].oneOf[12].MemorySystemV.connection.lock_method | oneOf[string | object{Mutex}] | 是 | 可选值：None、Semaphore；可选结构：string | object{Mutex} |
| [].oneOf[12].MemorySystemV.connection.lock_method.oneOf[1] | string | 是 | 可选值：None |
| [].oneOf[12].MemorySystemV.connection.lock_method.oneOf[2] | object | 是 |  |
| [].oneOf[12].MemorySystemV.connection.lock_method.oneOf[2].Mutex | integer | 是 |  |
| [].oneOf[12].MemorySystemV.connection.lock_method.oneOf[3] | string | 是 | 可选值：Semaphore |
| [].oneOf[12].MemorySystemV.connection.mem_addr_to_pos | object[string, integer] | 是 | key:寄存器地址,value:setting中vec<MemData>的位置；额外属性：integer |
| [].oneOf[12].MemorySystemV.connection.name | string | 是 |  |
| [].oneOf[12].MemorySystemV.connection.point_to_pos | object[string, integer] | 是 | 额外属性：integer |
| [].oneOf[12].MemorySystemV.connection.polling_period_to_data | object[string, array[integer]] | 是 | 轮询周期不同的数据, key is period in milli, value is position.；额外属性：array[integer] |
| [].oneOf[12].MemorySystemV.connection.total_size | integer | 否 | 取决于计算机位数，如果溢出，应该报错。；允许空值 |
| [].oneOf[12].MemorySystemV.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[12].MemorySystemV.identifier | integer | 是 | 格式：int32 |
| [].oneOf[12].MemorySystemV.is_transfer | boolean | 是 |  |
| [].oneOf[12].MemorySystemV.name | string | 是 | 通道名称 |
| [].oneOf[12].MemorySystemV.path | string | 是 |  |
| [].oneOf[13] | object | 是 |  |
| [].oneOf[13].OpcuaClient | object | 是 | Opcua客户端通道信息 |
| [].oneOf[13].OpcuaClient.certificate | array[integer] | 否 | certificate；允许空值 |
| [].oneOf[13].OpcuaClient.certificate[] | integer | 是 | certificate；格式：int32 |
| [].oneOf[13].OpcuaClient.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[13].OpcuaClient.is_writable | array[boolean] | 是 |  |
| [].oneOf[13].OpcuaClient.name | string | 是 | 通道名称 |
| [].oneOf[13].OpcuaClient.node_ids | array[NodeInfo] | 是 | corresponding node ids in opc ua server |
| [].oneOf[13].OpcuaClient.node_ids[] | object | 是 | corresponding node ids in opc ua server |
| [].oneOf[13].OpcuaClient.node_ids[].node_id | oneOf[object{Num} | object{Str}] | 是 | 可选结构：object{Num} | object{Str} |
| [].oneOf[13].OpcuaClient.node_ids[].node_id.oneOf[1] | object | 是 |  |
| [].oneOf[13].OpcuaClient.node_ids[].node_id.oneOf[1].Num | integer | 是 | 格式：int32 |
| [].oneOf[13].OpcuaClient.node_ids[].node_id.oneOf[2] | object | 是 |  |
| [].oneOf[13].OpcuaClient.node_ids[].node_id.oneOf[2].Str | string | 是 |  |
| [].oneOf[13].OpcuaClient.node_ids[].node_ns | integer | 是 | 格式：int32 |
| [].oneOf[13].OpcuaClient.point_id | integer | 是 | 通道状态对应的测点号；格式：int64 |
| [].oneOf[13].OpcuaClient.point_ids | array[array[any]] | 是 | 通过opcua读写的测点 |
| [].oneOf[13].OpcuaClient.poll_period | array[integer] | 是 |  |
| [].oneOf[13].OpcuaClient.poll_period[] | integer | 是 | 格式：int64 |
| [].oneOf[13].OpcuaClient.private_key | array[integer] | 否 | private_key；允许空值 |
| [].oneOf[13].OpcuaClient.private_key[] | integer | 是 | private_key；格式：int32 |
| [].oneOf[13].OpcuaClient.server | array[any] | 是 | 服务端的ip和port |
| [].oneOf[13].OpcuaClient.sub_properties | object[string, string] | 是 | subscribe properties；额外属性：string |
| [].oneOf[13].OpcuaClient.user_name | string | 否 | 用户名，可选；允许空值 |
| [].oneOf[13].OpcuaClient.user_password | string | 否 | 用户密码，可选；允许空值 |
| [].oneOf[14] | object | 是 |  |
| [].oneOf[14].OpcuaServer | object | 是 | Opcua服务端通道信息 |
| [].oneOf[14].OpcuaServer.browse_name | array[string] | 是 |  |
| [].oneOf[14].OpcuaServer.browse_name[] | string | 是 | 允许空值 |
| [].oneOf[14].OpcuaServer.certificate | array[integer] | 否 | certificate；允许空值 |
| [].oneOf[14].OpcuaServer.certificate[] | integer | 是 | certificate；格式：int32 |
| [].oneOf[14].OpcuaServer.id | integer | 是 | 通道id；格式：int64 |
| [].oneOf[14].OpcuaServer.is_writable | array[boolean] | 是 |  |
| [].oneOf[14].OpcuaServer.name | string | 是 | 通道名称 |
| [].oneOf[14].OpcuaServer.node_ids | array[array[NodeInfo]] | 是 |  |
| [].oneOf[14].OpcuaServer.node_ids[] | array[NodeInfo] | 是 |  |
| [].oneOf[14].OpcuaServer.node_ids[][] | object | 是 |  |
| [].oneOf[14].OpcuaServer.node_ids[][].node_id | oneOf[object{Num} | object{Str}] | 是 | 可选结构：object{Num} | object{Str} |
| [].oneOf[14].OpcuaServer.node_ids[][].node_id.oneOf[1] | object | 是 |  |
| [].oneOf[14].OpcuaServer.node_ids[][].node_id.oneOf[1].Num | integer | 是 | 格式：int32 |
| [].oneOf[14].OpcuaServer.node_ids[][].node_id.oneOf[2] | object | 是 |  |
| [].oneOf[14].OpcuaServer.node_ids[][].node_id.oneOf[2].Str | string | 是 |  |
| [].oneOf[14].OpcuaServer.node_ids[][].node_ns | integer | 是 | 格式：int32 |
| [].oneOf[14].OpcuaServer.point_ids | array[array[any]] | 是 | register settings |
| [].oneOf[14].OpcuaServer.private_key | array[integer] | 否 | private_key；允许空值 |
| [].oneOf[14].OpcuaServer.private_key[] | integer | 是 | private_key；格式：int32 |
| [].oneOf[14].OpcuaServer.server_port | integer | 是 | 服务端的ip和port；格式：int32 |
| [].oneOf[14].OpcuaServer.users | array[array[any]] | 否 | 用户；允许空值 |


### 删除指定lcc指定id的通道

- **方法**: `DELETE`
- **路径**: `/lcc/transports/models/{lcc_id}/{ids}`
- **工具名**: `delete_lcc_transports_models_by_lcc_by_s`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id
  - `ids` (path, string, 必填): 通道id列表，以,间隔

### 查询指定lcc未运行的AOE

- **方法**: `GET`
- **路径**: `/lcc/unrun_aoes/{lcc_id}`
- **工具名**: `get_lcc_unrun_aoes_by_lcc`
- **参数**:
  - `lcc_id` (path, string, 必填): lcc_id

### 查询指定id的lcc

- **方法**: `GET`
- **路径**: `/lcc/{id}`
- **工具名**: `get_lcc_by`
- **参数**:
  - `id` (path, string, 必填): lcc_id

### 查询所有的lcc

- **方法**: `GET`
- **路径**: `/lcc_list`
- **工具名**: `get_lcc_list`

***

## MEASURES 模块

### 量测值初始化

- **方法**: `POST`
- **路径**: `/measureinits/{day}`
- **工具名**: `add_measureinits_by_day`
- **参数**:
  - `day` (path, integer, 必填): 时间戳；元信息：format=int64

### 查询历史量测

- **方法**: `GET`
- **路径**: `/measures`
- **工具名**: `get_measures`
- **参数**:
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

### 查询SOE，结果按照时间排序

- **方法**: `GET`
- **路径**: `/soes`
- **工具名**: `get_soes`
- **参数**:
  - `id` (query, string, 可选): 测点id，多个id之间以,间隔；元信息：nullable=true
  - `start` (query, integer, 可选): 开始时间, 13位时间戳；元信息：format=int64, nullable=true
  - `end` (query, integer, 可选): 结束时间, 13位时间戳，（start、end） 如果仅设置1个参数，则查询范围为start-当天结束 或 当天开始-end；元信息：format=int64, nullable=true
  - `date` (query, string, 可选): 时间字符串，yyyy-MM-dd，（start、end）、date参数至少设定1个，如果同时设定，则以start、end为准；元信息：nullable=true
  - `source` (query, integer, 可选): 数据源；元信息：format=int32, nullable=true
  - `last_only` (query, boolean, 可选): 是否查询只最新的数据；元信息：nullable=true
  - `with_init` (query, boolean, 可选): 是否查询该天初始的数据；元信息：nullable=true
  - `reverse_order` (query, boolean, 可选): 是否时间倒序查询；元信息：nullable=true

***

## PLANS 模块

### 查询所有计划

- **方法**: `GET`
- **路径**: `/plans/models`
- **工具名**: `get_plans_models`

### 新增计划

- **方法**: `POST`
- **路径**: `/plans/models`
- **工具名**: `add_plans_models`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 是 | 计划描述 |
| id | integer | 是 | 计划id；格式：int64 |
| name | string | 是 | 计划名称 |
| plan | array[array[any]] | 是 | 计划内容数组，tuple格式为(开始时间:u64, 结束时间:u64, 功率值:f64) |


### 修改计划

- **方法**: `PUT`
- **路径**: `/plans/models`
- **工具名**: `update_plans_models`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 是 | 计划描述 |
| id | integer | 是 | 计划id；格式：int64 |
| name | string | 是 | 计划名称 |
| plan | array[array[any]] | 是 | 计划内容数组，tuple格式为(开始时间:u64, 结束时间:u64, 功率值:f64) |


### 查询指定id的计划列表

- **方法**: `GET`
- **路径**: `/plans/models/by_ids/{ids}`
- **工具名**: `get_plans_models_by_ids`
- **参数**:
  - `ids` (path, string, 必填): 计划id列表，以,间隔

### 删除指定id的计划

- **方法**: `DELETE`
- **路径**: `/plans/models/{ids}`
- **工具名**: `delete_plans_models_by_s`
- **参数**:
  - `ids` (path, string, 必填): 计划id列表，以,间隔

### 查询指定id的计划

- **方法**: `GET`
- **路径**: `/plans/models/{id}`
- **工具名**: `get_plans_models_by`
- **参数**:
  - `id` (path, integer, 必填): 计划id；元信息：format=int64

### 查询所有计划路径

- **方法**: `GET`
- **路径**: `/plans/paths`
- **工具名**: `get_plans_paths`

### 新增计划路径

- **方法**: `POST`
- **路径**: `/plans/paths`
- **工具名**: `add_plans_paths`
- **请求体**:

  - 无法解析请求体结构


### 修改计划路径

- **方法**: `PUT`
- **路径**: `/plans/paths`
- **工具名**: `update_plans_paths`
- **请求体**:

  - 无法解析请求体结构


### 删除指定的计划路径

- **方法**: `DELETE`
- **路径**: `/plans/paths`
- **工具名**: `delete_plans_paths`
- **请求体**:

  - 无法解析请求体结构


***

## POINTS 模块

### 查询所有测点

- **方法**: `GET`
- **路径**: `/points/models`
- **工具名**: `get_points_models`

### 保存测点

- **方法**: `POST`
- **路径**: `/points/models`
- **工具名**: `add_points_models`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | object | 是 | 测点对象 |
| [].alarm_level1_expr | string | 是 | 告警级别1的表达式 |
| [].alarm_level2_expr | string | 是 | 告警级别2的表达式 |
| [].alias_id | string | 是 | 字符串id |
| [].change_expr | string | 是 | 判断是否"变化"的公式，用于变化上传或储存 |
| [].data_unit | string | 是 | 单位 |
| [].desc | string | 是 | Description |
| [].expression | string | 是 | 如果是计算点，这是表达式 |
| [].init_value | integer | 是 | 默认值存储在8个字节，需要根据is_discrete来转换成具体的值；格式：int64 |
| [].inv_trans_expr | string | 是 | 逆变换公式 |
| [].is_computing_point | boolean | 是 | 是否是计算点 |
| [].is_discrete | boolean | 是 | 是否是离散量 |
| [].is_realtime | boolean | 是 | 如是，则不判断是否"变化"，均上传 |
| [].is_soe | boolean | 是 | 是否是soe点 |
| [].lower_limit | number | 是 | 下限，用于坏数据辨识；格式：double |
| [].point_id | integer | 是 | 唯一的id；格式：int64 |
| [].point_name | string | 是 | 测点名 |
| [].trans_expr | string | 是 | 变换公式 |
| [].upper_limit | number | 是 | 上限，用于坏数据辨识；格式：double |
| [].zero_expr | string | 是 | 判断是否为0值的公式 |


### 删除指定id的测点（body形式）

- **方法**: `DELETE`
- **路径**: `/points/models`
- **工具名**: `delete_points_models`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | integer | 是 | 格式：int64 |


### 获取根据版本号组装的测点应用对象

- **方法**: `GET`
- **路径**: `/points/models/for_apply`
- **工具名**: `get_points_models_for_apply`
- **参数**:
  - `version` (query, integer, 可选): 版本号，可选，若为空则默认0号版本；元信息：format=int32, nullable=true

### 删除指定id的测点

- **方法**: `DELETE`
- **路径**: `/points/models/{ids}`
- **工具名**: `delete_points_models_by_s`
- **参数**:
  - `ids` (path, string, 必填): 测点id列表，以,间隔

### 保存测点（文件形式）

- **方法**: `POST`
- **路径**: `/points/models_file`
- **工具名**: `add_points_models_file`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileContent | array[integer] | 否 | 允许空值 |
| fileContent[] | integer | 是 | 格式：int32 |
| fileName | string | 否 | 允许空值 |
| is_zip | boolean | 否 | 允许空值 |
| op | oneOf[string] | 否 | 可选值：UPDATE、DELETE、RENAME；可选结构：string |
| op.oneOf[1] | string | 是 | 可选值：UPDATE、DELETE、RENAME |


### 保存测点（多文件形式）

- **方法**: `POST`
- **路径**: `/points/models_file2`
- **工具名**: `add_points_models_file2`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | array[string] | 是 |  |
| file[] | string | 是 | 格式：binary |


### 查询控制器与测点的对应关系

- **方法**: `GET`
- **路径**: `/points/remote`
- **工具名**: `get_points_remote`

### 更新控制器与测点的关系

- **方法**: `POST`
- **路径**: `/points/remote`
- **工具名**: `add_points_remote`
- **请求体**:

  - 无法解析请求体结构


### 查询所有测点数据源

- **方法**: `GET`
- **路径**: `/points/source`
- **工具名**: `get_points_source`

### 保存测点数据源

- **方法**: `POST`
- **路径**: `/points/source`
- **工具名**: `add_points_source`
- **请求体**:

  - 无法解析请求体结构


### 查询所有的测点版本信息

- **方法**: `GET`
- **路径**: `/points/version`
- **工具名**: `get_points_version`

### 新增测点版本

- **方法**: `POST`
- **路径**: `/points/version`
- **工具名**: `add_points_version`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| note | string | 是 | 提交时的注释 |
| tree_id | string | 是 | 对应的tree_id |
| version | integer | 是 | 版本号；格式：int32 |


### 删除某一个测点版本

- **方法**: `DELETE`
- **路径**: `/points/version/{v}`
- **工具名**: `delete_points_version_by_v`
- **参数**:
  - `v` (path, integer, 必填): 版本id；元信息：format=int32

***

## PSCPU 模块

### 更新当前应用的AOE

- **方法**: `POST`
- **路径**: `/pscpu/aoes`
- **工具名**: `add_pscpu_aoes`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aoes | array[AoeModel] | 是 | AOE列表 |
| aoes[] | object | 是 | aoe模型 |
| aoes[].actions | array[ActionEdge] | 是 | 动作列表 |
| aoes[].actions[] | object | 是 | 边对象 |
| aoes[].actions[].action | oneOf[string | object{SetPoints} | object{SetPointsWithCheck} | object{SetPoints2} | object{SetPointsWithCheck2} | object{Solve} | object{Nlsolve} | object{Milp} | object{SimpleMilp} | object{Nlp}] | 是 | 动作定义；可选值：None；可选结构：string | object{SetPoints} | object{SetPointsWithCheck} | object{SetPoints2} | object{SetPointsWithCheck2} | object{Solve} | object{Nlsolve} | object{Milp} | object{SimpleMilp} | object{Nlp} |
| aoes[].actions[].action.oneOf[1] | string | 是 | 无动作；可选值：None |
| aoes[].actions[].action.oneOf[2] | object | 是 | 设点动作 |
| aoes[].actions[].action.oneOf[2].SetPoints | object | 是 | 设点动作 |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_id | array[string] | 是 |  |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v | array[Expr] | 是 |  |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[2].SetPoints.analog_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_id | array[string] | 是 |  |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v | array[Expr] | 是 |  |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[2].SetPoints.discrete_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[3] | object | 是 | 设点动作 |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck | object | 是 | 设点动作 |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_id | array[string] | 是 |  |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v | array[Expr] | 是 |  |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.analog_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_id | array[string] | 是 |  |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v | array[Expr] | 是 |  |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[3].SetPointsWithCheck.discrete_v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[4] | object | 是 | 设点动作 |
| aoes[].actions[].action.oneOf[4].SetPoints2 | object | 是 | 设点动作 |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs | array[PointsToExp] | 是 |  |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[] | object | 是 |  |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr | object | 是 | 表达式 |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[4].SetPoints2.analogs[].ids | array[string] | 是 | id列表 |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes | array[PointsToExp] | 是 |  |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[] | object | 是 |  |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr | object | 是 | 表达式 |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[4].SetPoints2.discretes[].ids | array[string] | 是 | id列表 |
| aoes[].actions[].action.oneOf[5] | object | 是 | 设点动作 |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2 | object | 是 | 设点动作 |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs | array[PointsToExp] | 是 |  |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[] | object | 是 |  |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr | object | 是 | 表达式 |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.analogs[].ids | array[string] | 是 | id列表 |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes | array[PointsToExp] | 是 |  |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[] | object | 是 |  |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr | object | 是 | 表达式 |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[5].SetPointsWithCheck2.discretes[].ids | array[string] | 是 | id列表 |
| aoes[].actions[].action.oneOf[6] | object | 是 | 求方程 |
| aoes[].actions[].action.oneOf[6].Solve | object | 是 | 求方程 |
| aoes[].actions[].action.oneOf[6].Solve.a | object | 是 | A矩阵 |
| aoes[].actions[].action.oneOf[6].Solve.a.m | integer | 是 | 行数 |
| aoes[].actions[].action.oneOf[6].Solve.a.n | integer | 是 | 列数 |
| aoes[].actions[].action.oneOf[6].Solve.a.v | array[array[any]] | 是 |  |
| aoes[].actions[].action.oneOf[6].Solve.b | array[Expr] | 是 | b向量 |
| aoes[].actions[].action.oneOf[6].Solve.b[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[6].Solve.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[6].Solve.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| aoes[].actions[].action.oneOf[6].Solve.x_init | array[Expr] | 是 | 变量初始值 |
| aoes[].actions[].action.oneOf[6].Solve.x_init[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[6].Solve.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[6].Solve.x_name | array[string] | 是 | 变量名称 |
| aoes[].actions[].action.oneOf[7] | object | 是 | 求非线性方程组 |
| aoes[].actions[].action.oneOf[7].Nlsolve | object | 是 | 求非线性方程组 |
| aoes[].actions[].action.oneOf[7].Nlsolve.f | array[Expr] | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[7].Nlsolve.f[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[7].Nlsolve.parameters | object[string, string] | 是 | 额外属性：string |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init | array[Expr] | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx | array[Expr] | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_init_cx[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[7].Nlsolve.x_name | array[string] | 是 |  |
| aoes[].actions[].action.oneOf[8] | object | 是 | 混合整数线性规划稀疏表示 |
| aoes[].actions[].action.oneOf[8].Milp | object | 是 | 混合整数线性规划稀疏表示 |
| aoes[].actions[].action.oneOf[8].Milp.a | object | 是 | Ax >=/<= b |
| aoes[].actions[].action.oneOf[8].Milp.a.m | integer | 是 | 行数 |
| aoes[].actions[].action.oneOf[8].Milp.a.n | integer | 是 | 列数 |
| aoes[].actions[].action.oneOf[8].Milp.a.v | array[array[any]] | 是 |  |
| aoes[].actions[].action.oneOf[8].Milp.b | array[Expr] | 是 |  |
| aoes[].actions[].action.oneOf[8].Milp.b[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[8].Milp.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[8].Milp.binary_int_float | array[integer] | 是 | 整数变量在x中的位置 |
| aoes[].actions[].action.oneOf[8].Milp.binary_int_float[] | integer | 是 | 整数变量在x中的位置；格式：int32 |
| aoes[].actions[].action.oneOf[8].Milp.c | array[array[any]] | 是 | min/max c^T*x |
| aoes[].actions[].action.oneOf[8].Milp.constraint_type | array[Operation] | 是 |  |
| aoes[].actions[].action.oneOf[8].Milp.constraint_type[] | string | 是 | Mathematical operations.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[8].Milp.min_or_max | boolean | 是 | min: true, max: false |
| aoes[].actions[].action.oneOf[8].Milp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| aoes[].actions[].action.oneOf[8].Milp.x_lower | array[array[any]] | 是 | 变量的下界约束：变量位置、约束表达式 |
| aoes[].actions[].action.oneOf[8].Milp.x_name | array[string] | 是 | 变量名称 |
| aoes[].actions[].action.oneOf[8].Milp.x_upper | array[array[any]] | 是 | 变量的上界约束：变量位置、约束表达式 |
| aoes[].actions[].action.oneOf[9] | object | 是 | 混合整数线性规划稠密表示 |
| aoes[].actions[].action.oneOf[9].SimpleMilp | object | 是 | 混合整数线性规划稠密表示 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a | object | 是 | Ax >=/<= b |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.m | integer | 是 | 行数 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.n | integer | 是 | 列数 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v | array[Expr] | 是 | 值 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.a.v[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b | array[Expr] | 是 |  |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.b[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.binary_int_float | array[integer] | 是 | 整数变量在x中的位置 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.binary_int_float[] | integer | 是 | 整数变量在x中的位置；格式：int32 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c | array[Expr] | 是 | min/max c^T*x |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.c[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[9].SimpleMilp.constraint_type | array[Operation] | 是 |  |
| aoes[].actions[].action.oneOf[9].SimpleMilp.constraint_type[] | string | 是 | Mathematical operations.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[9].SimpleMilp.min_or_max | boolean | 是 | min: true, max: false |
| aoes[].actions[].action.oneOf[9].SimpleMilp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| aoes[].actions[].action.oneOf[9].SimpleMilp.x_lower | array[array[any]] | 是 | 变量的下界约束：变量位置、约束表达式 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.x_name | array[string] | 是 | 变量名称 |
| aoes[].actions[].action.oneOf[9].SimpleMilp.x_upper | array[array[any]] | 是 |  |
| aoes[].actions[].action.oneOf[10] | object | 是 | 非整数线性规划 |
| aoes[].actions[].action.oneOf[10].Nlp | object | 是 | 非整数线性规划 |
| aoes[].actions[].action.oneOf[10].Nlp.g | array[Expr] | 是 | 等式约束式 g(x) == b |
| aoes[].actions[].action.oneOf[10].Nlp.g[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.g[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower | array[Expr] | 是 | 不等式约束式 g(x) <= b |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.g_lower[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper | array[Expr] | 是 | 不等式约束式 g(x) >= b |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.g_upper[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.min_or_max | boolean | 是 | min: true, max: false |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr | object | 是 | 目标函数表达式 min obj |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.obj_expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.parameters | object[string, string] | 是 | 求解器参数：参数名、参数值；额外属性：string |
| aoes[].actions[].action.oneOf[10].Nlp.x_init | array[Expr] | 是 | 变量初始值x0 |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.x_init[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower | array[Expr] | 是 | 整数变量在x中的位置 |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.x_lower[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.x_name | array[string] | 是 | 变量名称 |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper | array[Expr] | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[] | object | 是 | 表达式对象 |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn | array[Token] | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[12] | object | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].actions[].action.oneOf[10].Nlp.x_upper[].rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].actions[].aoe_id | integer | 是 | AOE id；格式：int64 |
| aoes[].actions[].failure_mode | string | 是 | action失败时的处理方式；可选值：Default、Ignore、StopAll、StopFailed |
| aoes[].actions[].name | string | 是 | 动作名称 |
| aoes[].actions[].source_node | integer | 是 | 源节点；格式：int64 |
| aoes[].actions[].target_node | integer | 是 | 目标节点；格式：int64 |
| aoes[].events | array[EventNode] | 是 | 节点列表 |
| aoes[].events[] | object | 是 | 节点对象 |
| aoes[].events[].aoe_id | integer | 是 | AOE id；格式：int64 |
| aoes[].events[].expr | object | 是 | 事件是否发生判断的bool表达式 |
| aoes[].events[].expr.rpn | array[Token] | 是 |  |
| aoes[].events[].expr.rpn[] | oneOf[object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func}] | 是 | Expression tokens.；可选值：LParen、RParen、BigLParen、BigRParen、RBracket、Comma；可选结构：object{Binary} | object{Unary} | string | object{Number} | object{Tensor} | object{Var} | object{Str} | object{Func} |
| aoes[].events[].expr.rpn[].oneOf[1] | object | 是 | Binary operation. |
| aoes[].events[].expr.rpn[].oneOf[1].Binary | string | 是 | Binary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].events[].expr.rpn[].oneOf[2] | object | 是 | Unary operation. |
| aoes[].events[].expr.rpn[].oneOf[2].Unary | string | 是 | Unary operation.；可选值：Plus、Minus、Times、Div、Rem、Pow、Fact、Equal、Unequal、LessThan、GreatThan、LtOrEqual、GtOrEqual、And、Or、Not、BitAnd、BitOr、BitXor、BitShl、BitShr、BitAt、BitNot、DotTimes、DotDiv、LeftDiv、DotPow、Transpose |
| aoes[].events[].expr.rpn[].oneOf[3] | string | 是 | Left parenthesis.   (；可选值：LParen |
| aoes[].events[].expr.rpn[].oneOf[4] | string | 是 | Right parenthesis.  )；可选值：RParen |
| aoes[].events[].expr.rpn[].oneOf[5] | string | 是 | Big Left parenthesis.  {；可选值：BigLParen |
| aoes[].events[].expr.rpn[].oneOf[6] | string | 是 | Big Right parenthesis. }；可选值：BigRParen |
| aoes[].events[].expr.rpn[].oneOf[7] | string | 是 | Right brackets. ]；可选值：RBracket |
| aoes[].events[].expr.rpn[].oneOf[8] | string | 是 | Comma: function argument separator；可选值：Comma |
| aoes[].events[].expr.rpn[].oneOf[9] | object | 是 | A number. |
| aoes[].events[].expr.rpn[].oneOf[9].Number | number | 是 | A number.；格式：double |
| aoes[].events[].expr.rpn[].oneOf[10] | object | 是 | A tensor. |
| aoes[].events[].expr.rpn[].oneOf[10].Tensor | integer | 是 | A tensor.；允许空值 |
| aoes[].events[].expr.rpn[].oneOf[11] | object | 是 | A variable. |
| aoes[].events[].expr.rpn[].oneOf[11].Var | string | 是 | A variable. |
| aoes[].events[].expr.rpn[].oneOf[12] | object | 是 |  |
| aoes[].events[].expr.rpn[].oneOf[12].Str | string | 是 |  |
| aoes[].events[].expr.rpn[].oneOf[13] | object | 是 | A function with name and number of arguments. |
| aoes[].events[].expr.rpn[].oneOf[13].Func | array[object] | 是 | A function with name and number of arguments. |
| aoes[].events[].id | integer | 是 | 节点id；格式：int64 |
| aoes[].events[].name | string | 是 | 节点名 |
| aoes[].events[].node_type | string | 是 | 节点类型；可选值：ConditionNode、SwitchNode、SwitchOfActionResult |
| aoes[].events[].timeout | integer | 是 | 事件还未发生时等待超时时间；格式：int64 |
| aoes[].id | integer | 是 | aoe id；格式：int64 |
| aoes[].name | string | 是 | aoe名称 |
| aoes[].trigger_type | oneOf[object{SimpleRepeat} | object{TimeDrive} | string | object{EventRepeatMix} | object{EventTimeMix}] | 是 | 触发类型；可选值：EventDrive；可选结构：object{SimpleRepeat} | object{TimeDrive} | string | object{EventRepeatMix} | object{EventTimeMix} |
| aoes[].trigger_type.oneOf[1] | object | 是 | 简单固定周期触发 |
| aoes[].trigger_type.oneOf[1].SimpleRepeat | object | 是 | 简单固定周期触发 |
| aoes[].trigger_type.oneOf[1].SimpleRepeat.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| aoes[].trigger_type.oneOf[1].SimpleRepeat.secs | integer | 是 | 秒；格式：int64 |
| aoes[].trigger_type.oneOf[2] | object | 是 | cron表达式 |
| aoes[].trigger_type.oneOf[2].TimeDrive | string | 是 | cron表达式 |
| aoes[].trigger_type.oneOf[3] | string | 是 | 事件驱动，AOE开始节点条件满足即触发；可选值：EventDrive |
| aoes[].trigger_type.oneOf[4] | object | 是 | 事件驱动 && 简单固定周期 联合 |
| aoes[].trigger_type.oneOf[4].EventRepeatMix | object | 是 | 事件驱动 && 简单固定周期 联合 |
| aoes[].trigger_type.oneOf[4].EventRepeatMix.nanos | integer | 是 | 剩余纳秒；格式：int32 |
| aoes[].trigger_type.oneOf[4].EventRepeatMix.secs | integer | 是 | 秒；格式：int64 |
| aoes[].trigger_type.oneOf[5] | object | 是 | 事件驱动 && cron表达式 联合 |
| aoes[].trigger_type.oneOf[5].EventTimeMix | string | 是 | 事件驱动 && cron表达式 联合 |
| aoes[].variables | array[array[any]] | 是 | 用户自定义的变量：变量名和表达式 |
| commit_msg | string | 是 | 版本描述 |
| version | integer | 是 | 版本号；格式：int32 |


### 查询当前应用的AOE

- **方法**: `GET`
- **路径**: `/pscpu/aoes/models`
- **工具名**: `get_pscpu_aoes_models`

### 查询当前应用的AOE版本号

- **方法**: `GET`
- **路径**: `/pscpu/aoes/version`
- **工具名**: `get_pscpu_aoes_version`

### 查询配置信息

- **方法**: `GET`
- **路径**: `/pscpu/info`
- **工具名**: `get_pscpu_info`

### 更新当前应用的电气岛

- **方法**: `POST`
- **路径**: `/pscpu/island`
- **工具名**: `add_pscpu_island`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commit_msg | string | 是 | 版本描述 |
| island | object | 是 | 电气岛 |
| island.cns | array[CN] | 是 | 连接节点列表 |
| island.cns[] | object | 是 | 连接节点 |
| island.cns[].id | integer | 是 | 连接节点id；格式：int64 |
| island.cns[].psr_id | string | 是 | 资源id |
| island.cns[].terminals | array[integer] | 是 | 端子id数组 |
| island.cns[].terminals[] | integer | 是 | 端子id数组；格式：int64 |
| island.measures | object[string, array[MeasureDef]] | 是 | 测点，设备id->测点列表；额外属性：array[MeasureDef] |
| island.prop_groups | object[string, RsrPropGroup] | 是 | 属性分组，属性分组id->属性分组；额外属性：RsrPropGroup |
| island.resources | object[string, NetworkRsr] | 是 | 资源，设备id->资源对象；额外属性：NetworkRsr |
| prop_defs | array[PropDefine] | 是 | 属性定义数组 |
| prop_defs[] | object | 是 | 设备属性 |
| prop_defs[].data_type | string | 是 | 属性类型；可选值：U8、U16、U32、U64、I8、I16、I32、I64、F32、F64、Str、Complex32、Complex64、TensorF32、TensorF64、TensorC32、TensorC64、Unknown |
| prop_defs[].data_unit | string | 是 | 属性单位；可选值：OnOrOff、A、V、kV、W、kW、MW、Var、kVar、MVar、VA、kVA、MVA、H、mH、Ah、mAh、kWh、Celsius、feet、km、meter、mm2、degree、rad、UnitOne、Percent、bit、B、kB、MB、GB、TB、PB、Unknown |
| prop_defs[].desc | string | 是 | 属性定义描述 |
| prop_defs[].id | integer | 是 | 属性定义id；格式：int64 |
| prop_defs[].name | string | 是 | 属性定义标识 |
| rsr_defs | array[RsrDefine] | 是 | 设备定义数组 |
| rsr_defs[] | object | 是 | 设备定义 |
| rsr_defs[].desc | string | 是 | 设备定义的描述 |
| rsr_defs[].id | integer | 是 | 定义id；格式：int64 |
| rsr_defs[].name | string | 是 | 设备类别名称 |
| rsr_defs[].prop_groups | array[PropGroupDefine] | 是 | 设备属性 |
| rsr_defs[].prop_groups[] | object | 是 | 属性分组定义 |
| rsr_defs[].prop_groups[].desc | string | 是 | 属性定义描述 |
| rsr_defs[].prop_groups[].name | string | 是 | 属性定义标识 |
| rsr_defs[].prop_groups[].prop_defines | array[integer] | 是 | 设备属性实际描述 |
| rsr_defs[].prop_groups[].prop_defines[] | integer | 是 | 设备属性实际描述；格式：int64 |
| rsr_defs[].rsr_type | string | 是 | 设备所属类型；可选值：Switch、Busbar、ACline、DCline、Winding、SyncGenerator、ESS、PCS、Transformer、Load、ShuntCompensator、SerialCompensator、ShuntReactor、ShuntCapacitor、SeriesReactor、SeriesCapacitor、Breaker、Disconnector、GroundDisconnector、SVC、SVG、Feeder、PWBusbar、Cable、Regulator、Connector、Measurement、Company、SubIsland、LoadArea、Substation、PowerPlant、VoltageLevel、BaseVoltage、HvdcSys、HvdcPoleSys、DCPole、DCLineDot、TLineDot、Converter、TLine、ACLineDot、TNode、Convergenceline、SeriesPowerTransformer、SeriesTransformerWinding、Acfilter、Synccondenser、DCBreaker、DCDisconnector、Signal、Combined、Composite、Section、SectionType、Bus、Branch、UserDefine1、UserDefine2、UserDefine3、UserDefine4、UserDefine5、UserDefine6、UserDefine7、UserDefine8、UserDefine9、UserDefine10、Unknown |
| rsr_defs[].terminal_num | integer | 是 | 端口数量；格式：int32 |
| version | integer | 是 | 版本号；格式：int32 |


### 查询当前应用的电气岛

- **方法**: `GET`
- **路径**: `/pscpu/island/models`
- **工具名**: `get_pscpu_island_models`

### 查询所有的测点路径（设备树）

- **方法**: `GET`
- **路径**: `/pscpu/island/paths`
- **工具名**: `get_pscpu_island_paths`

### 查询测点树

- **方法**: `GET`
- **路径**: `/pscpu/island/point_tree`
- **工具名**: `get_pscpu_island_point_tree`

### 查询当前应用的电气岛版本号

- **方法**: `GET`
- **路径**: `/pscpu/island/version`
- **工具名**: `get_pscpu_island_version`

### 更新当前应用的测点

- **方法**: `POST`
- **路径**: `/pscpu/points`
- **工具名**: `add_pscpu_points`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| beeid_to_points | array[array[any]] | 是 | beeId和测点列表对应的数组，tuple格式为(beeId:String, 测点列表:u64[]) |
| commit_msg | string | 是 | 版本描述 |
| points | array[Measurement] | 是 | 测点列表 |
| points[] | object | 是 | 测点对象 |
| points[].alarm_level1_expr | string | 是 | 告警级别1的表达式 |
| points[].alarm_level2_expr | string | 是 | 告警级别2的表达式 |
| points[].alias_id | string | 是 | 字符串id |
| points[].change_expr | string | 是 | 判断是否"变化"的公式，用于变化上传或储存 |
| points[].data_unit | string | 是 | 单位 |
| points[].desc | string | 是 | Description |
| points[].expression | string | 是 | 如果是计算点，这是表达式 |
| points[].init_value | integer | 是 | 默认值存储在8个字节，需要根据is_discrete来转换成具体的值；格式：int64 |
| points[].inv_trans_expr | string | 是 | 逆变换公式 |
| points[].is_computing_point | boolean | 是 | 是否是计算点 |
| points[].is_discrete | boolean | 是 | 是否是离散量 |
| points[].is_realtime | boolean | 是 | 如是，则不判断是否"变化"，均上传 |
| points[].is_soe | boolean | 是 | 是否是soe点 |
| points[].lower_limit | number | 是 | 下限，用于坏数据辨识；格式：double |
| points[].point_id | integer | 是 | 唯一的id；格式：int64 |
| points[].point_name | string | 是 | 测点名 |
| points[].trans_expr | string | 是 | 变换公式 |
| points[].upper_limit | number | 是 | 上限，用于坏数据辨识；格式：double |
| points[].zero_expr | string | 是 | 判断是否为0值的公式 |
| source_name | array[array[any]] | 是 |  |
| version | integer | 是 | 版本号；格式：int32 |


### 查询设备关联的测点

- **方法**: `GET`
- **路径**: `/pscpu/points/by_dev/{dev_id}`
- **工具名**: `get_pscpu_points_by_dev`
- **参数**:
  - `dev_id` (path, integer, 必填): 设备id；元信息：format=int64

### 查询当前应用的测点

- **方法**: `GET`
- **路径**: `/pscpu/points/models`
- **工具名**: `get_pscpu_points_models`
- **参数**:
  - `id` (query, string, 可选): 元信息：nullable=true
  - `name` (query, string, 可选): 元信息：nullable=true
  - `is_soe` (query, boolean, 可选): 元信息：nullable=true

### 查询量测值

- **方法**: `GET`
- **路径**: `/pscpu/points/values/{src}`
- **工具名**: `get_pscpu_points_values_by_src`
- **参数**:
  - `id` (query, integer, 可选): 测点id（优先）；元信息：format=int64, nullable=true
  - `ids` (query, string, 可选): 测点id列表，以,间隔；元信息：nullable=true
  - `src` (path, integer, 必填): 元信息：format=int32

### 查询当前应用的测点版本号

- **方法**: `GET`
- **路径**: `/pscpu/points/version`
- **工具名**: `get_pscpu_points_version`

### 重置pscpu

- **方法**: `POST`
- **路径**: `/pscpu/reset`
- **工具名**: `add_pscpu_reset`

### 启动pscpu

- **方法**: `POST`
- **路径**: `/pscpu/start`
- **工具名**: `add_pscpu_start`
- **请求体**:

  - 无法解析请求体结构


### 停止pscpu

- **方法**: `POST`
- **路径**: `/pscpu/stop`
- **工具名**: `add_pscpu_stop`

***

## SCRIPTS 模块

### 查询7z脚本文件

- **方法**: `GET`
- **路径**: `/script_file/{script_id}`
- **工具名**: `get_script_file_by_script`
- **参数**:
  - `script_id` (path, integer, 必填): 脚本id；元信息：format=int64

### 查询脚本md5

- **方法**: `GET`
- **路径**: `/script_md5`
- **工具名**: `get_script_md5`
- **参数**:
  - `id` (query, integer, 可选): 测点id（优先）；元信息：format=int64, nullable=true
  - `ids` (query, string, 可选): 测点id列表，以,间隔；元信息：nullable=true

### 查询所有脚本结果

- **方法**: `GET`
- **路径**: `/script_results`
- **工具名**: `get_script_results`

### 新增脚本结果

- **方法**: `POST`
- **路径**: `/script_results`
- **工具名**: `add_script_results`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| make_time | integer | 是 | 格式：int64 |
| model_id | integer | 是 | 格式：int64 |
| script_id | integer | 是 | 格式：int64 |
| target | string | 是 | 可选值：Aoe、Dff |


### 查询指定id脚本结果

- **方法**: `GET`
- **路径**: `/script_results/{id}`
- **工具名**: `get_script_results_by`
- **参数**:
  - `id` (path, integer, 必填): 脚本结果id；元信息：format=int64

### 保存脚本对应的wasm和js文件

- **方法**: `POST`
- **路径**: `/script_wasm`
- **工具名**: `add_script_wasm`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| js_file | array[integer] | 是 | js文件内容 |
| js_file[] | integer | 是 | js文件内容；格式：int32 |
| module_name | string | 是 | 模块名称 |
| script_id | integer | 是 | 脚本id；格式：int64 |
| wasm_file | array[integer] | 是 | wasm文件内容 |
| wasm_file[] | integer | 是 | wasm文件内容；格式：int32 |


### 查询指定id脚本

- **方法**: `GET`
- **路径**: `/scripts`
- **工具名**: `get_scripts`
- **参数**:
  - `id` (query, integer, 可选): 测点id（优先）；元信息：format=int64, nullable=true
  - `ids` (query, string, 可选): 测点id列表，以,间隔；元信息：nullable=true

### 新增脚本

- **方法**: `POST`
- **路径**: `/scripts`
- **工具名**: `add_scripts`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| desc | string | 是 | 脚本描述 |
| id | integer | 是 | 脚本id；格式：int64 |
| is_file_uploaded | boolean | 是 | 文件是否已上传 |
| is_js | boolean | 是 | 是否是javascript文件 |
| path | string | 是 | 脚本路径 |
| target | string | 是 | 脚本目标；可选值：Aoe、Dff |
| wasm_module_name | string | 是 | wasm模块名称 |
| wasm_update_time | integer | 是 | wasm上传时间；格式：int64 |


### 删除指定id的脚本

- **方法**: `DELETE`
- **路径**: `/scripts/{ids}`
- **工具名**: `delete_scripts_by_s`
- **参数**:
  - `ids` (path, string, 必填): 脚本id列表，以,间隔

***

## SYSTEM 模块

### 执行map映射操作

- **方法**: `POST`
- **路径**: `/common_map`
- **工具名**: `add_common_map`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| oneOf[1] | object | 是 | 查询 |
| oneOf[1].Query | array[integer] | 是 | 查询 |
| oneOf[1].Query[] | integer | 是 | 查询；格式：int32 |
| oneOf[2] | object | 是 | 增加 |
| oneOf[2].Update | array[array[integer]] | 是 | 增加 |
| oneOf[2].Update[] | array[integer] | 是 | 增加 |
| oneOf[2].Update[][] | integer | 是 | 增加；格式：int32 |
| oneOf[3] | object | 是 |  |
| oneOf[3].Update2 | array[array[integer]] | 是 |  |
| oneOf[3].Update2[] | array[integer] | 是 |  |
| oneOf[3].Update2[][] | integer | 是 | 格式：int32 |
| oneOf[4] | object | 是 | 删除 |
| oneOf[4].Delete | array[integer] | 是 | 删除 |
| oneOf[4].Delete[] | integer | 是 | 删除；格式：int32 |


### 查询Eig配置

- **方法**: `GET`
- **路径**: `/config`
- **工具名**: `get_config`

### 保存Eig配置

- **方法**: `POST`
- **路径**: `/config`
- **工具名**: `add_config`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| properties | object[string, string] | 是 | 主要配置属性；额外属性：string |
| properties2 | object[string, string] | 是 | 次要配置属性；额外属性：string |


### 查看ping结果

- **方法**: `GET`
- **路径**: `/ping`
- **工具名**: `get_ping`

***

## TAG_DEFINES 模块

### 查询指定分组的标签名称及id列表

- **方法**: `GET`
- **路径**: `/tag_defines/{group}`
- **工具名**: `get_tag_defines_by_group`
- **参数**:
  - `id` (path, integer, 必填): 分组id；元信息：format=int32
  - `group` (path, integer, 必填): 元信息：format=int32

***

## TAGS 模块

### 更新指定分组下标签名和测点数组关系

- **方法**: `PUT`
- **路径**: `/tags/{group}`
- **工具名**: `update_tags_by_group`
- **参数**:
  - `group` (path, integer, 必填): 分组id；元信息：format=int32
- **请求体**:

  - 无法解析请求体结构


### 删除指定分组下标签id和测点的关系

- **方法**: `DELETE`
- **路径**: `/tags/{group}`
- **工具名**: `delete_tags_by_group`
- **参数**:
  - `group` (path, integer, 必填): 分组id；元信息：format=int32
- **请求体**:

  - 无法解析请求体结构


***

## TAGS_CBOR 模块

### 查询指定分组下标签id对应的测点数组

- **方法**: `POST`
- **路径**: `/tags_cbor/{group}`
- **工具名**: `add_tags_cbor_by_group`
- **参数**:
  - `id` (path, integer, 必填): 分组id；元信息：format=int32
  - `group` (path, integer, 必填): 元信息：format=int32
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [] | integer | 是 | 格式：int32 |


***

## WEBPLUGINS 模块

### 保存插件对应的file

- **方法**: `POST`
- **路径**: `/webplugin_file`
- **工具名**: `add_webplugin_file`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| plugin_id | integer | 是 | 插件id；格式：int64 |
| sevenz_file | array[integer] | 是 | 内容 |
| sevenz_file[] | integer | 是 | 内容；格式：int32 |


### 查询插件对应的压缩文件

- **方法**: `GET`
- **路径**: `/webplugin_file/{plugin_id}`
- **工具名**: `get_webplugin_file_by_plugin`
- **参数**:
  - `plugin_id` (path, integer, 必填): 插件id；元信息：format=int64

### 查询插件md5

- **方法**: `GET`
- **路径**: `/webplugin_md5`
- **工具名**: `get_webplugin_md5`
- **参数**:
  - `id` (query, integer, 可选): 测点id（优先）；元信息：format=int64, nullable=true
  - `ids` (query, string, 可选): 测点id列表，以,间隔；元信息：nullable=true

### 查询所有界面插件

- **方法**: `GET`
- **路径**: `/webplugins`
- **工具名**: `get_webplugins`

### 新增插件

- **方法**: `POST`
- **路径**: `/webplugins`
- **工具名**: `add_webplugins`
- **请求体**:

| 字段名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | integer | 是 | 插件id；格式：int64 |
| is_file_uploaded | boolean | 是 | 文件是否已经上传 |
| is_monopoly | boolean | 是 | if is only one view |
| model_name | string | 是 | wasm或js或html文件的名称 |
| name | string | 是 | 在浏览模式下显示的名称 |
| path | string | 是 | 文件树中的路径 |


### 删除指定id的插件

- **方法**: `DELETE`
- **路径**: `/webplugins/{ids}`
- **工具名**: `delete_webplugins_by_s`
- **参数**:
  - `ids` (path, string, 必填): 插件id列表，以,间隔

### 查询指定id插件

- **方法**: `GET`
- **路径**: `/webplugins/{plugin_id}`
- **工具名**: `get_webplugins_by_plugin`
- **参数**:
  - `plugin_id` (path, integer, 必填): 插件id；元信息：format=int64

***

