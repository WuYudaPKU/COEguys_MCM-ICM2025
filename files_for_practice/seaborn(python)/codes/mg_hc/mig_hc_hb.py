import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# ...existing code...

# 设置全局字体为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

sns.set(style='whitegrid')
# 读取 CSV 文件
file_path = r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\codes\mig_herb.csv'  # 更新文件路径
data = pd.read_csv(file_path)

# 检查数据的前几行，确保读取正确
print(data.head())

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

# 假设每一行代表一个时间点
time = np.arange(len(data))

# 创建图形并绘制 herbicide
plt.figure(figsize=(10, 8))
sns.lineplot(x=time, y=data['herbicide'], label='herbicide', color=color_science_normalized[0], linewidth=5)
plt.title('Herbicide Biomass Over Time', fontsize=30)
plt.xlabel('Time', fontsize=25)
plt.ylabel('Biomass (g)', fontsize=25)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend(title='Populations', fontsize=25, title_fontsize=28, loc='best')  # 将图例放在合适位置
for spine in plt.gca().spines:
    plt.gca().spines[spine].set_visible(True)
    plt.gca().spines[spine].set_color('black')
    plt.gca().spines[spine].set_linewidth(2)
plt.tight_layout()
plt.show()