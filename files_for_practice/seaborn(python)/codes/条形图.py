import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 设置 Seaborn 风格
sns.set(style='whitegrid')

# 设置全局字体为 Times New Roman（英文）和 SimHei（中文）
plt.rcParams['font.family'] = ['Times New Roman', 'SimHei']

# 自定义调色板
color_science = [
    (153, 55, 153),   # #993799
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

# 示例数据
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [23, 45, 56, 78, 33]
}

df = pd.DataFrame(data)

# 绘制条形图
plt.figure(figsize=(10, 8))
sns.barplot(x='Category', y='Value', data=df, palette=color_science_normalized)

# 设置标题和标签
plt.title('Bar Plot Example', fontsize=30)  # 设置英文标题
plt.xlabel('Category', fontsize=25)
plt.ylabel('Value', fontsize=25)

# 调整坐标轴刻度和标签的字体大小
plt.tick_params(axis='both', which='major', labelsize=25)

for ax in plt.gca().spines:
    plt.gca().spines[ax].set_visible(True)
    plt.gca().spines[ax].set_color('black')
    plt.gca().spines[ax].set_linewidth(2)

# 显示图形
plt.show()