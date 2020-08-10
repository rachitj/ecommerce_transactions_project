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
  * Price
To keep it simple, we removed taxes, discounts. Note also that all prices are in USD (US Dollars).

### Exchange Rates Data 
We would like you to consolidate your orders along with an exchange rate for the date of the order creations. This way, orders prices can be unified in Canadian Dollars (CAD), the currency that the Finance department of Namaste uses to report on.
For this purpose, we use the free currency exchange rate API provided by: https://exchangeratesapi.io/

## Steps:
