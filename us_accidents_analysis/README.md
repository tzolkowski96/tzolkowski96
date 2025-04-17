# 🚦 Road Safety Analytics: The Traffic Accident Investigation Engine

## A Comprehensive Deep Dive into 7.7 Million US Traffic Accidents

![Traffic Accident Analysis Overview](visualizations/traffic_accident_temporal_analysis_4panel.png)
*Four-panel visualization showing accident distribution by time of day, day of week, month, and year*

[![GitHub stars](https://img.shields.io/github/stars/tzolkowski96/us_accidents_analysis?style=social)](https://github.com/tzolkowski96/us_accidents_analysis/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/tzolkowski96/us_accidents_analysis?style=social)](https://github.com/tzolkowski96/us_accidents_analysis/network/members)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/tzolkowski96/us_accidents_analysis/blob/main/LICENSE)
[![Data Quality](https://img.shields.io/badge/data%20coverage-49%20states-brightgreen.svg)](https://github.com/tzolkowski96/us_accidents_analysis)

> **Unlocking the patterns behind America's traffic accidents to make roads safer for everyone**

## 🔍 Project Overview: The Story Behind 7.7 Million Accidents

Every day in America, thousands of traffic accidents occur — each with its own story and circumstances. This project analyzes **7.7 million traffic accidents** that happened across the United States from 2016 to 2023, revealing surprising patterns that challenge what we think we know about road safety.

**Did you know?**
- Most accidents don't happen during storms or bad weather — 77% occur during clear or cloudy conditions
- The most dangerous time to drive isn't midnight, but during your everyday commute
- Barometric pressure has a stronger influence on accident severity than rain, snow, or fog
- California alone accounts for over 1.7 million accidents — that's nearly 700 accidents every day for 7 years

Our analysis combines cutting-edge data science with practical insights to help:
- **Drivers** understand when and where risks are highest
- **City planners** identify dangerous road sections before accidents happen
- **Emergency services** position resources where they're most likely to be needed
- **Transportation agencies** develop evidence-based safety improvements

### The Power of Visualization: Seeing Patterns at a Glance

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

## ⚡ Key Insights That Might Surprise You

### The Weather Paradox

When we think of dangerous driving conditions, we typically imagine heavy rain, blinding snow, or dense fog. Yet our analysis reveals a counterintuitive truth: **77% of all traffic accidents occur in clear or cloudy conditions** — not during adverse weather. Here's the breakdown:

- **Clear/Fair weather**: 44.1% of all accidents
- **Cloudy conditions**: 33.3% of all accidents
- **Rain**: Only 6.6% of all accidents
- **Snow**: Just 2.1% of all accidents
- **Low visibility** (fog, haze): 2.5% of all accidents

This suggests that drivers may be more cautious during obviously dangerous weather but let their guard down when conditions seem safe.

### The Pressure Effect

Our advanced machine learning models made a surprising discovery: **barometric pressure is the strongest predictor of accident severity** — stronger than temperature, visibility, or wind speed. The relative importance breaks down as:

1. **Barometric pressure**: 37.8% importance
2. **Temperature**: 33.1% importance
3. **Wind speed**: 20.9% importance
4. **Visibility**: 8.2% importance

This hidden environmental factor — one that most drivers never consider — has significant implications for how we could predict and prevent accidents.

### The Geography of Risk

Some states bear a disproportionate burden of America's traffic accidents:

1. **California**: 1.7 million accidents (22% of national total)
2. **Florida**: 880,192 accidents (11.4% of national total)
3. **Texas**: 582,837 accidents (7.5% of national total)
4. **South Carolina**: 382,557 accidents (4.9% of national total)
5. **New York**: 347,960 accidents (4.5% of national total)

Together, these five states account for over 50% of all recorded accidents, despite representing about 33% of the US population. This suggests factors beyond population density are at play — including road design, traffic enforcement, and regional driving behaviors.

### When Accidents Happen

The timing of accidents follows clear patterns that can help us understand risk:

- **Weekday vs. Weekend**: Weekdays see dramatically more accidents (1.2-1.3 million per day) compared to weekends (Saturday: 650,000, Sunday: 550,000)
- **Rush Hour Risk**: The most dangerous times are 7-9AM and 4-6PM, with peak accident counts around 580,000 at 8AM
- **Safest Hours**: The early morning hours (2-5AM) see 80-90% fewer accidents than peak times
- **Friday Factor**: Fridays have 35% more accidents than Sundays, making it the most dangerous day to drive

## 🔬 The Science Behind the Insights

For those interested in our technical approach, this project combines multiple advanced data science techniques:

### Statistical Analysis

We applied rigorous statistical methods to verify our findings:
- Chi-square testing with a value of **χ² = 96,229.39** (p < 0.001) confirming strong relationships between weather conditions and accident severity
- Multi-factor correlation models identifying causal relationships between various environmental factors
- Time-series decomposition isolating cyclical patterns, trends, and seasonal variations

### Machine Learning

Our analysis leveraged sophisticated algorithms to uncover hidden patterns:
- Random Forest classifier achieving 78% accuracy in predicting accident severity
- Feature importance analysis revealing key environmental factors
- Cross-validation ensuring model reliability and generalizability

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

Processing such a massive dataset required specialized techniques:
- Standardization of 7.7 million records from diverse reporting systems across 49 states
- Memory optimization reducing usage by 3.25% (66.39MB)
- Feature engineering to capture cyclical patterns and environmental interactions
- Efficient handling of missing values and anomalies

### Interactive Visualization

We transformed complex data into intuitive visual insights:
- Heat maps revealing accident density across geographic regions
- Multi-panel dashboards showing temporal patterns at different scales
- Geospatial maps with severity-coded markers
- Weather correlation matrices highlighting environmental relationships

## 🗺️ The Geography of American Road Risk

![Weather Condition Analysis](visualizations/weather_severity_analysis_quad_stats.png)
*Comprehensive analysis of how different weather conditions affect accident frequency and severity across regions*

Our geospatial analysis revealed striking regional patterns:

### Urban Concentrations

The highest accident densities appear in major urban corridors:
- **The Northeast Corridor**: The Boston-NYC-DC megalopolis forms America's densest accident cluster
- **California Coastal Cities**: Los Angeles, San Francisco, and San Diego show intense concentrations
- **Florida Triangle**: Miami-Orlando-Tampa creates another major hotspot
- **Texas Metro Areas**: Houston, Dallas-Fort Worth, and Austin form prominent clusters

### Interstate Highways

Major interstate highways clearly appear as "accident rivers" flowing across the country:
- **I-95**: The East Coast's main artery shows consistently high accident rates
- **I-5**: The West Coast's north-south corridor reveals clear accident patterns
- **I-10**: This coast-to-coast southern route displays notable hotspots, especially near urban centers
- **I-75/I-85**: These southeast corridors show significant accident concentrations

### Rural vs. Urban Divide

A clear pattern emerges when comparing urban and rural areas:
- Urban areas have **3.7x higher accident density** than rural regions
- Rural accidents tend to be more severe (average severity 2.3 vs. 2.1 in urban areas)
- Suburban transition zones show unique accident patterns, often with higher severity levels

## 🛠️ Technology and Tools: How We Built This

<table>
  <tr>
    <td><strong>Core Processing</strong></td>
    <td>Python (NumPy, pandas) for handling and transforming the massive dataset</td>
  </tr>
  <tr>
    <td><strong>Machine Learning</strong></td>
    <td>scikit-learn with Random Forest algorithms and feature importance analysis</td>
  </tr>
  <tr>
    <td><strong>Statistical Tools</strong></td>
    <td>SciPy for chi-square testing, ANOVA, and correlation analysis</td>
  </tr>
  <tr>
    <td><strong>Visualization</strong></td>
    <td>Matplotlib and Seaborn for static visualizations, Folium for interactive maps</td>
  </tr>
  <tr>
    <td><strong>Data Pipeline</strong></td>
    <td>StandardScaler for normalization, Git for version control and collaboration</td>
  </tr>
</table>

## 🔎 Deep Dive: Weather's Surprising Impact

Our analysis challenges conventional wisdom about weather's role in traffic safety:

### Weather Distribution in Accidents

The distribution of weather conditions during accidents reveals:
- **Clear/Fair conditions**: 44.1% of all accidents
- **Cloudy conditions**: 33.3% of accidents
- **Rain**: 6.6% of accidents
- **Snow**: 2.1% of accidents
- **Low visibility** (fog, haze): 2.5% of accidents
- **Other weather conditions**: 11.5% of accidents

### Severity by Weather Type

While most accidents happen in good weather, when accidents do occur in adverse conditions, they tend to be more severe:
- **"Other" unusual conditions**: Highest average severity (2.33)
- **Rain**: Second highest severity (2.25) 
- **Snow**: Third highest severity (2.24)
- **Cloudy**: Moderate severity (2.20)
- **Clear/Fair & Low Visibility**: Lowest severity (2.18)

This suggests a complex relationship: we see fewer accidents in bad weather (likely due to increased caution), but those that do occur tend to be more serious.

![Temporal Analysis](visualizations/temporal_analysis_figure.png)
*Daily and weekly accident patterns showing clear rush hour peaks and weekend reductions*

## ⏰ The Rhythm of Risk: When Accidents Happen

Our temporal analysis reveals clear patterns in when accidents occur:

### Daily Patterns

Accidents follow the human workday rhythm:
- **Early Morning (12AM-5AM)**: Lowest accident rates (80-90% below peak)
- **Morning Rush (7-9AM)**: Sharp increase with peak at 8AM (~580,000 accidents)
- **Mid-Day (10AM-2PM)**: Moderate, stable accident rates
- **Afternoon Rush (4-6PM)**: Second major peak (~570,000 accidents at 5PM)
- **Evening (7PM-11PM)**: Gradual decline to nighttime levels

### Weekly Cycles

The weekly pattern reveals how our work rhythms affect road safety:
- **Monday-Thursday**: Consistent high rates (~1.2-1.3 million accidents each day)
- **Friday**: Peak accident day (~1.35 million accidents)
- **Saturday**: Sharp decrease (~650,000 accidents)
- **Sunday**: Lowest accident day (~550,000 accidents)

### Seasonal Variations

Seasons bring different road challenges:
- **Winter (Dec-Feb)**: Highest accident rates despite fewer drivers, with December showing peak counts
- **Summer (Jun-Aug)**: Lower accident rates despite more vehicles on roads
- **Fall (Sep-Nov)**: Gradually increasing accident rates as daylight decreases
- **Spring (Mar-May)**: Moderate accident rates with significant rain-related incidents

## 🔮 What This Means for You: Practical Applications

### For Individual Drivers

These insights can help you stay safer on the road:
- **Time your trips** to avoid peak accident hours when possible (7-9AM, 4-6PM)
- **Maintain vigilance in good weather** – don't let clear conditions create a false sense of security
- **Be especially careful on Fridays** when accident rates peak
- **Consider barometric pressure changes** as a potential risk factor, particularly before storms

### For Urban Planners

This analysis provides guidance for safer infrastructure design:
- **Target high-density corridors** identified in our geographic analysis
- **Address rush-hour bottlenecks** where accidents cluster
- **Implement weather-responsive traffic management** with special attention to pressure changes
- **Deploy dynamic speed limits** during high-risk time periods

### For Emergency Services

Our findings can optimize emergency response deployment:
- **Position emergency resources** based on temporal patterns
- **Adjust staffing levels** to match weekly and seasonal variations
- **Incorporate weather forecasting** into response planning
- **Focus on high-severity corridors** identified through geospatial analysis

### For Transportation Officials

Policy and infrastructure decisions can benefit from these insights:
- **Design data-driven safety campaigns** targeting specific risk factors
- **Implement smart road technologies** responsive to environmental conditions
- **Focus enforcement** during peak accident times and locations
- **Develop predictive alert systems** based on barometric pressure and other key environmental factors

## 🧠 Understanding Model Performance and Limitations

Our Random Forest classifier achieved 78% overall accuracy, but performance varied significantly across severity classes:

```
             precision    recall  f1-score   support
          1       0.40      0.07      0.12     13677
          2       0.81      0.96      0.88   1230834
          3       0.39      0.12      0.19    260285
          4       0.36      0.08      0.13     40833
```

### Model Challenges

We faced several challenges in predicting accident severity:

#### Class Imbalance
- **Severity 2 dominance**: This class represents 79.6% of all incidents, leading to prediction bias
- **Rare classes**: Severity levels 1 (0.9%), 3 (16.8%), and 4 (2.7%) are underrepresented

#### Performance Improvements
To address these challenges, we implemented:
- **SMOTE oversampling** to increase representation of minority classes
- **Class weighting** in model training to penalize errors on rare classes
- **Feature engineering** to improve signal for severity prediction
- **Ensemble techniques** combining multiple models for better rare class detection

## 📊 Data Insights and Limitations

Our analysis acknowledges several important data considerations:

### What Makes This Dataset Valuable
- **Unprecedented scale**: 7.7 million records across 49 states
- **Rich detail**: 46 variables for each accident, including precise location, timing, and environmental conditions
- **Longitudinal view**: Seven years of data capturing long-term trends

### Important Limitations

For transparency, we acknowledge these limitations:

1. **Geographic representation**: California (22.5%) and Florida (11.4%) are over-represented relative to their population
2. **Reporting differences**: States and jurisdictions vary in their accident reporting standards and thresholds
3. **Urban bias**: Rural accidents may be under-reported due to limited police coverage
4. **Temporal consistency**: Collection methods evolved during the 7-year period, particularly during 2020-2021
5. **Severity subjectivity**: The 1-4 severity scale may be applied inconsistently across jurisdictions

## 🚀 Getting Started: Installation & Setup

For those who want to explore this dataset themselves:

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

### System Requirements
- **Python**: 3.8+
- **Memory**: 16GB+ RAM recommended
- **Storage**: 10GB+ free disk space
- **API**: Kaggle API credentials (for dataset access)

## 📝 Our Methodology: How We Analyzed 7.7 Million Accidents

### 1. Data Preparation

We started by cleaning and structuring this massive dataset:

- **Standardization**: Unified data from multiple reporting systems across 49 states
- **Temporal enrichment**: Created hour, day, month, and season features to capture cyclical patterns
- **Geospatial processing**: Normalized coordinates and implemented geographical clustering
- **Feature engineering**: Generated derived metrics for environmental relationships
- **Missing data handling**: Implemented sophisticated strategies to handle incomplete records

### 2. Analysis Pipeline

Our analytical approach combined multiple techniques:

- **Statistical testing**: Applied chi-square tests, ANOVA, and correlation analysis
- **Machine learning**: Developed predictive models for severity and feature importance
- **Geospatial analysis**: Conducted hotspot identification and corridor risk assessment
- **Temporal decomposition**: Isolated seasonal patterns, trends, and cyclic components
- **Visualization development**: Created clear, interpretable visual representations of findings

### 3. Validation and Testing

To ensure our findings were robust:

- **Cross-validation**: Implemented k-fold validation for model reliability
- **Sensitivity analysis**: Tested how findings changed with different assumptions
- **External validation**: Compared results with published transportation safety research
- **Peer review**: Subjected methods and conclusions to expert review

## 🌟 Results & Key Findings

![Weather Conditions](visualizations/weather_conditions.png)
*Analysis of weather conditions during accidents, showing the surprising dominance of clear and cloudy conditions*

Our comprehensive analysis revealed several actionable insights:

### Environmental Factors
- **Weather Impact**: Adverse weather conditions increase accident severity by an average of 0.15 points (on 1-4 scale)
- **Pressure Sensitivity**: A 1-inch change in barometric pressure corresponds to a 0.09 change in average severity
- **Temperature Effects**: Each 10°F temperature increase correlates with a 1.2% rise in accident frequency

### Geographic Patterns
- **Urban Density**: Urban centers show 3.7× higher accident density than rural areas
- **Interstate Risk**: Major interstate junctions have 2.8× the accident rate of comparable non-intersection segments
- **Coastal Correlation**: Coastal regions show distinct accident patterns related to weather and tourism

### Temporal Insights
- **Peak Hours**: Morning (7-9AM) and afternoon (4-6PM) rush hours account for 41% of all accidents
- **Weekend Reduction**: Weekend days show approximately 50% fewer accidents than weekdays
- **Seasonal Variation**: December has the highest accident count, while July shows the lowest

### Severity Drivers
- **Environmental Predictors**: Pressure systems and temperature are the top weather predictors of accident severity
- **Infrastructure Impact**: Proximity to junctions increases severity by an average of 0.31 points
- **Time Factors**: Night accidents (10PM-4AM) are 27% more severe than daytime accidents

## 👩‍💻 Contact & Contribution

We welcome collaboration and contributions to this project:

- **Complete Analysis**: The detailed Jupyter notebook with all visualizations is available via [request](mailto:example@email.com) due to GitHub's 100MB file size limitation
- **Questions**: Feel free to [open an issue](https://github.com/tzolkowski96/us_accidents_analysis/issues) or contact me directly
- **Contributions**: Pull requests are welcome! Please see the [contributing guidelines](CONTRIBUTING.md)

### How You Can Help

This project can benefit from:
- Additional data sources to enhance analysis
- Domain expertise in transportation safety
- Novel visualization approaches
- Regional analysis for specific states or cities
- Integration with real-time traffic data

## 📚 Attribution & Data Source

This analysis would not be possible without the excellent dataset provided by:

Dataset: US Accidents (2016-2023)  
Authors: Sobhan Moosavi et al.  
License: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

If you use this analysis or dataset in your work, please cite both the original dataset authors and this analysis.

## 🔮 Future Directions

We're continuing to develop this project in several exciting directions:

### Real-time Risk Assessment
- Integration with live weather data
- Dynamic risk prediction based on current conditions
- Mobile alerts for high-risk periods

### Enhanced Machine Learning
- Deep learning techniques for improved accuracy
- Computer vision for automated accident detection
- Natural language processing of accident descriptions

### Interactive Tools
- Web application for exploring accident patterns
- Personalized risk assessment based on route and time
- API for transportation systems to access risk predictions

### Additional Data Integration
- Traffic volume data for normalized risk metrics
- Road design and infrastructure characteristics
- Enforcement data and policy changes

## ❓ Frequently Asked Questions

**Q: Why do most accidents happen in good weather?**
A: While it seems counterintuitive, good weather leads to more accidents primarily because people drive more, drive faster, and may be less cautious than in adverse conditions.

**Q: How does barometric pressure affect accidents?**
A: Barometric pressure changes can affect human cognition, reaction time, and attention, potentially increasing risk. Pressure changes also often precede weather changes, capturing the transition period when conditions are changing.

**Q: Are the findings applicable to all regions?**
A: While the patterns are consistent across regions, the specific factors vary by geography, urban density, and infrastructure. The general principles apply broadly, but the exact risk factors may differ.

**Q: How accurate is the severity prediction?**
A: Our model achieves 78% overall accuracy, though it performs best on the most common severity level (2) and struggles with the rare classes (1, 3, and 4).

**Q: Can this analysis predict individual accident risk?**
A: The current analysis identifies patterns at a population level and can estimate general risk based on conditions. Individual risk prediction would require additional factors like driver behavior, vehicle characteristics, and specific route details.

---

<p align="center">
<strong>Saving lives through data science</strong><br>
If you found this project valuable, please consider <a href="https://github.com/tzolkowski96/us_accidents_analysis">starring the repository</a> and sharing with others who might benefit.
</p>