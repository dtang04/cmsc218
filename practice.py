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

# Exercise 3
data["bonus"] = np.array(data["salary"]) * 0.10

# Exercise 4
df_salary = df.groupby(["department"])["salary"].mean()
print(df_salary)

# Exercise 5
df_sorted = df.sort_values(by = ["salary", "name"], ascending = [False, False])
print(df_sorted)