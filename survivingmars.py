#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:19:40 2021

@author: zl
"""

import pandas as pd

#change here if you need to use a different file
df = pd.read_csv ('MapData-1617748994.csv')


#print(df.iat[2, 1])
#print(len(df))



for i in range(1, len(df)):
  #change here if you need different techs[1/2]
  #Research boost
  flag_alien = False    #Optional: 30% free research.
  flag_zero = False    #Optional: 25% free research.
  
  #Colonists and automation
  flag_brain = False    #Either this or Forever Young + Project Phoenix for good colonists.
  flag_safe = False    #Optional: You can't afford to lose someone to mismanagement.
  flag_ins = False    #Optional: Morale is important for work. Basically free +20 here.
  flag_service = False    #You need service bots reduce waste of labor.
  
  #Production
  flag_extractor = False    #Auto extractors to reduce waste of labor.
  flag_pump = False    #Optional: Important for map with low waste deposits.
  
  #Domes
  flag_gem_multi = False    #The most efficient domes in game.
  flag_prefab = False    #Optional: Use all spire variants without wasting research.

  
  
  for j in range(18, 35):
      
    if(df.iat[i, j] == 'Alien Imprints'):
      #change here if you need different techs[2/2]
      flag_alien = True;
      
    if(df.iat[i, j] == 'Zero-Space Computing'):
      #change here if you need different techs[2/2]
      flag_zero = True;
      
    if(df.iat[i, j] == 'The Positronic Brain'):
      #change here if you need different techs[2/2]
      flag_brain = True;
      
    if(df.iat[i, j] == 'Safe Mode'):
      #change here if you need different techs[2/2]
      flag_safe = True;
      
    if(df.iat[i, j] == 'Inspiring Architecture'):
      #change here if you need different techs[2/2]
      flag_ins = True;
      
    if(df.iat[i, j] == 'Service Bots'):
      #change here if you need different techs[2/2]
      flag_service = True;
      
    if(df.iat[i, j] == 'Extractor AI'):
      #change here if you need different techs[2/2]
      flag_extractor = True;
      
    if(df.iat[i, j] == 'Vector Pump'):
      #change here if you need different techs[2/2]
      flag_pump = True;
      
    if(df.iat[i, j] == 'Gem Architecture' or df.iat[i, j] == 'Multispiral Architecture'):
      #change here if you need different techs[2/2]
      flag_gem_multi = True;
      
    if(df.iat[i, j] == 'Prefab Compression'):
      #change here if you need different techs[2/2]
      flag_prefab = True;
    
    
  #fill in what you deem important
  if(flag_alien and flag_zero and flag_brain and flag_service and flag_extractor and flag_pump and flag_gem_multi):
    print(i)
    print('(' + str(df.iloc[i, 0]) + '' + str(df.iloc[i, 1]) + ', ' + str(df.iloc[i, 2]) + '' + str(df.iloc[i, 3]) + ')')
  