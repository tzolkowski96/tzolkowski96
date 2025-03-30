# US Household Income Analysis

<div align="center">

![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Advanced-success?style=for-the-badge)
![Data Quality](https://img.shields.io/badge/Data%20Quality-9.62/10-blue?style=for-the-badge)

</div>

> *Uncovering America's economic divides through data*

## Table of Contents

- [Overview](#overview)
- [Key Findings](#key-findings)
- [The Data Story](#the-data-story)
- [Technical Approach](#technical-approach)
  - [Data Cleaning Journey](#data-cleaning-journey)
  - [Analysis Techniques](#analysis-techniques)
- [Visualizing the Results](#visualizing-the-results)
  - [Regional Economic Divides](#regional-economic-divides)
  - [Income Distribution Patterns](#income-distribution-patterns)
  - [Inequality Insights](#inequality-insights)
- [Code Highlights](#code-highlights)
  - [Text Standardization Magic](#text-standardization-magic)
  - [Geographic Validation](#geographic-validation)
  - [Weighted Quality Scoring](#weighted-quality-scoring)
- [Database Architecture](#database-architecture)
- [Working with This Analysis](#working-with-this-analysis)
  - [Installation](#installation)
  - [Analytical Views](#analytical-views)
  - [Troubleshooting Tips](#troubleshooting-tips)
- [Behind the Numbers](#behind-the-numbers)
- [Technical Achievements](#technical-achievements)
- [Conclusion](#conclusion)
- [License](#license)
- [About the Author](#about-the-author)

## Overview

Ever wondered how income varies across America? I embarked on a data expedition through 32,533 US locations to uncover the economic story behind the numbers. Using MySQL 8.0+, I transformed messy geographical and income data into clear insights that reveal stark economic divides across US regions.

<div align="center">
<img src="https://images.unsplash.com/photo-1605231420144-cf322b457f85?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" alt="US Economic Landscape" width="750"/>
</div>

This project showcases both the technical skill of advanced SQL and the human impact of economic geography – demonstrating how data can illuminate real-world disparities that affect millions of Americans.

## Key Findings

<div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">

### 🏙️ Geographic Divides

The data reveals a striking 30% income gap between regions:

- **Northeast**: $102,068 median income (highest)
- **West**: $96,742 median income
- **Midwest**: $83,405 median income
- **Southwest**: $77,494 median income
- **Southeast**: $71,307 median income (lowest)

This coastal-to-interior prosperity gradient tells a story of two Americas – one thriving along the coasts and another struggling in between.

### 💰 Income Distribution Realities

- **National median household income**: $85,453
- **True 50th percentile**: $51,871 (when calculated directly from data)
- **Income ceiling effect**: Values capped at $300,000, affecting top 10% of records
- **Significant dispersion**: $87,810 standard deviation shows extreme variation

### ⚖️ Inequality Metrics

Some communities show alarming wealth concentration:
- **Extreme cases**: Mean-to-median ratios exceeding 3.65 (Alaska)
- **High inequality**: Mean income > 1.5× median income in 15% of locations
- **Wealth concentration**: Data suggests small percentages of high earners pull averages up dramatically

</div>

## The Data Story

When I first examined this dataset, I was struck by how much a simple ZIP code can tell us about economic opportunity in America. What started as rows and columns of numbers quickly transformed into a revealing portrait of regional prosperity and struggle.

The dataset contained nearly pristine geographic data (just one missing value!), but required careful standardization and validation. I discovered:

- City names needed consistent capitalization (26% of records)
- State names required standardization (18% of records)
- ZIP codes had validation issues (8.5% of records)
- Geographic coordinates occasionally placed locations in oceans or other countries (1.9% of records)

Beyond cleanup, the most fascinating discovery was in the income ceiling effect. The data seemed to "give up" at $300,000, suggesting that the highest incomes simply got grouped together. This ceiling affects our understanding of true inequality, as the gap between middle and upper incomes is likely even greater than the data shows.

## Technical Approach

My approach combined methodical data engineering with statistical insight to transform raw data into meaningful economic geography.

### Data Cleaning Journey

I built a systematic 12-step process to transform raw data into analysis-ready information:

1. **Error Handling Setup**: Created logging infrastructure to track every operation
2. **Initial Data Inspection**: Examined data structure and spotted potential quality issues
3. **Missing Value Handling**: Found and fixed just one missing Place value (0.003% of data!)
4. **Data Standardization**: Normalized text fields for consistent city and state names
5. **Duplicate Removal**: Identified potential duplicates using location identifiers
6. **Text Cleaning**: Created a smart text standardization procedure that handled multi-word cities
7. **Geographic Validation**: Added flags for invalid ZIP codes and coordinates rather than deleting records
8. **Outlier Detection**: Used standard deviation method to identify statistical anomalies
9. **Analysis Views**: Created optimized views for three different analytical perspectives
10. **Quality Reporting**: Built a weighted quality scoring system (9.62/10 final score)
11. **Statistical Analysis**: Generated distribution statistics, percentiles, and regional comparisons
12. **Optimization**: Added helper procedures and functions for code efficiency

### Analysis Techniques

The analysis leveraged several advanced SQL approaches:

<div style="display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 20px;">

<div style="flex: 1; min-width: 250px; background-color: #f0f8ff; padding: 15px; border-radius: 8px;">
<h4>Window Functions</h4>
<p>Used <code>DENSE_RANK()</code>, <code>ROW_NUMBER()</code>, and <code>OVER()</code> clauses to calculate percentiles and ranked inequality metrics without multiple table scans.</p>
</div>

<div style="flex: 1; min-width: 250px; background-color: #f0f8ff; padding: 15px; border-radius: 8px;">
<h4>Common Table Expressions</h4>
<p>Implemented CTEs for multi-stage analyses, like income percentile calculations that required ordering data before processing.</p>
</div>

<div style="flex: 1; min-width: 250px; background-color: #f0f8ff; padding: 15px; border-radius: 8px;">
<h4>Dynamic SQL</h4>
<p>Created flexible data transformations using prepared statements and parameter substitution for reusable operations.</p>
</div>

<div style="flex: 1; min-width: 250px; background-color: #f0f8ff; padding: 15px; border-radius: 8px;">
<h4>Transaction Management</h4>
<p>Wrapped operations in transactions with savepoints to ensure data consistency and enable rollback if needed.</p>
</div>

</div>

## Visualizing the Results

### Regional Economic Divides

The regional income analysis revealed stark differences in prosperity:

<div align="center">
<img src="https://images.unsplash.com/photo-1682686580950-960d1d513532?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" alt="Regional Income Comparison" width="700"/>
</div>

| Region     | Location Count | Average Mean Income | Average Median Income |
|------------|----------------|---------------------|------------------------|
| Northeast  | 9              | $118,973.42         | $102,068.17            |
| West       | 11             | $107,982.53         | $96,741.82             |
| Midwest    | 12             | $84,627.29          | $83,405.26             |
| Southwest  | 4              | $82,354.18          | $77,493.61             |
| Southeast  | 12             | $74,968.11          | $71,307.15             |
| Other      | 3              | $89,271.63          | $78,125.92             |

The 30% gap between Northeast and Southeast regions represents thousands of dollars in economic opportunity difference for typical households.

### Income Distribution Patterns

Diving deeper into percentiles revealed how income is distributed across America:

| Analysis Type      | 25th Percentile | 50th Percentile | 75th Percentile | 90th Percentile |
|--------------------|-----------------|-----------------|-----------------|-----------------|
| Income Percentiles | $36,039         | $51,871         | $80,909         | $300,000        |

The jump from the 75th to 90th percentile shows a massive income acceleration at the top end, though the $300,000 ceiling masks the true extent of high-end incomes.

### Inequality Insights

Some states showed particularly striking inequality patterns:

| State      | Mean Income | Median Income | Inequality Ratio | Category              |
|------------|-------------|---------------|------------------|------------------------|
| Alaska     | $98,750     | $27,050       | 3.652            | High Income Inequality |
| New Mexico | $78,430     | $35,680       | 2.198            | High Income Inequality |
| California | $115,670    | $54,320       | 2.130            | High Income Inequality |
| Wyoming    | $87,990     | $42,650       | 2.063            | High Income Inequality |
| Texas      | $92,780     | $46,580       | 1.992            | High Income Inequality |

When mean income vastly exceeds median income, it indicates a small number of high earners pulling the average up while most households earn less.

## Code Highlights

### Text Standardization Magic

One of my favorite technical achievements was this elegant procedure that handles multi-word city name standardization:

```sql
CREATE PROCEDURE standardize_text_field(
    IN p_table_name VARCHAR(100),
    IN p_column_name VARCHAR(100),
    IN p_where_clause VARCHAR(255)
)
BEGIN
    DECLARE where_condition VARCHAR(300);
    DECLARE affected_rows_count INT DEFAULT 0;
    
    -- Set default WHERE clause if not provided
    IF p_where_clause IS NULL OR p_where_clause = '' THEN
        SET where_condition = '';
    ELSE
        SET where_condition = CONCAT(' WHERE ', p_where_clause);
    END IF;
    
    -- First letter uppercase, rest lowercase
    SET @sql = CONCAT('UPDATE ', p_table_name, 
                    ' SET ', p_column_name, ' = CONCAT(UPPER(SUBSTRING(', p_column_name, ', 1, 1)), ',
                    'LOWER(SUBSTRING(', p_column_name, ', 2)))', 
                    where_condition);
    
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    SET affected_rows_count = ROW_COUNT();
    DEALLOCATE PREPARE stmt;
    
    -- For multi-word cities, handle each word separately
    IF p_where_clause IS NULL OR p_where_clause = '' THEN
        SET @sql = CONCAT('UPDATE ', p_table_name, 
                      ' SET ', p_column_name, ' = CONCAT(', 
                      'UPPER(SUBSTRING(SUBSTRING_INDEX(', p_column_name, ', '' '', 1), 1, 1)), ',
                      'LOWER(SUBSTRING(SUBSTRING_INDEX(', p_column_name, ', '' '', 1), 2)), ',
                      ''' '', ',
                      'UPPER(SUBSTRING(SUBSTRING_INDEX(', p_column_name, ', '' '', -1), 1, 1)), ',
                      'LOWER(SUBSTRING(SUBSTRING_INDEX(', p_column_name, ', '' '', -1), 2))) ',
                      'WHERE ', p_column_name, ' LIKE ''% %''');
    ELSE
        -- Add custom WHERE clause if provided
        SET @sql = CONCAT('UPDATE ', p_table_name, 
                      ' SET ', p_column_name, ' = CONCAT(', 
                      'UPPER(SUBSTRING(SUBSTRING_INDEX(', p_column_name, ', '' '', 1), 1, 1)), ',
                      'LOWER(SUBSTRING(SUBSTRING_INDEX(', p_column_name, ', '' '', 1), 2)), ',
                      ''' '', ',
                      'UPPER(SUBSTRING(SUBSTRING_INDEX(', p_column_name, ', '' '', -1), 1, 1)), ',
                      'LOWER(SUBSTRING(SUBSTRING_INDEX(', p_column_name, ', '' '', -1), 2))) ',
                      'WHERE ', p_where_clause, ' AND ', p_column_name, ' LIKE ''% %''');
    END IF;
    
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    SET affected_rows_count = affected_rows_count + ROW_COUNT();
    DEALLOCATE PREPARE stmt;
    
    -- Log the standardization
    INSERT INTO error_log (error_section, error_message, affected_rows)
    VALUES ('Text Standardization', CONCAT('Standardized ', p_column_name, ' in ', p_table_name), affected_rows_count);
END
```

This procedure transformed inconsistent entries like "new york" and "NEW YORK" to properly formatted "New York" for consistent analysis.

### Geographic Validation

Instead of simply removing records with questionable geographic data, I implemented a flagging system:

```sql
-- Flag invalid zip codes (not 5 digits)
ALTER TABLE USHouseholdIncome_Clean
ADD COLUMN invalid_zip_code BOOLEAN DEFAULT FALSE;

UPDATE USHouseholdIncome_Clean
SET invalid_zip_code = TRUE
WHERE Zip_Code < 10000 OR Zip_Code > 99999;

-- Flag potentially invalid latitude/longitude
ALTER TABLE USHouseholdIncome_Clean
ADD COLUMN invalid_coordinates BOOLEAN DEFAULT FALSE;

UPDATE USHouseholdIncome_Clean
SET invalid_coordinates = TRUE
WHERE Lat < 24 OR Lat > 50    -- Continental US latitude boundaries
   OR Lon < -125 OR Lon > -66;  -- Continental US longitude boundaries
```

This approach preserved all data while allowing analytical views to filter appropriately.

### Weighted Quality Scoring

I developed a nuanced quality assessment that weighted different factors based on their importance:

```sql
SELECT
    'Enhanced Data Quality Score' AS metric,
    ROUND((
        -- Place quality (25% weight)
        (1 - (@missing_place / @total_records)) * 25 +
        -- ZIP quality (35% weight)
        (1 - (@invalid_zip / @total_clean)) * 35 +
        -- Coordinate quality (40% weight)
        (1 - (@invalid_coords / @total_clean)) * 40
    ) / 10, 2) AS score_out_of_10
```

This produced a final quality score of 9.62/10, reflecting the high quality of the cleaned dataset.

## Database Architecture

The database design connected geographic location data with income statistics through carefully designed tables and views:

```
USHouseholdIncome (Original)
↓
USHouseholdIncome_Clean (Cleaned data with validation flags)
↓
Three analytical views:
  ↳ v_income_by_location (Location-specific income analysis)
  ↳ v_income_by_state (State-level aggregation with counts)
  ↳ v_income_inequality_metrics (Income distribution patterns)
```

Additionally, I created support tables:
- `error_log`: Tracked all data modifications
- `duplicate_records_log`: Documented potential data duplication

## Working with This Analysis

### Installation

Getting started with this analysis is straightforward:

1. **Set up your environment**:
   ```sql
   CREATE DATABASE us_income_analysis;
   USE us_income_analysis;
   ```

2. **Import source tables**:
   - `USHouseholdIncome`: Location data
   - `ushouseholdincome_statistics`: Income statistics

3. **Run the script**:
   ```
   SOURCE us_household_income_cleaning_analysis.sql;
   ```

### Analytical Views

I've created three ready-to-use views that make exploring insights easy:

**1. Location-specific income data**:
```sql
SELECT * FROM v_income_by_location 
WHERE State_Name = 'New York' 
ORDER BY Median_Income DESC 
LIMIT 10;
```

Results:

| id | State_Name | County      | City        | Zip_Code | Lat      | Lon       | Mean_Income | Median_Income | Income_StdDev |
|----|------------|-------------|-------------|----------|----------|-----------|-------------|---------------|---------------|
| 42 | New York   | Westchester | Scarsdale   | 10583    | 41.00454 | -73.78736 | 250000      | 300000        | 152000        |
| 57 | New York   | Nassau      | Brookville  | 11545    | 40.81927 | -73.56223 | 250000      | 300000        | 147500        |
| 61 | New York   | Nassau      | Manhasset   | 11030    | 40.79371 | -73.70122 | 225600      | 300000        | 134890        |
| 68 | New York   | Nassau      | Old Westbury| 11568    | 40.77649 | -73.59818 | 240400      | 300000        | 132750        |
| 72 | New York   | Nassau      | Oyster Bay  | 11771    | 40.77205 | -73.50234 | 230100      | 300000        | 145780        |

**2. State-level comparison**:
```sql
SELECT * FROM v_income_by_state
ORDER BY Mean_Income DESC
LIMIT 5;
```

Results:

| State_Name     | State_ab | Mean_Income | Median_Income | County_Count | City_Count |
|----------------|----------|-------------|---------------|--------------|------------|
| Connecticut    | CT       | 135790      | 115400        | 8            | 169        |
| District of Columbia | DC | 130200      | 108600        | 1            | 18         |
| New Jersey     | NJ       | 129450      | 111300        | 21           | 565        |
| Massachusetts  | MA       | 124850      | 106500        | 14           | 351        |
| New York       | NY       | 120620      | 103200        | 62           | 998        |

**3. Income inequality insights**:
```sql
SELECT * FROM v_income_inequality_metrics
WHERE income_inequality_category = 'High Income Inequality'
ORDER BY income_inequality_ratio DESC
LIMIT 5;
```

Results:

| State_Name | Mean   | Median | Stdev  | income_inequality_ratio | income_inequality_category | inequality_rank |
|------------|--------|--------|--------|-------------------------|----------------------------|----------------|
| Alaska     | 98750  | 27050  | 56430  | 3.652                   | High Income Inequality     | 1              |
| New Mexico | 78430  | 35680  | 49870  | 2.198                   | High Income Inequality     | 5              |
| California | 115670 | 54320  | 62340  | 2.130                   | High Income Inequality     | 8              |
| Wyoming    | 87990  | 42650  | 48820  | 2.063                   | High Income Inequality     | 11             |
| Texas      | 92780  | 46580  | 53470  | 1.992                   | High Income Inequality     | 12             |

### Troubleshooting Tips

During my development process, I encountered and solved several common issues:

<div style="background-color: #fff8f0; padding: 15px; border-radius: 8px; margin: 15px 0;">

#### "Table already exists" errors

When re-running the script, you might see errors about existing tables.

**Solution**: Add these lines to the beginning of your script:
```sql
DROP TABLE IF EXISTS USHouseholdIncome_Clean;
DROP TABLE IF EXISTS error_log;
DROP TABLE IF EXISTS duplicate_records_log;
```

#### Performance timeouts with large queries

Some complex joins might time out with large datasets.

**Solution**: Add strategic indexes and limit results:
```sql
-- Create indexes for faster joins
CREATE INDEX idx_state_name ON USHouseholdIncome_Clean(State_Name);
CREATE INDEX idx_income ON ushouseholdincome_statistics(Median);

-- Limit large result sets
SELECT ... FROM big_table LIMIT 1000;
```

#### SQL mode compatibility issues

You might encounter timestamp default value errors with certain SQL modes.

**Solution**: Check your SQL mode and adjust table creation:
```sql
-- Check SQL mode
SELECT @@sql_mode;

-- Modify error_log table creation
CREATE TABLE IF NOT EXISTS error_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    error_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- other columns
);
```

</div>

## Behind the Numbers

The numbers tell a fascinating story about modern America:

**The Coastal Premium**: The Northeast and West regions command significantly higher incomes than interior regions. This 30% "coastal premium" reflects the concentration of high-paying industries, educational institutions, and economic opportunities in these areas.

**The Ceiling Effect**: The data's apparent $300,000 cap on high incomes affects our understanding of true wealth distribution. The 90th percentile hitting this cap suggests that what we're seeing is a censored view of America's highest earners.

**Income Inequality Hot Spots**: Some states show extreme income inequality ratios:
- **Alaska**: The 3.65 mean-to-median ratio reveals extreme wealth concentration, likely due to oil industry wealth contrasting with rural subsistence economies
- **California & New York**: These economic powerhouses show high inequality likely driven by tech and finance sectors creating tremendous wealth alongside service economy jobs

## Technical Achievements

This project demonstrates several technical achievements:

1. **Comprehensive Error Handling**: Built a robust tracking system that documented every data transformation with timestamp and impact metrics

2. **Advanced Text Processing**: Developed a parameterized procedure for text standardization that handled both single and multi-word cases

3. **Geographic Validation**: Implemented coordinate and ZIP code validation without data loss by using boolean flags

4. **Statistical Techniques**: Used window functions to calculate accurate percentiles (avoiding compatibility issues with `PERCENTILE_CONT`)

5. **Performance Optimization**: Added strategic indexing and created helper procedures to avoid redundant code

6. **Weighted Quality Assessment**: Created a nuanced data quality scoring system that prioritized more important data elements

7. **Data Preservation**: Employed a "flag, don't remove" strategy that preserved all original records while enabling filtering

## Conclusion

<div style="background-color: #f0f7ff; padding: 20px; border-radius: 8px; border-left: 5px solid #3173d8; margin: 20px 0;">

This project started as a technical exercise but revealed a profound economic story. The 30% income gap between Northeast and Southeast regions represents real differences in opportunity and prosperity for millions of Americans.

The data exposed not just regional divides but fascinating patterns of inequality within states. Places like Alaska, with its 3.65 inequality ratio, demonstrate how different economic forces can create vastly different realities even within the same state.

Beyond the numbers, this analysis showcases how robust data engineering can transform raw information into meaningful insights. The combination of SQL techniques—window functions, CTEs, dynamic SQL, transaction management—allowed for an enterprise-grade approach that maintained data integrity while extracting powerful economic patterns.

What began as 32,533 rows of data became a revealing portrait of America's economic geography, demonstrating both technical SQL mastery and the human impact of regional economic divides.

</div>

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 Tobin Zolkowski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## About the Author

<div style="background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin-top: 20px;">
  <div>
    <h3 style="margin: 0;">Tobin Zolkowski</h3>
    <p style="margin: 5px 0;">Data Analyst</p>
    <p style="margin: 5px 0; font-style: italic;">March 2025</p>
    <p style="margin: 5px 0;">I created this project to demonstrate how SQL can transform raw data into meaningful economic insights. By combining rigorous data cleaning with statistical analysis, I've shown how technical skills can illuminate real-world patterns that affect millions of people. This analysis is part of my data portfolio showcasing advanced SQL techniques in practical applications.</p>
  </div>
</div>