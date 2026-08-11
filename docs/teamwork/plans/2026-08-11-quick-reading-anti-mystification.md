# clear-eyed-reading 祛魅摘要优化执行计划

## Intended result and selected direction

目标是让 quick skill 继承 deep skill 已验证的“先让读者理解、再作判断”的读者顺序，但不继承 deep 的完整覆盖义务。默认输出面向零领域背景读者，先建立问题和方法的可运行心智模型，再帮助读者判断真实增量、证据强度和适用边界。

选定方向是：

`问题与必要背景 → 方法跑一遍 → 真正新在哪里 → 2–3 项决定性证据 → 主张收窄、五维评分与用途`

紧凑性不以硬字数门槛实现，而由一条主线、一个贯穿例子、2–3 项最改变判断的证据和非穷举覆盖共同形成。保留以下保护边界：

- 保留五维独立整数评分：创新性、严谨性、意义、清晰度、可复现/可复核性；不平均、不计算总分，证据不足时留空并说明缺什么；非完整论文不强套评分。
- 方法部分必须用同一个小例子走完核心输入到输出，并明确教学性解释不等于论文已经证明的结果。
- 证据只选 2–3 项真正改变判断的比较、消融、反例或证明；依赖图表时必须实际查看渲染后的原图/表并描述关键可见信息，但不引入逐图、逐公式或附录全覆盖义务。
- 内部仍需独立核验会改变创新判断的关键前例；只是把创新和真实增量放到读者理解方法之后再讲。未完成独立定位时，创新性和意义不评分。
- quick/deep 路由边界保持不变：quick 不退化为逐节精读、全实验盘点或固定模板；需要完整图表、公式、实验和附录覆盖时仍转 deep。

本计划只记录后续实施设计；当前阶段不修改候选 skill、README 或 eval 文件。

## Work, ownership, and dependencies

按依赖顺序执行以下工作单元：

1. **冻结范围与保护 dirty worktree（集成 owner）**
   - 目标：确认 quick 源目录、兼容安装副本和当前 dirty worktree，留存旧版真实输出作为前后对照。
   - 目标文件/表面：`skills/clear-eyed-reading/`、已发现的兼容安装目录、`git status --short` 与目标文件清单。
   - 结果与保护行为：只纳入 quick 优化所需目标；不触碰已修改的 `skills/clear-eyed-deep-reading/`、`docs/` 或无关文件，不删除旧兼容目录。
   - 依赖/验证：无上游依赖；以 `git status --short` 和目标文件清单确认范围。

2. **重建 quick 主线（Quick-skill implementer）**
   - 目标文件：`skills/clear-eyed-reading/SKILL.md`。
   - 结果：将默认叙事改为“问题与必要背景 → 方法跑一遍 → 真正新在哪里 → 2–3 项决定性证据 → 主张收窄/五维评分/用途”，以一个例子走通方法输入到输出。
   - 保护行为：不要求每节 verdict-first；教学版例子不得被写成论文结果；不引入 deep 的全量覆盖义务。
   - 依赖/验证：依赖步骤 1；逐段检查旧的“先判创新/成色，再讲方法”叙事已移除，同时保留读者可复述的主线。

3. **保留内部前例核验与评分边界（Quick-skill implementer）**
   - 目标文件：同上。
   - 结果：内部仍先独立核验会改变创新判断的关键前例，但最终叙述在方法理解后才说明前例和真实增量；未独立定位则创新性/意义不评分。
   - 保护行为：输出顺序变化不能放松创新性判断，也不能把“没查到”写成“作者没做”。
   - 依赖/验证：依赖步骤 2；检查材料不足和非论文行为仍有明确处理。

4. **收敛决定性证据与图表核验（Quick-skill implementer）**
   - 目标文件：同上。
   - 结果：每项证据交代任务/指标/比较对象、直接观察、能支持什么、不能证明什么；若依赖图或表，实际查看渲染原图/表后再写。
   - 保护行为：不机械抄数字，不把图注冒充视觉分析，不引入逐图或全实验覆盖要求。
   - 依赖/验证：依赖步骤 2；检查关键图表核验要求与非穷举边界同时存在。

5. **保留五维评分契约（Quick-skill implementer）**
   - 目标文件：同上。
   - 结果：完整论文保留五维独立整数评分；不平均、不总分；证据不足留空并说明缺口；博客、评论等不强套论文评分。
   - 保护行为：评分不能替代问题、方法和证据的解释。
   - 依赖/验证：依赖步骤 2；检查材料不足、非论文和评分行为的近邻边界。

