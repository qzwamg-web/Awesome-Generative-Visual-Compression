# Contributing

欢迎提交漏收论文、纠错和训练配置补全。

## 提交要求

1. 论文须符合 `docs/scope-and-protocol.md` 的范围。
2. 修改 `data/papers.json`，不得只改展示页。
3. 中文方法摘要建议 60–180 字，说明“编码什么、如何生成、解决什么问题、主要代价”，避免照译摘要。
4. 训练字段必须注明证据来源；没有披露时写 `NR（未报告）`。
5. 提交前运行：

```bash
python scripts/validate.py
```

## 建议的 PR 标题

```text
paper(image): add PerCoV2
paper(video): complete GLC-Video training config
fix(metadata): correct venue for <paper>
```

