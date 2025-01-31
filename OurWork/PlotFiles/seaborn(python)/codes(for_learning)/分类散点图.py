# 分类散点图可以用stripplot()绘制
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid',color_codes=True) # styles:darkgrid, whitegrid, dark, white, ticks
tips=pd.read_csv(r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\datasets\datasets\tips.csv')
# sns.relplot(x='total_bill',y='tip',data=tips,hue='day',col='sex',row='time') # 绘制total_bill和tips的散点图
sns.stripplot(x='day',y='total_bill',data=tips,hue='day')
plt.show()