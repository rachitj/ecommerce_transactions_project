#!/usr/bin/env python
# coding: utf-8

# # Import libraries

# In[22]:


import pandas as pd
import seaborn as sns


# In[23]:


df_orders= pd.read_csv("orders.csv")
df_cust = pd.read_csv("customers.csv")
df_line_items = pd.read_csv("line_items.csv")
df_exch = pd.read_csv("exchange_rates.csv")


# ### Check for nulls

# In[24]:


print("Shape of df_orders: ", df_orders.shape)
print("Shape of df_cust: ", df_cust.shape)
print("Shape of df_line_items: ", df_line_items.shape)
print("Shape of df_exch: ", df_exch.shape)


# In[25]:


# Visualizing nulls using heatmap
sns.heatmap(df_orders.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[26]:


sns.heatmap(df_cust.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[27]:


sns.heatmap(df_line_items.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[28]:


sns.heatmap(df_exch.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# As no nulls are presen in our datasets, we need not do any null value treatment

# ## Exploring  Data Analysis
# 
# After checking for nulls, we would like to know what our datsets look like, what are the ranges, datatypes and unique values. WE will also try to determine if any feature engineering needs to be done.

# ### Exploring Customers Dataset

# In[29]:


def rstr(df, pred=None): 
    obs = df.shape[0]
    types = df.dtypes
    counts = df.apply(lambda x: x.count())
    uniques = df.apply(lambda x: [x.unique()])
    nulls = df.apply(lambda x: x.isnull().sum())
    distincts = df.apply(lambda x: x.unique().shape[0])
    missing_ration = (df.isnull().sum()/ obs) * 100
    skewness = df.skew()
    kurtosis = df.kurt() 
    print('Data shape:', df.shape)
    
    if pred is None:
        cols = ['types', 'counts', 'distincts', 'nulls', 'missing ration', 'uniques', 'skewness', 'kurtosis']
        str = pd.concat([types, counts, distincts, nulls, missing_ration, uniques, skewness, kurtosis], axis = 1)

    else:
        corr = df.corr()[pred]
        str = pd.concat([types, counts, distincts, nulls, missing_ration, uniques, skewness, kurtosis, corr], axis = 1, sort=False)
        corr_col = 'corr '  + pred
        cols = ['types', 'counts', 'distincts', 'nulls', 'missing_ration', 'uniques', 'skewness', 'kurtosis', corr_col ]
    
    str.columns = cols
    dtypes = str.types.value_counts()
    print('___________________________\nData types:\n',str.types.value_counts())
    print('___________________________')
    return str


# In[30]:


details_cust = rstr(df_cust)
display(details_cust)


# ### Exploring Line Items Dataset

# In[31]:


details_line_items = rstr(df_line_items)
display(details_line_items)


# In[32]:


df_line_items['product_name'].value_counts()


# In[33]:


df_line_items.head(10)


# ### Exploring Orders Dataset

# In[34]:


details_orders = rstr(df_orders)
display(details_orders)


# In[35]:


df_orders['orders_day'].value_counts()


# The most number of orders were made on Wednesday and Sunday in that order. The least orders were made on Friday, which is interesting.

# In[ ]:




