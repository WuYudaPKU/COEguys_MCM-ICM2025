# 论文中文稿

## 1 Introduction

### 1.1 Background

在过去的几十年间，随着人口数量急剧增长，粮食供给成为世界一大亟待解决的问题。在科学技术未完全普及的条件下，原有的耕地面积不足以满足粮食需求，所以很多地区采取了毁林造田的措施，如图1所示。图二显示，当森林生态系统被人为地破坏以后，其复杂的空间结构被破坏。因此，converted forest需要经历一个漫长的重建的过程。但是由于过程中有人类活动的影响，砍伐后的森林生态系统不能再恢复到原状，而是不断地演替成为稳定的农田生态系统。为了实现经济与生态的双重收益，实现可持续发展目标，有必要考察converted forest到农田生态系统的演替过程以及绿色农业如何带来经济和生态指标的双重收益。

> In the past few decades, with the rapid population growth, food supply has become one of the most pressing global issues. Under the conditions where scientific and technological advancements have not been fully adopted, the existing arable land area is insufficient to meet the food demand. As a result, many regions have resorted to deforestation for land conversion, as shown in Figure 1. Figure 2 illustrates that when the forest ecosystem is artificially disrupted, its complex spatial structure is destroyed. Therefore, the converted forest area must undergo a long process of ecological reconstruction. However, due to the influence of human activities during this process, the post-clearing forest ecosystem can no longer return to its original state, but instead continuously undergoes succession into a stable agricultural ecosystem. To achieve both economic and ecological benefits and fulfill sustainable development goals, it is necessary to examine the ecological succession from converted forest to agricultural ecosystems and explore how green agriculture can bring dual benefits in terms of economic and ecological indicators.

### 1.2 Problem Analysis

题目的基本要求是建立一个能够反映从converted forest area随时间演替到成熟的农场生态系统变化过程的模型，在模型中要包含自然过程和人类的农业活动。具体地，题目要求：

* 建立converted forest area的生态系统模型。特别地：
  * 要建立至少包含生产者和消费者的食物网；
  * 要考虑农业活动周期和季节性的影响；
  * 要考虑除草剂、杀虫剂等化学品对植物、昆虫、蝙蝠、鸟类以及生态系统稳定性的影响。
* 当生态系统逐渐成熟时，要考虑两种reemergence of species及其对生态系统的影响.
* 生态系统成熟后，人们会尝试去除化学品。考察去除除草剂后生态系统的稳定性，由生产者和消费者体现；
* 将蝙蝠引入到食物网中，考察蝙蝠作为食虫动物和授粉者如何与植物、昆虫和捕食者互动并影响生态系统的稳定性；找到另一种可以给生态系统带来收益的生物并比较不同的影响。
* 最后，分析采用有机农业的影响，考虑不同的情境和组成部分。评估其对整体生态系统及个体元素的影响，如害虫控制、作物健康、植物繁殖、生物多样性、长期可持续性和成本效益。评估有机实践对害虫管理、土壤健康和生物多样性的影响，同时权衡经济成本和收益。提供全面的生态和经济权衡分析，判断有机农业的可行性。

>The basic requirements of the project are to establish a model that reflects the ecological succession process from a converted forest area to a mature agricultural ecosystem over time. The model should incorporate both natural processes and human agricultural activities. Specifically, the requirements are as follows:
>
>- **Develop an ecological model for the converted forest area**, particularly:
>  - **Food web construction**: The model should include at least producers (e.g., plants) and consumers (e.g., herbivores and predators) and their interactions.
>  - **Consideration of agricultural cycles and seasonality**: The impact of seasonal and cyclical agricultural activities should be taken into account.
>  - **Impact of chemicals**: The model should account for the effects of chemicals such as herbicides and pesticides on plants, insects, bats, birds, and the stability of the ecosystem.
>- **Reemergence of species during ecosystem maturation**: As the ecosystem matures, the model should consider the reemergence of two species and their impact on the ecosystem.
>- **Impact of removing chemicals**: After the ecosystem matures, humans will attempt to remove chemicals. The model should assess the stability of the ecosystem after herbicides are removed, with the effects reflected through producers and consumers.
>- **Introduction of bats into the food web**: The model should examine how bats, as insectivores and pollinators, interact with plants, insects, and predators, and how their inclusion influences the stability of the ecosystem. Additionally, the model should identify another species that could benefit the ecosystem and compare the effects of different species.
>- **Analysis of the impact of organic farming**: The model should assess the impact of adopting organic farming practices, considering various scenarios and components. The evaluation should include the effects on the overall ecosystem and individual elements, such as pest control, crop health, plant reproduction, biodiversity, long-term sustainability, and cost-effectiveness. The model should analyze the impact of organic practices on pest management, soil health, and biodiversity, while weighing the economic costs and benefits. A comprehensive ecological and economic trade-off analysis should be provided to assess the feasibility of organic farming.

### 1.3 Our Work

## 2 Assumptions and Notations

### 2.1 Assumptions and Explanations

