# RoadSafety-Gpt
交通垂直领域微调大模型

## 目录

- [项目介绍](#项目介绍)
- [更新日志](#更新日志)
- [模型](#模型)
- [训练方法](#训练方法)
- [数据集](#数据集)
- [软硬件依赖](#软硬件依赖)
- [如何使用](#如何使用)
- [交通领域测试](#交通领域测试)
- [免责声明](#免责声明)
- [协议](#协议)
- [致谢](#致谢)


## 项目介绍
###
当前交通系统的运行高度依赖交通决策者的参与，但不同决策者的决策行为具有较大异质性，交通系统的安全和效率都难以得到有效保证。理想的交通安全管理体系计划基于云端提供实时海量数据、算力支持和高度智能化的车辆以及道路，能够不依赖于人类决策满足各种驾驶场景的要求，通过交通领域的专用大模型为交通系统赋予一套整合的安全管理系统，实现从感知到控制全过程的智能一体化的安全保障，是保障智慧交通出行安全的关键。
###
针对上述目标，为实现交通系统安全的智能化，提升系统的智能服务水平，本团队设计并研发了RoadSafety-GPT道路交通安全大模型。该模型以大型预训练语言模型为基座，采用层叠模型和权重共享技术，通过多任务学习和数据集平衡，实现领域特化的正则化，通过继续预训练、有监督微调、强化学习三个步骤，使得模型在保留通用能力的同时在交通领域展现出强大的专业能力。通过多模态生成、循环迭代机制等技术，模型能够及时适应交通的复杂场景变化，增强其下游任务的解决能力。
###
## 模型
**模型文件已开源**

RoadSafety-GPT-6b-chat:- [**ModelSpace**](https://modelscope.cn/models/LSSSSSSSSSS/RoadSafety-GPT-6b-chat/files)

RoadSafety-GPT-14b-chat:- [**ModelSpace**](https://modelscope.cn/models/LSSSSSSSSSS/RoadSafety-GPT-14b-chat/files)
###
## 训练方法
**训练集扩充**
![image](https://github.com/l-show/RoadSafety_Gpt-14b/blob/main/assets/%E6%95%B0%E6%8D%AE%E6%89%A9%E5%85%85.png)
###
**全训练流程**
![image](https://github.com/l-show/RoadSafety_Gpt-14b/blob/main/assets/%E8%AE%AD%E7%BB%83%E6%B5%81%E7%A8%8B.png)
###
## 交通领域测试
使用了小样本分类任务测试方式，RoadSafety-GPT-14b模型的表现使用混淆矩阵记录
###
![image](https://github.com/l-show/RoadSafety_Gpt-14b/blob/main/assets/%E6%B7%B7%E6%B7%86%E7%9F%A9%E9%98%B5.png)
###
模型在测试集上的表现与ChatGLM4.0进行对比
![image](https://github.com/l-show/RoadSafety_Gpt-14b/blob/main/assets/%E5%AF%B9%E6%AF%94.png)
## 致谢

本项目基于如下开源项目展开，在此对相关项目和开发人员表示诚挚的感谢：

- [**Qwen-14B**](https://github.com/QwenLM/Qwen?tab=readme-ov-file)
- [**LLaMA Factory**](https://github.com/hiyouga/LLaMA-Factory?tab=readme-ov-file)
- [**ChatGLM3-6B**](https://github.com/THUDM/ChatGLM3)

```
@Misc{llama-factory,
  title = {LLaMA Factory},
  author = {hiyouga},
  howpublished = {\url{https://github.com/hiyouga/LLaMA-Factory}},
  year = {2023}
}
```
  
同样感谢其他未能列举的为本项目提供了重要帮助的工作。
## 免责声明

1. **RoadSafety-GPT**有着目前大语言模型尚无法克服的问题和缺陷,尽管它能够在许多交通事故分析和隐患排查方面提供可供参考的建议, 但模型仅供用户参考使用，仍然可能产生错误的、有害的、冒犯性的或其他不良的输出;我们不对因使用 **RoadSafety-GPT** 所引发的任何问题、风险或不良后果承担责任,用户在关键或高风险场景中应谨慎行事, 不要使用这些模型作为最终决策参考, 以免导致人身伤害、财产损失或重大损失.

2. **RoadSafety-GPT**由**ChatGLM3-6B**模型、**Qwen-14B**领域调优而得, 按"原样"提供, 在任何情况下, 作者、贡献者或版权所有者均不对因模型使用或其他因模型产生的交易而产生的任何索赔、损害赔偿或其他责任(无论是合同、侵权还是其他原因)承担责任.

3. 使用**RoadSafety-GPT**即表示您同意这些条款和条件, 并承认您了解其使用可能带来的潜在风险. 

## 协议
RoadSafety_Gpt-14b-chat 可在 Apache 许可证下使用。请查看 LICENSE 文件获取更多信息。
## 引用

