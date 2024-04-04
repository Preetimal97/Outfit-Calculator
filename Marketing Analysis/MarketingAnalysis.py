#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install scikit-learn


# In[3]:


import sklearn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
from sklearn.preprocessing import OneHotEncoder



# In[5]:


#https://www.kaggle.com/datasets/ahsan81/superstore-marketing-campaign-dataset?resource=download
df = pd.read_csv("C:\\Users\\preet\\Documents\\MarketingAnalysis\\superstore_data.csv")

#print (df)

df.head()


# ### A store wants to attract new customers. They want to have three seperately tailored marketing camapigns for web, catalog, and store buyers. They want each campaign to be tailored to each of these three types of buyers. They also want a fourth campaign that will focus on broader based ads to target those who purchase the most from the company. From analyzing the traits and behavior from current customers we will be analyzing the data in order to find more insights into the type of prospective new customers we would be tailoring the campaign to for each of the marketing campaigns.

# In[17]:


df.shape


# ### To better visualize the data we are going to calculate the age of the customers and make a new column that contains these values.
# 

# In[26]:


print(df['Year_Birth'])


# In[9]:


df['Age'] = 2024 - (df['Year_Birth'])


# In[36]:


df.head()


# ### Create a sub-table to analyze the relationship between the age, if there are kids or teens at home with how the customer likes to purchase their products.

# In[10]:


df_2 =df[['Age','Kidhome','Teenhome','NumWebPurchases','NumCatalogPurchases','NumStorePurchases']]


# In[46]:


print (df_2)


# ### Running the correlation function to find the numeric correlations between the variables.

# In[11]:


df_2.corr()


# In[51]:


sns.heatmap(df_2.corr(),  cmap= "YlGnBu")


# ### It seems like if the customers have kids or teens they are more likely to purchase using the web. Those with kids have a negative correlation to using the store. Lets now try to put more variables to analyze the dataset further.

# In[13]:


df['Education'].unique()


# ### Convert nominal data into ordinal data by encoding it

# In[16]:


ohe = OneHotEncoder(handle_unknown='ignore', sparse_output = False).set_output(transform= 'pandas')


# In[17]:


ohetransform = ohe.fit_transform(df[['Education']])


# In[18]:


ohetransform


# ### Add the encoded nominal values to the original dataset

# In[19]:


df = pd.concat([df,ohetransform], axis = 1)


# In[20]:


df


# In[21]:


df_3 =df[['Education_2n Cycle','Education_Basic','Education_Graduation','Education_Master','Education_PhD','NumWebPurchases','NumCatalogPurchases','NumStorePurchases']]


# In[22]:


df_3


# ### Find correlation using corr() function

# In[23]:


df_3.corr()


# ### Now visualizing data with heatmap

# In[24]:


sns.heatmap(df_3.corr(),  cmap= "YlGnBu")


# ### From this we can see very clearly that those with PHD, masters, and graduation contribute to the most purchases and the ones with basic education contrubute to the least purchases. We can also see most of them prefer web purchases although store and catalog purchases are still plentiful.

# In[25]:


df['Marital_Status'].unique()


# In[26]:


ohetransform2 = ohe.fit_transform(df[['Marital_Status']])


# In[27]:


ohetransform2 


# In[28]:


df = pd.concat([df,ohetransform2], axis = 1)


# In[29]:


df


# In[30]:


df_4 =df[['Marital_Status_Absurd','Marital_Status_Alone','Marital_Status_Divorced','Marital_Status_Married','Marital_Status_Single','Marital_Status_Together','Marital_Status_Widow','Marital_Status_YOLO','NumWebPurchases','NumCatalogPurchases','NumStorePurchases',]]


# In[31]:


df_4


# In[32]:


df_4.corr()


# In[47]:


sns.heatmap(df_4.corr(),  cmap= "YlGnBu")


# ### From this heatmap we can deduce widows tend to purchase the most. The divorced seem to spend a lot through the web. And the absurd martial status group tends to be the ones to spend the most through the catalog.

# ### It seems the ones with highest income make the most catalog purchases
# 

# ### From our analysis we have learned:
# ### Most Web purchases: Divorced, and with Teens
# ### Most Catalog purchases: Absurd martial status
# ### Most Store purchases: Those with kids have a negative correlation to buying in store.
# ### Most purchases in general: Widows, PHD, Masters, and those who graduated
# 

# In[57]:


df = pd.read_csv("C:\\Users\\preet\\Documents\\MarketingAnalysis\\superstore_data.csv")


# In[62]:


df


# ### Creating Webfocusgroup where it will target customers who are divorced and have teens at home

# In[195]:


#filtered_df = df.query('Marital_Status == "Divorced"')

Webfocusgroup = df.query('(Marital_Status == "Divorced") & (Teenhome == 1)' )


# In[197]:


Webfocusgroup

#Webfocusgroup = df.query('(Marital_Status == "Divorced") & (Kidhome == 1)')


# ### Creates Catalogfocusgroup which will target those who label their martial status as absurd.

# In[201]:


Catalogfocusgroup = df.query('Marital_Status == "Absurd"')


# In[202]:


Catalogfocusgroup


# ### Creates Storefocusgroup which targets those without kids at home.

# In[205]:


Storefocusgroup = df.query('Kidhome == 0')


# In[206]:


Storefocusgroup


# ### Creates Totalfocusgroup which focuses on the ones who make the most purchases overall which are those who are widowed and have either Phd, Master, or Graduation as their education.

# ### First I will filter through education

# In[291]:


filter1 = df.query('Education == "PhD" or Education == "Master" or Education == "Graduation"')


# In[292]:


filter1


# ### Then I will filter by Marital Status

# In[294]:


Totalfocusgroup = filter1.query('Marital_Status == "Widow"')


# In[295]:


Totalfocusgroup


# ### To conclude based on this analysis the company can choose the right target groups for each of their ad types and the amount of money and labor to be spent behind each one

# In[ ]:




