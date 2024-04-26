#!/usr/bin/env python
# coding: utf-8

# In[15]:


import sklearn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')


# In[3]:


df = pd.read_csv(r"C:\Users\preet\Documents\AdvertisingData\Advertising.csv")


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


sns.scatterplot(data=df, x="TV", y="Sales")
plt.xticks([0,100,200,300,400])


# In[7]:


sns.scatterplot(data=df, x="Radio", y="Sales")
plt.xticks([0,100,200,300,400])


# In[8]:


sns.scatterplot(data=df, x="Newspaper", y="Sales")
plt.xticks([0,100,200,300,400])


# In[9]:


reg = LinearRegression()


# In[10]:


reg.fit(df[['TV','Radio','Newspaper']], df.Sales)


# In[17]:


reg.predict([[300,0,0]])


# In[12]:


df.head(89)


# In[13]:


display(df.iloc[88])


# In[16]:


reg.predict([[88.3,25.5,73.4]])


# In[ ]:





# In[ ]:




