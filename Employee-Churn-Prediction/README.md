# Employee-Churn-Prediction: A Capstone Project

## Overview
This repository contains the capstone project which is focused on building predictive models to assess employee churn. Employee churn, or turnover, is a measure of the number of individuals moving out of a collective over a specific period. It is a critical metric in HR analytics, providing insights into overall employee satisfaction and the organization’s ability to retain talent.

## Objective
The primary goal of this project is to develop machine learning models to predict the likelihood of an employee leaving the company, enabling the organization to implement proactive measures to enhance employee retention and manage organizational health.

## Dataset
The dataset used for this project includes various features related to employee characteristics, their job roles, and their job satisfaction levels. The features include but are not limited to:

- Employee satisfaction level
- Last evaluation
- Number of projects
- Average monthly hours
- Tenure at the company
- Salary level
- Department

## Methodology
1. **Data Preparation**: Involved cleaning the dataset and encoding categorical variables using one-hot encoding.
2. **Exploratory Data Analysis (EDA)**: Comprehensive exploration to understand the relationships and patterns in the data.
3. **Modeling**: Implementation of Logistic Regression, Random Forest, and XGBoost classifiers to predict employee churn.
4. **Model Evaluation**: Used various metrics like precision, recall, F1-score, and AUC-ROC to assess model performance.
5. **Hyperparameter Tuning**: Applied GridSearchCV to fine-tune the Random Forest model.
6. **Feature Importance Analysis**: Identified and visualized the most influential features contributing to employee churn.
7. **Cross-Validation**: Employed k-fold cross-validation to assess model performance more reliably.

## Results
- Developed robust models achieving accuracy levels up to approximately 98%.
- Identified key features such as satisfaction level, tenure, and the number of projects as significant predictors of employee churn.
- Presented actionable insights and visualizations to assist in organizational decision-making processes.

## Technologies Used
- Python
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn
- XGBoost

## Conclusion & Recommendations
This project offers insights into the key drivers of employee churn and provides robust models to predict employee turnover. It is recommended that organizations use these insights to design employee engagement and retention strategies, focusing on the identified key areas, to foster a conducive work environment and minimize employee attrition.

## Next Steps
- Implementation of more advanced models and techniques like neural networks and ensemble learning to improve model performance.
- Exploration of different feature engineering and selection methods to enhance model interpretability and accuracy.
- Deployment of the developed model into a production environment to enable real-time prediction and monitoring of employee churn.

## Note
This is a capstone project aimed at showcasing analytical, statistical, and machine learning skills and is intended for educational and professional portfolio purposes. 
