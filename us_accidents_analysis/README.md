# 🚦 Traffic Accident Analytics Engine

## Advanced Geospatial-Temporal Analysis System

![Traffic Accident Analysis Overview](visualizations/traffic_accident_temporal_analysis_4panel.png)
*Four-panel visualization showing accident distribution by time of day, day of week, month, and year*

[![GitHub stars](https://img.shields.io/github/stars/tzolkowski96/us_accidents_analysis?style=social)](https://github.com/tzolkowski96/us_accidents_analysis/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/tzolkowski96/us_accidents_analysis?style=social)](https://github.com/tzolkowski96/us_accidents_analysis/network/members)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/tzolkowski96/us_accidents_analysis/blob/main/LICENSE)
[![Data Quality](https://img.shields.io/badge/data%20coverage-49%20states-brightgreen.svg)](https://github.com/tzolkowski96/us_accidents_analysis)

> **A journey through 7.7 million accidents that reveals surprising patterns in American road safety**

## 🔍 Project Overview

This project analyzes **7.7 million US traffic accidents** (2016-2023) using advanced data science techniques to uncover hidden patterns and generate actionable insights for public safety. Our analysis:

- Reveals counterintuitive findings about weather impacts on traffic safety
- Identifies critical geographic and temporal accident hotspots
- Quantifies the relationship between environmental conditions and crash severity
- Provides data-driven recommendations for reducing accident frequency and severity

### Key Visualizations

<table>
  <tr>
    <td><img src="visualizations/accident_hotspots.png" alt="Accident Hotspots" width="100%"></td>
    <td><img src="visualizations/severity_analysis.png" alt="Severity Analysis" width="100%"></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><em>Left: Geographic distribution of accident hotspots across the US. Right: Analysis of severity factors and their relative impact.</em></td>
  </tr>
  <tr>
    <td><img src="visualizations/weather_impact.png" alt="Weather Impact Analysis" width="100%"></td>
    <td><img src="visualizations/geographic_distribution.png" alt="Geographic Distribution" width="100%"></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><em>Left: Weather conditions and their influence on accident severity. Right: State-by-state breakdown of accident distribution.</em></td>
  </tr>
</table>

## ✨ Key Findings That Might Surprise You

### The Weather Paradox
Did you know that **77% of all traffic accidents occur in clear or cloudy conditions** – not during rain, snow, or fog? Our analysis reveals this counterintuitive pattern, suggesting drivers may be more cautious in visibly adverse conditions but let their guard down when the weather seems safe.

### The Pressure Factor
Our machine learning models identified **barometric pressure as the strongest predictor of accident severity (37.8%)**, outweighing temperature (33.1%), wind speed (20.9%), and visibility (8.2%) – a finding that challenges conventional wisdom about weather-related risk factors.

### America's Accident Landscape
The geographic distribution is striking: **California accounts for 1.7 million accidents** (22% of the national total), followed by Florida (880K) and Texas (582K). This concentration suggests regional factors beyond population density are at play.

### The Rhythm of Risk
The data reveals clear temporal patterns: **weekday rush hours (7-9AM and 4-6PM) see 6× more accidents** than the early morning hours, while **Fridays experience 35% more accidents than Sundays**. This time-based insight can help target safety initiatives and emergency resource allocation.

## 🧪 Technical Achievements

### Statistical Analysis
- Conducted robust weather impact analysis using chi-square testing (**χ² = 96,229.39, p < 0.001**) establishing definitive correlations between weather conditions and accident severity
- Developed multi-factor correlation models identifying causal relationships between environmental variables
- Performed time-series decomposition to isolate seasonal patterns and long-term trends

### Machine Learning
- Developed and optimized Random Forest classifier achieving **78% accuracy** in severity prediction
- Conducted feature importance analysis revealing key environmental risk factors
- Implemented hyperparameter tuning with cross-validation to optimize model performance

```python
# Sample code: Feature importance extraction
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Prepare features
X = df[weather_features].copy()
y = df['Severity']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model and extract importance
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
importances = pd.Series(rf.feature_importances_, index=weather_features)
importances.sort_values(ascending=False).plot(kind='barh')
```

### Data Engineering
- Processed and standardized nationwide temporal and geospatial data across 49 states
- Optimized data processing pipeline reducing memory usage by **3.25%** (66.39MB)
- Engineered temporal features to capture cyclical patterns and seasonal variations

### Visualization
- Created interactive heatmaps visualizing accident density across the US
- Developed multi-panel dashboards for analyzing temporal and weather patterns
- Generated geospatial visualizations of high-risk corridors with severity coding

## 🗺️ Geographic Insights

![Weather Condition Analysis](visualizations/weather_severity_analysis_quad_stats.png)
*Comprehensive analysis of how different weather conditions affect accident frequency and severity across regions*

Our geospatial analysis revealed distinct regional patterns:

- **The Northeast Corridor** (Boston-NYC-DC) forms America's densest accident cluster, reflecting high population density combined with aging infrastructure
- **California's coastal highways** show intense accident patterns, particularly around Los Angeles, San Francisco, and San Diego
- **Rural vs. urban divide** is clearly visible – fewer accidents in rural areas, but those that occur tend to be more severe (average severity 2.3 vs. 2.1)
- **Interstate convergence points** consistently appear as high-risk zones, especially where three or more major highways intersect

## 🛠️ Technology Stack

<table>
  <tr>
    <td><strong>Core Processing</strong></td>
    <td>Python (NumPy, pandas)</td>
  </tr>
  <tr>
    <td><strong>Machine Learning</strong></td>
    <td>scikit-learn (Random Forest, Feature Importance)</td>
  </tr>
  <tr>
    <td><strong>Statistical Tools</strong></td>
    <td>SciPy (Chi-square, ANOVA)</td>
  </tr>
  <tr>
    <td><strong>Visualization</strong></td>
    <td>Matplotlib, Seaborn, Folium</td>
  </tr>
  <tr>
    <td><strong>Data Pipeline</strong></td>
    <td>StandardScaler, Git version control</td>
  </tr>
</table>

## 🔎 Behind the Numbers: Weather Impact

Our analysis goes beyond simply counting accidents to understand deeper patterns:

### Weather Distribution
- **Clear/Fair conditions**: 44.1% of all accidents
- **Cloudy conditions**: 33.3% of accidents
- **Rain**: Only 6.6% of accidents
- **Snow**: Just 2.1% of accidents
- **Low visibility** (fog, haze): 2.5% of accidents
- **Other conditions**: 11.5% of accidents

### Severity by Weather Type
- **"Other" unusual conditions**: Highest average severity (2.33)
- **Rain**: Second highest severity (2.25) 
- **Snow**: Third highest severity (2.24)
- **Cloudy**: Moderate severity (2.20)
- **Clear/Fair & Low Visibility**: Lowest severity (2.18)

![Temporal Analysis](visualizations/temporal_analysis_figure.png)
*Daily and weekly accident patterns showing clear rush hour peaks and weekend reductions*

## 🔬 Model Performance & Limitations

Our Random Forest classifier achieved 78% overall accuracy, but performance varied significantly across severity classes:

```
             precision    recall  f1-score   support
          1       0.40      0.07      0.12     13677
          2       0.81      0.96      0.88   1230834
          3       0.39      0.12      0.19    260285
          4       0.36      0.08      0.13     40833
```

### Understanding the Challenges
- **Class imbalance**: Severity 2 dominates the dataset (79.6% of incidents)
- **Recall issues**: Low recall values for classes 1 (0.07), 3 (0.12), and 4 (0.08)
- **Mitigation strategies**: We implemented SMOTE oversampling and class weighting techniques to improve minority class prediction

## 📊 Real-World Applications

- **Emergency Response**: Data-driven resource allocation optimization based on temporal and geographic risk patterns
- **Urban Planning**: Evidence-based infrastructure development recommendations focused on high-risk corridors
- **Traffic Management**: Real-time risk assessment capabilities integrating weather and temporal factors
- **Public Safety**: Development of targeted safety campaigns addressing specific risk factors and driver behaviors

## 🚀 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/tzolkowski96/us_accidents_analysis.git
cd us_accidents_analysis

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download the dataset (requires Kaggle API)
python scripts/download_data.py

# Run analysis notebook
jupyter notebook notebooks/accident_analysis.ipynb
```

### Requirements
- Python 3.8+
- 16GB+ RAM recommended
- 10GB+ free disk space
- Kaggle API credentials (for dataset access)

## 📝 Methodology

### 1. Data Preparation
- Standardized 7.7M multi-jurisdictional records from diverse reporting systems
- Engineered temporal features to capture cyclical patterns (hour, day, month, season)
- Normalized geospatial data and handled missing coordinates
- Implemented efficient missing value strategies for weather metrics

### 2. Analysis Pipeline
- Conducted comprehensive statistical hypothesis testing to validate relationships
- Developed machine learning models for severity prediction and feature importance
- Applied geographic clustering techniques to identify high-risk corridors
- Performed multi-variable correlation analysis to identify key risk factors

### 3. Visualization Development
- Created interactive geospatial maps with severity-coded markers
- Developed temporal pattern dashboards showing multi-scale time patterns
- Generated weather correlation matrices revealing environmental factor relationships
- Produced severity distribution analyses highlighting regional risk variations

## 🧠 Data Limitations & Biases

Our analysis acknowledges several important data limitations:

1. **Geographic representation**: California (22.5%) and Florida (11.4%) are over-represented relative to their population
2. **Reporting differences**: States and jurisdictions vary in their accident reporting standards and thresholds
3. **Urban bias**: Rural accidents may be under-reported due to limited police coverage and reporting
4. **Temporal consistency**: Collection methods evolved during the 7-year period, particularly during 2020-2021
5. **Severity subjectivity**: The 1-4 severity scale may be applied inconsistently across jurisdictions

## 📈 Results & Key Insights

![Weather Conditions](visualizations/weather_conditions.png)
*Analysis of weather conditions during accidents, showing the surprising dominance of clear and cloudy conditions*

Our comprehensive analysis revealed several actionable insights:

- **Weather Impact**: Adverse weather conditions increase accident severity by an average of 0.15 points (on 1-4 scale)
- **Regional Patterns**: Urban centers show 3.7× higher accident density than rural areas
- **Temporal Factors**: Peak accident times occur during 7-9AM and 4-6PM rush hours on weekdays
- **Severity Drivers**: Pressure systems and temperature are the top weather predictors of accident severity

## 🤝 Contact & Contribution

- **Complete Analysis**: The detailed Jupyter notebook with all visualizations is available via [request](mailto:example@email.com) due to GitHub's 100MB file size limitation
- **Questions**: Feel free to [open an issue](https://github.com/tzolkowski96/us_accidents_analysis/issues) or contact me directly
- **Contributions**: Pull requests are welcome! Please see the [contributing guidelines](CONTRIBUTING.md)

## 📚 Attribution

Dataset: US Accidents (2016-2023)  
Authors: Sobhan Moosavi et al.  
License: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## 🔮 Future Directions

- Integration of real-time weather data for dynamic risk assessment
- Development of predictive models for accident likelihood based on current conditions
- Creation of an API for transportation systems to access risk predictions
- Expansion of the analysis to include traffic volume data for normalized risk metrics

---

<p align="center">
<strong>Saving lives through data science</strong><br>
If you found this project valuable, please consider <a href="https://github.com/tzolkowski96/us_accidents_analysis/stargazers">starring the repository</a> and sharing with others who might benefit.
</p>