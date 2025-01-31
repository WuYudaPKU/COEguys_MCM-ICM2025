import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np  # 保留 numpy 引用

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

# 读取 Excel 文件
file_path = r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\codes\temparature_mean_chart.xlsx'
data = pd.read_excel(file_path)

# 创建三条折线图
plt.figure(figsize=(10, 6))

# 绘制三条折线图，使用自定义颜色
sns.lineplot(x='Category', y='AveMax', data=data, label='Mean daily maximum °C', marker='o', color=color_science_normalized[0])
sns.lineplot(x='Category', y='AveMean', data=data, label='Daily mean °C', marker='^', color=color_science_normalized[1])
sns.lineplot(x='Category', y='AveMin', data=data, label='Mean daily minimum °C', marker='o', color=color_science_normalized[2])

# 设置图表标题和标签
plt.title('Temperature Trends Across the Year', fontsize=30)
plt.xlabel('Month', fontsize=25)
plt.ylabel('Temperature (°C)', fontsize=25)

# 设置 x 轴的月份，旋转标签
plt.xticks(rotation=45, fontsize=25)

# 添加图例
plt.legend(title='Temperature Types', fontsize=25, title_fontsize=28)

# 调整坐标轴刻度的字体大小
plt.tick_params(axis='both', which='major', labelsize=25)

# 设置坐标轴范围和刻度标签
plt.gca().set_xlim(left=0)
plt.gca().set_ylim(bottom=0)

# 绘制黑色框线
for spine in plt.gca().spines:
    plt.gca().spines[spine].set_visible(True)
    plt.gca().spines[spine].set_color('black')
    plt.gca().spines[spine].set_linewidth(2)

# 显示图形
plt.tight_layout()
plt.show()