* 准确的数据：模型假设所采用的数据准确。

  justification：模型所采用的数据都来自于官方数据库，我们认为数据准确无误。

* 区域假设：假设模型适用的区域是东南亚地区，这里农田每年种植两茬水稻。

  justification：东南亚地区气候变化简单，只有雨季和旱季两个季节；此外，一年之内温度变化幅度很小，可以认为是常数。此外，种植水稻符合东南亚的种植模式，同时作物种类简单，便于建立模型。

* 稳定的性状假设：模型假设所有生物的性状保持稳定。

  justification：由于模型考察的时间范围远远小于生物发生进化或变异需要的时间，所以生物性状保持稳定，这也有利于模型的简化。

* 稳定的光照条件：假设模型所考察的地区在四季有稳定的光照。

  justification：由于模型考察的范围是热带地区，一年中不同月份日照时长变化很小，因此模型将光照条件视为常量。

* 稳定的生长环境假设：假设模型适用时间范围内没有大幅度影响农田生态系统的自然灾害。

  justification：自然灾害在农业活动中属于小概率事件，为保证模型的泛用性，不应当考虑自然灾害。

  >- **Accurate Data Assumption**: The model assumes that the data used are accurate.
  >
  >  **Justification**: The data used in the model are sourced from official databases, and we believe the data to be accurate and reliable.
  >
  >- **Regional Assumption**: The model assumes that the applicable region is Southeast Asia.
  >
  >  **Justification**: The climate of Southeast Asia is simple, with only two seasons—rainy and dry. Additionally, the temperature variation within a year is minimal.
  >
  >- **Planting Pattern Assumption**: The model assumes that two crops of rice are planted each year in the farmland.
  >
  >  **Justification**: This aligns with the planting patterns commonly observed in Southeast Asia, and the simplicity of crop types makes the model easier to establish.
  >
  >- **Stable Growth Environment Assumption**: The model assumes that no natural disasters, which could significantly impact the agricultural ecosystem, will occur during the time frame considered.
  >
  >  **Justification**: Natural disasters are considered low-probability events in agricultural activities. To ensure the generalizability of the model, natural disasters should not be considered.
  >
  >- **Stable Lighting Conditions Assumption**: The model assumes that the region under study experiences stable lighting conditions throughout the four seasons.
  >
  >  **Justification**: Since the model focuses on tropical regions, the variation in daylight duration across different months within a year is minimal, thus the lighting conditions are treated as constant in the model.

### 2.2 Notations

## 3 Models

生态系统组分复杂且相互影响。在最简单的情形下，当气候、土壤等一切其他条件适宜时，可以只考虑生物因素。如果用生产者、初级消费者的种群数量来描述整个系统，则由Lotka-Volterra模型【cite】和Leslie-Gower模型【cite】可以建立模型如下。

下面对模型做几点说明。

首先，之所以选择生物量而非种群密度，是因为水稻是农田生态系统的主要生产者，其种群密度已被人为确定（即不繁殖），只有用它总生物量的变化趋势才能表现出水稻种群的发展趋势。

其次，对于种间竞争，由于此时农田生态系统本身并不复杂，出于简化模型的目的，仅考虑水稻和杂草之间的种间竞争，下文的模型同样如此。

然后，同样出于模型简化的考虑，我们进行了一些参数的合并，如捕食率被合并入被捕食物种的捕食系数A。

最后，由于消费者处于自然繁殖状态，种群年龄结构基本固定，平均个体生物量可以认为是常数，因此生物量与种群中个体数量呈正比，下文同理。

> First, biomass rather than population density is chosen , because rice, as the primary producer in the agricultural ecosystem, has its population density artificially determined (i.e., it does not reproduce). Only the changes in its total biomass can reflect the development trend of the rice population.
>
> Second, for interspecific competition, since the agricultural ecosystem is relatively simple at this stage, in order to simplify the model, only interspecific competition between rice and weeds is considered. The model outlined below similarly assumes this.
>
> Next, in the interest of model simplification, some parameters are combined. For instance, the predation rate is incorporated into the predation coefficient of the prey species, denoted as $A$.
>
> Finally, since the consumers are in a natural reproductive state with a relatively fixed age structure, the average individual biomass can be assumed to be constant, which is similarly applied in the following sections.

需要指出，上文提到的所有系数都是正数。

> It should be noted that all the coefficients mentioned above are positive real numbers.

The components of an ecosystem are complex and interdependent. In the simplest case, when climate, soil, and other conditions are favorable, only biological factors can be considered. If the population sizes of producers and primary consumers are used to describe the entire system, the models proposed by Lotka-Volterra [cite] and Leslie-Gower [cite] can be applied as follows:
$$
\frac{\mathrm{d}W_{crp}}{\mathrm{d}t}&=r_{crp}W_{crp}\left( 1-\frac{W_{crp}+\beta _{w\rightarrow c}W_{wd}}{\mathscr{K} _{crp}} \right) -\frac{A_{crp}W_{crp}W_{ins}}{1+B_{crp}W_{crp}}\\

