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

---

# Merge Exercises

## Merge Setup

```python
import pandas as pd

# Employees
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'dept_id': [101, 102, 101, 103, None]
})

# Departments
departments = pd.DataFrame({
    'dept_id': [101, 102, 104],
    'dept_name': ['Sales', 'Engineering', 'HR']
})

# Salaries
salaries = pd.DataFrame({
    'employee_id': [1, 2, 3, 6],
    'salary': [50000, 75000, 55000, 60000]
})

# Projects
projects = pd.DataFrame({
    'project_id': ['P1', 'P2', 'P3'],
    'project_name': ['Website', 'Mobile App', 'Database'],
    'lead_id': [1, 2, 4]
})

# Assignments (many-to-many relationship)
assignments = pd.DataFrame({
    'emp_id': [1, 1, 2, 3, 3, 3],
    'project_id': ['P1', 'P2', 'P2', 'P1', 'P2', 'P3']
})
```

---

## Exercise 11: Inner Join
Merge `employees` with `departments` to show only employees who have a matching department.

---

## Exercise 12: Left Join
Merge `employees` with `departments` keeping all employees, even those without a department.

---

## Exercise 13: Right Join
Merge `employees` with `departments` keeping all departments, even those with no employees.

---

## Exercise 14: Outer Join
Merge `employees` with `departments` keeping all records from both tables.

---

## Exercise 15: Different Column Names
Merge `employees` with `salaries` where the key columns have different names (`emp_id` vs `employee_id`).

---

## Exercise 16: Multiple Keys
Given this DataFrame, merge on multiple columns:
```python
sales_q1 = pd.DataFrame({
    'region': ['East', 'East', 'West'],
    'product': ['A', 'B', 'A'],
    'q1_sales': [100, 150, 200]
})

sales_q2 = pd.DataFrame({
    'region': ['East', 'West', 'West'],
    'product': ['A', 'A', 'B'],
    'q2_sales': [120, 180, 90]
})
# Merge on both region and product
```

---

## Exercise 17: Self Join
Find all pairs of employees who work in the same department (excluding pairing an employee with themselves).

---

## Exercise 18: Chained Merges
Create a report showing: employee name, department name, and salary. (Requires merging 3 DataFrames)

---

## Exercise 19: Many-to-Many
Using `employees`, `projects`, and `assignments`, create a DataFrame showing employee names with their project names.

---

## Exercise 20: Indicator Column
Merge `employees` with `salaries` using a left join and add an indicator column to see which employees have salary records.

---

## Bonus: concat vs merge
When would you use `pd.concat()` instead of `pd.merge()`? Try stacking these DataFrames:
```python
jan_data = pd.DataFrame({'day': [1, 2], 'sales': [100, 120]})
feb_data = pd.DataFrame({'day': [1, 2], 'sales': [90, 110]})
```
