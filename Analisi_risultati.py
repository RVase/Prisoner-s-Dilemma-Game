# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:53:10 2023

@author: ricca
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('my_data_no_list.csv')
df1 = pd.read_csv('my_data_010.csv')
df2 = pd.read_csv('my_data_020.csv')
df3 = pd.read_csv('my_data_030.csv')
df4 = pd.read_csv('my_data_040.csv')
df5 = pd.read_csv('my_data_050.csv')
df6 = pd.read_csv('my_data_060.csv')
df7 = pd.read_csv('my_data_070.csv')
df8 = pd.read_csv('my_data_080.csv')
df9 = pd.read_csv('my_data_090.csv')


mean_strat = df.groupby('Time')['Strat'].mean()

std_dev = df.groupby('Time')['Strat'].std()

run_group = df.groupby('Run')['Strat'].mean()

mean_strat = df.groupby('Time')['Strat'].mean()
mean_strat_1 = df1.groupby('Time')['Strat'].mean()
mean_strat_2 = df2.groupby('Time')['Strat'].mean()
mean_strat_3 = df3.groupby('Time')['Strat'].mean()
mean_strat_4 = df4.groupby('Time')['Strat'].mean()
mean_strat_5 = df5.groupby('Time')['Strat'].mean()
mean_strat_6 = df6.groupby('Time')['Strat'].mean()
mean_strat_7 = df7.groupby('Time')['Strat'].mean()
mean_strat_8 = df8.groupby('Time')['Strat'].mean()
mean_strat_9 = df9.groupby('Time')['Strat'].mean()

# grouped_df = df.groupby('Time')['Strat'].agg(['mean', 'std'])
# #error_custom = {'capsize': 4, 'capthick': 1, 'ecolor': 'black', 'elinewidth': 1}
# # plot the means with error bars
# #ax = grouped_df.plot(kind='line', y='mean', yerr='std', legend=None)
# ax = grouped_df.plot(kind='line', y='mean', legend= 'luba')
# ax.set_xlabel('Time')

# # set the y-axis label
# ax.set_ylabel('Strat')

# # set the plot title
# ax.set_title('Strategy Mean Value')

# # show the plot
# plt.show()

y1 = mean_strat.plot(kind='line', y='mean', label = 'no list') 
y2 = mean_strat_1.plot(kind='line', y='mean', label = '10%') 
y3 = mean_strat_2.plot(kind='line', y='mean', label = '20%') 
y4 = mean_strat_3.plot(kind='line', y='mean', label = '30%') 
y5 = mean_strat_4.plot(kind='line', y='mean', label = '40%%') 
y6 = mean_strat_5.plot(kind='line', y='mean', label = '50%') 
y7 = mean_strat_6.plot(kind='line', y='mean', label = '60%') 
y8 = mean_strat_7.plot(kind='line', y='mean', label = '70%') 
y9 = mean_strat_8.plot(kind='line', y='mean', label = '80%') 
y10 = mean_strat_9.plot(kind='line', y='mean', label = '90%')

plt.xlabel('Time')
plt.ylabel('Mean Cooperation Score')

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), )
y10.plot(color = 'blue')
y9.plot(color = 'blue')
y8.plot(color = 'blue')
y7.plot(color = 'blue')
y6.plot(color = 'blue')
y5.plot(color = 'blue')
y4.plot(color = 'blue')
y3.plot(color = 'blue')
y2.plot(color = 'blue')
y1.plot(color = 'blue')


plt.show()





