# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:50:43 2023

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
df9 = pd.read_csv('100_ag_09_rl.csv')


df =  df[df['Time'] == 1000]
df1 = df1[df1['Time'] == 1000]
df2 = df2[df2['Time'] == 1000]
df3 = df3[df3['Time'] == 1000]
df4 = df4[df4['Time'] == 1000]
df5 = df5[df5['Time'] == 1000]
df6 = df6[df6['Time'] == 1000]
df7 = df7[df7['Time'] == 1000]
df8 = df8[df8['Time'] == 1000]
df9 = df9[df9['Time'] == 1000]

# run = 5
# df =  df[df['Run'] == run]
# df1 = df1[df1['Run'] == run]
# df2 = df2[df2['Run'] == run]
# df3 = df3[df3['Run'] == run]
# df4 = df4[df4['Run'] == run]
# df5 = df5[df5['Run'] == run]
# df6 = df6[df6['Run'] == run]
# df7 = df7[df7['Run'] == run]
# df8 = df8[df8['Run'] == run]
# df9 = df9[df9['Run'] == run]

data_1 = df['Strat']
data_2 = df2['Strat']
data_3 = df3['Strat']
data_4 = df4['Strat']
data_5 = df5['Strat']
data_6 = df6['Strat']
data_7 = df7['Strat']
data_8 = df8['Strat']
data_9 = df9['Strat']
data = [data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9]

fig = plt.figure(figsize =(10, 7))
ax = fig.add_axes([0, 0, 1, 1])
# df['Strat'].hist()
# df1['Strat'].hist()
# df2['Strat'].hist()
# df3['Strat'].hist()
# df4['Strat'].hist()
# df5['Strat'].hist()
# df6['Strat'].hist()
# df7['Strat'].hist()
# df8['Strat'].hist()
df9['Strat'].hist()

# bp = ax.boxplot(data)

plt.show()