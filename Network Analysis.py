# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:37:26 2023

@author: ricca
"""


import networkx as nx
import pandas as pd
import numpy
import matplotlib.pyplot as plt
# s = "a:1,b:3,c:4"
# x = s.split(",")

# d={}
# for i in x:
#     y=i.split(":")
#     d[y[0]]=int(y[1])

# def strig_to_dict(s):
#     for x in s: 
#         s = s.split(",")


df = pd.read_csv("my_data_with_dict.csv") 

df_2 = df[df['Time'] == 2000]
df_time = df[df['Time'] == 2000]


df_2 = df_2[['Agent', 'Coop_list']]

df_2['Coop_list'] = df['Coop_list'].str.split(",")
df_2['Coop_list_dict'] = pd.Series([None] * len(df['Coop_list']), dtype=object)
df_3 = df_2.reset_index(drop=True)
for i in range(len(df_3['Coop_list'])):
    df_3['Coop_list_dict'][i] = {}
    for ju in range(len(df_3['Coop_list'][i])):
            df_3['Coop_list'][i][ju] = df_3['Coop_list'][i][ju].split(":")
            df_3['Coop_list'][i][ju][0] = df_3['Coop_list'][i][ju][0].replace('{','')
            df_3['Coop_list'][i][ju][0] = df_3['Coop_list'][i][ju][0].replace('Agent','')
            df_3['Coop_list'][i][ju][0] = df_3['Coop_list'][i][ju][0].replace(' ','')
            df_3['Coop_list'][i][ju][1] = df_3['Coop_list'][i][ju][1].replace('}','')

df_3['Agent'] = df_3['Agent'].apply(str)
for i in range(len(df_3['Coop_list'])):
    for ju in range(len(df_3['Coop_list'][i])):
        df_3['Coop_list_dict'][i][df_3['Coop_list'][i][ju][0]] = int(df_3['Coop_list'][i][ju][1])
        

G = nx.DiGraph()


for _, row in df_3.iterrows():
    node_id = row['Agent']
    node_connections = row['Coop_list_dict']
    for connected_node, weight in node_connections.items():
        G.add_edge(node_id, connected_node, weight=weight)
        

# nx.info(G)
        
degree_counts = nx.degree_histogram(G)
print("Degree distribution:", degree_counts)

# clustering_coefficient = nx.average_clustering(G)
# print("Average clustering coefficient:", clustering_coefficient)

# print(type(G))



# #Drawing
# pos = nx.spring_layout(G)
# node_size = 500
# node_color = 'lightblue'

# edge_width = 2.5
# edge_color = 'gray'

# fig, ax = plt.subplots(figsize=(50, 50))
# nx.draw(G, pos=pos, with_labels=True, node_size=node_size, node_color=node_color,
#         width=edge_width, edge_color=edge_color, ax=ax)
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)
# plt.show()