Overview
The Bankruptcy Prediction System is a machine learning project designed to detect financial distress in businesses, potentially leading to bankruptcy. The project uses a dataset collected from the Taiwan Economic Journal, covering financial ratios of companies from 1999 to 2009. The aim is to apply machine learning techniques to predict company bankruptcy based on quarterly data.

Project Structure
1. Introduction
Overview of bankruptcy prediction
Problem statement
Project goals

2.Dataset Details
Source: Taiwan Economic Journal
Data period: 1999 to 2009
Dataset: bank.csv
Rows: 6819
Columns: 96

3. Data Preprocessing and EDA
Importing libraries and loading datasets
Constructing additional columns for locations
Handling inappropriate blank values
Checking data types, null values, and duplicates
Descriptive statistics

4. Data Visualization
Numerical data visualization
Outlier detection using boxplots
3D visualization using PCA

5. Model Selection and Building
Bagging for decision tree
Correlation analysis
Mutual information
ANOVA F test
Model accuracy and selection process

6. Deployment
Deployment using Streamlit
Integration into production environment

7. Challenges
Complexity in EDA
Variable selection and effective visualization
Accuracy challenges in model building
Trial and error with multiple models

8. References
Pandas Documentation
Matplotlib Documentation
Streamlit Documentation
Kaggle

Deployment
The project is deployed using Streamlit, allowing the machine learning model to be integrated into a live application for real-time predictions.


Conclusion
This project highlights the potential of machine learning in financial distress detection and provides a robust model for predicting company bankruptcy. The system's deployment using Streamlit ensures ease of use and accessibility for end-users.
