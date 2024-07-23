
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, ttest_ind
from sklearn.linear_model import LinearRegression

# Simulate a dataset
np.random.seed(0)
data_simulated = pd.DataFrame({
    'salary': np.random.normal(50000, 15000, 1000),
    'experience': np.random.normal(5, 2, 1000),
    'education_level': np.random.choice(['High School', 'Bachelors', 'Masters', 'PhD'], 1000),
    'skills': np.random.choice(['skill1', 'skill2', 'skill3'], 1000)
})

# Data cleaning
data_cleaned = data_simulated.dropna()

# Salary distribution - Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data_cleaned['salary'], kde=True)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.savefig('experience_vs_salary.jpeg', format='jpeg')
plt.close()

# Skills distribution - Countplot
plt.figure(figsize=(10, 6))
sns.countplot(y='skills', data=data_cleaned, order=data_cleaned['skills'].value_counts().index)
plt.title('Skills Distribution')
plt.xlabel('Number of Offers')
plt.ylabel('Skills')
plt.savefig('salary_by_education_level.jpeg', format='jpeg')
plt.close()

# Correlation matrix
plt.figure(figsize=(12, 8))
correlation_matrix = data_cleaned.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('salary_by_skills.jpeg', format='jpeg')
plt.close()

# Normality test
stat, p = shapiro(data_cleaned['salary'])
normality_test_result = 'The data follows a normal distribution' if p > 0.05 else 'The data does not follow a normal distribution'

# Significance test
group1 = data_cleaned[data_cleaned['skills'] == 'skill1']['salary']
group2 = data_cleaned[data_cleaned['skills'] == 'skill2']['salary']

stat, p = ttest_ind(group1, group2)
significance_test_result = 'There is a significant difference between the two groups' if p < 0.05 else 'There is no significant difference between the two groups'

# Linear Regression
X = data_cleaned[['experience']]
y = data_cleaned['salary']

# Encode categorical variables
X = pd.get_dummies(X, drop_first=True)

# Model fitting
model = LinearRegression()
model.fit(X, y)

# Display coefficients
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coefficients)
