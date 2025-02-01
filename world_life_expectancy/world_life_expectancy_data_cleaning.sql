-- World Life Expectancy Data Cleaning Project
-- Author: [Your Name]
-- Date: February 1, 2025
-- Description: Comprehensive data cleaning and standardization script

-- 1. Create backup before modifications
CREATE TABLE IF NOT EXISTS worldlifexpectancy_backup AS
SELECT * FROM worldlifexpectancy;

-- 2. Handle duplicate records
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

-- 3. Standardize Status values
UPDATE worldlifexpectancy
SET Status = CASE 
    WHEN Status = '' THEN 'Unknown'
    WHEN Status IN ('Developing', 'Developed') THEN Status
    ELSE 'Unknown'
END;

-- 4. Clean and standardize Life Expectancy values
UPDATE worldlifexpectancy t1
JOIN (
    SELECT Country, Year, 
        CASE 
            WHEN Lifeexpectancy = '' THEN NULL
            WHEN CAST(Lifeexpectancy AS DECIMAL(5,1)) > 100 THEN NULL
            ELSE CAST(Lifeexpectancy AS DECIMAL(5,1))
        END as clean_life_expectancy
    FROM worldlifexpectancy
) t2
ON t1.Country = t2.Country AND t1.Year = t2.Year
SET t1.Lifeexpectancy = t2.clean_life_expectancy;

-- 5. Fill missing Life Expectancy values using interpolation
UPDATE worldlifexpectancy t1
JOIN (
    SELECT Country, Year,
        AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))) OVER (
            PARTITION BY Country 
            ORDER BY Year 
            ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
        ) as interpolated_life_expectancy
    FROM worldlifexpectancy
    WHERE Lifeexpectancy IS NOT NULL
) t2
ON t1.Country = t2.Country AND t1.Year = t2.Year
SET t1.Lifeexpectancy = t2.interpolated_life_expectancy
WHERE t1.Lifeexpectancy IS NULL;

-- 6. Clean numeric columns
UPDATE worldlifexpectancy
SET 
    AdultMortality = CASE 
        WHEN AdultMortality <= 0 OR AdultMortality > 1000 THEN NULL 
        ELSE AdultMortality 
    END,
    GDP = CASE 
        WHEN GDP < 0 THEN NULL 
        ELSE GDP 
    END,
    BMI = CASE 
        WHEN BMI <= 0 OR BMI > 100 THEN NULL 
        ELSE BMI 
    END;

-- 7. Add data quality tracking
ALTER TABLE worldlifexpectancy
ADD COLUMN data_quality_score INT,
ADD COLUMN last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- 8. Calculate data quality score
UPDATE worldlifexpectancy
SET data_quality_score = (
    CASE WHEN Lifeexpectancy IS NOT NULL THEN 20 ELSE 0 END +
    CASE WHEN AdultMortality IS NOT NULL AND AdultMortality > 0 THEN 20 ELSE 0 END +
    CASE WHEN GDP IS NOT NULL AND GDP > 0 THEN 20 ELSE 0 END +
    CASE WHEN BMI IS NOT NULL AND BMI BETWEEN 10 AND 100 THEN 20 ELSE 0 END +
    CASE WHEN Schooling > 0 THEN 20 ELSE 0 END
);

-- 9. Create indexes for better performance
/* 
This script creates optimal indexes for the worldlifexpectancy table
while avoiding the key length limitation error
*/

-- 1. Create index for Year (smaller integer column)
CREATE INDEX idx_year 
ON worldlifexpectancy(Year);

-- 2. Create index for Status (using prefix length)
CREATE INDEX idx_status 
ON worldlifexpectancy(Status(255));

-- 3. Create index for Country (using prefix length)
CREATE INDEX idx_country 
ON worldlifexpectancy(Country(255));

-- 4. Create composite index for commonly used numeric columns
CREATE INDEX idx_mortality_gdp 
ON worldlifexpectancy(AdultMortality, GDP);

-- 5. Create index for Life expectancy
CREATE INDEX idx_life_expectancy 
ON worldlifexpectancy(Lifeexpectancy(255));

/* 
Best Practices Implemented:
1. Limited string column indexes to 255 characters to avoid key length issues
2. Created selective indexes on frequently queried columns
3. Added composite index for commonly paired columns
4. Focused on columns used in WHERE, JOIN, and ORDER BY clauses
5. Balanced between query performance and storage/maintenance overhead
*/

-- 10. Create summary view
CREATE OR REPLACE VIEW vw_life_expectancy_summary AS
SELECT 
    Country,
    Status,
    MIN(Year) as start_year,
    MAX(Year) as end_year,
    ROUND(AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))), 1) as avg_life_expectancy,
    ROUND(AVG(data_quality_score), 0) as avg_data_quality,
    COUNT(*) as record_count
FROM worldlifexpectancy
GROUP BY Country, Status;