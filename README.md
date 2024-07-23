# Job Market Analysis Project

This project aims to analyze job market trends, focusing on the skills demanded and salary distributions. The analysis is performed using Python and various data science libraries.

## Project Overview

The main objectives of this project are:
1. To identify the most demanded skills in the job market.
2. To analyze the salary distribution based on different factors like experience, education level, and skills.
3. To perform statistical tests and build a linear regression model to predict salaries.

## Dataset

The dataset used in this project is simulated to mimic real-world job listing data. It includes the following columns:
- `salary`: The salary offered for the job.
- `experience`: The years of experience required.
- `education_level`: The required education level for the job.
- `skills`: The skills required for the job.

## Steps and Analysis

1. **Data Cleaning**: Handling missing values and ensuring data quality.
2. **Exploratory Data Analysis**: Understanding the data distribution and relationships.
3. **Statistical Analysis**: Performing normality and significance tests.
4. **Regression Modeling**: Building a linear regression model to predict salaries.

## Visualizations

The project includes several visualizations to illustrate the findings:
- **Salary Distribution**: Histogram showing the distribution of salaries.
- **Skills Distribution**: Countplot showing the frequency of different skills in job listings.
- **Correlation Matrix**: Heatmap showing the correlation between different variables.
- **Experience vs. Salary**: Scatter plot showing the relationship between experience and salary.
- **Salary by Education Level**: Boxplot showing salary distribution across different education levels.
- **Salary by Skills**: Boxplot showing salary distribution across different skills.
- **Average Salary by Skills and Education Level**: Heatmap showing the average salary for combinations of skills and education levels.

## Usage

To run the analysis, execute the `job_analysis_project.py` script. The script will generate the visualizations and perform the necessary statistical tests and modeling.

## Requirements

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scipy
- Scikit-learn

## How to Run

1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the `job_analysis_project.py` script.

## Results

The analysis provides insights into:
- The most demanded skills in the job market.
- The impact of education level and experience on salary.
- Statistical validation of salary distributions.
- A predictive model for estimating salaries based on experience and skills.

## Conclusion

This project demonstrates how data analysis and statistical modeling can provide valuable insights into job market trends, helping job seekers to better understand the market and make informed decisions.

