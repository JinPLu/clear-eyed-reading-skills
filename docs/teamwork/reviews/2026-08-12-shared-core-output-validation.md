# 祛魅阅读共享核心与输出解耦候选的最终 Ordinary Review

## Candidate, scope, and criteria

本次 Review 覆盖本轮已生成、同步并安装的共享核心候选及其验证表面：

- `skill-src/core.md`；
- `skill-src/depth/quick.md` 与 `skill-src/depth/deep.md`；
- `skill-src/output/chat.md`；
- `scripts/sync_skills.py`；
- 生成的 `skills/clear-eyed-reading/`、`skills/clear-eyed-deep-reading/` 及其 `agents/openai.yaml`；
- `evals/cases.yaml`、`README.md`、`README_EN.md` 与 `CONTRIBUTING.md`；
- 两个 canonical 安装目录及其源文件字节一致性。

保护边界是：共享核心负责同一套“易懂 + 祛魅”读法，quick/deep 只改变输出展开粒度；chat renderer 只负责对话呈现，不复制阅读逻辑；当前图示要求以一张按需、简洁、可渲染的 Mermaid 流程/关系图为主，必要时仍展示或裁切决定性论文原图，不要求复杂 HTML、交互 artifact 或图集；HTML renderer 仍是未来扩展，不属于本轮交付。接受标准是源与生成结果一致、已安装 Skill 自包含、显式入口行为一致、回归与真实论文路径支持零基础理解和证据定标，并且多 subagent 调研不再以固定四篇替代领域、近邻和反证先例的充分覆盖。

## Outcome Fit

applicability: applicable

reason: 本轮架构、输出边界和真实论文验收均给出了可直接判断的目标。

evidence: `sync --check`、`py_compile`、两个官方 `quick_validate`、13 条 cases 的 YAML 解析和 `git diff --check` 均通过；canonical quick/deep 安装已校验，源文件与安装副本字节一致。VeloxSeg fresh deep thread `019ff184-767f-7ee2-974c-648e9e364e96` 自动启动 `field_landscape`、`nearest_work`、`counter_precedent` 三路 subagent，核对约 30 页正文、附录和代码，形成约 6690 字符的输出，并给出有意义的 JL 理论启发与实证定标判断。LIGO fresh quick thread `019ff188-79ca-7950-92cc-442a1f82e2ac` 同样启动三路调研，输出五段、约 2464 字符，且与领域前例一致。

findings: 早期前向测试暴露共同视觉失败（只给 fenced Mermaid、没有展示原图）；随后已修改 shared core/chat renderer，并定向复查确认可生成真实 `veloxseg-system-map.html` artifact 和论文图 2/3/4 裁图，文件存在且图 2 已由根 agent 视觉检查。经用户最新确认，HTML artifact 仅作为诊断证据，最终要求收敛为 Mermaid 足够；因此该修复满足当前输出边界，不把 artifact 当成默认交付。当前未见会阻止接受的 outcome-fit finding。

## Engineering Quality

applicability: applicable

reason: 候选包含 canonical 源、确定性生成脚本、生成文件、接口元数据、eval、文档和安装同步，工程一致性直接影响可维护性与宿主行为。

evidence: `scripts/sync_skills.py` 的检查与生成路径已验证；`sync --check`、`py_compile`、两份官方 `quick_validate`、13 条 cases YAML 解析和 `git diff --check` 全部通过。canonical quick/deep 安装已校验，生成的 Skill 保持自包含，源与安装副本逐字节一致。旧 deep 目录已移入 Trash；旧 quick 目录仍保留，因为删除选择尚未得到确认，不影响 canonical 安装校验。

findings: 未发现需要修复的工程质量问题。唯一需要保留的维护边界是：以后修改应继续只改 `skill-src`，再运行同步；HTML 只能作为新增 renderer 消费同一核心，不能在 HTML 中另写阅读逻辑。

## Real-Path Evidence

applicability: applicable

reason: 本轮声称了实际宿主线程、多路调研、全文材料核对、渲染和视觉呈现效果，必须用真实执行路径核对。

evidence: VeloxSeg deep 线程真实启动三路调研并合并领域脉络、近邻工作和反证先例；主 agent 核对了正文、附录与官方代码，输出没有停留在固定篇数摘要，而是形成了能区分 JL 的理论启发与实证支持范围的判断。LIGO quick 线程走同样的三路调研路径，压缩为五段短输出，且判断与领域前例相符。首次 VeloxSeg 外部研究约耗时 16 分钟，且需要根 agent 要求收敛；因此 core 后续增加了派工时传入贡献原子、截止时间和收敛门槛，以避免综述扩张。视觉定向复查已实际生成 `veloxseg-system-map.html` 并取得论文图 2/3/4 裁图；在最终输出契约中，图示以可渲染 Mermaid 为主，决定性原图按需展示或裁切。

findings: 实际运行证明了多 subagent 调研和视觉修复路径可用，但尚未在加入“贡献原子/截止/收敛门槛”后完成一次完整的二次端到端重跑。这是已知残余不确定性，不是已观察到的失败或接受阻塞；目前不能把该新收敛控制宣称为已完成的完整前向验证。

## Supersession and durable index state

`docs/teamwork/plans/2026-08-11-quick-reading-anti-mystification.md` 保留为历史记录，正文不改写。其中关于“固定四篇验证”和“保留旧 alias”的旧执行假设，已被 `docs/teamwork/discussions/2026-08-11-reading-core-output-separation.md` 与 `docs/teamwork/discussions/2026-08-11-multiagent-literature-research.md` 的后续决策取代，不能继续作为 active 执行方案。当前实现应以共享核心/输出解耦架构、多路证据调研和本 Review 的验证边界为准。

## Verdict

**ACCEPT**。源—生成—安装链路、回归检查和两条真实论文路径共同支持本轮“共享核心、深度 profile 与 chat 输出解耦”的目标；视觉失败已被发现并按最终 Mermaid 约束收敛；实验与调研解释围绕核心结论、创新和贡献，而非堆叠审稿式小问题。未完成的二次端到端重跑和旧 quick alias 的保留状态属于后续确认项，不构成当前候选的材料性阻塞。

## Residual Risk and Next Action

仍需记录两点：一是新加入的调研收敛门槛尚未经过完整第二轮 VeloxSeg/LIGO 端到端执行；二是旧 quick 安装目录是否删除尚未得到用户确认。下一步在需要发布或再次大改 core 时，使用最终 Mermaid renderer 做一次 fresh deep 与 quick 复查，并在取得删除授权后再处理旧 quick alias；在此之前不要把历史 quick plan 当作 active 方案，也不要把诊断用 HTML artifact 提升为默认输出要求。