\frac{\mathrm{d}W_{wd}}{\mathrm{d}t}&=r_{wd}W_{wd}\left( 1-\frac{W_{wd}+\beta _{c\rightarrow w}W_{crp}}{\mathscr{K} _{wd}} \right) -\frac{A_{wd}W_{wd}W_{ins}}{1+B_{wd}W_{wd}}\\

\frac{\mathrm{d}W_{ins}}{\mathrm{d}t}&=r_{ins}W_{ins}\left[ 1-\frac{D_{ins}W_{ins}}{1+E_{ins}\left( 0.6W_{crp}+0.4W_{wd} \right)} \right] -\frac{A_{ins}W_{ins}W_{bd}}{1+B_{ins}W_{ins}}\\

\frac{\mathrm{d}W_{bd}}{\mathrm{d}t}&=r_{bd}W_{bd}\left( 1-\frac{D_{bd}W_{bd}}{1+E_{bd}W_{ins}} \right)\\
$$
一般地，这四个方程都引入了种群的自然增长$r_iW_i$项。前两个方程$\beta _{i\rightarrow j}W_{i}$项考虑了种间竞争的影响，这一项越大，种间竞争越激烈，种群$i$的生物量增长速率越慢；前三个方程$\frac{A_{crp}W_{crp}W_{ins}}{1+B_{crp}W_{crp}}$项考虑了被捕食的影响。后两个方程中的$\frac{D_{ins}W_{ins}}{1+E_{ins}\left( 0.6W_{crp}+0.4W_{wd} \right)}  $项表示了由食物缺乏造成的生物量减少，其中分母项的一个因子按照捕食比例加权，食物越少，捕食者越多，捕食者种群数量增长越慢。

>In general, these four equations all introduce the natural growth term riWir_i W_i for population growth. The first two equations consider the impact of interspecific competition through the term βi→jWi\beta_{i \rightarrow j} W_i; the larger this term, the more intense the interspecific competition, and the slower the growth rate of biomass for species ii. The first three equations include the term AcrpWcrpWins1+BcrpWcrp\frac{A_{crp} W_{crp} W_{ins}}{1 + B_{crp} W_{crp}}, which accounts for the effect of predation. The last two equations include the term DinsWins1+Eins(0.6Wcrp+0.4Wwd)\frac{D_{ins} W_{ins}}{1 + E_{ins} (0.6 W_{crp} + 0.4 W_{wd})}, representing biomass reduction due to food scarcity. In the denominator, one factor is weighted according to the predation ratio: the less food available, the more predators there are, leading to a slower growth rate of the predator population.

### 3.1 模型的构建背景、顺序与思路

在上文假设的基础上，我们逐步建立模型。由于最终模型的考察因素繁多，我们采取由简到繁的思路构建模型。

* 最初，我们将依据Lotka-Volterra模型和Leslie-Gower模型，在最简单的食物网条件下构建模型I：LVLG模型，考虑仅存在生产者、初级消费者和次级消费者的情况；
* 随后，生态系统逐渐发展，我们构建模型II。在这个模型中，我们考虑了农业循环（一年三熟），季节轮替（雨季旱季）和化学品的使用（除草剂和杀虫剂）。
* 然后，我们考虑生物的再迁入，构建更加复杂的食物网，形成模型III。在这个模型中，我们将在保留模型II特性的基础上，考虑多种生物间、生物与环境间的复杂作用。
* 最后，我们考虑在农田生态系统成熟后人的农业决策，如去除杀虫剂、人为引入新种群等策略，构建模型IV。

### 3.2 模型I LVLG

我们将先从生物种群的角度讨论模型的初始条件。热带森林的垂直结构通常分为几个层次，包括：树冠层、亚冠层、灌木层和地面层。每个层次不仅承载着不同的植物种类，还为各种动物提供栖息地和食物来源。对森林的砍伐将严重破坏热带雨林食物网的垂直结构，因而，我们的模型认为: 在去森林化后的初始时间节点上，地面上方的生态系统垂直结构只保留地面层的一部分，而原有的依赖于树冠层、亚冠层、灌木层作栖息地和食物来源的种群全部迁出生态系统。

基于这种假设，农田生态系统在最初的食物网只保留以下几个种群：植物、昆虫和鸟类。首先，为了保存种间竞争关系以及尽可能符合现实，我们将植物分为水稻和杂草两个种群。其次，尽管昆虫可能有取食偏好差别，简单起见，我们假设只有一种同时以两种作物为食的昆虫。最后，根据现实中鸟类的习性，我们认为鸟类同时取食昆虫和两种植物。图1给出了生态系统的示意图，图2给出了生态系统的初始食物网。

### 3.3 模型II CAGED

模型I的考量十分简单，旨在搭建起一个基础的短期模型。考虑到长期的环境因素影响，为了更好地模拟较长期的生态系统模型演化行为，我们下面将逐个加入简化的agricultural cycle, seasonalily, soil fertility,random factor对系统动力学模型的影响。进一步地，我们将在此自然农业生态系统的基础上考虑chemical use，即考虑除草剂和杀虫剂投放对系统的影响。

