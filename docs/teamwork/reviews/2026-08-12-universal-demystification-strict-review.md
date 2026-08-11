# 通用祛魅共享核心候选的最终 Strict Review

## Candidate, scope, and crossed boundary

本次 Strict Review 覆盖已实现并生成同步的通用祛魅候选：

- `skill-src/core.md`；
- `skill-src/depth/quick.md` 与 `skill-src/depth/deep.md`；
- 生成的 `skills/clear-eyed-reading/SKILL.md`、`skills/clear-eyed-reading/agents/openai.yaml`；
- 生成的 `skills/clear-eyed-deep-reading/SKILL.md`、`skills/clear-eyed-deep-reading/agents/openai.yaml`；
- `README.md`、`README_EN.md`；
- `evals/cases.yaml`；
- `assets/clear-eyed-reading-map-v4.png`。

本轮实际跨越的是**已发布的公共行为契约**：两个显式调用的 Skill 现在承诺共享同一套独立祛魅判断——去掉作者命名和包装后重构问题、机制与能力/知识来源，定位真实贡献，解释结果、结论或系统为何成立，并以竞争性解释和材料范围校准归因；quick 与 deep 只改变展开粒度，不再把祛魅收窄成 boundary-only audit。README、入口元数据、生成的 Skill 和回归用例共同构成该对外可观察契约。保护边界是保持自然读者输出、跨研究类型可复用、材料不足时诚实收缩，并避免把内部判断链倒成固定用户清单。

接受标准是：候选源与生成结果同步；回归契约能区分真正的去框架化重构与只做证据边界审计；shared core 在完成独立研究后再确定贡献和归因；quick/deep 的差异仍限于输出细粒度；静态检查不引入其他材料性问题。

## Initial findings and corrections

首轮 Strict Review 返回 `REVISE`，有两个材料性 finding。两项均已按最小路径修正，并在 delta 上完成 bounded recheck。

1. **材料性（首轮阻塞，`REVISE`）：配对近邻回归没有提供可判别的两段材料。** `demystification-paired-boundary-near-miss` 原先只重复 LiveWorld 提示，并在 `expect` 中描述 boundary-only 答案，无法让验收真正区分“只收窄边界”与“独立重构”。修正后，`evals/cases.yaml` 的 prompt 直接嵌入 Candidate A（boundary-only audit）和 Candidate B（去包装后的独立重构），并要求输出语义分类、解释机制、能力来源、贡献和结果从哪来的差异，以及自己的简短判断。

2. **材料性（首轮阻塞，`REVISE`）：shared core 的贡献/归因顺序曾与研究顺序矛盾。** `skill-src/core.md` 先写成已经确定贡献并解释归因，随后才写“研究发生在判断贡献之前”，会把临时判断误读为最终结论。修正后，贡献和归因明确标为 provisional；中性的研究阶段先完成，主 agent 合并证据后才 finalize 贡献类型、强度与归因，边界规则也改为跟随该研究定稿之后执行。

## Direct validation and bounded recheck

- 运行 `python3 scripts/sync_skills.py --check`，确认源文件、生成的 Skill 和入口元数据不存在生成漂移。
- 官方 `quick_validate.py` 在系统 Python 与 bundled Python 中均只因 `ModuleNotFoundError: yaml` 无法导入 PyYAML，未把该工具失败伪写成通过。随后使用 Ruby YAML parser 完成等价的静态解析与约束检查：`evals/cases.yaml` 解析成功，22 个 case ID 唯一，且 frontmatter 约束满足。
- 运行 `git diff --check`，无 whitespace error。
- Bounded recheck 重新读取了修正后的配对回归 prompt、`skill-src/core.md` 的 provisional/finalize 研究顺序、生成同步结果及上述静态检查结果；两个 initial findings 均闭合，未发现需要继续阻止候选的其他问题。

## Post-review forward evidence

- blind LiveWorld deep test 已完成：使用 arXiv v2 及其 appendix、官方 project/repo 和主要 lineage sources；输出实际完成了独立重构、能力来源追踪、field-removal counterfactual 贡献定位，并讲清结果从哪来，而不是只做 boundary-only audit。
- 同一材料的 quick/deep parity test 已完成：两者给出相同的实质判断，deep 只展开了更多细节，支持 quick/deep 共享判断而仅改变输出粒度的公共契约。
- 两项 forward test 均未执行代码或做独立 reproduction；下述剩余限制仍适用。

## Verdict

**PASS**。在已审阅的公共行为契约、直接静态证据和已完成的前向阅读行为证据范围内，候选满足 Strict Review 的材料性接受标准；两项 `REVISE` finding 已被最小修正确认闭合。该 verdict 不把未执行的代码 reproduction 或未发布的 LiveBench 当作已验证事实。

## Residual uncertainty and next action

LiveWorld 的 blind deep test 与同材料 quick/deep parity test 已完成，但没有代码执行或独立 reproduction；LiveBench 仍未发布。因此，本 Review 支持的是已观察到的阅读行为与公共契约一致性，不把未做的复现或未发布 benchmark 写成结果。若后续新增的运行或材料暴露公共行为偏差，应针对新候选重新进入 Review。
