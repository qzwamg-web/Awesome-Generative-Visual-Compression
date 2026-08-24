# 检索与审计协议

## 1. 时间与主题边界

- 检索窗口：2016-08-23 至 2026-08-23（滚动十年窗口）。
- 图像：自然图像、面部图像、语义图像的生成式有损压缩。
- 视频：通用视频、人物/会议视频、隐式视频表示与基于视频生成先验的有损压缩。
- 排除：仅面向机器视觉任务的特征压缩、纯图像/视频生成 tokenizer、压缩感知恢复但无编码码流、点云/3D/音频压缩、单纯的后处理增强。

## 2. 来源优先级

1. 会议/期刊官方页面与正式论文 PDF；
2. 作者 arXiv 版本及补充材料；
3. 作者官方代码仓库与项目页；
4. DBLP/Crossref 用于补齐书目信息；
5. 综述和 Awesome 列表只用于发现候选，不作为训练配置的最终证据。

## 3. 检索式

在 CVF Open Access、OpenReview、PMLR、NeurIPS Proceedings、IEEE Xplore、ACM DL、Springer、arXiv 与 DBLP 中组合检索：

```text
(generative OR perceptual OR diffusion OR GAN OR tokenizer OR implicit neural representation)
AND (image compression OR image coding OR video compression OR video coding)
```

扩展检索词：`ultra-low bitrate`、`extreme compression`、`generative prior`、`diffusion decoder`、`semantic compression`、`perception-distortion`。

## 4. 逐篇训练配置审计

- `verified`：字段在论文、附录或官方代码中有明确证据。
- `not_reported`：作者材料中未公开。
- `pending`：已定位论文，但尚未完成全文核验。
- GPU 型号仅在明确写出“训练使用”时填写；论文只用 GPU 做速度测试时不得误记为训练硬件。
- “训练集”与“测试集”严格分开，OpenImages train/test 等异常用法保留作者原文含义并附注。
- 多阶段训练必须分阶段记录，不能只留一个学习率或步数。
- 视频工作额外审计参考结构（IPPP/GOP/双向锚点）、递归状态、误差进入下一帧的路径，以及作者用于抑制漂移/闪烁/运动停滞的机制。

## 5. 纳入工作流

1. 发现候选并去重（标题、DOI、arXiv ID）。
2. 确认任务与生成式机制满足范围。
3. 核验正式发表状态，预印本不得伪标会议。
4. 阅读方法、实验设置和补充材料，填写中文摘要与训练字段。
5. 运行 `python scripts/validate.py` 检查结构、链接和必填字段。
6. 通过 Pull Request 增补，并在描述中给出训练配置证据位置。
