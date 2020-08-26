#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pyodbc


# ## Get the data in dataframes

# In[2]:


df_orders= pd.read_csv("orders.csv")
df_cust = pd.read_csv("customers.csv")
df_line_items = pd.read_csv("line_items.csv")
df_exch = pd.read_csv("exchange_rates.csv")


# In[3]:


# Loop through all the drivers we have available in pyodbc
for drivers in pyodbc.drivers():
    print(drivers)


# ## Define SQL Connection String

# In[4]:


# Define server and database 
server = 'DESKTOP-VILFN01\MSSQLSERVER01'
database = 'E-Commerce'

# define connection string
sql_con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};                        SERVER='+ server +';                        DATABASE='+ database +';                       Trusted_Connection=yes;')


# ## Load Orders Data in SQL

# In[5]:


df_orders.rename(columns={'id' : 'order_id'}, inplace=True)
df_orders.head()


# In[6]:


df_orders.columns


# In[7]:


df_orders.drop_duplicates (subset=None, keep= 'first', inplace=True)


# In[8]:


df_orders.shape


# In[9]:


df_orders.to_csv("orders.csv")


# In[157]:


# Create orders table
cursor = sql_con.cursor()
sql_con.execute('CREATE TABLE orders (order_id varchar(30) not null, cust_id int, total_price float, created_at datetime, line_item_id int,orders_day varchar(10), orders_date date)')
sql_con.commit()
cursor.close()


# In[158]:


# Insert data into orders table in sql
cursor = sql_con.cursor()

# loop through to insert each row.
for order_id,cust_id,total_price,created_at, line_item_id,orders_day,orders_date in zip(df_orders['order_id'],df_orders['cust_id'],df_orders['total_price'],df_orders['created_at'],df_orders['line_item_id'],df_orders['orders_day'],df_orders['orders_date']):
    
    # define an insert query with place holders for the values.
    insert_query = '''INSERT INTO orders 
                      VALUES (?, ?, ?, ?, ?, ?,?);'''
    
    # define the values
    values = (order_id,cust_id,total_price,created_at, line_item_id,orders_day, orders_date)
    #print(insert_query, values)
    
    # insert the data into the database
    cursor.execute(insert_query, values)

# Close the cursor
cursor.close()


# In[159]:


# grab all the rows from the table
cursor = sql_con.cursor()
cursor.execute('SELECT Count(1) FROM orders')
for row in cursor:
    print(row)

# Records in orders dataframe
print(df_orders.shape)
# close the cursor and connection  
cursor.close()


# ## Load Customers Data in SQL

# In[161]:


df_cust.head()


# In[162]:


df_cust['cust_id'].value_counts()


# In[163]:


df_cust.shape


# In[164]:


df_cust.drop_duplicates (subset=None, keep= 'first', inplace=True)


# In[165]:


df_cust.shape


# In[166]:


df_cust['cust_id'].value_counts()


# In[167]:


df_cust['cust_email'].unique()


# In[192]:


df_cust.to_csv("customers.csv")


# In[204]:


# Create Customers table in SQL
cursor = sql_con.cursor()
sql_con.execute('CREATE TABLE customers (cust_id int primary key, cust_name varchar(100), cust_email varchar(255))')
sql_con.commit()
cursor.close()


# In[169]:


# Insert data into customers table in sql
cursor = sql_con.cursor()

# loop through to insert each row.
for cust_id,cust_name,cust_email in zip(df_cust['cust_id'],df_cust['cust_name'],df_cust['cust_email']):
    
    # define an insert query with place holders for the values.
    insert_query = '''INSERT INTO customers 
                      VALUES (?, ?, ?);'''
    
    # define the values
    values = (cust_id,cust_name,cust_email)
    #print(insert_query, values)
    
    # insert the data into the database
    cursor.execute(insert_query, values)

# Close the cursor
cursor.close()


# In[170]:


# grab all the rows from the table
cursor = sql_con.cursor()
cursor.execute('SELECT Count(1) FROM customers')
for row in cursor:
    print(row)

# Records in orders dataframe
print(df_cust.shape)
# close the cursor and connection  
cursor.close()


# ## Load Line Items Data in SQL

# In[171]:


df_line_items.shape


# In[172]:


df_line_items


# In[173]:


df_line_items.drop_duplicates (subset=None, keep= 'first', inplace=True)


# In[174]:


df_line_items.shape


# In[194]:


df_line_items.to_csv("line_items.csv")


# In[195]:


df_line_items


# In[229]:


# Create Line Items table in SQL
cursor = sql_con.cursor()
sql_con.execute('CREATE TABLE line_items (line_item_id int primary key, product_id int not null, product_sku varchar(255), product_name varchar(255), product_price float )')
sql_con.commit()
cursor.close()


# In[177]:


# Insert data into line_items table in sql
cursor = sql_con.cursor()

# loop through to insert each row.
for line_item_id, product_id, product_sku, product_name, product_price in zip(df_line_items['line_item_id'],df_line_items['product_id'],df_line_items['product_sku'],df_line_items['product_name'],df_line_items['product_price']):
    
    # define an insert query with place holders for the values.
    insert_query = '''INSERT INTO line_items 
                      VALUES (?, ?, ?,?,?);'''
    
    # define the values
    values = (line_item_id, product_id, product_sku, product_name, product_price)
    #print(insert_query, values)
    
    # insert the data into the database
    cursor.execute(insert_query, values)

# Close the cursor
cursor.close()


# In[178]:


# grab all the rows from the table
cursor = sql_con.cursor()
cursor.execute('SELECT Count(1) FROM line_items')
for row in cursor:
    print(row)

# Records in orders dataframe
print(df_line_items.shape)
# close the cursor and connection  
cursor.close()


# ## Load Exchange ratesData in SQL

# In[253]:


df_exch.shape


# In[254]:


df_exch.head()


# In[255]:


df_exch.drop_duplicates (subset=None, keep= 'first', inplace=True)


# In[256]:


df_exch.shape


# In[257]:


df_exch.rename(columns={'date' : 'exchange_date'}, inplace=True)


# In[258]:


df_exch.columns


# In[244]:


# Create Exchange Rate table  in SQL
cursor = sql_con.cursor()
sql_con.execute('CREATE TABLE exchange_rates (exch_id int IDENTITY(1,1) PRIMARY KEY, rates float, base varchar(10), exchange_date date unique not null, exchanged_to varchar(10), day varchar(15) not null)')
sql_con.commit()
cursor.close()


# In[259]:


# Insert data into exchange rates table in sql
cursor = sql_con.cursor()

# loop through to insert each row.
for rates, base, exchange_date,exchanged_to,day in zip(df_exch['rates'],df_exch['base'],df_exch['exchange_date'],df_exch['exchanged_to'],df_exch['day']):
    
    # define an insert query with place holders for the values.
    insert_query = '''INSERT INTO exchange_rates 
                      VALUES (?,?,?,?,?);'''
    
    # define the values
    values = (rates, base, exchange_date,exchanged_to,day)
    #print(insert_query, values)
    
    # insert the data into the database
    cursor.execute(insert_query, values)

# Close the cursor
cursor.close();


# In[263]:


# grab all the rows from the table
cursor = sql_con.cursor()
cursor.execute('SELECT Count(1) FROM exchange_rates')
for row in cursor:
    print(row)

# Records in orders dataframe
print(df_exch.shape)
# close the cursor and connection  
cursor.close()


# In[260]:


#Close the connection
sql_con.close()


# In[ ]:




