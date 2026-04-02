import pandas as pd
import numpy as np

# Sample data to work with
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'age': [25, 30, 35, 28, 22, 40],
    'department': ['Sales', 'Engineering', 'Sales', 'Engineering', 'Marketing', 'Sales'],
    'salary': [50000, 75000, 55000, 80000, 45000, 60000],
    'hire_date': ['2020-01-15', '2019-03-22', '2021-07-01', '2018-11-30', '2022-02-14', '2017-06-10']
}
df = pd.DataFrame(data)

# Exercise 1
print(df[df["age"] > 25][["name", "salary"]])
print("--------------")

# Exercise 2
df_ind = df[df["department"] == "Engineering"]
df_ind = df_ind[df_ind["salary"] > 70000]["name"]
print(df_ind)
print("")

# Exercise 3
data["bonus"] = np.array(data["salary"]) * 0.10

# Exercise 4
df_salary = df.groupby(["department"])["salary"].mean()
print(df_salary)
print("")

# Exercise 5
df_sorted = df.sort_values(by = ["salary", "name"], ascending = [False, False])
print(df_sorted)
print("")

# Exercise 6
print(df.count()["name"])

# Exercise 7

df["hire_date"] = pd.to_datetime(df["hire_date"])

def classify_senior(i):
    if i.year < 2020:
        return "Senior"
    else:
        return "Junior"

df["seniority"] = df["hire_date"].apply(classify_senior)

print(df["seniority"])

# Exercise 8

df_stats = df.groupby(["department"])["salary"].agg(["min", "max", "mean"])
print(df_stats)

# Exercise 9

df_with_raise = df.copy()
df_with_raise["salary"] = df_with_raise["salary"] + 5000

# Exercise 10

budgets = pd.DataFrame({
    'department': ['Sales', 'Engineering', 'Marketing'],
    'budget': [200000, 500000, 150000]
})

df_merged = pd.merge(df, budgets, on = "department")
print(df_merged)