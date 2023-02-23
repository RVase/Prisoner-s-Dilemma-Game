# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 18:37:26 2023

@author: ricca
"""


import networkx as nx
import pandas as pd
import numpy

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

df = df[df['Time'] == 2000]


df = df[['Agent', 'Coop_list']]

df['Coop_list'] = df['Coop_list'].str.split(",")
df['Coop_list_dict'] = pd.Series([None] * len(df['Coop_list']), dtype=object)

for i in range(len(df['Coop_list'])):
    x = df['Coop_list'][i].split(":")
    df['Coop_list_dict'][i]= int(x[1])
    

G = nx.Graph()


for _, row in df.iterrows():
    node_id = row['Agent']
    node_connections = row['Coop_list']
    for connected_node, weight in node_connections.items():
        G.add_edge(node_id, connected_node, weight=weight)