#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np


# In[17]:


df = pd.read_csv("C:\\Project\\corona_tested_individuals_ver_00225.csv")
df


# In[18]:


df.isnull().sum()
df = df.dropna()


# In[19]:


df


# In[20]:


df.head()


# In[21]:


df.info()


# In[31]:


df['gender'] = df['gender'].replace({"זכר": 1, "נקבה": 0})
df['corona_result'] = df['corona_result'].replace({"חיובי": 1, "שלילי": 0})
df['age_60_and_above'] = df['age_60_and_above'].replace({"Yes": 1, "No": 0})


# In[40]:


df.describe()


# In[39]:


df[df['corona_result']==1].describe()


# In[41]:


df[df['corona_result']==0].describe()


# In[37]:


df['gender'].value_counts()


# In[ ]:





# In[ ]:




