# RoadSafety-Gpt
交通垂直领域微调大模型
###
当前交通系统的运行高度依赖交通决策者的参与，但不同决策者的决策行为具有较大异质性，交通系统的安全和效率都难以得到有效保证。理想的交通安全管理体系计划基于云端提供实时海量数据、算力支持和高度智能化的车辆以及道路，能够不依赖于人类决策满足各种驾驶场景的要求，通过交通领域的专用大模型为交通系统赋予一套整合的安全管理系统，实现从感知到控制全过程的智能一体化的安全保障，是保障智慧交通出行安全的关键。
###
针对上述目标，为实现交通系统安全的智能化，提升系统的智能服务水平，本团队设计并研发了RoadSafety-GPT道路交通安全大模型。该模型以大型预训练语言模型为基座，采用层叠模型和权重共享技术，通过多任务学习和数据集平衡，实现领域特化的正则化，通过继续预训练、有监督微调、强化学习三个步骤，使得模型在保留通用能力的同时在交通领域展现出强大的专业能力。通过多模态生成、循环迭代机制等技术，模型能够及时适应交通的复杂场景变化，增强其下游任务的解决能力。
###
**模型文件已开源**

RoadSafety-GPT-6b-chat:- [**ModelSpace**](https://modelscope.cn/models/LSSSSSSSSSS/RoadSafety-GPT-6b-chat/files)

RoadSafety-GPT-14b-chat:- [**ModelSpace**](https://modelscope.cn/models/LSSSSSSSSSS/RoadSafety-GPT-14b-chat/files)
###
**训练集扩充**
![image](https://github.com/l-show/RoadSafety_Gpt-14b/blob/main/assets/%E6%95%B0%E6%8D%AE%E6%89%A9%E5%85%85.png)
###
**全训练流程**
![image](https://github.com/l-show/RoadSafety_Gpt-14b/blob/main/assets/%E8%AE%AD%E7%BB%83%E6%B5%81%E7%A8%8B.png)
###
# 检索增强模块
我们在RoadSafety_Gpt-14b-chat的基础上增加了一个基于开源检索框架 Langchain的检索增强模块。
# 交通领域测试
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
  
同样感谢其他未能列举的为本项目提供了重要帮助的工作。
## 声明
RoadSafety_Gpt-14b-chat 有着目前大语言模型尚无法克服的问题和缺陷，尽管它能够在许多交通事故分析和隐患排查方面提供可供参考的建议，但模型仅供用户参考使用，并不能完全还原真实情景下的情况，我们不对因使用 RoadSafety_Gpt-14b-chat 所引发的任何问题、风险或不良后果承担责任。
## 协议
RoadSafety_Gpt-14b-chat 可在 Apache 许可证下使用。请查看 LICENSE 文件获取更多信息。
# 参考文献
```
@Misc{llama-factory,
  title = {LLaMA Factory},
  author = {hiyouga},
  howpublished = {\url{https://github.com/hiyouga/LLaMA-Factory}},
  year = {2023}
}
```
