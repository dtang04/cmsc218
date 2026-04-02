# Pandas DataFrame Exercises

## Setup

```python
import pandas as pd
import numpy as np

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'age': [25, 30, 35, 28, 22, 40],
    'department': ['Sales', 'Engineering', 'Sales', 'Engineering', 'Marketing', 'Sales'],
    'salary': [50000, 75000, 55000, 80000, 45000, 60000],
    'hire_date': ['2020-01-15', '2019-03-22', '2021-07-01', '2018-11-30', '2022-02-14', '2017-06-10']
}
df = pd.DataFrame(data)
```

---

## Exercise 1: Basic Selection
Select only the `name` and `salary` columns for employees older than 25.

---

## Exercise 2: Filtering
Find all employees in the Engineering department with a salary greater than 70000.

---

## Exercise 3: Adding Columns
Add a new column `bonus` that is 10% of each employee's salary.

---

## Exercise 4: Groupby Aggregation
Calculate the average salary for each department.

---

## Exercise 5: Sorting
Sort the DataFrame by salary in descending order, then by name alphabetically.

---

## Exercise 6: Value Counts
Count how many employees are in each department.

---

## Exercise 7: Apply Function
Create a column `seniority` that labels employees as "Senior" if hired before 2020, otherwise "Junior".

---

## Exercise 8: Multiple Aggregations
For each department, find the min, max, and mean salary.

---

## Exercise 9: Conditional Update
Give a 5000 raise to all employees in the Sales department.

---

## Exercise 10: Merging DataFrames
Create a second DataFrame with department budgets and merge it with the original.

```python
budgets = pd.DataFrame({
    'department': ['Sales', 'Engineering', 'Marketing'],
    'budget': [200000, 500000, 150000]
})
# Merge df with budgets
```