#### 3.3.1 Agricultural Cycle

根据rice production of Indonesia [cite],东南亚的水稻生产采取一年三熟的模式。我们认为二月、六月和十月是两个agricultural cycle的交叠期(from last post-harvest period to new planting period). 在交叠期内，水稻种群经过收割后以种子的形式重新进入食物网，开始新的agricultural cycle；收割后成熟的水稻秸秆作为农业副产物残留在生态系统中，经过焚烧、还田等手段处理后的水稻生物量经过分解者和昆虫的摄取后递减到0.

综上，经过文献查阅后综合考虑[cite]，成熟水稻在每个交叠期的生物量去向可以统一由下图描述[cite].由于我们的food web model中不考虑分解者的生物量，本文中仅分析分解摄取秸秆剩余物(1)对新的循环中生产者-即水稻、杂草-的影响。有关这一点，详见后文的soil fertility部分。

出于模型的简化考虑，将水稻种群在每个交叠期的生物量变化在数学模型（即差分方程组）中表现为特定时间节点的生物量阶跃。由于$t=0$对应第一个播种季节的开始，以一年（不妨设一年恒有52周）为周期，每周为一个时间节点，结合水稻的生产模式[cite]，设每一年中第0周、第17周、第34周开始为阶跃时刻，对水稻生物量有
$$
W_{crp}|_{t=n}=0.1W_{crp}|_{t=n-1}\,\,\\
n =52k,52k+17,52k+34,\left( year\,\,k\geqslant 0,week\ n\geqslant 1 \right)
$$
考虑秸秆对昆虫生物量的影响时，我们不妨将秸秆看作昆虫的‘prey’，运用modified LG predator-prey model刻画这种影响。在每个阶跃时刻，秸秆以$0.09W_{crp}$的初始生物量进入食物网模型，且$r_{stw}=0$,由此建立秸秆-昆虫模型：
$$
\frac{\mathrm{d}W_{stw}}{\mathrm{d}t}=\frac{A_{stw}W_{stw}W_{ins}}{1+B_{stw}W_{stw}}\left( t\ne n \right) \\
W_{stw}|_{t=n}=W_{stw}|_{t=n-1}+0.09W_{crp}|_{t=n-1}\\
n=52k,52k+17,52k+34,\left( k\geqslant 0,n\geqslant 1 \right)
$$
而昆虫的生物量差分方程修改为
$$
\frac{\mathrm{d}W_{ins}}{\mathrm{d}t}=r_{ins}W_{ins}\left[ 1-\frac{D_{ins}W_{ins}}{1+E_{ins}\left( 0.6W_{crp}+0.4W_{wd}+W_{stw} \right)} \right] -\frac{A_{ins}W_{ins}W_{bd}}{1+B_{ins}W_{ins}}
$$


#### 3.3.2 Seasonality

季节性影响主要包括光照、气候（温度、降水）、生物习性等，对于种群内的r和K都有重要的直接影响。考虑到诸多因素难以严格量化，我们参考[cite]设置

sinusoidal perturbations in periodic parameter $p(T)$如下：
$$
p(t)=\bar{p}[1+\epsilon sin(\Omega t+\phi)]
$$


具体地，设定上述LV-LG模型中，对于种群$i$，其$r_i,K_i$具有如下的形式：
$$
r_i=\bar{r}_i\left[ 1+\epsilon _i\sin \left( \Omega _it+\phi _i \right) \right] 
\\
\mathscr{K} _i=\bar{\mathscr{K}}_i\left[ 1+\epsilon _i\sin \left( \Omega _it+\phi _{i}^{\prime} \right) \right] \,\,, \left( i=crp\,\,or\,\,wd \right) 
\\
D_i=\frac{\bar{D}_{i}^{\prime}}{1+\epsilon _i\sin \left( \Omega _it+\phi _{i}^{\prime} \right)}\,\,, \left( i\ne crp\,\,or\,\,wd \right)
$$


其中$\bar{r}_i,\bar{\mathscr{K}}_i$为对应的周期均值，我们可以认定为常数；$\Omega_i$为季节波动角频率，$T=\frac{2\pi}{\Omega}$即为季节性波动周期；$\epsilon$为季节影响度参数，由于$r_i,\mathscr{K}_i\geqslant0$，显然恒有$-1\leqslant \epsilon_i \leqslant 1$；$\phi_i,\phi _{i}^{\prime}$为相位，$0\leqslant \phi _i<2\pi$，刻画不同种群生物量asynchronous fluctuation的特点。

可以从数学上证明，加入上述变化后的LVLG模型系统理论上在参数处于一定范围时存在非平凡的稳定点。在这种点附近时生态系统可以从小扰动中恢复，即可以达到动态的生态平衡。

#### 3.3.3 Soil Fertility

