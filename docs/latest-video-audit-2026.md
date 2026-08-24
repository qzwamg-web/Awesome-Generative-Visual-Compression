# 2026 新工作与引用链审计

最后核验：2026-08-23。

## 用户点名论文的结论

1. **GenVC 不是另一篇论文。** `GenVC` 是 [Generative Video Compression with Adaptive Score Distillation](https://arxiv.org/abs/2607.22772) 提出的 codec 名称。
2. **该文不是阿里团队论文。** 作者单位包括微软亚洲研究院、中国科学技术大学、中国科学院数学与系统科学研究院、Communication University of China；其中多位第一作者/学生作者为微软亚研院实习生。
3. **YODA 已补入正式发表表。** 官方代码仓库标注 IEEE TCSVT 2026 Early Access；公开仓库含推理、真实码流与评估代码，不含训练代码。
4. **GNVC-VD 已从预印本修正为 CVPR 2026。** 训练配置已由作者论文/补充材料补齐到数据、分阶段学习率、batch、迭代数和 2×A800。

## GenVC 直接对比/引用的近期方法

| 方法 | 状态（本轮核验） | 与 GenVC 的关系 | 本仓库动作 |
|---|---|---|---|
| YODA | IEEE TCSVT 2026 Early Access | 一步扩散对比；约 1B 参数级 | 新增，补训练阶段与 IPPP 风险 |
| S2VC | CVPR 2026 | 一步扩散 + 语义时间引导 | 新增，补 30k iter / 4×A100 |
| GNVC-VD | CVPR 2026 | 多步 VideoDiT 先验基线 | 更新发表状态并补全训练配置 |
| DiffVC-OSD | arXiv 2025 | 一步扩散基线 | 新增，保留 partial 状态 |
| DiffVC-RT | arXiv 2026 | 实时扩散基线 | 新增；H800 只记推理，不误记训练卡 |
| GLVC | arXiv 2025 | GenVC 报告 LPIPS/FID 码率节省时的主要 anchor | 新增，正式录用状态待确认 |
| GLC-Video | IEEE TCSVT 2025 | 生成 latent 编码前序路线 | 已有；纳入 P 帧误差对照 |
| Free-GVC | arXiv 2026 | training-free 视频扩散路线 | 已有；保留预印本分栏 |

## GenVC 训练配置核验

- 数据：OpenVid，随机裁剪 512×512；每个样本 96 帧，即 3 个 32 帧 GOP。
- 初始化：只用预训练 DCVC-UF 初始化条件 codec；478M 视频扩散模型为压缩任务从零训练。
- 阶段 1：多步教师 12 epoch，`λR={0.56,0.80,1.12,1.76,2.40}`。
- 阶段 2：一步学生与 codec 联合训练 3 epoch，`λR={10.24,5.12,2.56,1.28,0.64,0.32}`。
- 阶段 3：冻结 codec，ASD 训练 1 epoch；`λaux=.01, λL=1, λF=2, λD=8, τ=.015, κ=.02, nfake=4`。
- 优化器/硬件：AdamW，4×A100 80GB；论文已核验实现段未给出学习率和 batch size，明确记作 NR。

## 为什么 ASD 与传统“P 帧误差累积”不能混为一谈

GenVC 定位的 motion-stalling 是一步蒸馏反馈失稳：学生输出偏离教师训练分布后，冻结教师给出错误 score，DMD 更新反而强化漂移。ASD 用更新方向与真实视频方向的一致性门控这一梯度，并以像素、LPIPS、RAFT 光流损失锚定内容和运动。

传统 P 帧误差累积则来自历史重建被再次用作条件。GenVC 底层沿用 DCVC-UF 条件 codec，因此两类问题应分别测量：

- GOP 内随帧序号变化的 PSNR/LPIPS/DISTS；
- 重建光流相对原视频的 EPE/运动幅度偏差；
- scene cut、遮挡和快速运动后的恢复时间；
- 固定码率下 32/64/96 帧递归长度的退化曲线。

## 本轮仍需持续跟踪

- GLVC、DiffVC-OSD、DiffVC-RT 等预印本的正式录用状态与最终附录；
- YODA 未公开的训练 optimizer、batch size 与训练硬件；
- GVC-RT 论文附录中的完整学习率、batch 和 GPU；
- 新工作是否公开训练代码、真实 entropy-coded bitstream 与逐帧误差曲线。