6. **同步 skill metadata（Metadata owner）**
   - 目标文件：`skills/clear-eyed-reading/agents/openai.yaml`。
   - 结果：更新 UI 描述和默认提示，使其明确“先解释问题和方法，再作祛魅判断”；`default_prompt` 继续显式调用 `$clear-eyed-reading`。
   - 依赖/验证：依赖步骤 2；执行 YAML 解析并核对 frontmatter/skill metadata 一致性。

7. **同步双语说明并保护 deep 边界（Docs owner）**
   - 目标文件：`README.md`、`README_EN.md`。
   - 结果：quick 路径说明改为零基础读者先理解问题/方法、一个例子和少量决定性证据；明确 quick 不做完整图表、公式、实验、附录覆盖，deep 边界不变。
   - 依赖/验证：依赖步骤 2；逐项中英文核对，避免改写 deep 已有说明。

8. **更新回归契约（Eval owner）**
   - 目标文件：`evals/cases.yaml`。
   - 结果：更新 `quick-system-paper`、`quick-readable-output`、`routing-short`，新增 `quick-key-figure-evidence`；保留并复跑 `quick-insufficient-material`、`quick-non-paper`、`routing-deep` 及 deep 相关近邻案例。
   - 保护行为：用最小可观察断言锁定读者顺序、例子、决定性证据、图表核验、评分和路由边界，不把 quick 变成 deep 的全覆盖测试。
   - 依赖/验证：依赖步骤 2；执行 YAML 解析并检查路由近邻案例。

9. **同步兼容安装版本（Compatibility-sync owner）**
   - 目标文件：`$CODEX_HOME/skills/clear-eyed-paper-reading/SKILL.md`、对应 `agents/openai.yaml`。
   - 结果：在源版本静态检查通过后，将同一行为契约同步到旧安装兼容版。
   - 保护行为：保留兼容目录名、frontmatter 名 `clear-eyed-paper-reading` 和 `$clear-eyed-paper-reading` 默认提示；不能直接字节复制而破坏旧调用名，也不删除或改名旧 alias。
   - 依赖/验证：依赖步骤 2、6、8；逐项语义对照源版与兼容版。

10. **静态、真实论文对照与独立审查（Validation owner + fresh forward-test/reviewer agents）**
    - 目标表面：上述源版、兼容版、metadata、README、eval 和测试输出的临时位置（测试输出不入库）。
    - 结果：完成静态、路由和真实论文前后对照；独立 reviewer 只看论文、提示和输出，不预先获得预期修复方案。
    - 依赖/验证：依赖步骤 6–9；只有通过后才交付。

## Verification

真实输出采用四篇跨领域、公开且有完整正文与可读图表的论文；执行前再次确认原始全文可访问，否则替换为同类型公开主论文并记录原因：

1. Vaswani et al., *Attention Is All You Need*（方法/系统、架构与消融）；
2. Abbott et al., *Observation of Gravitational Waves from a Binary Black Hole Merger*（物理实证、图形证据与主张边界）；
3. RECOVERY Collaborative Group, *Dexamethasone in Hospitalized Patients with Covid-19*（临床随机试验、对照与统计解释）；
4. 1000 Genomes Project Consortium, *A global reference for human genetic variation*（生物/资源型研究、规模与泛化主张）。

对每篇用同一类零基础用户提示，在修改前后分别运行新鲜会话。候选输出必须同时满足：

- 在创新评价和评分前讲清问题、输入输出、困难与必要背景；
- 用一个贯穿例子让核心方法可在脑中运行；
- 只核验会改变结论的关键前例；
- 选 2–3 项决定性证据，并实际查看其中关键图或表；
- 分清论文报告、直接观察、分析推断和未知；
- 给出五维评分或明确留空原因；
- 不退化为逐节精读、全实验盘点或固定字数模板。

最终验证依次执行：

- 两个 quick skill 目录的 `quick_validate.py`；
- `evals/cases.yaml` 的 YAML 解析；
- 目标 harness 中所有变更 quick cases 加 `routing-deep`；
- `git diff --check` 与 focused diff；
- 源版 `$clear-eyed-reading` 和兼容版 `$clear-eyed-paper-reading` 各一次真实输出抽检；
- 独立 reviewer 对“读者顺序、边界、评分、图表核验、兼容别名”作接受/退回判断。

## Blockers and stop or replan conditions

执行应在以下任一条件出现时停止并重规划，而不是用假设补齐：

- 修改后的 trigger description 造成 quick/deep 路由重叠，或必须改 deep 路由才能解决；
- 兼容目录不再是授权安装目标，或同步必须删除/改名旧 alias；
- 无法取得完整正文或清晰关键图表，却仍试图声称完成图表核验；
- 新结构只有依靠硬字数、固定复杂模板或全图覆盖才能维持紧凑；
- 用户改为要求完整精读、正式同行评审、接受/拒绝建议，或撤回五维评分要求。