现在我们引入土壤肥力对植物生长的影响。同样地，出于简化模型的考虑，将土壤肥力对植物生长的影响分为二氧化碳浓度和植物吸收的无机盐浓度的影响。

对于二氧化碳浓度项，由于农田生态系统是开放系统，且在我们的背景下可以认为被巨大规模的复杂森林生态系统包围，所以可以忽略农田生态系统中各组分呼吸作用对空气中二氧化碳浓度的影响，将二氧化碳浓度近似为常数$C_{CO_2}$，基于此，我们引入土壤肥力因子$\mu_{fri}=f(C_{isi})$.土壤肥力对种群生物量增长速率、竞争系数、环境最大生物量容纳量等参数都有复杂而深刻的作用。此处重要考量$\mu$对环境最大生物容纳量的影响，如下所示：
$$
\frac{\mathrm{d}W_{i}}{\mathrm{d}t}=r_{i}W_{i}\left( 1-\frac{W_{i}+\beta _{j\rightarrow i}W_{j}}{\mathscr{K} _{i}\cdot \mu _{fri}} \right) -\frac{A_{i}W_{i}W_{ins}}{1+B_{i}W_{i}}
$$
对于吸收的无机盐浓度项，其与肥料浓度（受秸秆和化肥影响）、分解者活性和植物生长阶段密切相关。以水稻为例，它在生长至幼苗期时，其体内无机盐浓度较低，浓度增长加速度为正；在分蘖期到拔节期，水稻对无机盐需求量快速增大，体内无机盐浓度达到拐点；在孕穗期到抽穗开花期，水稻体内无机盐浓度增速趋缓直至达到最大浓度；在乳熟期和黄熟期，水稻对无机盐的吸收逐渐减少，体内无机盐浓度下降[cite]。

我们采用类正态分布的概率密度函数拟合每个agricultural cycle中植物体内的inorganic salt随时间的变化趋势，即
$$
C_{isi}(t)=\alpha_{isi}e^{-\frac{(t-T_{mc})^{2}}{\sigma_{isi}}}
$$
其中T表示在某一循环中水稻或杂草体内无机盐浓度最大的时刻；余下两个对应水稻或早的模型待定参数，由肥料浓度（化肥和秸秆）、分解者活性和植物的生长阶段共同确定。

出于模型简化考虑，我们不妨设$\mu_{fri}=\xi_{i}C_{isi}$.

#### 3.3.4 Random Factors

考虑到自然界的随机因素的影响，我们对不同种群各自引入高斯白噪声$\sigma_{i}$。

这里的高斯白噪声$\sigma_{i}(t)=x$的概率密度为
$$
f(x)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{x^2}{2\sigma^{2}}}
$$
即$\sigma_{i}$服从均值为0的正态分布。

我们的生成方式是：

* 生成$[0,1]$内的两个不同随机函数$U_{1}(t),U_{2}(t)$；
* 取$\delta(t)=-\sqrt{-2lnU_1(t)}\cdot cos(2\pi U_2(t))$，则$\delta(t)$为高斯白噪声函数。

不同物种对应方程中的噪声如图。

#### 3.3.5. 传粉因子

在水稻成长的8-12周为传粉时期，此时我们考虑昆虫对传粉的促进作用，只需要在自然增长率上乘以传粉因子即可。传粉因子形式是
$$
f_{pd}=\begin{cases}
	1,\  non-pollinating\,\,period\\
	f_0+c_1W_{ins},\  pollinating\,\,period\\
\end{cases}
$$

#### 3.3.5 chemical use

* 对于除草剂，考虑到水稻种植过程中除草剂投放时间主要是在播种前、秧苗期、分蘖期，假设在一个agricultural cycle中投放三次除草剂，时间节点分别为第0周,第3周和第8周。除草剂投放浓度与当前的杂草生物量成正比。由于此情形下除草剂的投放频率较低，我们可以忽略除草剂对水稻的特定负面作用（极少量的负面影响可以由3.3.4的随机过程涵盖）。

  考虑将杂草视为除草剂的‘prey’，与前述的秸秆-昆虫模型相似地，可以采用modified LG predator-pre model,此处$r_n\equiv0$.

  对于除草剂的降解，我们则可以使用指数衰减模型来刻画。由此，建立起杂草-除草剂模型：

$$
C_{hc}|_{t=m}=C_{hc}|_{t=m-1}+\alpha_{uh} W_{wd}|_{t=m}\\
\frac{dW_{wd}}{dt}=r_{wd}W_{wd}(1-\frac{W_{wd}+\beta_{c\rightarrow w} W_{crp}}{\mathscr{K}_{wd}})-\frac{A_{wd}W_{wd}W_{ins}}{1+\beta_{wd}W_{wd}}-\frac{A_{hc}W_{wd}C_{hc}}{1+B_{hc}W_{wd}}\\
\frac{dC_{hc}}{dt}=-\alpha_{dh}C_{hc}
$$

* 对于杀虫剂，可以建立起与杂草-除草剂模型机理类似的昆虫-杀虫剂模型。我们设置杀虫剂在一个agricultural cycle中的投放时间是week 4, week 8, week 12. 与杂草-除草剂模型有所不同，由于昆虫中有以水稻为主要食物的害虫和主要以杂草为食的其他昆虫，而杀虫剂对害虫的消灭作用显著大于对其他昆虫的消灭作用，因此在使用杀虫剂后，昆虫作为一个整体时的食物构成发生变化，即水稻占比显著减少，杂草占比显著增大。基于此，我们引入参数$\lambda_{pc}$，受杀虫剂浓度主导，描述杀虫剂对昆虫食物构成的影响如下：

$$
C_{pc}|_{t=m}=C_{pc}|_{t=m-1}+\alpha_{up} W_{ins}|_{t=m}\\
\frac{dW_{ins}}{dt}=r_{ins}W_{ins}(1-\frac{D_{ins}W_{ins}}{1+E_{ins}[(0.6-\lambda_{pc})W_{crp}+(0.4+\lambda_{prc})W_{wd}]})-\frac{A_{ins}W_{ins}W_{bd}}{1+\beta_{ins}W_{ins}}-\frac{A_{pc}W_{ins}C_{pc}}{1+B_{pc}W_{ins}}\\
\frac{dC_{hc}}{dt}=-\alpha_{dp}C_{hc}
$$

#### 3.3.6 Multiple Digestion Delays

由于能量流动需要时间，食物网中不同捕食关系对系统动力学的影响实际上是异时的[cite]。考虑这种异时性，我们引入multiple digestion delays, for digestion periods corresponding to consumer-eat-producer and predator-eat-consumer, which are called the producer digestion delay (PDD) and consumer digestion delay (CDD)，respectively.

在数学上，PDD和CDD影响消费者种群i的对应微分方程的食物缺乏影响项$L_{i}$:
$$
L_{i}=-r_{i}\frac{D_{i}W_{i}^2}{1+E_i \cdot \Sigma_{food}\gamma_i W_{i_j}}
$$
其中$\Sigma_{food}\gamma_i W_{i_j}$是$i$捕食的种群按照捕食比例的生物量加权之和。考虑delay后，将此项修改为如下形式后纳入原微分方程：
$$
L_{i}^{\prime}=-\frac{r_{i}}{t-\tau_i}\cdot \frac{D_{i}W_{i}^2}{1+E_i \cdot \Sigma_{food}\gamma_i W_{i_j}}
$$
其中$\tau_i$为digestion delay factor of population $i$，$D_i,E_i$是$i$对应的环境待定参数。

### 3.4 模型II改（考虑重迁）

> 成熟，新的物种重新迁入（说明迁入条件）；
>
> 新的更复杂的食物网（青蛙和蛇）

当生态系统逐渐成熟时，曾经的种群将会重新迁入。我们假设当待迁入种群的猎物的生物量达到阈值（可调参数）时，该种群会迁入该生态系统，形成更复杂的食物网。在我们的模型中，我们只考虑青蛙和蛇的迁入。在他们迁入后，此前构建的方程适用于描述他们生物量的情况（假设不受化学品的影响）。

### 3.5 模型III SAGED

> 在食物网充分复杂时，考虑人类的农业决策。
>
> 去除除草剂和杀虫剂，引入蝙蝠和鸭。
>
> 在水稻成长的8-12周为传粉时期，此时除了r外再乘以传粉因子（昆虫和蝙蝠生物量影响）
>
> ==叙述为什么引进蝙蝠和鸭子==

当食物网充分复杂时，人类可以开始进行农业决策。我们的模型考虑的农业决策是：去除除草剂和杀虫剂，引入蝙蝠和鸭。

蝙蝠对传粉有促进作用，因此传粉因子变成
$$
f_{pd}=\begin{cases}
	1,\  non-pollinating\,\,period\\
	f_0+c_1W_{ins}+c_2W_{bt},\  pollinating\,\,period\\
\end{cases}
$$
除此之外，变化后的模型只需要在CAGED模型的基础上去掉化学品，并再引入两个新种群形成终极食物网即可。

## 4. Application of the Model

模型的建立过程叙述已经完整地呈现在了上一个subsection中，在本subsection，我们将讨论模型的应用。

#### 参数的选取

经过文献查阅以及参数和现实意义的对应，我们确定了一系列参数。由于参数繁多，我们只给出主要参数的表格：

下面的模型都将应用这些参数。

#### 情境陈述

|          | Scenario1 | Scenario2 | Scenario3 | Scenario4 | Scenario5.A | Scenario5.B | Scenario6 |
| -------- | --------- | --------- | --------- | --------- | ----------- | ----------- | --------- |
| 农业活动 | √         | √         | √         | √         | √           | √           | √         |
| 季节因素 | √         | √         | √         | √         | √           | √           | √         |
| 化学品   | ×         | √         | √         | ×         | ×           | ×           | ×         |
| 迁入     | ×         | ×         | √         | √         | √           | √           | √         |
| 引入蝙蝠 | ×         | ×         | ×         | ×         | √           | ×           | ×         |
| 引入鸭子 | ×         | ×         | ×         | ×         | ×           | √           | ×         |
| others   | ×         | ×         | ×         | ×         | ×           | ×           | √         |

