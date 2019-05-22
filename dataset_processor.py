#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(filepath_or_buffer='~/Desktop/boston/housing.csv',sep='\s+',header=None)
#print(df.to_string())


# In[43]:


#computation of summary
print(df.describe())
#advance to label the columns
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']

#Optional loop over all columns plotting multiple charts
for column in df.columns:
    plt.figure()
    plt.plot(df[column],color='red')
    plt.xlabel('District')
    plt.show()
             


# In[19]:


#Basic Visualize the data, 1-feature (column) at a time
plt.plot(df['CRIM'],color='red' )
plt.title('Criminal rate vs. District')
plt.xlabel('District')
plt.ylabel('Criminal rate')
plt.savefig('Criminal rate.png',format='png')
#plt.clf()
#plt.scatter(df[0],df[1]


# In[22]:


#plot scatter Visualize the data, 2-features (columns) at a time
plt.scatter(df['TAX'],df['LSTAT'], color = 'b')
plt.title('Property tax vs % lower status of the population')
plt.xlabel('PTRATIO')
plt.ylabel('TAX')
plt.savefig('TAX vs status.png', format='png')


# In[27]:


# Reach sample bar chart for tax vs pupil-teacher ratio by town
plt.bar(df['TAX'],df['PTRATIO'], color='blue')
plt.title('TAX vs pupil-teacher ratio by town')
plt.xlabel('TAX')
plt.ylabel('PTRATIO')
plt.savefig('Bar graph.png', format='png')


# In[ ]:




