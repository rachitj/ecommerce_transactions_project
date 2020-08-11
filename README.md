# ecommerce_transactions_project

## Description
"Company X" sells cannabis online via their e-commerce Shopify platform. To fulfill their reporting requirements, the Company X Finance department asks you to create a report so they can process their Q1 financial results. This exercise is a simplified view, focused on the Shopify orders in Q1.

## Goal: 
* To provide a dashboard to the Finance department about the sales results for Q1.
* Analyze the data and present any inisghts
* Automate the code

## Data
### Orders data : The dump is a JSON array that contains orders, following this structure:

* Order ID
* Customer
* ID
* Name
* Email
* Total Order price
* Creation date
* Line items. For each one:
  * ID
  * Product ID
  * Product SKU
  * Product Name
  * Pricez
To keep it simple, we removed taxes, discounts. Note also that all prices are in USD (US Dollars).

### Exchange Rates Data 
We would like you to consolidate your orders along with an exchange rate for the date of the order creations. This way, orders prices can be unified in Canadian Dollars (CAD), the currency that the Finance department of Namaste uses to report on.
For this purpose, we use the free currency exchange rate API provided by: https://exchangeratesapi.io/

## Steps:

### Step 1 : Get the relevant orders data from order.json file in data_collection.ipynb file
* In this step, we have extracted the orders data from order.json file.
* The orders data is in a nested dictioanry format.
* Extract the orders data in 3 different dataframes namely :
  * df_orders : Summary of orders
  * df_customers : information about customers
  * df_line_items : Line item details
* The main idea is to think data in terms of data modelling. Once we get the dimensions and facts, based on the requirements and context, we can determeine if we should 
  * Create a star schema
  * Create a snowflake schema
  * Create a fact that shows data in tabular format and that can be used as a table in Tableau dashboards

### Step 2 : Get the relevant exchange rates data from api in data_collection.ipynb file
* Extract the exchange rates data in df_line_items 
* We have assumed all transactions time zone is EDT
* Performed data cleaning

### Step 2 : Export the data to SQL tables in data_models.ipynb file
* In this step, we have cleaned data for any duplicates.
* Created a SQL Server connection. Note : Please change the connnection string values as per your system
* Created SQL tables and inserted the pandas dataframes data into these SQL tables:
  * orders
  * customers
  * line_items
  * exchange_rates
 
 ### Step 3 : Creation of fact_sales in SQL Server 2019
* As the data is not large enough, we are creating a 'sales_fact' that will store the data in tabular format, which can then be accessed through any BI tool. 
* sales_fact SQL query and CSV data is provided here
* Note : The main challenge was to map the exchange rates to order-dates as for some days, exchange rates are not provided due to holidays or weekends. So a correct mapping needs to be done
* Checked for duplicates and data quality

### Step 3 : Create interactive tableau dashboards
* [Q1 Analysis Tableau Link](https://public.tableau.com/profile/rachitjauhari#!/vizhome/e-commerce_analysis/Q1Dashboard?publish=yes)
* [Monthly Analysis Tableau Link](https://public.tableau.com/profile/rachitjauhari#!/vizhome/e-commerce_analysisMonthly/MonthlyDashboard?publish=yes)

![Q1 Analysis](https://github.com/rachitj/ecommerce_transactions_project/blob/master/q1_analysis.png)

## Resources
* https://github.com/namasteTechnologies/data-analyst-challenge