#### S1与S2对比：化学品的作用

S1，S2中生产者、消费者的种群密度分别如图[cite]。

\begin{figure}

\end{figure}

分析可知，在S1下，生态系统正常发展，但是水稻不能长期存活，所以系统不能演变成一个农业生态系统。这说明了水稻与杂草的竞争能力以及对害虫的抵抗能力都比较弱，不能在没有人类干预的情况下稳定地存在于生态系统中。

在农田生态系统早期时，还没有物种的再迁入，此时的模型符合S2。这时生态系统正常发展，水稻能够长期存活，系统逐渐演替成为一个成熟的农业生态系统，这说明传统的化学品-农业模式能够维护一个农业生态系统。

上面两个结果均与现实相符合。

#### S2与S3对比：物种迁入的作用

当生态系统演替一定时间后，外来物种再次迁入，我们考察S2（发展早期）和S3（发展成熟时）的对比，旨在说明生态系统的稳定性。

S2，S3系统的动态情况如图。

\begin{figure}

\end{figure}

对比两种情况可以发现，

#### S3和S4对比：化学品-农业模式对化学品的依赖性

在有物种迁入后，我们考虑撤掉化学品，对比生态系统在前后两个时期的情况。如图。

\begin{figure}

\end{figure}

对比两种情况可以发现，在传统的化学品-农业模式下，农田生态系统对化学品高度依赖。一旦撤去化学品，水稻开始在与杂草的竞争中占据下风，同时受害虫干扰增大，农田生态系统的产出逐渐降低，生态系统越来越不适宜于农业活动。

#### S3和S5的对比：农业模式相对于化学品-农业模式的优越性

在情境2的讨论中，我们考虑一个真实的情境。现在有一个农民刚刚砍伐了一片森林用来种植水稻，起初，他使用除草剂和杀虫剂等化学用品抑制杂草和害虫，生态系统逐渐发展。当生态系统成熟到一定程度时，一些曾经从森林生态系统迁出的种群重新迁入，丰富了农田生态系统的食物网。生态系统再发展一段时间，已经变得比较稳定，农民开始不再使用除草剂和杀虫剂，转而使用绿色农业的方案，引进鸭子或蝙蝠到生态系统中。

具体地：

* 鸭子的生理构造决定了它不能摄取水稻，但是可以摄取杂草和害虫；
* 鸭子在每季播种两周后引入，在收割时同步地作为农产品产出；
* 蝙蝠一次性投放，它可以作为授粉者和昆虫的捕食者。

最终的食物网如图所示。

[图：食物网]

我们将着重对比人类使用化学品（常规情境）和人类使用绿色农业方案（目标情境）时生态系统的演替情况。

当人类使用化学品时，生态系统的动态情况如下图：

==2：人类使用化学品的情况下生态系统的情况 以situation_chem.csv命名==

我们发现相比于情境1，人类活动可以有效地控制杂草生长，抑制害虫，持续地从农田中收获水稻，能够形成可运行的农业系统。

当人类使用绿色农业方案时，生态系统的动态情况如下图：

==3：人类使用绿色农业方案情况下生态系统的情况 以situation_green.csv命名==

我们发现相比于情境1，绿色农业方案同样地可以有效地控制杂草生长，抑制害虫，持续地从农田中收获水稻，能够形成可运行的农业系统。

为了对比化学品和绿色农业的区别，我们尝试在使用化学品达到稳定后停止使用化学品（并且不引入生物防治），得到生态系统的动态情况如下图：

==4：人类停止使用化学品且不使用绿色农业方案情况下生态系统的情况 以situation_ban_chem.csv命名==

我们立即发现，在不使用绿色农业方案时，一旦停止使用化学品，杂草和害虫迅速繁殖并与水稻竞争，系统生物量波动很大，稳定性不强。而如果采取绿色农业方案，即使不使用化学品，杂草和害虫也能得到有效的控制，系统生物量波动小，系统非常稳定。这是因为引入了更多的组分，食物网复杂，生物多样性强。当一种生物处于劣势时有其他生物可以暂时地接管他的生态位，从而增强了系统的稳定性，这与现代生态理论高度相符。

综上所述，当模型被应用到情境中时，其高度符合现实世界的情况，这证明了模型的泛用性和准确性。

#### 4.4 绿色农业的经济效益分析

