# 贡献地图祛魅实现计划

> 状态：已定稿。本计划记录已选实现方向与执行边界；计划定稿不等同于实现、审查或前向验收已经完成。

## Intended result and selected direction

目标是把“贡献地图”落实为 Quick/Deep 输出前都必须完成的内部重建，而不是把祛魅退化为默认的边界审计。对每篇材料，主流程必须先完成同一条贡献地图：

1. 枚举文章声称的全部候选技术、系统、实验或叙事增量；
2. 调研相关设计与领域脉络，识别会改变判断的近邻和已有路线；
3. 核验目标设计、实验结果与文章叙事是否共同支持这些声称；
4. 在 Quick 或 Deep 成文前，还原文章实际做了什么、实际创新是什么、实际贡献是什么。

Quick 必须覆盖所有会影响理解的重要设计和贡献，只压缩方程、图表和实验细节；Deep 保留同一贡献地图判断并展开所需细节。默认输出不添加独立的边界审计腔或固定边界段；只有会改变实际内容、创新、贡献或结果归因的范围信息才进入相应解释。

实现范围限定为：`skill-src/core.md`、`skill-src/depth/quick.md`、`skill-src/depth/deep.md`；`evals/cases.yaml`；`README.md`、`README_EN.md`；以及由 `scripts/sync_skills.py` 生成的两个 `skills/` 目录结果。保持 `skill-src/` 为唯一指令源码，不手工改写生成文件；只在现有视觉与新叙事顺序发生矛盾时更新已有视觉。保留当前 dirty worktree，不创建或切换 Git 分支，不覆盖无关改动，也不删除旧 alias 或其他兼容表面。

## Work, ownership, and dependencies

按依赖顺序执行以下工作单元；每个 owner 只修改所列目标表面，并为下游保留可检查的行为契约。

1. **冻结范围并保护 dirty worktree（Root / 集成 owner）**
   - 目标：在实施开始前记录当前工作树状态和本计划的四个目标表面，确认本轮只纳入贡献地图方向相关文件。
   - 保护行为：不还原、覆盖或重排已有用户改动；不创建分支；生成目录只在源文件变更并完成检查后同步。
   - 依赖/验证：无上游依赖；以 `git status --short`、目标文件清单和 focused diff 作为范围基线。

2. **建立强制贡献地图重建（Source owner）**
   - 目标文件：`skill-src/core.md`、`skill-src/depth/quick.md`、`skill-src/depth/deep.md`。
   - 结果：把“候选增量枚举 → 相关设计/领域研究 → 目标设计、实验、叙事核验 → 实际内容/创新/贡献重建”写成 Quick/Deep 共有的前置契约；让贡献判断来自重建后的证据整合，而不是作者标签或默认 boundary-only 检查。
   - Quick 保护行为：所有重要设计和贡献都必须在摘要中出现；方程、图表、实验只按解释负荷压缩；不把“重要设计”缩成少数身份原子；不强制固定可见章节。
   - Deep 保护行为：沿用同一重建结论并展开需要复现、理解或归因的公式、图表、实验和叙事细节；不因共享契约而退化为 Quick。
   - 共同保护行为：不把默认边界段、重复的“是 X/不是 Y”清单或限制清单当作祛魅本身；边界信息仅在改变实际重建时出现。
   - 依赖/验证：依赖步骤 1；逐段检查四步顺序、Quick 完整覆盖/细节压缩、Deep 展开差异和无默认边界 prose 是否能被静态识别。

3. **锁定 paired Quick/Deep 与材料门槛回归（Eval owner）**
   - 目标文件：`evals/cases.yaml`。
   - 结果：新增一组共享同一合成多主张材料的 Quick/Deep 配对回归，要求两者都完成候选增量枚举、相关设计/领域核验和实际内容/创新/贡献重建；Quick 覆盖所有重要设计/贡献但压缩细节，Deep 展开细节而不改变实质判断。
   - 结果：新增 Quick no-subagent/material gating 回归，检查无 subagent 或材料不足时不会跳过贡献地图、伪造领域/创新结论或用裸分代替证据，并会披露受限范围。
   - 保护行为：回归必须能区分真正的去包装重建、只做边界审计、Quick 过度删减和 Deep 过度压缩；不把固定字数、固定章节或全图表覆盖变成 Quick 的隐性要求。
   - 依赖/验证：依赖步骤 2 的文本契约；解析 YAML，并在目标 harness 中运行这组 paired cases、no-subagent/material case 及其相邻 Quick/Deep 路由回归。

4. **同步双语公共说明与条件性视觉（Docs owner）**
   - 目标文件：`README.md`、`README_EN.md`；仅在必要时更新仓库已有视觉资源。
   - 结果：中英文都说明贡献地图是 Quick/Deep 成文前的强制重建，列出四步顺序，说明 Quick 覆盖重要设计/贡献而压缩方程、图表、实验细节，说明 Deep 的展开边界，并明确默认不输出独立边界审计段。
   - 保护行为：不把实现细节、内部账本或未验证判断写成用户承诺；视觉只修正与新顺序直接冲突的现有图，不新增无关素材。
   - 依赖/验证：依赖步骤 2；逐项中英文对照和 focused diff，若改视觉则检查其箭头/节点顺序与文字契约一致。

5. **生成并静态验证派生 Skill（Root / 集成 owner）**
   - 目标表面：两个 `skills/*/SKILL.md` 与 `skills/*/agents/openai.yaml`，由 `scripts/sync_skills.py` 生成。
   - 结果：运行 `python3 scripts/sync_skills.py`，使派生文件反映已审阅的 source/profile 契约；随后运行 `python3 scripts/sync_skills.py --check` 确认无漂移。
   - 保护行为：不直接编辑生成文件来绕过 source；保留各自 frontmatter 名称、默认调用 alias 和 `allow_implicit_invocation: false`。
   - 依赖/验证：依赖步骤 2–4；审阅两个生成 `SKILL.md` 和两个 metadata 文件的 focused diff，执行 `git diff --check`，并解析 `evals/cases.yaml` 与 Teamwork index JSON。

6. **独立审查与 clean real-path 前向验收（Independent reviewer + Root）**
   - 目标表面：source、生成结果、eval、README、必要视觉以及临时测试输出（测试输出不入库）。
   - 结果：独立 reviewer 在不预先获得预期修复方案的情况下，检查贡献地图四步是否真正成为前置契约、Quick/Deep 是否保持同一实质判断而仅改变展开粒度、默认边界 prose 是否消失、材料门槛是否诚实。
   - 结果：在干净新会话中使用选定的 Dyna-2-like 材料和对应 Quick/Deep 调用，观察真实输出是否先完成贡献地图重建，再给出覆盖重要设计/贡献的祛魅解释；no-subagent/material 限制必须按回归契约披露。
   - 依赖/验证：依赖步骤 5；reviewer 给出接受或退回结论，Root 保存前向运行标识和可复核输出片段，不把未执行的复现、未取得的材料或未观察到的效果写成已完成。

依赖关系为：步骤 1 → 2；步骤 2 → 3、4；步骤 2–4 → 5；步骤 5 → 6。步骤 3 与步骤 4 在步骤 2 完成后可并行，但不得修改彼此目标表面。

## Verification

- **源与派生一致性**：`python3 scripts/sync_skills.py --check` 返回成功；生成的两个 Skill 与 metadata 均只反映 `skill-src/` 的已审阅内容。
- **结构与格式**：解析 `evals/cases.yaml`；运行 Teamwork schema-v4 index validator（`docs/teamwork/index.json --documents`）；运行 `python3 -m json.tool docs/teamwork/index.json` 和 `git diff --check`；审阅 focused diff，确认无意外文件、分支或 dirty worktree 覆盖。
- **行为回归**：在目标 harness 运行新增 paired Quick/Deep synthetic multi-claim cases、Quick no-subagent/material gating case，以及受影响的相邻 routing/Quick/Deep cases。验收重点是四步贡献地图、重要设计/贡献完整覆盖、Quick 细节压缩、Deep 细节展开和无默认 boundary-only prose。
- **独立真实路径**：在干净新会话完成选定 Dyna-2-like Quick/Deep 前向测试；记录输出中候选增量、相关设计/领域核验、目标设计/实验/叙事核验、实际内容/创新/贡献重建的可观察证据，并由独立 reviewer 复核。

## Blockers and stop or replan conditions

执行在以下任一情况出现时停止并返回 Root 重规划，不用假设补齐：

- 用户改变已选方向，或要求把贡献地图改成另一个可见输出架构、完整精读义务或默认边界审计流程；
- `skill-src/` 与生成目标的 owner、接口或 source-of-truth 关系发生变化，`scripts/sync_skills.py` 无法安全生成，或只能通过手工改派生文件绕过同步；
- 当前 dirty worktree 无法在不覆盖用户改动的前提下实施，或出现创建/切换分支、删除 alias、扩大目标表面的要求；
- paired eval 无法区分“完整贡献地图重建”与“只列边界/只列少数原子”，或 no-subagent/material gating 仍允许无证据的创新、贡献、领域结论或裸分；
- Quick 为满足“紧凑”被迫删除重要设计/贡献、引入固定字数/固定章节，或 Deep 与 Quick 的实质判断发生漂移；
- README/已有视觉的顺序冲突需要超出本计划范围的重绘或新增素材；
- 无法获得可复核的 Dyna-2-like 材料、干净前向路径或独立 reviewer，因而不能观察承诺的行为；此时不得把静态通过写成真实路径完成；
- 任一 JSON/YAML/差异检查失败，或 focused diff 暴露计划外文件和未授权变更。
