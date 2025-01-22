import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 设置 Seaborn 风格
sns.set(style='darkgrid')

# 设置全局字体为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# 读取数据
tips = pd.read_csv(r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\datasets\datasets\tips.csv')

# 自定义调色板
color_science = [
    (153, 55, 153),  # #993799
    (254, 136, 0),    # #FE8800
    (50, 90, 160),    # #325AA0
    (100, 100, 100),  # #646464
    (66, 153, 56),    # #429938
    (245, 113, 109),  # #F5716D
    (255, 172, 96),   # #FFAC60
    (97, 172, 255)    # #61ACFF
]

# 将 RGB 颜色转换为 [0, 1] 范围
color_science_normalized = [np.array(color) / 255.0 for color in color_science]

# 在 scatterplot 中使用自定义调色板和设置散点大小
g = sns.relplot(
    x='total_bill', y='tip', 
    data=tips, 
    hue='day', 
    palette=color_science_normalized,
    marker='o',
    s=250
    )

# 设置标签
g.set_xlabels("Total Bill ($)")
g.set_ylabels("Tip ($)")
g.set_axis_labels()

# 调整图例
g.legend.set_title("Day of the Week")

# 使用 plt.setp 调整图例字体大小
plt.setp(g.legend.get_texts(), fontsize=25)  # 调整图例字体大小
plt.setp(g.legend.get_title(), fontsize=30)  # 调整图例标题字体大小

# 显示图形前添加四框线
sns.despine(trim=False)  # 确保坐标轴在0点处不间断

# 设置坐标轴范围和刻度标签，确保只有一个0点
plt.gca().set_xlim(left=0)
plt.gca().set_ylim(bottom=0)

# 获取当前的刻度标签
xticks = plt.gca().get_xticks()
yticks = plt.gca().get_yticks()

# 移除横坐标轴上的0
xticks = xticks[xticks != 0]

# 设置新的刻度标签
plt.gca().set_xticks(xticks)
plt.gca().set_yticks(yticks)

# 设置坐标轴刻度和标签的大小
plt.tick_params(axis='both', which='major', labelsize=25)  # 设置所有刻度的字体大小
plt.xlabel("Total Bill ($)", fontsize=30)  # X 轴标签的字体大小
plt.ylabel("Tip ($)", fontsize=30)  # Y 轴标签的字体大小

# 显示图形
plt.show()