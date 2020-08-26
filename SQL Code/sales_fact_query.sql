/****** Script for sales_fact  ******/

-- CREATE A SALES FACT BASED ON ORDER ID

CREATE Table fact_sales
(
	order_id varchar(30) not null
	,created_at	datetime not null
	,orders_date date not null
	, order_day varchar(10) not null
	,cust_id  int not null
	,cust_name varchar(100) 
	,cust_email varchar(255) not null
	,line_item_id int not null
	,product_id int not null
	,product_sku varchar(255) not null
	,product_name  varchar(255) not null
	,exchange_date  date not null
	,exchange_rate  float not null
	,exchange_base_currency varchar(10) not null
	,exchanged_to_currency varchar(10) not null
	,product_price float not null
	,order_total_price float not null
)

-- INSERT DATA 
INSERT INTO fact_sales
Select distinct
	ord.order_id as order_id
	, ord.created_at as order_created_at
	, ord.orders_date as order_date
	, ord.orders_day as order_day
	, ord.cust_id as cust_id
	, cust.cust_name as cust_name
	,cust.cust_email as cust_email
	,ord.line_item_id as line_item_id
	,line.product_id as product_id
	,line.product_sku as product_sku
	, line.product_name as product_name
	,(Select Top 1 ex.exchange_date 
        From exchange_rates ex 
        Where ord.orders_date > ex.exchange_date 
        Order by ex.exchange_date desc 
    )  exchange_date
	,(Select Top 1 ex.rates 
        From exchange_rates ex 
        Where ord.orders_date > ex.exchange_date 
        Order by ex.exchange_date desc 
    )  exchange_rate
	,'USD' as exchange_base_currency
	,'CAD' as exchanged_to_currency
	, line.product_price as product_price
	, ord.total_price as order_total_price


from orders ord
Left Join customers cust
	on ord.cust_id =  cust.cust_id
Left Join line_items line
	on ord.line_item_id = line.line_item_id