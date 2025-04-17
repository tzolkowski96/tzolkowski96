# Traffic Accident Analytics Engine
## Advanced Geospatial-Temporal Analysis System

![Traffic Accident Analysis Overview](visualizations/traffic_accident_temporal_analysis_4panel.png)

[![GitHub stars](https://img.shields.io/github/stars/tzolkowski96/us_accidents_analysis?style=social)](https://github.com/tzolkowski96/us_accidents_analysis/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/tzolkowski96/us_accidents_analysis?style=social)](https://github.com/tzolkowski96/us_accidents_analysis/network/members)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/tzolkowski96/us_accidents_analysis/blob/main/LICENSE)

> Comprehensive analysis of 7.7 million US traffic accidents with advanced statistical modeling, machine learning, and interactive visualizations

## Project Overview

This project analyzes **7.7 million US traffic accidents** (2016-2023) using advanced data science techniques to generate actionable insights for traffic management and public safety. The system leverages:

- Statistical modeling to identify accident cause patterns
- Machine learning to predict accident severity
- Geospatial analysis to visualize high-risk locations
- Temporal pattern recognition for accident forecasting

### Key Visualizations

<table>
  <tr>
    <td><img src="visualizations/accident_hotspots.png" alt="Accident Hotspots" width="100%"></td>
    <td><img src="visualizations/severity_analysis.png" alt="Severity Analysis" width="100%"></td>
  </tr>
  <tr>
    <td><img src="visualizations/weather_impact.png" alt="Weather Impact Analysis" width="100%"></td>
    <td><img src="visualizations/geographic_distribution.png" alt="Geographic Distribution" width="100%"></td>
  </tr>
</table>

## Technical Achievements

### Statistical Analysis
- Implemented robust weather impact analysis using chi-square testing (**χ² = 96229.39, p < 0.001**) and ANOVA
- Developed multi-factor correlation models to identify causal relationships
- Performed time-series decomposition to isolate seasonal patterns

### Machine Learning
- Developed and optimized Random Forest classifier achieving **78% accuracy** in severity prediction
- Feature importance analysis identifying key environmental factors
- Hyperparameter tuning with cross-validation to optimize model performance

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
- Optimized data processing pipeline reducing memory usage by **3.25%**
- Engineered temporal features to capture cyclical patterns

### Visualization
- Created interactive heatmaps visualizing accident density across the US
- Developed multi-panel dashboards for analyzing temporal and weather patterns
- Generated geospatial visualizations of high-risk corridors

## GIS and Geospatial Analytics

![Weather Condition Analysis](visualizations/weather_severity_analysis_quad_stats.png)

- Created interactive heat maps visualizing accident density across 49 states
- Developed custom geospatial clustering algorithms for hotspot identification
- Implemented coordinate-based analysis for high-risk corridor detection
- Generated dynamic Folium maps for temporal-spatial pattern visualization

## Technology Stack

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

## Key Features

### Weather Impact Analysis
- Pressure and temperature correlation analysis
- Severity classification by weather condition
- Feature importance quantification
- Environmental factor impact assessment

### Spatial Analytics
![Temporal Analysis](visualizations/temporal_analysis_figure.png)

- Urban accident density mapping
- Interstate corridor risk analysis
- Regional weather pattern correlation
- Geographic hotspot identification

### Temporal Pattern Recognition
- Peak hour accident analysis
- Seasonal trend identification
- Day-of-week distribution analysis
- Time-weather interaction mapping

## Model Performance Analysis

The Random Forest classifier achieved 78% accuracy overall, but performance varied significantly across severity classes:

```
             precision    recall  f1-score   support
          1       0.40      0.07      0.12     13677
          2       0.81      0.96      0.88   1230834
          3       0.39      0.12      0.19    260285
          4       0.36      0.08      0.13     40833
```

### Class Imbalance Challenges
- **Severity 2 dominance**: 79.6% of incidents are Severity 2, leading to model bias
- **Recall issues**: Low recall values for classes 1 (0.07), 3 (0.12), and 4 (0.08)
- **Mitigation strategies**: Implemented SMOTE oversampling and class weighting to improve minority class prediction

### Performance Optimization
- Conducted feature selection to reduce dimensionality and improve model generalization
- Implemented ensemble techniques combining multiple models to improve rare class detection
- Refined hyperparameters through grid search with stratified cross-validation

## Data Limitations and Biases

Our analysis acknowledges several important data limitations:

1. **Reporting bias**: Accident data is influenced by jurisdictional reporting standards, potentially underrepresenting rural areas with limited police coverage
   
2. **Geographic coverage**: While the dataset includes 49 states, representation varies significantly, with California (22.5%) and Florida (11.4%) disproportionately represented

3. **Temporal consistency**: Data collection methods evolved over time, with significant collection methodology changes in 2020-2021 potentially impacting trend analysis

4. **Severity classification subjectivity**: The 1-4 severity scale may be applied inconsistently across jurisdictions, affecting comparative analysis

5. **Environmental data quality**: Weather data is collected from nearest weather stations, not accident sites, introducing potential environmental condition inaccuracies

## Real-World Applications

- **Emergency Response**: Data-driven resource allocation optimization
- **Urban Planning**: Evidence-based infrastructure development recommendations
- **Traffic Management**: Real-time risk assessment capabilities
- **Public Safety**: Weather-specific safety protocol development

## Installation & Setup

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

## Methodology

### 1. Data Preparation
- Standardization of 7.7M multi-jurisdictional records
- Feature engineering for temporal patterns
- Geospatial data normalization
- Missing value handling

### 2. Analysis Pipeline
- Statistical hypothesis testing
- Machine learning model development
- Feature importance analysis
- Cross-validation and testing

### 3. Visualization Development
- Interactive geospatial mapping
- Temporal pattern dashboards
- Weather correlation matrices
- Severity distribution analysis

## Visualization Enhancement Strategies

To improve visualization clarity and information density:

1. **Weather condition grouping**: Consolidated similar weather conditions into interpretable categories
   
2. **Color scheme optimization**: Used colorblind-friendly palettes with proper contrast
   
3. **Interactive elements**: Implemented tooltips and filtering in Folium maps
   
4. **Layout improvements**: Redesigned multi-panel visualizations with consistent scales
   
5. **Simplified legends**: Reduced visual clutter while maintaining information integrity

Example improvement (Weather conditions chart):
```python
# Original overcrowded chart
weather_counts = df_clean['Weather_Condition'].value_counts().head(10)
sns.barplot(x=weather_counts.index, y=weather_counts.values)

# Improved visualization with grouped conditions
weather_mapping = {
    'Fair': 'Clear/Fair', 'Clear': 'Clear/Fair',
    'Mostly Cloudy': 'Cloudy', 'Partly Cloudy': 'Cloudy',
    # Additional mappings...
}
df_clean['Weather_Simple'] = df_clean['Weather_Condition'].map(
    lambda x: next((v for k, v in weather_mapping.items() 
                   if k in x), 'Other')
)
```

## Results & Findings

![Weather Conditions](visualizations/weather_conditions.png)

Key insights from the analysis:

- **Weather Impact**: Adverse weather conditions increase accident severity by an average of 0.15 points (on 1-4 scale)
- **Regional Patterns**: Urban centers show 3.7x higher accident density than rural areas
- **Temporal Factors**: Peak accident times occur during 7-9am and 4-6pm rush hours on weekdays
- **Severity Drivers**: Pressure systems and temperature are the top weather predictors of accident severity

## Contact & Contribution

- **Source Code**: Due to GitHub's 100MB file size limitation, the complete Jupyter notebook is available via [request](mailto:example@email.com)
- **Questions**: Feel free to [open an issue](https://github.com/tzolkowski96/us_accidents_analysis/issues) or contact me directly
- **Contributions**: Pull requests are welcome! Please see the [contributing guidelines](CONTRIBUTING.md)

## Attribution

Dataset: US Accidents (2016-2023)  
Authors: Sobhan Moosavi et al.  
License: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Future Development

- Integration of real-time weather data
- Enhancement of predictive modeling accuracy
- Development of API for external system integration
- Expansion of visualization capabilities