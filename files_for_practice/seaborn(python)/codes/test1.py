import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set(style='darkgrid') # styles:darkgrid, whitegrid, dark, white, ticks
sns.set(palette='RdBu')
tips=pd.read_csv(r'D:\2025_PKUCOE_MCM\files_for_practice\seaborn(python)\datasets\datasets\tips.csv')
sns.relplot(
    data=tips,
    x='total_bill',y='tip',col='time',
    hue='smoker',style='smoker',size='size'
)
plt.show()