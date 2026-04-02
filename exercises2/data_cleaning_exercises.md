# Data Cleaning Exercises

## Setup

```python
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
    'transaction_id': [101, 102, 103, 104, 105, 106],
    'employee_id': [1, 2, 1, 3, 999, 2],
    'amount': [500.0, None, 750.0, -100.0, 300.0, 'pending'],
    'region': ['East', 'east', 'EAST', 'West', 'North', '  West  ']
})

# Messy department budget data
budgets = pd.DataFrame({
    'dept_name': ['Sales', 'Engineering', 'Marketing', 'Sales', 'HR'],
    'budget': [200000, 500000, 150000, 180000, 100000],
    'year': [2024, 2024, 2024, 2023, 2024]
})
```

---

## Exercise 1: Handling Missing Values
Identify all missing values in the `employees` DataFrame. Then fill missing names with "Unknown" and drop rows where `hire_date` is missing.

---

## Exercise 2: Standardizing Text Case
The `department` column has inconsistent casing ('Sales', 'sales', 'SALES'). Standardize all department names to title case.

---

## Exercise 3: Trimming Whitespace
Some names have leading/trailing whitespace ('  Charlie', 'Diana '). Clean the `name` column by stripping whitespace.

---

## Exercise 4: Fixing Data Types
The `salary` column is stored as strings with issues ('50000', 'N/A', '55k'). Convert it to numeric values, handling:
- 'N/A' should become NaN
- '55k' should become 55000

---

## Exercise 5: Standardizing Date Formats
The `hire_date` column has inconsistent formats. Convert all dates to datetime objects.

---

## Exercise 6: Handling Abbreviations
The department column has abbreviations ('Mktg' for 'Marketing'). Create a mapping to standardize department names.

---

## Exercise 7: Filtering Invalid Data
In the `sales` DataFrame, remove rows with negative amounts, non-numeric amounts ('pending'), and transactions from employees that don't exist in your employee records.

---

## Exercise 8: Regional Sales Report
After cleaning the `sales` data, your manager wants to know the total revenue generated in each region. Prepare this report.

---

## Exercise 9: Department Budget Analysis
Create a report showing each employee alongside their department's 2024 budget. Note that the budget data contains entries from multiple years.

---

## Exercise 10: Full Pipeline
The CEO wants a report showing total sales revenue by department. You have employee data, sales transactions, and department info spread across multiple tables with various data quality issues. Prepare this report.
