#importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Specify the path to your data file
file_path = "D:/Fundamental of data science project (coding)/data1-11.csv"

# Read data from the specified file path
data = pd.read_csv(file_path)

# Assuming 'salary' is the column you want to analyze
salary_data = data['salary']

# Create a histogram to represent the probability density function
hist, bins = np.histogram(salary_data, bins=30, density=True)
bin_centers = (bins[:-1] + bins[1:]) / 2

# Calculate mean annual salary (W˜)
mean_salary = np.mean(salary_data)

# Calculate X (replace this with the specific calculation for your case)
# Example: X represents the 80th percentile of the salary distribution
X = np.percentile(salary_data, 80)

# Plot histogram
plt.hist(salary_data, bins=30, density=True, alpha=0.5, color='gray', label='Probability Density Function')

# Plot mean annual salary (W˜) as a vertical line
plt.axvline(mean_salary, color='r', linestyle='dashed', linewidth=2, label=f'Mean Salary (W˜): {mean_salary:.2f}')

# Plot X as a vertical line
plt.axvline(X, color='g', linestyle='dashed', linewidth=2, label=f'X: {X:.2f}')

# Add labels, title, and legend
plt.xlabel('Salary')
plt.ylabel('Probability Density')
plt.title('Probability Density Function of Salary Distribution')
plt.legend()

# Display the graph
plt.show()

