# ecommerce_transactions_project

## Data
The dump is a JSON array that contains orders, following this structure:

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
