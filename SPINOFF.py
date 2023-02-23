# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 18:49:45 2022

@author: ricca
"""
import pandas as pd
import numpy as np 
import random 
from random import seed
from scipy import stats 
from random import randint, uniform
import networkx as nx
import matplotlib.pyplot as plt
import math 
from random import choices
import pickle



class Agent():
    def __init__(self, agent_id): 
        self.agent_id = agent_id
        self.strategy = 0.5 + random.uniform(-0.2 , 0.2) #np.random.normal(loc = 0.5 ,scale = 0.1) #random.uniform(0,1)
        self.payoff = 0
        self.coop_dict = {}
        self.coop_list =[]
    #strategy tra 0 e 1 prob. di cooperare
    #payoff
    #list di cooperatori (goods)
    def __repr__(self):
        rep = 'Agent' + str(self.agent_id) 
        return rep

class World():
    def __init__(self, run_nums, time, repr_rate, agent_number, rate_list):
        self.run_nums = run_nums
        self.time = time
        self.repr_rate = repr_rate
        self.agent_number = agent_number
        self.rate_list = rate_list
        self.agent_set = []
        self.payoff = 0
        self.list_of_dict = []
        self.tick = 0
        self.run = 0
        
        
    def create_agent_set(self):
        for i in range(self.agent_number):
            self.agent_set.append(Agent(i))
            
            
            
    def char_df_creation(self):
        for agent in self.agent_set:
            self.char_dict = {'Time':self.tick,
                              'Agent':agent.agent_id,   
                             'Strat':agent.strategy,
                             'Payoff':agent.payoff,
                             'Run':self.run,
                             'Coop_list':agent.coop_dict}
            self.list_of_dict.append(self.char_dict) 
        self.char_df = pd.DataFrame(self.list_of_dict)


#run_nums = quante simulazioni
#time = numero di cicli della simul. 
#repr_rate = dopo quanto mi riproduco
#numero degli agenti =
#r_l = rate di scelta dalla lista


#dataframe con i risultati : 
#run
#t
# strategy
# numero di cooperazioni
# numero di link stesi 
# numero di spedizioni 
# lunghezza media liste
# variabilita' dentro le liste 


#for run 
    #for t
        #for n = numero degli agent
            #pick an agent i and pick an agent j r_l from list (weight), else random
            #i plays with j (prisoner dilemma) 
            #payoff update
            #metto nella lista di i j se j cooperato, stessa cosa per j
        #if t%rep_rate= 0 : 
            #riproduzione for n = agent: 
                #pick an agent lotteria stocastica sul suo payoff allora lo riproduco (sostituisco un agente)
        #salva nel dataframe ogni rate di salvataggio 
        

# def chose_player(player1):
    
#     choice = random.choices([0,1], weights = (my_world.rate_list, 1-my_world.rate_list))
#     if choice == 0 and player1.coop_list:
#         return p2 = random.choice(player1.coop_list)    
#     else:
#         return p2 = random.choice(my_world.agent_set)
        




def game(p1, p2):
    strat = ['coop', 'defect']
    if p1 != p2:
        p1_strat_chosen = random.choices(strat, weights = (p1.strategy, 1-p1.strategy))
        p2_strat_chosen = random.choices(strat, weights = (p2.strategy, 1-p2.strategy))
        
        if p1_strat_chosen == ['coop'] and p2_strat_chosen == ['coop']:
            p1.payoff += 3
            p2.payoff += 3
            
            if p2  in p1.coop_dict:
                p1.coop_dict[p2] += 1
            else:
                p1.coop_dict[p2] = 1
                
            if p1  in p2.coop_dict:
                p2.coop_dict[p1] += 1
            else:
                p2.coop_dict[p1] = 1
            
            # p1.coop_list.append(p2)
            # p2.coop_list.append(p2)
            
        elif  p1_strat_chosen == ['defect'] and p2_strat_chosen == ['coop']:
            p1.payoff += 5
            p2.payoff += 0
            
            if p1 in p2.coop_dict:
                p2.coop_dict[p1] -= 1
            
            if p2 in p1.coop_dict:
                p1.coop_dict[p2] += 1
            else:
                p1.coop_dict[p2] = 1
            p1.coop_list.append(p2)
            
        elif  p1_strat_chosen == ['coop'] and p2_strat_chosen == ['defect']:
            p1.payoff += 0
            p2.payoff += 5
            
            
            if p2 in p1.coop_dict:
                p1.coop_dict[p2] -= 1
        
            if p1  in p2.coop_dict:
                p2.coop_dict[p1] += 1
            else:
                p2.coop_dict[p1] = 1
            p2.coop_list.append(p2)
            
        elif  p1_strat_chosen == ['defect'] and p2_strat_chosen == ['defect']:
            p1.payoff += 1
            p2.payoff += 1   
    
        
                

my_world = World(1, 1000, 5, 50, 0.8) #run_nums, time, repr_rate, agent_number, rate_list

df_result = pd.DataFrame()

df_list = []

for seeds in range(my_world.run_nums):
    seed_number = seeds   #4 3 2 0 no 1 
    np.random.seed(seed_number)   
    seed(seed_number)

    my_world.tick = 0
   # my_world.char_dict = {}   
    my_world.agent_set = []
    
    my_world.create_agent_set()
                              
        
    for t in range(my_world.time):

        for n in range(my_world.agent_number):
            
            p1 = my_world.agent_set[n]
            choice = random.choices([0,1], weights = (my_world.rate_list, 1-my_world.rate_list))
        
    
            # create a list of keys and a list of weights
            keys = list(p1.coop_dict.keys())
            weights = list(p1.coop_dict.values())
            
            ordered_agents_strat = sorted(my_world.agent_set, key = lambda x: x.strategy, reverse = True)
    
            
            
            
            if choice == [0] and len(p1.coop_dict) > 0:
                p2 = random.choices(keys, weights=weights, k=1)[0]    
                game(p1, p2)
    
    
    
    
    
                                       #### random.choice(my_world.agent_set) #p2 = random.choice(p1.coop_list)    
            else:
                p2 = random.choice(my_world.agent_set)
                
                game(p1, p2)
                        
            d1 = p1.coop_dict
            dict_sum = 0
            if len(d1) > 0: 
                for key, value in d1.items():
                    dict_sum += value
                dict_avg = dict_sum / len(d1)
            
            if  t>50: #p1.strategy >0.6 and
                for key, value in d1.items():
                    if value > dict_avg:
                        d2 = key.coop_dict
                        for key2, value2 in d1.items():
                            if key2 != key and value2 > dict_avg:#and key2.strategy > 0.7 :# and key2 not in p1.coop_list:
                                if key2 in d2:
                                    d2[key2] += 1
                                else:
                                    d2[key2] = 1
                
            
            
            
            
                    # if p1.strategy > 0.75:
                    #     for i in range(50):
                    #         v = ordered_agents_strat[-1] 
                    #         if v  in p1.coop_dict:
                    #             p1.coop_dict[v] += 1
                    #         else:
                    #             p1.coop_dict[v] = 1
    
                
            # p3 = random.choice(my_world.agent_set)                
            # if p1 != p3:
            #     p3.coop_list += p1.coop_list
        
        for agent in my_world.agent_set:
            random.choices(my_world.agent_set)
            
        tuple_list = []
        for i in range(len(my_world.agent_set)):
            tuple_list.append([my_world.agent_set[i],my_world.agent_set[i].payoff, my_world.agent_set[i].strategy])
            
        if (t % 5) == 0:    
            for ag in range(10):
                poff_array = np.array(tuple_list)
                poff_col = poff_array[:,1]
                poff_min = np.min(poff_col)
                adj_poff = poff_col + abs(poff_min)        
                poff_sum = np.sum(adj_poff)
                adj_poff = adj_poff/poff_sum 
                
                poff_max = np.max(poff_col)
                adj_poff_vic = - (poff_col - abs(poff_max))
                poff_sum_vic = np.sum(adj_poff_vic)
                adj_poff_vic = adj_poff_vic/poff_sum_vic 
                
                replicant = random.choices(poff_array[:,0], adj_poff)    
                victim = random.choices(poff_array[:,0], adj_poff_vic)
                
                victim[0].strategy = replicant[0].strategy + random.uniform(-0.05 , 0.05)
                victim[0].coop_dict = {}
                
                for i in range(len(my_world.agent_set)):
                    if victim[0] in my_world.agent_set[i].coop_dict:
                        del my_world.agent_set[i].coop_dict[victim[0]]
                
          #      my_world.agent_set[victim].strategy = my_world.agent_set[victim].strategy + random.uniform(-0.1 , 0.1)
                if victim[0].strategy < 0:
                    victim[0].strategy = 0
                elif victim[0].strategy > 1:
                    victim[0].strategy = 1
    
            
        my_world.tick += 1 
    
        if t == 0 or (t+1) % 50 == 0:
            my_world.char_df_creation()
            df = my_world.char_df
            df_list.append(df)
    my_world.run += 1
    
            

mean_strat = df.groupby('Time')['Strat'].mean()
mean_strat.plot()
plt.xlabel('Time')
plt.ylabel('Mean Cooperation Score')
plt.show()
