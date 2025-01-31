'''
小提琴图结合了箱型图和密度图的特征，
用于展示数据的分布形状。粗黑线表示四分数范围，
延伸的细线表示95%的置信区间，白点为中位数。
小提琴图弥补了箱型图的不足，
可以展示数据分布是双模还是多模。
'''
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid',color_codes=True) # styles:darkgrid, whitegrid, dark, white, ticks
tips=pd.read_csv(r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\datasets\datasets\tips.csv')

sns.violinplot(x='day',y='total_bill',data=tips,hue='time')
plt.show()