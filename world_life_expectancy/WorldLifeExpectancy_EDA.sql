-- =============================================================================
-- SECTION 0: SCRIPT DOCUMENTATION AND SETUP
-- =============================================================================
-- Purpose: Provide comprehensive analysis of World Life Expectancy dataset
-- Author: Tobin Zolkowski
-- Date: February 2, 2025
-- Dependencies: Cleaned worldlifexpectancy table with data_quality_score
-- Expected Runtime: 5-10 minutes for complete analysis
-- =============================================================================

-- =============================================================================
-- WORLD LIFE EXPECTANCY EXPLORATORY DATA ANALYSIS (EDA)
-- Author: Tobin Zolkowski
-- Date: February 2, 2025
-- =============================================================================

/*******************************************************************************
 * ANALYSIS OVERVIEW
 * 
 * This script performs comprehensive exploratory data analysis on the World Life 
 * Expectancy dataset. It includes data quality assessment, statistical analysis,
 * and trend identification across multiple dimensions.
 * 
 * DEPENDENCIES:
 * - Requires cleaned worldlifexpectancy table
 * - Requires data_quality_score column
 * 
 * OUTPUT METRICS:
 * - Data quality statistics
 * - Temporal trends
 * - Development status comparisons
 * - Geographic clustering
 * - Correlation analysis
 ******************************************************************************/

-- =============================================================================
-- SECTION 1: DATA VALIDATION AND QUALITY ASSESSMENT
-- =============================================================================
-- Purpose: Evaluate dataset completeness and reliability
-- Dependencies: data_quality_score column
-- Expected Runtime: < 1 minute
-- Output Tables: None (direct query results)
-- 
-- RESULTS SUMMARY:
-- -----------------------------------------------------------------------------
-- Total Records: 2,938
-- High Quality Records (score >= 80): 2,730
-- High Quality Percentage: 92.92%
-- Average Quality Score: 93.41
-- Data Range: 2007-2022 (15 years)
-- 
-- INTERPRETATION:
-- - Dataset shows excellent overall quality (93.41 average score)
-- - Strong reliability with 92.92% high-quality records
-- - Complete 15-year coverage from 2007 to 2022
-- -----------------------------------------------------------------------------

/*******************************************************************************
 * Purpose: Evaluate overall dataset quality and completeness
 * 
 * Methodology:
 * - Calculates total record count
 * - Identifies high-quality records (score >= 80)
 * - Computes average quality score
 * - Determines temporal coverage
 * 
 * Output Fields:
 * - total_records: Total number of observations
 * - high_quality_records: Records with quality score >= 80
 * - high_quality_percentage: Percentage of high-quality records
 * - avg_quality_score: Mean quality score across dataset
 * - min_year, max_year: Temporal range
 ******************************************************************************/
WITH DataQualityMetrics AS (
    -- Using CTE for better readability and reusability
    SELECT 
        COUNT(*) as total_records,                   -- Get total dataset size
        -- Count high quality records using CASE expression for boolean counting
        SUM(CASE WHEN data_quality_score >= 80 THEN 1 ELSE 0 END) as high_quality_records,
        -- Round average to 2 decimal places for readability
        ROUND(AVG(data_quality_score), 2) as avg_quality_score,
        -- Identify dataset temporal boundaries
        MIN(Year) as min_year,
        MAX(Year) as max_year
    FROM worldlifexpectancy
)
SELECT 
    total_records,
    high_quality_records,
    ROUND(100.0 * high_quality_records / total_records, 2) as high_quality_percentage,
    avg_quality_score,
    min_year,
    max_year
FROM DataQualityMetrics;

-- =============================================================================
-- SECTION 2: TEMPORAL ANALYSIS
-- =============================================================================
-- Purpose: Analyze trends and patterns over time
-- Dependencies: Valid life expectancy values
-- Expected Runtime: 1-2 minutes
-- Statistical Methods: Confidence intervals, moving averages
-- 
-- RESULTS SUMMARY:
-- -----------------------------------------------------------------------------
-- Time Series Trends (2007-2022):
-- - Starting point (2007): 66.75 years (CI: 65.26-68.24)
-- - Ending point (2022): 71.62 years (CI: 70.44-72.79)
-- - Net improvement: 4.87 years
-- 
-- Key Observations:
-- - Steady increase from 2007-2019 (66.75 to 70.92 years)
-- - COVID-19 impact in 2020: Sharp drop to 67.55 years
-- - Strong recovery in 2021-2022 (71.54 to 71.62 years)
-- - Decreasing variability over time (SD: 10.27 to 8.10)
-- - Consistent sample size (183 countries) except 2020 (193)
-- -----------------------------------------------------------------------------

/*******************************************************************************
 * Purpose: Analyze life expectancy trends over time with statistical confidence
 * 
 * Methodology:
 * - Groups data by year
 * - Calculates mean life expectancy
 * - Computes 95% confidence intervals
 * - Determines year-specific sample sizes
 * 
 * Output Fields:
 * - Year: Reference year
 * - avg_life_exp: Mean life expectancy
 * - ci_lower, ci_upper: 95% confidence interval bounds
 * - standard_deviation: Year-specific variability
 * - country_count: Number of countries per year
 ******************************************************************************/
WITH YearlyStats AS (
    -- Group by year to analyze temporal patterns
    SELECT 
        Year,
        COUNT(*) as country_count,                   -- Number of countries per year
        -- Cast to DECIMAL for precise average calculation
        AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))) as avg_life_exp,
        -- Calculate standard deviation for confidence intervals
        STDDEV(CAST(Lifeexpectancy AS DECIMAL(5,1))) as stddev_life_exp,
        -- Count only valid records for accurate sample size
        COUNT(CASE WHEN Lifeexpectancy IS NOT NULL THEN 1 END) as valid_records
    FROM worldlifexpectancy
    GROUP BY Year
)
SELECT 
    Year,
    avg_life_exp,
    -- Calculate 95% confidence intervals
    avg_life_exp - (1.96 * stddev_life_exp / SQRT(valid_records)) as ci_lower,
    avg_life_exp + (1.96 * stddev_life_exp / SQRT(valid_records)) as ci_upper,
    stddev_life_exp as standard_deviation,
    country_count
FROM YearlyStats
ORDER BY Year;

-- =============================================================================
-- SECTION 3: DEVELOPMENT STATUS ANALYSIS
-- =============================================================================
-- Purpose: Compare metrics across development categories
-- Dependencies: Standardized Status values
-- Expected Runtime: 1-2 minutes
-- Statistical Methods: Z-scores, significance testing
-- 
-- RESULTS SUMMARY:
-- -----------------------------------------------------------------------------
-- Developed Countries (n=32):
-- - Average Life Expectancy: 79.20 years
-- - GDP: $19,334.54
-- - Adult Mortality: 79.81 per 1000
-- - Average Schooling: 14.39 years
-- - Z-score: 0.99 (Not statistically significant)
--
-- Developing Countries (n=161):
-- - Average Life Expectancy: 66.84 years
-- - GDP: $3,613.99
-- - Adult Mortality: 182.69 per 1000
-- - Average Schooling: 10.69 years
-- - Z-score: -0.21 (Not statistically significant)
--
-- Key Findings:
-- - 12.36 year gap in life expectancy between developed and developing nations
-- - 5x higher GDP in developed countries
-- - 2.3x higher mortality rate in developing countries
-- - 3.7 year education gap
-- -----------------------------------------------------------------------------

/*******************************************************************************
 * Purpose: Compare life expectancy across development status with significance testing
 * 
 * Methodology:
 * - Groups countries by development status
 * - Calculates key statistical measures
 * - Performs z-score based significance testing
 * - Evaluates economic indicators
 * 
 * Output Fields:
 * - Status: Development category
 * - country_count: Countries per category
 * - avg_life_exp: Mean life expectancy
 * - Economic indicators: GDP, mortality, schooling
 * - z_score: Standard deviations from global mean
 * - significance_level: Statistical significance indicator
 ******************************************************************************/
WITH StatusComparison AS (
    SELECT 
        Status,
        -- Count distinct countries to avoid duplicate counting
        COUNT(DISTINCT Country) as country_count,
        -- Calculate average life expectancy with proper decimal casting
        AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))) as avg_life_exp,
        -- Standard deviation for significance testing
        STDDEV(CAST(Lifeexpectancy AS DECIMAL(5,1))) as stddev_life_exp,
        -- Calculate key economic indicators
        AVG(GDP) as avg_gdp,                        -- Average GDP per status
        AVG(AdultMortality) as avg_mortality,       -- Average mortality rate
        AVG(Schooling) as avg_schooling,            -- Average years of schooling
        -- Z-score calculation using subqueries for global metrics
        (AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))) - 
         (SELECT AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))) FROM worldlifexpectancy)) /
        (SELECT STDDEV(CAST(Lifeexpectancy AS DECIMAL(5,1))) FROM worldlifexpectancy) as z_score
    FROM worldlifexpectancy
    WHERE Status != 'Unknown'                        -- Exclude unknown status
    GROUP BY Status
)
SELECT 
    *,
    -- Calculate p-value from z-score (simplified approximation)
    CASE 
        WHEN ABS(z_score) > 2.576 THEN 'p < 0.01'
        WHEN ABS(z_score) > 1.96 THEN 'p < 0.05'
        ELSE 'Not significant'
    END as significance_level
FROM StatusComparison;

-- =============================================================================
-- SECTION 4: CORRELATION ANALYSIS
-- =============================================================================
-- Purpose: Identify relationships between key variables
-- Dependencies: Numeric columns (GDP, mortality, etc.)
-- Expected Runtime: 2-3 minutes
-- Statistical Methods: Pearson correlation coefficients
-- 
-- RESULTS SUMMARY:
-- -----------------------------------------------------------------------------
-- Correlations with Life Expectancy:
-- 
-- Strong Negative:
-- - None
--
-- Moderate Positive:
-- - Schooling (r = 0.5615)
-- - BMI (r = 0.4976)
-- - GDP (r = 0.4040)
--
-- Moderate Negative:
-- - Adult Mortality (r = -0.6962)
-- - HIV/AIDS (r = -0.5051)
--
-- Weak:
-- - Infant Deaths (r = -0.1749)
--
-- Key Findings:
-- - Adult mortality shows strongest correlation
-- - All health and education indicators show meaningful relationships
-- - Economic factors (GDP) show moderate positive impact
-- - Infant deaths show surprisingly weak correlation
-- -----------------------------------------------------------------------------

/*******************************************************************************
 * Purpose: Quantify relationships between life expectancy and key indicators
 * 
 * Methodology:
 * - Calculates Pearson correlation coefficients
 * - Evaluates correlation strength
 * - Handles missing values appropriately
 * 
 * Output Fields:
 * - metric: Indicator being correlated
 * - correlation_coefficient: Pearson's r value
 * - correlation_strength: Qualitative strength indicator
 * - correlation_direction: Positive or Negative correlation
 * 
 * Correlation Interpretation:
 * - Strong: |r| > 0.7
 * - Moderate: 0.3 < |r| <= 0.7
 * - Weak: |r| <= 0.3
 ******************************************************************************/
WITH CorrelationMetrics AS (
    -- GDP Correlation
    SELECT 
        'GDP' as metric,
        -- Pearson correlation formula implementation
        (
            COUNT(*) * SUM(Lifeexpectancy * GDP) - SUM(Lifeexpectancy) * SUM(GDP)
        ) / SQRT(
            (COUNT(*) * SUM(Lifeexpectancy * Lifeexpectancy) - POW(SUM(Lifeexpectancy), 2)) *
            (COUNT(*) * SUM(GDP * GDP) - POW(SUM(GDP), 2))
        ) as correlation_coefficient
    FROM worldlifexpectancy
    WHERE Lifeexpectancy IS NOT NULL AND GDP IS NOT NULL

    UNION ALL

    -- Adult Mortality Correlation
    SELECT 
        'Adult Mortality' as metric,
        (
            COUNT(*) * SUM(Lifeexpectancy * AdultMortality) - SUM(Lifeexpectancy) * SUM(AdultMortality)
        ) / SQRT(
            (COUNT(*) * SUM(Lifeexpectancy * Lifeexpectancy) - POW(SUM(Lifeexpectancy), 2)) *
            (COUNT(*) * SUM(AdultMortality * AdultMortality) - POW(SUM(AdultMortality), 2))
        ) as correlation_coefficient
    FROM worldlifexpectancy
    WHERE Lifeexpectancy IS NOT NULL AND AdultMortality IS NOT NULL

    UNION ALL

    -- BMI Correlation
    SELECT 
        'BMI' as metric,
        (
            COUNT(*) * SUM(Lifeexpectancy * BMI) - SUM(Lifeexpectancy) * SUM(BMI)
        ) / SQRT(
            (COUNT(*) * SUM(Lifeexpectancy * Lifeexpectancy) - POW(SUM(Lifeexpectancy), 2)) *
            (COUNT(*) * SUM(BMI * BMI) - POW(SUM(BMI), 2))
        ) as correlation_coefficient
    FROM worldlifexpectancy
    WHERE Lifeexpectancy IS NOT NULL AND BMI IS NOT NULL

    UNION ALL

    -- Schooling Correlation
    SELECT 
        'Schooling' as metric,
        (
            COUNT(*) * SUM(Lifeexpectancy * Schooling) - SUM(Lifeexpectancy) * SUM(Schooling)
        ) / SQRT(
            (COUNT(*) * SUM(Lifeexpectancy * Lifeexpectancy) - POW(SUM(Lifeexpectancy), 2)) *
            (COUNT(*) * SUM(Schooling * Schooling) - POW(SUM(Schooling), 2))
        ) as correlation_coefficient
    FROM worldlifexpectancy
    WHERE Lifeexpectancy IS NOT NULL AND Schooling IS NOT NULL

    UNION ALL

    -- HIV/AIDS Correlation
    SELECT 
        'HIV/AIDS' as metric,
        (
            COUNT(*) * SUM(Lifeexpectancy * HIVAIDS) - SUM(Lifeexpectancy) * SUM(HIVAIDS)
        ) / SQRT(
            (COUNT(*) * SUM(Lifeexpectancy * Lifeexpectancy) - POW(SUM(Lifeexpectancy), 2)) *
            (COUNT(*) * SUM(HIVAIDS * HIVAIDS) - POW(SUM(HIVAIDS), 2))
        ) as correlation_coefficient
    FROM worldlifexpectancy
    WHERE Lifeexpectancy IS NOT NULL AND HIVAIDS IS NOT NULL

    UNION ALL

    -- Infant Deaths Correlation
    SELECT 
        'Infant Deaths' as metric,
        (
            COUNT(*) * SUM(Lifeexpectancy * infantdeaths) - SUM(Lifeexpectancy) * SUM(infantdeaths)
        ) / SQRT(
            (COUNT(*) * SUM(Lifeexpectancy * Lifeexpectancy) - POW(SUM(Lifeexpectancy), 2)) *
            (COUNT(*) * SUM(infantdeaths * infantdeaths) - POW(SUM(infantdeaths), 2))
        ) as correlation_coefficient
    FROM worldlifexpectancy
    WHERE Lifeexpectancy IS NOT NULL AND infantdeaths IS NOT NULL
)
SELECT 
    metric,
    ROUND(correlation_coefficient, 4) as correlation_coefficient,
    -- Determine correlation strength
    CASE 
        WHEN ABS(correlation_coefficient) > 0.7 THEN 'Strong'
        WHEN ABS(correlation_coefficient) > 0.3 THEN 'Moderate'
        ELSE 'Weak'
    END as correlation_strength,
    -- Add correlation direction
    CASE 
        WHEN correlation_coefficient > 0 THEN 'Positive'
        ELSE 'Negative'
    END as correlation_direction
FROM CorrelationMetrics
ORDER BY ABS(correlation_coefficient) DESC;

-- =============================================================================
-- SECTION 5: GEOGRAPHIC ANALYSIS AND OUTLIERS
-- =============================================================================
-- Purpose: Detect spatial patterns and anomalous values
-- Dependencies: Country-level aggregates
-- Expected Runtime: 1-2 minutes
-- Statistical Methods: Z-scores, standard deviations
-- 
-- RESULTS SUMMARY:
-- -----------------------------------------------------------------------------
-- Outlier Analysis:
-- 
-- Significant Low Outliers (z < -2):
-- - 10 countries with zero life expectancy (z = -6.68)
--   * Cook Islands, Dominica, Marshall Islands, Monaco, etc.
-- - Sierra Leone: 46.11 years (z = -2.22)
--
-- Notable Low Values (Not Outliers):
-- - Central African Republic: 48.51 years
-- - Lesotho: 48.78 years
-- - Angola: 49.02 years
-- - Average for bottom 10: 48.87 years
--
-- Highest Life Expectancy:
-- - Japan: 82.54 years
-- - Sweden: 82.52 years
-- - Iceland: 82.44 years
-- - Average for top 10: 81.95 years
--
-- Key Findings:
-- - 11 total statistical outliers identified
-- - 33.7 year gap between highest and lowest (excluding zeros)
-- - Developed nations cluster above 80 years
-- - Most developing nations fall between 65-75 years
-- -----------------------------------------------------------------------------

/*******************************************************************************
 * Purpose: Identify geographic patterns and anomalous countries
 * 
 * Methodology:
 * - Calculates country-level statistics
 * - Performs z-score based outlier detection
 * - Evaluates life expectancy volatility
 * 
 * Output Fields:
 * - Country: Nation identifier
 * - Status: Development category
 * - avg_life_exp: Mean life expectancy
 * - life_exp_volatility: Standard deviation of life expectancy
 * - z_score: Standard deviations from global mean
 * - outlier_status: Binary outlier indicator
 ******************************************************************************/
WITH CountryMetrics AS (
    SELECT 
        Country,
        Status,
        -- Calculate average life expectancy per country
        AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))) as avg_life_exp,
        -- Measure of variability within each country
        STDDEV(CAST(Lifeexpectancy AS DECIMAL(5,1))) as life_exp_volatility,
        -- Z-score calculation for outlier detection
        -- Compare country average to global average
        (AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))) - 
         (SELECT AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))) FROM worldlifexpectancy)) /
        (SELECT STDDEV(CAST(Lifeexpectancy AS DECIMAL(5,1))) FROM worldlifexpectancy) as z_score
    FROM worldlifexpectancy
    GROUP BY Country, Status
)
SELECT 
    Country,
    Status,
    avg_life_exp,
    life_exp_volatility,
    z_score,
    CASE 
        WHEN ABS(z_score) > 2 THEN 'Outlier'
        ELSE 'Normal'
    END as outlier_status
FROM CountryMetrics
ORDER BY ABS(z_score) DESC;

-- =============================================================================
-- SECTION 6: TIME SERIES DECOMPOSITION
-- =============================================================================
-- Purpose: Analyze temporal components and growth patterns
-- Dependencies: Sequential yearly data
-- Expected Runtime: 1-2 minutes
-- Statistical Methods: Moving averages, growth rates
-- 
-- RESULTS SUMMARY:
-- -----------------------------------------------------------------------------
-- Growth Phases:
-- 1. Initial Growth (2007-2010):
--    - Starting: 66.75 years
--    - Modest annual growth: 0.33-0.57%
--    - Stable moving average: ~67.2 years
--
-- 2. Acceleration (2011-2019):
--    - Consistent yearly improvements
--    - Peak growth in 2018 (0.91%)
--    - Moving average reached 70.15 years
--
-- 3. COVID-19 Impact (2020):
--    - Sharp decline to 67.55 years
--    - -4.75% year-over-year drop
--    - Largest single-year change
--
-- 4. Recovery (2021-2022):
--    - Strong rebound to 71.54 years (5.91% growth)
--    - Stabilization at 71.62 years in 2022
--    - Moving average recovery to 70.23 years
--
-- Overall Trends:
-- - Net improvement: 4.87 years (7.3% total increase)
-- - Average annual growth: 0.42% (excluding 2020-2021)
-- - Moving average shows consistent upward trend
-- -----------------------------------------------------------------------------

/*******************************************************************************
 * Purpose: Analyze temporal patterns and growth rates
 * 
 * Methodology:
 * - Calculates yearly averages
 * - Computes 5-year moving averages
 * - Determines year-over-year growth rates
 * 
 * Output Fields:
 * - Year: Reference year
 * - avg_life_exp: Mean life expectancy
 * - moving_avg_5year: 5-year centered moving average
 * - yoy_growth_percent: Year-over-year percentage change
 ******************************************************************************/
WITH YearlyTrends AS (
    SELECT 
        Year,
        -- Base calculation for life expectancy
        AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))) as avg_life_exp,
        -- 5-year centered moving average using window function
        -- 2 years before and 2 years after current year
        AVG(AVG(CAST(Lifeexpectancy AS DECIMAL(5,1)))) OVER (
            ORDER BY Year
            ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING
        ) as moving_avg_5year,
        -- Year-over-year growth calculation using LAG
        -- Compare current year to previous year
        (AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))) - 
         LAG(AVG(CAST(Lifeexpectancy AS DECIMAL(5,1)))) OVER (ORDER BY Year)) /
         LAG(AVG(CAST(Lifeexpectancy AS DECIMAL(5,1)))) OVER (ORDER BY Year) * 100 as yoy_growth
    FROM worldlifexpectancy
    GROUP BY Year
)
SELECT 
    Year,
    ROUND(avg_life_exp, 2) as avg_life_exp,
    ROUND(moving_avg_5year, 2) as moving_avg_5year,
    ROUND(yoy_growth, 2) as yoy_growth_percent
FROM YearlyTrends
ORDER BY Year;

-- =============================================================================
-- SECTION 7: MULTIVARIATE ANALYSIS
-- =============================================================================
-- Purpose: Examine relationships between multiple variables
-- Dependencies: Multiple numeric indicators
-- Expected Runtime: 1-2 minutes
-- Statistical Methods: Composite scoring, weighted averages
-- 
-- RESULTS SUMMARY:
-- -----------------------------------------------------------------------------
-- Developed Nations (n=511):
-- Health Metrics:
--   - Life Expectancy: 79.20 years
--   - Adult Mortality: 79.81 per 1000
--   - BMI: 51.77
-- Economic & Social:
--   - GDP: $19,334.54
--   - Schooling: 14.39 years
-- Development Score: 82.87
--
-- Developing Nations (n=2,419):
-- Health Metrics:
--   - Life Expectancy: 66.84 years
--   - Adult Mortality: 182.69 per 1000
--   - BMI: 35.44
-- Economic & Social:
--   - GDP: $3,614.00
--   - Schooling: 10.69 years
-- Development Score: 67.35
--
-- Key Disparities:
-- - 15.52 point gap in development scores
-- - 5.3x difference in GDP
-- - 2.3x difference in mortality rates
-- - 3.7 year gap in education
-- - 16.33 point difference in BMI
-- -----------------------------------------------------------------------------

/*******************************************************************************
 * Purpose: Evaluate relationships between multiple variables
 * 
 * Methodology:
 * - Groups by development status
 * - Calculates multiple health and economic indicators
 * - Computes composite development score
 * 
 * Output Fields:
 * - Status: Development category
 * - Multiple averages: life_exp, gdp, mortality, schooling, bmi
 * - record_count: Observations per category
 * - development_score: Weighted composite indicator
 * 
 * Development Score Components:
 * - Life expectancy (40% weight)
 * - GDP (30% weight)
 * - Schooling (30% weight)
 ******************************************************************************/
WITH MultivariateMetrics AS (
    SELECT 
        Status,
        -- Round averages for cleaner output
        ROUND(AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))), 2) as avg_life_exp,
        ROUND(AVG(GDP), 2) as avg_gdp,              -- Economic indicator
        ROUND(AVG(AdultMortality), 2) as avg_mortality,  -- Health indicator
        ROUND(AVG(Schooling), 2) as avg_schooling,  -- Education indicator
        ROUND(AVG(BMI), 2) as avg_bmi,             -- Health indicator
        COUNT(*) as record_count                    -- Sample size
    FROM worldlifexpectancy
    WHERE Status != 'Unknown'
    GROUP BY Status
)
SELECT 
    *,
    -- Calculate composite score
    ROUND((avg_life_exp / 100 * 0.4 + 
           LOG(avg_gdp) / 10 * 0.3 + 
           avg_schooling / 20 * 0.3) * 100, 2) as development_score
FROM MultivariateMetrics;

-- =============================================================================
-- SECTION 8: QUALITY METRICS TRACKING
-- =============================================================================
-- Purpose: Monitor data quality trends across time
-- Dependencies: data_quality_score column
-- Expected Runtime: < 1 minute
-- Output Metrics: Quality scores, completion rates
-- 
-- RESULTS SUMMARY:
-- -----------------------------------------------------------------------------
-- Overall Quality Trends:
-- - Average quality score range: 91.50 - 94.21
-- - Lowest score: 2020 (91.50, COVID-19 impact year)
-- - Highest score: 2009 (94.21)
-- - Most recent score (2022): 93.77
--
-- Sample Size:
-- - Consistent 183 records per year (2007-2019, 2021-2022)
-- - Exception: 2020 with 193 records
--
-- High-Quality Records (score >= 80):
-- - Minimum: 166 records (2007, 90.71%)
-- - Maximum: 176 records (2020, 91.19%)
-- - Latest: 173 records (2022, 94.54%)
--
-- Historical Data:
-- Year  Avg Score  Records  High Quality  Quality %
-- 2007    92.79      183        166        90.71
-- 2008    94.10      183        170        92.90
-- 2009    94.21      183        169        92.35
-- 2010    93.88      183        169        92.35
-- 2011    93.88      183        169        92.35
-- 2012    93.01      183        171        93.44
-- 2013    93.88      183        171        93.44
-- 2014    93.11      183        171        93.44
-- 2015    93.55      183        170        92.90
-- 2016    93.88      183        170        92.90
-- 2017    93.01      183        171        93.44
-- 2018    93.44      183        172        93.99
-- 2019    93.33      183        171        93.44
-- 2020    91.50      193        176        91.19
-- 2021    93.33      183        171        93.44
-- 2022    93.77      183        173        94.54
-- -----------------------------------------------------------------------------

/*******************************************************************************
 * Purpose: Monitor data quality trends across years
 * 
 * Methodology:
 * - Groups quality metrics by year
 * - Calculates quality statistics
 * - Tracks high-quality record proportions
 * 
 * Output Fields:
 * - Year: Reference year
 * - avg_quality_score: Mean quality score
 * - total_records: Records per year
 * - high_quality_records: Records with score >= 80
 * - quality_percentage: Proportion of high-quality records
 ******************************************************************************/
SELECT 
    Year,
    ROUND(AVG(data_quality_score), 2) as avg_quality_score,
    COUNT(*) as total_records,
    SUM(CASE WHEN data_quality_score >= 80 THEN 1 ELSE 0 END) as high_quality_records,
    ROUND(100.0 * SUM(CASE WHEN data_quality_score >= 80 THEN 1 ELSE 0 END) / COUNT(*), 2) as quality_percentage
FROM worldlifexpectancy
GROUP BY Year
ORDER BY Year;