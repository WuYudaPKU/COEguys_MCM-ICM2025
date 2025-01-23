import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 设置 Seaborn 风格
sns.set(style='whitegrid')

# 设置全局字体为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

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

# 生成一个示例数据矩阵
data = np.random.rand(10, 12)

# 创建一个 DataFrame（可选，用于显示行列标签）
df = pd.DataFrame(data, columns=[f'Col{i}' for i in range(1, 13)], index=[f'Row{i}' for i in range(1, 11)])

# 绘制热力图
plt.figure(figsize=(10, 8))
sns.heatmap(df, annot=True, fmt='.2f', linewidths=0.5)

# 设置标题和标签
# plt.title('HeatmapExamples', fontsize=20)
plt.xlabel('Column', fontsize=15)
plt.ylabel('Row', fontsize=15)

# 显示图形
plt.show()
