#!/usr/bin/env python
# coding: utf-8

# In[55]:


import sklearn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


# ### Loading csv file into a data frame

# In[56]:


df = pd.read_csv(r"C:\Users\preet\Documents\Credit Fraud\PS_20174392719_1491204439457_log.csv")


# In[57]:


df.shape


# ### Preview of data frame

# In[58]:


df.head


# In[116]:


selectedColumns =['amount','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest','isFraud']
dfCorr = df[selectedColumns]


# ### Finding correlation between important variables and if it is classified as fraud

# In[117]:


dfCorr.corr()


# ### Picking features that are correlated with fraud the most

# In[118]:


X = df[['amount', 'oldbalanceOrg', 'newbalanceOrig']]
y = df[['isFraud']]


# ### Training the model

# In[119]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[120]:


model = LogisticRegression()
model.fit(X_train, y_train)


# In[121]:


y_pred = model.predict(X_test)


# In[122]:


accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")


# ### Picking a case where fraud is obvious.
# ### Amount transacted = 79999
# ### Original Balance = 80000
# ### New Balance = 1

# In[124]:


new_data = np.array([79999, 80000, 1])  
new_predictions = model.predict(new_data.reshape(1, -1))  


# ### The array shows 1 which is another way for saying that 1 = true which means fraud has been detected

# In[125]:


new_predictions


# In[ ]:




