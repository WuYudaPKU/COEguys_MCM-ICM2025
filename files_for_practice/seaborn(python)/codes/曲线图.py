import seaborn as sns
import matplotlib.pyplot as plt
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
x = np.linspace(0, 10, 100)
y = np.sin(x)  # 正弦波

# 绘制曲线图
plt.figure(figsize=(10, 8))
sns.lineplot(x=x, y=y, color=color_science_normalized[0])  # 使用自定义颜色

# 设置标题和标签
plt.title('Sine Wave Example', fontsize=30)  # 设置英文标题
plt.xlabel('X Axis', fontsize=25)
plt.ylabel('Y Axis', fontsize=25)

# 自动调整坐标轴范围以适应数据
plt.axis('tight')  # 自动调整坐标轴范围到数据的边界

# 或者，也可以手动调整 x 和 y 坐标轴范围：
# plt.gca().set_xlim([min(x), max(x)])  # 设置 x 轴范围
# plt.gca().set_ylim([min(y), max(y)])  # 设置 y 轴范围

# 调整坐标轴刻度和标签的字体大小
plt.tick_params(axis='both', which='major', labelsize=25)

# 绘制黑色框线
for ax in plt.gca().spines:
    plt.gca().spines[ax].set_visible(True)
    plt.gca().spines[ax].set_color('black')
    plt.gca().spines[ax].set_linewidth(2)

# 显示图形
plt.show()
