import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
plt.rcParams['text.usetex'] = True

# 设置全局字体为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

sns.set(style='whitegrid')
# 读取 CSV 文件
file_path = r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\ourcodes\sensibility\change_capacity.csv'  # 更新文件路径
data = pd.read_csv(file_path)

# 检查数据的前几行，确保读取正确
print(data.head())

color_science_dict = {
    'crop': (153/255, 55/255, 153/255),      # #993799
    'straw': (254/255, 136/255, 0/255),      # #FE8800
    'weed': (50/255, 90/255, 160/255),       # #325AA0
    'insect': (100/255, 100/255, 100/255),   # #646464
    'bird': (66/255, 153/255, 56/255),       # #429938
    'frog': (245/255, 113/255, 109/255),     # #F5716D
    'duck': (255/255, 172/255, 96/255),      # #FFAC60
    'bat': (0/255, 0/255, 0/255),            # #000000
    'snake': (204/255, 228/255, 203/255),    # #CCE4CB
    'herbicide': (233/255, 226/255, 156/255),# #E9E29C
    'pesticide': (227/255, 26/255, 28/255),  # #E31A1C
    '1': (153/255, 55/255, 153/255),    # #993799
    '2': (185/255, 103/255, 180/255),   # #B967B4
    '3': (213/255, 166/255, 208/255),   # #D5A6D0
    '4': (0/255, 0/255, 0/255),    # #FE8800
    '5': (102/255, 102/255, 102/255),   # #FFAC33
    '6': (150/255, 150/255, 150/255)   # #FFCC66
}


# print(color_science_dict)
# 假设每一行代表一个时间点
time = np.arange(len(data))

# 创建平滑曲线函数
def smooth_curve(x, y, points=500):
    x_smooth = np.linspace(x.min(), x.max(), points)
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_smooth)
    return x_smooth, y_smooth

# 创建图形并绘制 insect, bat 和 duck
plt.figure(figsize=(10, 8))

x_smooth, y_smooth = smooth_curve(time, data['K=35000'])
sns.lineplot(x=x_smooth, y=y_smooth, label=r'$K=35000$',linewidth=4,color=color_science_dict['crop'])

x_smooth, y_smooth = smooth_curve(time, data['K=30000'])
sns.lineplot(x=x_smooth, y=y_smooth, label=r'$K=30000$', linewidth=4,color=color_science_dict['weed'])

x_smooth, y_smooth = smooth_curve(time, data['K=25000'])
sns.lineplot(x=x_smooth, y=y_smooth, label=r'$K=25000$', linewidth=4,color=color_science_dict['straw'])

# x_smooth, y_smooth = smooth_curve(time, data['wd0.1'])
# sns.lineplot(x=x_smooth, y=y_smooth, label='wd,0.1', linewidth=3,dashes=[3,1],color=color_science_dict['6'])

# x_smooth, y_smooth = smooth_curve(time, data['wd0.3'])
# sns.lineplot(x=x_smooth, y=y_smooth, label='wd,0.3', linewidth=3,dashes=[3,1],color=color_science_dict['5'])

# x_smooth, y_smooth = smooth_curve(time, data['wd0.5'])
# sns.lineplot(x=x_smooth, y=y_smooth, label='wd,0.5', linewidth=3,dashes=[3,1],color=color_science_dict['4'])

plt.title('Change of Biomass Capacity of Rice', fontsize=30)
plt.xlabel('t(Week)', fontsize=25)
plt.ylabel('Biomass(kg) of Rice', fontsize=25)  # 修改单位为 kg
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend(title='Size', fontsize=25, title_fontsize=28, loc='best')  # 将图例放在合适位置
for spine in plt.gca().spines:
    plt.gca().spines[spine].set_visible(True)
    plt.gca().spines[spine].set_color('black')
    plt.gca().spines[spine].set_linewidth(2)
plt.tight_layout()
plt.show()