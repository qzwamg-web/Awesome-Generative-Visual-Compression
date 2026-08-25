# 生成式图像修复

> 收录显式使用 GAN、扩散/score/flow、自回归生成模型或大规模生成先验的图像修复方法。纯判别式 restoration、仅做生成/编辑、仅用生成数据扩增的工作不收录。训练卡只在论文或官方代码明确说明用于训练时记录。

## 正式发表

| 年份 | 状态 | 论文 | 发表 | 任务 | 方法族 | 训练数据集 | 训练硬件（卡数） | 中文核心思路 |
|---:|:---:|---|---|---|---|---|---|---|
| 2022 | ✅ | [DDRM](https://arxiv.org/abs/2201.11793) | NeurIPS | 线性逆问题 | training-free diffusion posterior | 无任务训练 | 不适用 | 在预训练无条件扩散模型的谱空间中加入观测一致性，统一求解超分、去模糊、修补和着色。 |
| 2022 | ✅ | [RePaint](https://arxiv.org/abs/2201.09865) | CVPR | 图像修补 | resampling diffusion | 无任务训练 | 不适用 | 每个去噪步用已知像素重采样约束，并通过前后跳步协调掩膜边界。 |
| 2022 | ◐ | [CodeFormer](https://arxiv.org/abs/2206.11253) | NeurIPS | 盲人脸修复 | VQ codebook + Transformer | FFHQ | NR（未报告） | 预测离散人脸码本 token，再以可调 fidelity weight 平衡真实纹理与身份忠实度。 |
| 2023 | ✅ | [DDNM](https://arxiv.org/abs/2212.00490) | ICLR | 线性逆问题 | null-space diffusion | 无任务训练 | 不适用 | 把更新拆成量程空间的数据一致性与零空间的生成补全，无需为具体退化重新训练。 |
| 2023 | ✅ | [DPS](https://arxiv.org/abs/2209.14687) | ICLR | 通用逆问题 | posterior score sampling | 无任务训练 | 不适用 | 用扩散先验 score 加测量似然梯度近似后验采样，覆盖线性与非线性观测。 |
| 2023 | ✅ | [DiffPIR](https://arxiv.org/abs/2305.08995) | CVPR | 通用逆问题 | plug-and-play diffusion | 无任务训练 | 不适用 | 把扩散去噪器嵌入半二次分裂，在生成先验和显式数据保真子问题间交替。 |
| 2023 | ◐ | [I²SB](https://arxiv.org/abs/2302.05872) | ICML | 图像到图像/修复 | Schrödinger bridge | ImageNet 与任务配对数据 | NR（未报告） | 以退化图像和清晰图像为两端学习 Schrödinger bridge，直接建模退化到真实分布的随机路径。 |
| 2023 | ◐ | [ResShift](https://arxiv.org/abs/2307.12348) | NeurIPS | 超分/盲修复 | residual-shifting diffusion | DIV2K、Flickr2K、OST；FFHQ | NR（未报告） | 从低质图像向高质图像逐步移动残差，缩短从纯噪声出发的生成链并强化输入约束。 |
| 2024 | ◐ | [StableSR](https://arxiv.org/abs/2305.07015) | IJCV | 真实图像超分 | frozen Stable Diffusion prior | LAION 高质量图像子集 | NR（未报告） | 冻结 Stable Diffusion 主干，用 time-aware encoder 和可控特征变换注入低质结构。 |
| 2024 | ◐ | [DiffBIR](https://arxiv.org/abs/2308.15070) | ECCV | 盲修复 | restoration module + IRControlNet | ImageNet-1K；过滤 LAION-2B-en | NR（未报告） | 先确定性去除退化，再让受控 latent diffusion 生成真实细节，并以可调 guidance 平衡保真度。 |
| 2024 | ◐ | [PASD](https://arxiv.org/abs/2308.14469) | ECCV | 真实超分/旧照修复 | pixel-aware Stable Diffusion | LSDIR、FFHQ 等 | NR（未报告） | 像素级 cross-attention 注入局部结构，退化移除模块与语义提示共同驱动生成。 |
| 2024 | ◐ | [SinSR](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_SinSR_Diffusion-Based_Image_Super-Resolution_in_a_Single_Step_CVPR_2024_paper.html) | CVPR | 超分 | one-step distillation | DIV2K、Flickr2K、LSDIR | NR（未报告） | 将 ResShift 的确定性多步映射蒸馏为一步，并用一致性保持损失避免受教师上限束缚。 |
| 2024 | ✅ | [OSEDiff](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a8223b0ad64007423ffb308b0dd92298-Abstract-Conference.html) | NeurIPS | 真实超分/人脸修复 | one-step VSD | LSDIR 84,991 张 + FFHQ 前 10k；人脸版 FFHQ | 官方脚本示例 4×GPU；型号 NR | 直接以低质 latent 为一步扩散起点，用 VSD 与 LoRA 微调恢复真实细节，消除随机噪声不确定性。 |
| 2024 | ◐ | [DreamClear](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6452474601429509f3035dc81c233226-Abstract.html) | NeurIPS | 通用真实修复 | DiT + MLLM + MoAM | GenIR 生成的 100 万高质量图像 | NR（未报告） | 用隐私安全数据生成管线扩展训练集，并以退化 token 动态路由不同修复专家。 |
| 2025 | ◐ | [Defusion](https://openaccess.thecvf.com/content/CVPR2025/html/Luo_Visual-Instructed_Degradation_Diffusion_for_All-in-One_Image_Restoration_CVPR_2025_paper.html) | CVPR | all-in-one 修复 | degradation-space diffusion | 多任务合成/真实修复数据 | NR（未报告） | 从标准视觉元素构造与语义无关的退化指令，在退化空间扩散以处理未知和混合退化。 |
| 2025 | ◐ | [ResFlow](https://openaccess.thecvf.com/content/CVPR2025/html/Qin_Reversing_Flow_for_Image_Restoration_CVPR_2025_paper.html) | CVPR | 通用修复 | augmented flow matching | 多任务图像修复数据 | NR（未报告） | 用辅助变量消除清晰图像预测歧义，学习可逆的确定性退化流，少于四步完成恢复。 |
| 2025 | ◐ | [VarFormer](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Navigating_Image_Restoration_with_VARs_Distribution_Alignment_Prior_CVPR_2025_paper.html) | CVPR | 多任务修复 | VAR autoregressive prior | 多任务图像修复数据 | NR（未报告） | 将 VAR 的多尺度 next-scale latent 作为分布对齐先验，按从结构到纹理的顺序恢复。 |
| 2025 | ◐ | [TSD-SR](https://openaccess.thecvf.com/content/CVPR2025/html/Dong_TSD-SR_One-Step_Diffusion_with_Target_Score_Distillation_for_Real-World_Image_CVPR_2025_paper.html) | CVPR | 真实超分 | target-score distillation | 真实超分合成训练语料 | NR（未报告） | 用真实高质参考构造目标 score，并以分布感知采样增强细节梯度，蒸馏为一步。 |
| 2025 | ◐ | [PURE](https://openaccess.thecvf.com/content/ICCV2025/html/Wei_Perceive_Understand_and_Restore_Real-World_Image_Super-Resolution_with_Autoregressive_Multimodal_ICCV_2025_paper.html) | ICCV | 真实超分 | autoregressive multimodal model | 论文 Real-ISR 训练集 | NR（未报告） | 指令微调 Lumina-mGPT，使模型先识别退化、生成语义描述，再自回归恢复图像 token。 |
| 2025 | ◐ | [CODiff](https://openaccess.thecvf.com/content/ICCV2025/html/Guo_Compression-Aware_One-Step_Diffusion_Model_for_JPEG_Artifact_Removal_ICCV_2025_paper.html) | ICCV | JPEG 去伪影 | compression-aware one-step diffusion | DIV2K、Flickr2K 等合成 JPEG 对 | NR（未报告） | CaVE 同时显式预测压缩质量并隐式学习重建特征，作为一步扩散的压缩条件。 |

## 高相关预印本

| 年份 | 状态 | 论文 | 任务 | 方法族 | 训练数据集 | 训练硬件（卡数） | 中文核心思路 |
|---:|:---:|---|---|---|---|---|---|
| 2024 | ◐ | [SUPIR](https://arxiv.org/abs/2401.13627) | 通用真实修复 | scaled generative prior | 2,000 万高分辨率图文图像 | NR（未报告） | 扩大模型和图文训练规模，以正/负质量提示及 restoration-guided sampling 控制真实度与保真度。 |
| 2025 | ◐ | [IRBridge](https://arxiv.org/abs/2505.24406) | 六类修复任务 | pretrained diffusion bridge | 六任务数据；精确划分待核验 | NR（未报告） | 推导共享终点分布的过渡方程，把从低质图出发的 bridge 接到预训练噪声扩散过程。 |
| 2025 | ✅ | [Restora-Flow](https://arxiv.org/abs/2511.20152) | 掩膜型修复 | training-free flow matching | 无任务训练 | 不适用 | 以退化掩膜引导预训练 flow，并用轨迹校正强制输出服从已知观测。 |
| 2026 | ◐ | [ResFlow-Tuner](https://arxiv.org/abs/2603.22027) | 真实图像修复 | FLUX + test-time scaling | 适配数据 NR | NR（未报告） | 统一多模态条件接入 FLUX.1-dev，并在测试时用奖励模型反馈动态调整生成方向。 |
| 2026 | ◐ | [Quantitative Flow Matching](https://arxiv.org/abs/2604.02392) | 自适应去噪 | noise-adaptive flow matching | 自然、医学与显微图像 | NR（未报告） | 估计局部噪声强度后联动选择 ODE 起点、步数和步长，使推理轨迹匹配真实噪声。 |

逐篇完整训练字段与核验状态见 [`data/restoration-papers.json`](../data/restoration-papers.json)。
