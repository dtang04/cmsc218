import pandas as pd
import numpy as np

# Messy employee data
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5, 6, 7],
    'name': ['Alice', 'bob', '  Charlie', 'Diana ', 'EVE', None, 'Frank'],
    'department': ['Sales', 'sales', 'SALES', 'Engineering', 'engineering', 'Marketing', 'Mktg'],
    'salary': ['50000', '75000', 'N/A', '80000', '45000', '60000', '55k'],
    'hire_date': ['2020-01-15', '2019/03/22', 'March 1, 2021', '2018-11-30', None, '2022-02-14', '06-10-2017']
})

# Messy sales data
sales = pd.DataFrame({
    'transaction_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'employee_id': [1, 2, 1, 3, 999, 2, 1, 3],
    'amount': [500.0, None, 750.0, -100.0, 300.0, 'pending', 500, 102.5],
    'region': ['East', 'east', 'EAST', 'West', 'North', '  West  ', 'North', 'North']
})

# Messy department budget data
budgets = pd.DataFrame({
    'dept_name': ['Sales', 'Engineering', 'Marketing', 'Sales', 'HR'],
    'budget': [200000, 500000, 150000, 180000, 100000],
    'year': [2024, 2024, 2024, 2023, 2024]
})

ABBREVS = {"Mktg": "Marketing"}

print(sales)

# Exercise 1
employees["name"] = employees["name"].fillna("Unknown")
employees = employees.dropna(subset=["hire_date"])


# Exercise 2
employees["department"] = employees["department"].apply(str.capitalize)

# Exercise 3
employees["name"] = employees["name"].apply(str.strip)

# Exercise 4
def convertToNumeric(s):
    if type(s) == str:
        pos_k = s.find("k")
        if pos_k != -1:
            base = int(s[:pos_k])
            return base * 1000
    return s

def convertNA(s):
    if s == "N/A":
        return float("nan")
    return s

employees["salary"] = employees["salary"].apply(convertToNumeric)
employees["salary"] = employees["salary"].apply(convertNA)

# Exercise 5
employees["hire_date"] = pd.to_datetime(employees["hire_date"], format = "mixed")

# Exercise 6
def convertAbbrevs(s):
    if s in ABBREVS:
        return ABBREVS[s]
    return s

employees["department"] = employees["department"].apply(convertAbbrevs)

# Exercise 7
sales = sales[sales["amount"] != "pending"] # pandas & does not short-circuit, must filter the pending separately
sales = sales[(sales["amount"] > 0) & (sales["employee_id"].isin(employees["emp_id"]))] #First conditional implicitly factors out None amounts

# Exercise 8
sales["region"] = sales["region"].apply(str.capitalize)
tot_rev = sales.groupby(["region"])["amount"].sum()
print(tot_rev)

# Exercise 9
budgets = budgets[budgets["year"] == 2024]
merged_df = pd.merge(employees, budgets, left_on = "department", right_on = "dept_name")[["name", "budget"]]
print(merged_df)

# Exercise 10
merged_df = pd.merge(employees, sales, left_on = "emp_id", right_on = "employee_id")
print(merged_df.groupby(["department"])["amount"].sum())