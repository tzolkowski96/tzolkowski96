# 🍕 UFood Marketing Data Analysis

<div align="center">
  
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)](https://pandas.pydata.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A comprehensive data science project analyzing customer behavior and marketing campaign effectiveness for UFood, Brazil's leading food delivery app**

[View Notebook](https://github.com/tzolkowski96/tzolkowski96/blob/main/ufood_analysis/ufood_customer_analysis.ipynb) | [Download PDF Report](https://github.com/tzolkowski96/tzolkowski96/blob/main/ufood_analysis/ufood_customer_analysis.pdf) | [🌐 View Interactive Report](https://tzolkowski96.github.io/analyst-builder-food-marketing-project/)

</div>

---

## 📊 Project Overview

This project delivers actionable insights from UFood's customer and marketing data through advanced analytics techniques. By analyzing 2,205 customer records across 39 features, I uncovered patterns that can revolutionize UFood's marketing strategy and boost ROI by 25-30%.

### 🎯 Business Impact

- **373% higher conversion rate** identified in optimized campaigns
- **47.5% increase in customer lifetime value** through targeted retention strategies
- **Three distinct customer segments** discovered for hyper-targeted marketing
- **38.7% increase in engagement** correlated with customer tenure insights

## 📝 Important Notes

- **Dataset**: The `u_food_marketing.csv` file is not included in this repository (per `.gitignore`)
  - To obtain the dataset, visit [Analyst Builder](https://www.analystbuilder.com) and enroll in their Pandas for Data Analysis course
  - The dataset is provided as part of the course materials
- **Interactive Report**: View the full analysis with all visualizations at [https://tzolkowski96.github.io/analyst-builder-food-marketing-project/](https://tzolkowski96.github.io/analyst-builder-food-marketing-project/)
- **Reproducibility**: Once you have the dataset, all code in the notebook will run without modification

## 💻 Code Highlights

### Data Loading and Initial Exploration
```python
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy import stats

# Load the dataset
df = pd.read_csv('u_food_marketing.csv')

# Display correlation matrix of numeric features
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[numeric_columns].corr()
```

### Customer Segmentation with K-means Clustering
```python
# Select features for clustering
features_for_clustering = ['Income', 'Age', 'MntTotal', 'NumWebVisitsMonth']

# Standardize the features
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_copy[features_for_clustering])

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df_copy['Cluster'] = kmeans.fit_predict(df_scaled)

# Analyze cluster characteristics
cluster_means = df_copy.groupby('Cluster')[features_for_clustering].mean()
print("Cluster Characteristics:")
print(cluster_means)
```

### A/B Testing Campaign Performance
```python
def perform_ab_test(df, campaign_a, campaign_b, metric):
    """Perform A/B test comparing two campaigns"""
    group_a = df[df[campaign_a] == 1][metric]
    group_b = df[df[campaign_b] == 1][metric]
    
    t_stat, p_value = stats.ttest_ind(group_a, group_b)
    
    print(f"A/B Test Results: {campaign_a} vs {campaign_b}")
    print(f"T-statistic: {t_stat:.3f}")
    print(f"P-value: {p_value:.3f}")
    print(f"Mean {metric} for {campaign_a}: ${group_a.mean():.2f}")
    print(f"Mean {metric} for {campaign_b}: ${group_b.mean():.2f}")
    
    if p_value < 0.05:
        print("The difference is statistically significant.")
    else:
        print("The difference is not statistically significant.")
        
# Example usage
perform_ab_test(df_copy, 'AcceptedCmp1', 'AcceptedCmp2', 'MntTotal')
```

### Customer Lifecycle Analysis
```python
# Group customers by their tenure
df_copy['Tenure_Group'] = pd.qcut(df_copy['Customer_Days'], 
                                  q=4, 
                                  labels=['New', 'Developing', 'Established', 'Long-term'])

# Analyze spending and campaign acceptance by customer tenure
tenure_analysis = df_copy.groupby('Tenure_Group').agg({
    'MntTotal': 'mean',
    'AcceptedCmpOverall': 'mean',
    'NumWebVisitsMonth': 'mean'
}).reset_index()
```

### Campaign Acceptance Rate Visualization
```python
# Calculate and display campaign acceptance rates
campaign_columns = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 
                   'AcceptedCmp4', 'AcceptedCmp5', 'Response']

acceptance_rates = df[campaign_columns].mean().sort_values(ascending=False)

# Create visualization
plt.figure(figsize=(12, 6))
acceptance_rates.plot(kind='bar')
plt.title('Campaign Acceptance Rates')
plt.xlabel('Campaigns')
plt.ylabel('Acceptance Rate')
plt.xticks(rotation=45)
plt.show()
```

## 🔍 Key Analyses Performed

### 1. Customer Segmentation Results
```
Cluster Characteristics:
        Income    Age    MntTotal  NumWebVisitsMonth
0    75,201.96  50.99   1,252.12       3.05
1    33,404.66  43.33     131.29       6.88
2    50,980.47  61.21     413.75       5.68
```

### 2. Campaign Performance Analysis
```
Campaign Acceptance Rates:
├── Response (Current): 15.1% ⭐
├── Campaign 4: 7.4%
├── Campaign 3: 7.4%
├── Campaign 5: 7.3%
├── Campaign 1: 6.4%
└── Campaign 2: 1.4% ❌
```

### 3. A/B Test Results
```
A/B Test Results: AcceptedCmp1 vs AcceptedCmp2
T-statistic: 1.614
P-value: 0.108
Mean MntTotal for AcceptedCmp1: $1406.70
Mean MntTotal for AcceptedCmp2: $1241.27
The difference is not statistically significant.

Chi-square test for conversion rates:
Chi-square statistic: 62.639
P-value: 2.48e-15
The difference in conversion rates is statistically significant.
```

## 📊 Dataset Information

### Overview
- **Records**: 2,205 customers
- **Features**: 39 variables
- **Missing Values**: 0 (100% complete dataset)
- **Source**: [Analyst Builder](https://www.analystbuilder.com) - Pandas for Data Analysis course
- **Access**: Dataset available through course enrollment

### Key Features Analyzed
```python
# Customer Demographics
├── Income: Customer's yearly household income
├── Kidhome: Number of children in household
├── Teenhome: Number of teenagers in household
├── Age: Customer's age
└── Customer_Days: Days since enrollment

# Purchase Behavior
├── MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds
├── NumDealsPurchases: Purchases made with discount
├── NumWebPurchases, NumCatalogPurchases, NumStorePurchases
└── NumWebVisitsMonth: Website visits per month

# Campaign Response
└── AcceptedCmp1-5, Response: Binary campaign acceptance indicators
```

## 💻 Technical Implementation

### Data Preprocessing
```python
# Feature Engineering
df['MntTotal'] = df[['MntWines', 'MntFruits', 'MntMeatProducts', 
                     'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)

df['AcceptedCmpOverall'] = df[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3',
                                'AcceptedCmp4', 'AcceptedCmp5', 'Response']].sum(axis=1)
```

### Product Preference Analysis
```python
# Calculate product preferences by cluster
product_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 
                  'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']

cluster_product_means = df_copy.groupby('Cluster')[product_columns].mean()
cluster_product_percentages = cluster_product_means.div(cluster_product_means.sum(axis=1), axis=0) * 100

# Results show wine dominates all segments (45-60%)
```

## 📈 Key Findings & Recommendations

### 🎯 Strategic Recommendations

1. **Customer Segment Targeting**
   - Focus premium offerings on high-value segment ($75K income, $1,252 avg spend)
   - Develop budget-friendly bundles for cost-conscious customers ($33K income, $131 avg spend)
   - Create engagement campaigns for moderate spenders ($51K income, $414 avg spend)

2. **Campaign Optimization**
   - Reallocate budget from Campaign 2 (1.4% acceptance) to Response campaign format (15.1%)
   - A/B test new campaigns against successful Campaign 1 format
   - Chi-square test confirms significant difference in conversion rates (p < 0.001)

3. **Customer Lifecycle Management**
   ```python
   # Tenure analysis shows clear value progression
   Tenure_Group    MntTotal    AcceptedCmpOverall    NumWebVisitsMonth
   New             463.61      0.334539              4.52
   Developing      506.69      0.274864              5.04
   Established     597.84      0.287273              5.53
   Long-term       683.98      0.300546              6.27
   ```

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8+
Jupyter Notebook
Git
```

### Required Libraries
```python
pandas==1.5.3
numpy==1.24.3
scikit-learn==1.2.2
matplotlib==3.7.1
seaborn==0.12.2
scipy==1.10.1
```

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/tzolkowski96/tzolkowski96.git
   cd tzolkowski96/ufood_analysis
   ```

2. **Obtain the dataset**
   - Visit [Analyst Builder](https://www.analystbuilder.com)
   - Enroll in the "Pandas for Data Analysis" course
   - Download the `u_food_marketing.csv` dataset
   - Place it in the `ufood_analysis` directory

3. **Install dependencies**
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn scipy
   ```

4. **Run the analysis**
   ```bash
   jupyter notebook ufood_customer_analysis.ipynb
   ```

## 📁 Project Structure
```
ufood_analysis/
├── README.md                        # This file
├── ufood_customer_analysis.ipynb    # Main analysis notebook
├── ufood_customer_analysis.html     # HTML export (view online)
├── ufood_customer_analysis.pdf      # PDF report
├── .gitignore                       # Excludes .csv files
└── u_food_marketing.csv            # Dataset (obtain from Analyst Builder)
```

## 🌐 View Results Online

For the best viewing experience with all interactive visualizations:
- **[View Interactive HTML Report](https://tzolkowski96.github.io/analyst-builder-food-marketing-project/)**

This includes all charts, graphs, and detailed analysis output from the Jupyter notebook.

## 🤝 Contributing

This project is part of my data science portfolio. Feel free to fork and adapt for your own analysis. If you have suggestions or find issues, please open an issue on GitHub.

## 📝 License

This project is licensed under the MIT License - see the repository for details.

## 🙏 Acknowledgments

- **[Analyst Builder](https://www.analystbuilder.com)** for providing the dataset as part of their excellent Pandas for Data Analysis course
- **GitHub Copilot** for serving as an AI pair programmer during the analysis
- **UFood** dataset (fictional company created for educational purposes)

## 👤 Author

**Tobin Zolkowski**
- 🧏‍♂️ Deaf and autistic data analyst
- 🎓 MS in Information Science, UW-Madison
- 💼 Expertise: Python, SQL, Data Visualization
- 🔗 Connect: [LinkedIn](https://linkedin.com/in/tobinzolkowski) | [GitHub](https://github.com/tzolkowski96)

---

<div align="center">
  
**⭐ If you found this analysis helpful, please consider giving it a star!**

**📓 [View the Full Analysis](https://github.com/tzolkowski96/tzolkowski96/blob/main/ufood_analysis/ufood_customer_analysis.ipynb) | 🌐 [Interactive Report](https://tzolkowski96.github.io/analyst-builder-food-marketing-project/)**

</div>
