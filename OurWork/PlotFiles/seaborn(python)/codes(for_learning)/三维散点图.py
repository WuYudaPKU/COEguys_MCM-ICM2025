import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# 创建一个 3D 图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制三维散点图，使用你的调色方案
scatter = ax.scatter(x, y, z, c=z, cmap=plt.cm.get_cmap('coolwarm'), s=50)

# 设置标题和坐标轴标签
ax.set_title('3D Scatter Plot Example', fontsize=30)
ax.set_xlabel('X Axis', fontsize=25)
ax.set_ylabel('Y Axis', fontsize=25)
ax.set_zlabel('Z Axis', fontsize=25)

# 调整坐标轴刻度
plt.tick_params(axis='both', which='major', labelsize=25)

# 设置框线为黑色
for spine in ['top', 'bottom', 'left', 'right']:
    ax.spines[spine].set_visible(True)
    ax.spines[spine].set_color('black')
    ax.spines[spine].set_linewidth(2)

# 显示图形
plt.show()