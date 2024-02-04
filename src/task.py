import pandas as pd

# Compute the total revenue generated by the online store for each month in the dataset
# Extract the month from the order_date column
# Calculate the revenue for each order by multiplying the product_price and the quantity
# Group the data by month and sum the revenue
def calculate_monthly_revenue(data):
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['total_price'] = data['product_price'] * data['quantity']
    data['month'] = data['order_date'].dt.to_period('M')
    monthly_revenue = data.groupby('month')['total_price'].sum()
    return monthly_revenue

# Compute the total revenue generated by each product in the dataset
# Group the data by product_id and product_name and sum the revenue
def calculate_product_revenue(data):
    data['total_price'] = data['product_price'] * data['quantity']
    product_revenue = data.groupby('product_name')['total_price'].sum()
    return product_revenue

# Compute the total revenue generated by each customer in the dataset
# Group the data by customer_id and sum the revenue
def calculate_customer_revenue(data):
    data['total_price'] = data['product_price'] * data['quantity']
    customer_revenue = data.groupby('customer_id')['total_price'].sum()
    return customer_revenue

# Identify the top 10 customers by revenue generated
# Sort the customer revenue in descending order and take the first 10 rows
def identify_top_customers(data, top_n=10):
    data['total_price'] = data['product_price'] * data['quantity']
    top_customers = data.groupby('customer_id')['total_price'].sum().nlargest(top_n)
    return top_customers

# Reading the csv file orders.csv
data = pd.read_csv('orders.csv')


# Storing the data returned by all the functions
monthly_revenue = calculate_monthly_revenue(data)
product_revenue = calculate_product_revenue(data)
customer_revenue = calculate_customer_revenue(data)
top_customers = identify_top_customers(data)


print("Monthly Revenue")
print(monthly_revenue)
print("----------------------------------------------------")

print("Product Revenue")
print(product_revenue)
print("----------------------------------------------------")

print("Customer Revenue")
print(customer_revenue)
print("----------------------------------------------------")

print("Top 10 Customers")
print(top_customers)