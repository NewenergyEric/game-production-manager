# 从意图到执行的工作包

`schema_version=0.1`。原始要求、有效决定、任务计划、执行证据和验收是不同层。

| 层 | 字段与用途 |
|---|---|
| Project | id、version、goal、strategy、constraints、scope_in/out、assumptions |
| Requirements | id、text、source、status（confirmed/proposed）、acceptance、owner_role |
| Deliverables | id、requirement_ids、name、type、spec、acceptance、reviewer_role |
| Assets | 作为 type=asset 的交付物，spec 写 category/family/base_or_variant/states/source_format/runtime_format/art_pack_ref |
| Tasks | id、deliverable_ids、depends_on、owner_role、executor_kind（human/agent/either）、inputs、action、acceptance、status、artifacts、review |
| Milestones | id、goal、task_ids、exit_criteria；日历时间依赖真实容量另行核定 |
| Feedback | id、source、target_ids、observation、proposed_change、status；确认后发布新版本 |

`inputs` 至少指明有效版本或明确缺口；外部美术 Feature 绑定放适配文件，不添加现有 Art Director 原请求不接受的字段。

## 状态和交接

任务状态：planned / ready / in_progress / submitted / accepted / blocked / cancelled。submitted 需要实际产物引用；accepted 还需要 pass 的验收记录、reviewer、authority_reference 与证据。结构检查只能判断字段/关系，不能验证私人仓库外的字节或艺术质量。

“计划采用 Agent”不是“Agent 已有制作能力”。执行契约明确工具、权限、预算、重试/停止与升级对象；工具不可用时交人工或标 blocked。当前工具不调度外部 Agent，不修改团队任务系统。

## 拆解到多细

任务应能由一个责任入口接收、产出可检查结果，并有明确依赖。复杂专业实现可由执行者进一步拆，不要求所有工作精确到小时。资产目录要覆盖状态与组合；估算区分基础制作、变体、评审、集成、测试。

`impact` 接受需求、交付物或任务 ID，列直接/间接受影响任务；提出修订，不自动重写批准内容。变更必须说明目标、范围、工期/资源、验收和旧任务处理方式。

同一工作包为各岗位生成视图；不维护互相冲突的手工副本。主策决定玩法，主美决定视觉，技术确定实现可行性，项目经理确保这些决定被正确理解和落实。
