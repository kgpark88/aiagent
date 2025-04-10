import pandas as pd
import numpy as np

# Sample employee data
data = {
    "Name": ["박민수", "이주원", "강지은", "최영호", "김영빈"],
    "Age": [25, 30, 35, 28, 22],
    "City": ["판교", "광교", "수지", "서초", "강남"],
    "Salary": [8300, 7500, 7000, 8000, 8500],
    "Department": ["관리팀", "개발팀", "마케팅팀", "영업팀", "재무팀"],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file

# Read the CSV file back into a DataFrame

# Perform operations on the DataFrame
# Calculate average age

# Filter employees with salary greater than 8000
high_earners = df[df["Salary"] > 8000]

# Group by department and calculate average salary

# Sort DataFrame by age in descending order

# Add a new column for bonus (10% of salary)

# Display some information about the DataFrame
print(df.head())
print("\nDataFrame Info:")
print(df.info())

# Common DataFrame operations for practice:

# Accessing a non-existent column (for error handling practice)
average_experience = df["Experience"].mean()
