#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[ ]:


# %load ../helper_funcs/get_df.py
def get_df(yr):
    return pd.read_csv("../../inputs/Environmental_Data_Deep_Moor_{}.csv".format(yr))


# In[14]:


# %load ../helper_funcs/get_seasons.py
def get_seasons(yr):
    df = get_df(yr)
    return [df[df['date'].between('{}_03_20'.format(yr),'{}_06_19'.format(yr))],
            df[df['date'].between('{}_06_20'.format(yr),'{}_09_21'.format(yr))],
            df[df['date'].between('{}_09_22'.format(yr),'{}_12_20'.format(yr))],
            df[~df['date'].between('{}_03_20'.format(yr),'{}_12_20'.format(yr))]]


# In[15]:


seasons = ["Spring","Summer","Fall","Winter"]
heights = [season['Air_Temp'].mean() for season in get_seasons('2013')]


# In[22]:


alphas = [height/max(heights) for height in heights]
colors = [(.1,.7,.2,a) for a in alphas]


# In[24]:


plt.bar(seasons,heights,.6,color = colors)
plt.ylabel('Fahrenheit', fontsize=12)
plt.title('Average Temperature', fontsize=16)
plt.show

