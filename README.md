# Paper Demystifier Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/OpenAI-Skills-111111)](https://developers.openai.com/plugins/build/skills)

一组面向 ChatGPT 与 Codex 的中文论文祛魅阅读 Skills。它们不满足于摘要，也不靠罗列局限制造批判感，而是先判断工作真正推进了什么，再用领域前例、方法机制和关键证据校准结论。

> 当前状态：`v0.1`。两个 Skill 已通过结构校验，正在用不同学科和文章类型持续回归。

## 快速选择

- 只想迅速弄清“这篇到底做了什么、有没有水分”，用 **文章祛魅导读**。
- 想把背景、方法、公式、图表和实验完整读懂，用 **文章祛魅精读**。

## 两个 Skill

| Skill | 适合什么场景 | 默认产出 |
| --- | --- | --- |
| `clear-eyed-paper-reading` | “读一下、解读、评价、辣评这篇文章” | 紧凑的祛魅导读、五维简评与一句总评 |
| `clear-eyed-paper-deep-reading` | “精读、逐节、逐图逐表、完整展开” | 背景地图、方法心智模型、全部图表与实验解读、最终判断 |

二者刻意分开：快速导读不会被完整精读流程拖长；只有用户明确要求深读时，精读 Skill 才会触发。

## 设计原则

- 贡献和创新决定评价基调，证据负责校准，而不是把零碎缺点相加。
- 先把方法还原成普通部件，再评价架构是否配得上论文声称的能力。
- 创新性和意义必须经过独立领域定位，不能照抄作者的 Related Work。
- “毒舌”只针对主张、证据和推理；狠句必须能落回原文、图表或前例。
- 少说“边界、风险、存在一定局限”，直接说哪句话应收回，以及收回后还剩什么价值。

## 安装

每个 Skill 都是独立目录，核心文件是 `SKILL.md`，符合 OpenAI 的 Skill 目录结构。OpenAI 官方文档也建议让每个 Skill 聚焦一个可识别的用户目标，并用 description 决定触发条件。

### ChatGPT

在支持个人 Skills 的 ChatGPT 中，分别上传以下两个文件；具体入口以当前界面为准。两个 Skill 需要分别安装。

- [文章祛魅导读 SKILL.md](skills/clear-eyed-paper-reading/SKILL.md)
- [文章祛魅精读 SKILL.md](skills/clear-eyed-paper-deep-reading/SKILL.md)

### Codex

将所需目录复制到个人 skills 目录，例如：

```bash
cp -R skills/clear-eyed-paper-reading ~/.codex/skills/
cp -R skills/clear-eyed-paper-deep-reading ~/.codex/skills/
```

## 使用

自然语言通常可以自动触发，也可以显式调用：

```text
使用 $clear-eyed-paper-reading 读懂并评价这篇论文：<链接或附件>
```

```text
使用 $clear-eyed-paper-deep-reading 祛魅精读这篇论文，展开背景、方法、图表和实验：<链接或附件>
```

## 项目结构

```text
paper-demystifier-skills/
├── skills/
│   ├── clear-eyed-paper-reading/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── clear-eyed-paper-deep-reading/
│       ├── SKILL.md
│       └── agents/openai.yaml
├── evals/cases.yaml
├── CONTRIBUTING.md
└── LICENSE
```

## 开发与验证

修改后应检查：两个 description 是否仍然互斥；导读是否保持紧凑；精读是否覆盖全文图表和关键公式；创新性评分是否来自独立领域定位。`evals/cases.yaml` 提供基础回归用例。

发现输出太保守、太模板化、遗漏致命问题或误触发时，请使用 [Output quality issue](https://github.com/JinPLu/paper-demystifier-skills/issues/new?template=output-quality.yml) 提交脱敏样例。贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，安全问题见 [SECURITY.md](SECURITY.md)。

本项目使用 [MIT License](LICENSE)。

## 参考

- [OpenAI：Build skills](https://developers.openai.com/plugins/build/skills)
- [OpenAI：Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