> 经过文献查阅和现实对比，我们比较精确地确定了一系列参数：下面给出主要的参数table。
>
> 在这套参数下，为了彰显模型的泛用性和准确性，我们着重对比下面条件下系统的演替过程：
>
> 4.1 人类不采取措施
>
> 对照组（仅起到介绍基础模型的作用）
>
> 可能不能形成一个可运行的农业系统（水稻竞争能力和抵抗能力弱）
>
> 4.2 化学品和绿色农业的对比
>
> 考虑真实情境。先使用化学品，再改用绿色农业。
>
> * 人类使用化学品
>
>   正常情境
>
>   可以有效控制杂草的增长，抑制害虫，能够形成可运行的农业系统；
>
>   但是，系统稳定性不强，生物量波动很大，一旦停下除草剂，杂草迅速繁殖并与水稻竞争。
>
> * 人类使用绿色农业方案（如生物防治等）
>
>   目标情境
>
>   系统稳定性增强，能够有效控制杂草，同时，因为引入了更多组分，生物多样性越好，生物量波动减少，系统非常稳定；

## 5. System Stability Analysis to Certain Disasters

## 6. Sensitivity Analysis

我们这里仅考虑两方面的模型参量改变对系统的影响：动力学模型中生物量密度$W$的初值和典型的环境参数。取系统敏感性分析的时间范围为0-80周，这段时期的农业生态系统模型为为存在化学品使用的、考虑物种重迁入的数学模型（model Ⅲ）。考虑到水稻为此农业生态系统中最主要的生产者和作物，下述讨论中的图象以水稻生物量随时间变化为典例。

### 6.1 生物量密度初值变化

将系统中所有生物量密度$W$的初值分别取chap 4.中图象对应初值的原值、原值的5倍、原值的0.2倍这三个不同值，以模拟现实的各种农业环境中converted forest和耕种条件的多样性，作出图象如图 \ref。

\begin{figure}

\includegraph{Change_init}

\end{figure}

从图象中可见，分别代表三种初值情况的生物量曲线在较长期的自然演变下趋于重合。其余生态系统中的种群图象与之类似。由此可说明我们的农业生态系统模型具有一定的自调节能力，这与生态学中实际生态系统的稳定性和自恢复能力是相符的。

### 6.2 典型环境参数变化

我们取四种具有重要影响的典型环境参数：水稻生物量密度的自然增长率$r_{crp}$、杂草-水稻竞争系数$\beta_{c\rightarrow w})$、水稻的环境最大生物量容纳量$\mathscr{K}_{crp}$、系统高斯白噪声的标准差$σ$，考察它们的各自变化对系统的影响。将这四个参数分别取三个不同值（已在下述图象中注明），作出图象如下。杂草-水稻竞争系数$β_{c-w}$相关图象中还包含了杂草生物量随时间变化的曲线，以与水稻作比较。

\begin{figure}

\includegraph{Change_all}

\end{figure}

下面对四种情形下的图象曲线作分析。

对于水稻生物量密度的自然增长率$r_{crp}$的影响，由图\ref{} (A)可知,随$r_{crp}$的增大，在同一时刻的水稻生物量呈现出增大趋势，反之亦然。从生态学理论上分析，$r_{crp}$的增大表示水稻生物量的平均边际增长量增大，生长速度加快，这与上述图象是相符的。另一方面，可以看出当$r_{crp}$在一定幅度内变化时，系统的总体演化趋势近似相同，体现了系统的稳定性。

对于杂草-水稻竞争系数$\beta_{c\rightarrow w}$的影响，由图象\ref{} (B)可知随$\beta_{c\rightarrow w}$的增大，在同一时刻的水稻生物量呈现出减少趋势，杂草生物量呈现出增大趋势，反之亦然。从生态学理论上分析，$\beta_{c\rightarrow w}$的增大表示杂草相对水稻的竞争能力增加，更容易在种间竞争中取得优势地位，这与上述图象是相符的。另一方面，可以看出在$\beta_{c\rightarrow w}$在一定幅度内变化时，系统的总体演化趋势近似相同，体现了系统的稳定性。

对于水稻的环境最大生物量容纳量$\mathscr{K}_{crp}$的影响，由图象\ref{} (C)可知随$\mathscr{K}_{crp}$的增大，在同一时刻的水稻生物量呈现出增大趋势，反之亦然。从生态学理论上分析，$\mathscr{K}_{crp}$的增大表示水稻生物量的最大可能值增大，且在适宜的生长环境下水稻生物量会随时间逐渐趋于此值，这与上述图象是相符的。另一方面，可以看出当$\mathscr{K}_{crp}$在一定幅度内变化时，系统的总体演化趋势近似相同，体现了系统的稳定性。

对于系统高斯白噪声的标准差$σ$的影响，由图象(4)可知当$σ$处于一定取值范围内时水稻生物量随时间变化的趋势近似相同，进一步地可说明系统的总体演化趋势基本不变。由于$σ$本身与系统随机波动的振幅呈正相关，这体现了系统的稳定性。但另一方面，注意到$σ=0.1$时，水稻在约70周时灭绝。这是由于随机波动的振幅过大，可能在水稻的动力学方程中$W_{crp}$的变化速率本身较低时受到了剧烈的负向扰动，使得水稻生物量迅速归零。由此说明系统面对扰动时的稳定性和恢复力是有限的，这与生态学中生态系统的抵抗力和恢复力有限是相符的。

​                 

## 7. Suggestions