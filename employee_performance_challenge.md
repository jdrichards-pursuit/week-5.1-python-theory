# Employee Performance Analysis with Pandas

<img src="assets/panda.svg" alt="Pandas Logo" width="300">
## Objective:

Analyze the employee performance dataset using Pandas to perform data loading, exploration, selection, and operations.

## Code

Place your code for this challenge in the `employee_performance_analysis.py` file.

## Dataset:

The employee performance dataset is stored in a CSV file named `employee_performance.csv` in the `data` directory.

## Steps:

### 1. Load the Data:

Write a function `load_employee_data()` to load the dataset into a Pandas DataFrame.

### 2. Explore the DataFrame:

Write a function `explore_employee_dataframe(df)` to:

- Display the first 10 rows.
- Show the DataFrame info.
- Provide summary statistics.

### 3. Select and Filter Data:

Write a function `select_and_filter_employee_data(df)` to:

- Select the `name` and `department` columns.
- Filter employees with a `performance_score` greater than 80.
- Use `loc` to select specific rows and columns.

### 4. Perform Data Operations:

Write a function `employee_data_operations(df)` to:

- Add a new column `salary_per_year` calculated as `salary / years_at_company`.
- Sort the DataFrame by `performance_score` in descending order.

### 5. Advanced Tasks:

Write a function `advanced_employee_analysis(df)` to:

- Find the department with the highest average `performance_score`.
- Identify the top 3 employees with the highest `salary_per_year` and display their `name`, `department`, and `salary_per_year`.
