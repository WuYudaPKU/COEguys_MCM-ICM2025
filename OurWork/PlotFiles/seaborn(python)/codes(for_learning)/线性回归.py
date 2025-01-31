# 线性回归可以用sns.lmplot()绘制
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid') # styles:darkgrid, whitegrid, dark, white, ticks
tips=pd.read_csv(r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\datasets\datasets\tips.csv')

sns.lmplot(x='total_bill',y='tip',data=tips,ci=60,hue='smoker') # 绘制total_bill和tips的散点图

# 如果是局部加权线性回归，可以传一个参数lowess=True，自行尝试一下。
sns.lmplot(x='total_bill',y='tip',data=tips,ci=60,hue='smoker',lowess=True)
plt.show()
