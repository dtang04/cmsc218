import pandas as pd
import numpy as np

city_norm = {"nyc": "NYC", "la": "LA", "chicago": "Chicago"}

customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice', 'Bob', 'charlie', 'Diana', '  Eve  ', 'Frank'],
    'city': ['NYC', 'LA', 'nyc', 'Chicago', 'LA', 'Chicago'],
    'membership': ['Gold', 'Silver', 'gold', 'Bronze', 'Gold', None]
})

products = pd.DataFrame({
    'product_id': ['A', 'B', 'C', 'D', 'E'],
    'product_name': ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories'],
    'price': [1200, 800, 400, 150, 25]
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'customer_id': [1, 2, 1, 3, 4, 2, 5, 3, 1, 6],
    'product_id': ['A', 'B', 'C', 'A', 'D', 'E', 'B', 'B', 'E', 'C'],
    'quantity': [1, 2, 1, 1, 3, 5, 1, 2, 2, 1],
    'date': ['2024-01-15', '2024-01-16', '2024-01-16', '2024-02-01', '2024-02-10', 
             '2024-02-15', '2024-03-01', '2024-03-05', '2024-03-10', '2024-03-15']
})

stores = pd.DataFrame({
    'city': ['NYC', 'LA', 'Chicago', 'Houston'],
    'store_name': ['Manhattan Hub', 'Hollywood Store', 'Loop Center', 'Space City Shop'],
    'employee_count': [25, 30, 20, 15]
})

# Exercise 1
customers["name"] = customers["name"].apply(str.strip)

def norm_city(s):
    if s in city_norm:
        return city_norm[s]
    return s

def fill_membership(s):
    if not(s):
        return "Basic"
    return s

customers["city"] = customers["city"].apply(norm_city)
customers["membership"] = customers["membership"].apply(fill_membership)
customers["membership"] = customers["membership"].apply(str.capitalize)

# Exercise 2
print(customers)

df_orders = orders.groupby(["customer_id"])["quantity"].sum()

print(df_orders)

# Exercise 3

df_products = orders.groupby(["product_id"]).agg(quantity = ("quantity", "sum"),  num_orders = ("product_id", "count"))

# Exercise 4
df_combined = pd.merge(orders, products, on = "product_id")
df_combined["total_price"] = df_combined["quantity"] * df_combined["price"]
print(df_combined)


# Exercise 5
df_tot_rev = df_combined.groupby(["category"])["total_price"].sum()
print(df_tot_rev)

# Exercise 6
df_all_merged = pd.merge(orders, customers, on = "customer_id", how = "right")
print(df_all_merged)

complete_orderbook = pd.merge(df_all_merged, products, on = "product_id", how = "left")
print(complete_orderbook)

# Exercise 7
spending_by_customer = complete_orderbook.groupby(["customer_id"])["price"].sum()
print(spending_by_customer)

# Exercise 8
print(customers)
print(stores)
df_customers_stores = pd.merge(customers, stores, on = "city", how = "right")
print(df_customers_stores)

# Exercise 9
unique_orders = complete_orderbook.groupby(["name"])["order_id"].nunique()
unique_orders = pd.DataFrame({"Orders" : unique_orders})
print(complete_orderbook)
customer_info = complete_orderbook.groupby(["name", "city"]).agg(orders = ("order_id", "nunique"), quantity = ("quantity", "sum"), amount_spent = ("price", "sum"))
print(customer_info)


# Exercise 10
complete_orderbook_by_mon = complete_orderbook.copy()
complete_orderbook_by_mon["date"] = pd.to_datetime(complete_orderbook_by_mon["date"])
complete_orderbook_by_mon["month"] = complete_orderbook_by_mon["date"].dt.month
rev_by_mon = complete_orderbook_by_mon.groupby(["month"]).agg(price = ("price", "sum")).sort_values(ascending = False, by = "price")
print("\nMax month revenue: ", int(rev_by_mon.head(1).reset_index()["month"]))
rev_by_mon_prod = complete_orderbook_by_mon.groupby(["month", "product_name"]).agg(price = ("price", "sum")).sort_values(ascending = False, by = "price")
rev_by_mon_prod = rev_by_mon_prod.loc[pd.DataFrame(rev_by_mon.head(1)).reset_index()["month"]]
print("\nMax revenue product in highest earning month: ", rev_by_mon_prod[rev_by_mon_prod["price"] == rev_by_mon_prod["price"].max()].reset_index()["product_name"].iloc[0])

# Exercise 11

complete_orderbook["rev"] = complete_orderbook["quantity"] * complete_orderbook["price"]
product_highest_purchase = complete_orderbook.groupby(["category"])["rev"].max().reset_index()
cname_product_highest = pd.merge(complete_orderbook, product_highest_purchase, on = ["category", "rev"])[["name", "category", "rev"]]
print(cname_product_highest)

