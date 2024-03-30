#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os


# In[10]:


hair = pd.read_csv('PredictHairFall.csv')
hair.head()


# In[5]:


hair = pd.read_csv('PredictHairFall.csv')
hair.head()
#hair.query('Age == 30')
#hair.query(['Hormonal Changes'] == "Yes")
#plt.hist(hair['Environmental Factors'])
hair = hair.rename(columns={'Hormonal Changes': 'Hormonal_Changes'})
hair = hair.rename(columns={'Hair Loss': 'Hair_Loss'})

#print(hair.Hormonal_changes)

#print (hair)
#hair.head()

#hair.query('Hormonal_Changes == "No"')



 






# In[302]:


hair = hair.rename(columns={'Medical Conditions': 'Medical_Conditions'})
hair.query('Medical_Conditions == "Eczema" and Stress == "High"')

EHquery = hair.query('Medical_Conditions == "Eczema" and Stress == "High"')
EHquery['Hair_Loss'] = EHquery['Hair_Loss'].astype(str)

EHquery['Hair_Loss'].replace('1', 'Yes', inplace=True)
EHquery['Hair_Loss'].replace('0', 'No', inplace=True)
print (EHquery)


 


# In[324]:


plt.hist(EHquery.Hair_Loss)
plt.title('Occurrence of Hair loss when subject is having Eczema and high stress')
plt.figure(figsize=(55, 5))

#It seems having eczema and a high stress life does not affect hair loss that much


# In[30]:


#Creating a pie chart to show the stress levels of those with Hair Loss

hair = pd.read_csv('PredictHairFall.csv')
hair = hair.rename(columns={'Hair Loss': 'Hair_Loss'})
hair['Hair_Loss'] = hair['Hair_Loss'].astype(str)

hair['Hair_Loss'].replace('1', 'Yes', inplace=True)
hair['Hair_Loss'].replace('0', 'No', inplace=True)
#print (hair)
YesHigh = hair.query( 'Hair_Loss == "Yes" and Stress == "High"').count()[0] #156
YesModerate = hair.query( 'Hair_Loss == "Yes" and Stress == "Moderate"').count()[0] #182
YesLow = hair.query( 'Hair_Loss == "Yes" and Stress == "Low"').count()[0] #159
#print (YesHigh)
#print (YesModerate)
#print (YesLow)
NoHigh = hair.query( 'Hair_Loss == "No" and Stress == "High"').count()[0] #165
NoModerate = hair.query( 'Hair_Loss == "No" and Stress == "Moderate"').count()[0] #169
NoLow = hair.query( 'Hair_Loss == "No" and Stress == "Low"').count()[0] #168
#print (NoHigh)
#print (NoModerate)
print (NoLow)
#EHquery = hair.query('Medical_Conditions == "Eczema" and Stress == "High"')

#Psoriasis = hair.loc[hair['Medical Conditions'] == 'Psoriasis'].count()[0]
#Eczema = hair.loc[hair['Medical Conditions'] == 'Eczema'].count()[0]

#print(Psoriasis)
#print(Eczema)





# In[45]:


hair = pd.read_csv('PredictHairFall.csv')
hair = hair.rename(columns={'Hair Loss': 'Hair_Loss'})
hair['Hair_Loss'] = hair['Hair_Loss'].astype(str)

hair['Hair_Loss'].replace('1', 'Yes', inplace=True)
hair['Hair_Loss'].replace('0', 'No', inplace=True)
#print (hair)
YesHigh = hair.query( 'Hair_Loss == "Yes" and Stress == "High"').count()[0] #156
YesModerate = hair.query( 'Hair_Loss == "Yes" and Stress == "Moderate"').count()[0] #182
YesLow = hair.query( 'Hair_Loss == "Yes" and Stress == "Low"').count()[0] #159
#print (YesHigh)
#print (YesModerate)
#print (YesLow)
plt.title('Distribution of stress levels when there is hair loss')
labels = ['High','Moderate','Low']
colors = ['Red', 'Yellow','Green']
plt.pie([YesHigh,YesModerate,YesLow], labels = labels, autopct = '%.2f%%')
plt.show()


# In[51]:


hair = pd.read_csv('PredictHairFall.csv')
hair = hair.rename(columns={'Hair Loss': 'Hair_Loss'})
hair['Hair_Loss'] = hair['Hair_Loss'].astype(str)

hair['Hair_Loss'].replace('1', 'Yes', inplace=True)
hair['Hair_Loss'].replace('0', 'No', inplace=True)

NoHigh = hair.query( 'Hair_Loss == "No" and Stress == "High"').count()[0] #165
NoModerate = hair.query( 'Hair_Loss == "No" and Stress == "Moderate"').count()[0] #169
NoLow = hair.query( 'Hair_Loss == "No" and Stress == "Low"').count()[0] #168

plt.title('Distribution of stress levels when there is no hair loss')
labels = ['High','Moderate','Low']
colors = ['Red', 'Yellow','Green']
plt.pie([NoHigh,NoModerate,NoLow], labels = labels, autopct = '%.2f%%')
plt.show()


# In[ ]:




