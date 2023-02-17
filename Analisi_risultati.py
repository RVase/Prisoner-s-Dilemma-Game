# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:53:10 2023

@author: ricca
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('my_data_no_list.csv')

mean_strat = df.groupby('Time')['Strat'].mean()

std_dev = df.groupby('Time')['Strat'].std()

run_group = df.groupby('Run')['Strat'].mean()


grouped_df = df.groupby('Time')['Strat'].agg(['mean', 'std'])
error_custom = {'capsize': 4, 'capthick': 1, 'ecolor': 'black', 'elinewidth': 1}
# plot the means with error bars
ax = grouped_df.plot(kind='line', y='mean', yerr='std', legend=None)

ax.set_xlabel('Time')

# set the y-axis label
ax.set_ylabel('Strat')

# set the plot title
ax.set_title('Mean Value with Standard Deviation')

# show the plot
plt.show()







