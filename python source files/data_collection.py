#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[1]:


# Import Libraries
import requests
import pandas as pd
import json
from urllib.request import urlopen

pd.set_option("max_rows",100)


# ## Get Orders data from json file

# In[2]:


# Loading as python object
with open('orders.json') as f:
    data_orders = json.load(f)


# In[3]:


type(data_orders)


# In[4]:


data_orders[0]


# In[97]:


df_orders = pd.DataFrame(columns=['id','cust_id','total_price','created_at', 'line_item_id'])

for orders in data_orders:
    id = orders['id']
    cust_id = orders['customer']['id']
    total_price = orders['total_price']
    created_at = orders['created_at']
    for line_item in orders['line_items'] :
        line_item_id = line_item['id']
        #print(line_item_id,id,cust_id,total_price,created_at)
        orders = {'id':id,'cust_id':cust_id,'total_price':total_price,'created_at':created_at,'line_item_id':line_item_id}
        df_orders = df_orders.append(orders,ignore_index=True)
    #print(id,cust_id,total_price,created_at)


# In[98]:


df_orders.tail()


# ## Get Customers Data

# In[8]:


# Create Customers dataframe from orders
df_cust = pd.DataFrame(columns=['cust_id','cust_name','cust_email'])

for customer in data_orders:
    cust_id = customer['customer']['id']
    cust_name = customer['customer']['name']
    cust_email = customer['customer']['email']
    #print(cust_id,cust_name,cust_email)
    customers = {'cust_id':cust_id,'cust_name':cust_name,'cust_email':cust_email}
    df_cust = df_cust.append(customers,ignore_index=True)
    #print(id,cust_id,total_price,created_at)


# In[9]:


df_cust.head()


# ## Get Line Items Data

# In[10]:


# Create Line Items dataframe from orders
df_line_items = pd.DataFrame(columns=['line_item_id','product_id','product_sku','product_name','product_price'])

for orders in data_orders:
    for line_item in orders['line_items'] :
        line_item_id = line_item['id']
        product_id = line_item['product_id']
        product_sku = line_item['product_sku']
        product_name = line_item['product_name']
        product_price = line_item['price']
        #print(line_item_id,product_id,product_sku,product_name,product_price)
        line_items = {'line_item_id':line_item_id,'product_id':product_id,'product_sku':product_sku,'product_name':product_name,'product_price':product_price}
        df_line_items = df_line_items.append(line_items,ignore_index=True)
    #print(id,cust_id,total_price,created_at)


# In[11]:


df_line_items.tail()


# ## Get exchange rates 

# In[12]:


with urlopen("https://api.exchangeratesapi.io/history?start_at=2019-12-01&end_at=2020-04-01&symbols=CAD&base=USD") as response:
    source = response.read()
data_exc = json.loads(source)


# In[13]:


data_exc


# In[35]:


type(data_exc)


# In[36]:


df = pd.DataFrame.from_dict(data_exc)


# In[37]:


df.drop(columns= ['start_at','end_at'], inplace = True)


# In[38]:


df.head()


# In[39]:


df['rates'] =df['rates'].astype('str')
df['rates'] = df['rates'].apply(lambda x : x.split(":")[1])
df['rates'] = df['rates'].apply(lambda x :x.replace('}',''))
df.head()                                                


# In[40]:


type(df['rates'])


# In[58]:


df['date'] = df.index
#df.set_index('date', inplace= True)


# In[59]:


df.head()


# In[60]:


df.iloc[0]


# In[61]:


df.sort_index(ascending = True,inplace = True)


# In[62]:



df.head()


# In[63]:


df.info()


# In[64]:


# Converting date to date type
df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')


# In[65]:


df.info()


# In[70]:


df.reset_index(drop=True, inplace = True)
df.head()


# In[73]:


df['exchanged_to'] = "CAD"
df['day']= df['date'].apply( lambda x: x.day_name())


# In[74]:


df.head()


# In[75]:


df['day'].value_counts()


# Exchange Rates for Saturday and Sunday are not present as financial working days do not include weekends

# ## Join exchange rates to orders

# In[100]:


# Convert created_at to date
df_orders.tail()


# In[101]:


df_orders['created_at'] = df_orders['created_at'].apply(lambda x : x.replace('T'," ").replace('Z',""))


# In[102]:


df_orders.tail()


# In[103]:


df_orders.info()


# In[104]:


# Convert to datetime
df_orders['created_at'] = pd.to_datetime(df_orders['created_at'], format = '%Y-%m-%d %H')


# In[105]:


df_orders.info()


# In[106]:


df_orders['orders_day'] = df_orders['created_at'].apply( lambda x: x.day_name())
df_orders['orders_date'] = df_orders['created_at'].apply( lambda x: x.date())


# In[107]:


df_orders.tail()


# In[108]:


df_orders['orders_day'].value_counts()


# As Orders are placed on weekends also, but exchange rates do not change on weekends; so we will take that Friday's exchange rate for weekend orders

# ## Save the csv files

# In[112]:


df_orders.to_csv("orders.csv", index = False)
df_cust.to_csv("customers.csv",index = False)
df_line_items.to_csv("line_items.csv",index = False)
df.to_csv("exchange_rates.csv",index = False)


# In[ ]:




