# World Life Expectancy Data Cleaning Project

## Overview
A comprehensive MySQL data cleaning and standardization project focused on global life expectancy statistics. This project demonstrates advanced SQL techniques for handling real-world data quality challenges while maintaining data integrity.

## Project Description
The project implements a robust data cleaning pipeline for the World Life Expectancy dataset, addressing common data quality issues such as duplicates, missing values, and inconsistent formats. The solution includes data validation, quality scoring, and performance optimization through proper indexing.

## Features
- Data backup and version control
- Duplicate record detection and removal
- Missing value interpolation
- Data standardization and validation
- Quality scoring system
- Performance optimization through indexing
- Statistical summary views

## Technical Implementation

### 1. Data Backup and Initialization
```sql
CREATE TABLE IF NOT EXISTS worldlifexpectancy_backup AS
SELECT * FROM worldlifexpectancy;
```

### 2. Duplicate Handling
```sql
WITH DuplicatesCTE AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY Country, Year
            ORDER BY 
                CASE WHEN Status != '' THEN 1 ELSE 2 END,
                CASE WHEN Lifeexpectancy != '' THEN 1 ELSE 2 END,
                CASE WHEN GDP > 0 THEN 1 ELSE 2 END,
                Row_ID
        ) as row_num
    FROM worldlifexpectancy
)
DELETE FROM worldlifexpectancy 
WHERE Row_ID IN (
    SELECT Row_ID 
    FROM DuplicatesCTE 
    WHERE row_num > 1
);
```

### 3. Data Quality Scoring
```sql
UPDATE worldlifexpectancy
SET data_quality_score = (
    CASE WHEN Lifeexpectancy IS NOT NULL THEN 20 ELSE 0 END +
    CASE WHEN AdultMortality IS NOT NULL AND AdultMortality > 0 THEN 20 ELSE 0 END +
    CASE WHEN GDP IS NOT NULL AND GDP > 0 THEN 20 ELSE 0 END +
    CASE WHEN BMI IS NOT NULL AND BMI BETWEEN 10 AND 100 THEN 20 ELSE 0 END +
    CASE WHEN Schooling > 0 THEN 20 ELSE 0 END
);
```

## Skills Demonstrated
- Advanced SQL query writing
- Data cleaning and validation
- Window functions
- CTEs (Common Table Expressions)
- Index optimization
- View creation
- Data quality management

## Tools Used
- MySQL
- MySQL Workbench

## Acknowledgments
This project was completed as part of the MySQL for Data Analytics course by Analyst Builder. The course provided valuable insights into real-world data cleaning challenges and best practices.