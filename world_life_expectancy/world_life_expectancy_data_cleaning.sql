-- =============================================================================
-- SECTION 0: SCRIPT DOCUMENTATION AND OVERVIEW
-- =============================================================================
/*******************************************************************************
 * World Life Expectancy Data Cleaning Project
 *
 * Author: Tobin Zolkowski
 * Date: February 1, 2025
 * 
 * Description: 
 * This script performs comprehensive data cleaning and standardization on the 
 * World Life Expectancy dataset. It handles duplicate records, standardizes values,
 * performs data validation, and implements quality tracking.
 *
 * Dependencies:
 * - Requires an existing 'worldlifexpectancy' table
 * - Requires appropriate permissions for CREATE, ALTER, and UPDATE operations
 *
 * Features:
 * - Data backup creation
 * - Duplicate record handling
 * - Data standardization
 * - Missing value interpolation
 * - Data quality scoring
 * - Performance optimization through indexing
 * - Summary view creation
 *
 * Usage:
 * Execute the script sections sequentially to ensure proper data transformation
 * Monitor the data_quality_score column for validation
 ******************************************************************************/

-- =============================================================================
-- SECTION 1: INITIALIZATION AND BACKUP
-- =============================================================================
-- Purpose: Create backup and prepare environment for data cleaning operations
-- Dependencies: None
-- Expected Runtime: < 1 minute for typical dataset size
-- =============================================================================

-- 1. Create backup before modifications
/*
 * Creates a full backup of the worldlifexpectancy table before any modifications
 * This ensures data recovery capability if needed
 */
CREATE TABLE IF NOT EXISTS worldlifexpectancy_backup AS
SELECT * FROM worldlifexpectancy;

-- =============================================================================
-- SECTION 2: DATA DEDUPLICATION
-- =============================================================================
-- Purpose: Remove duplicate records while preserving highest quality entries
-- Dependencies: Original table structure
-- Expected Runtime: 1-2 minutes depending on duplicate count
-- =============================================================================

-- 2. Handle duplicate records
/*
 * Identifies and removes duplicate country/year combinations
 * Keeps the record with the most complete information based on:
 * - Status presence
 * - Life expectancy presence
 * - GDP validity
 * - Original Row_ID as tiebreaker
 */
WITH DuplicatesCTE AS (
    SELECT *,
        -- Use ROW_NUMBER to assign ranks within each Country-Year group
        -- Lower rank (1) is given to rows with:
        --   1. Non-empty Status (priority 1)
        --   2. Non-empty Life expectancy (priority 2)
        --   3. Valid GDP (priority 3)
        --   4. Lower Row_ID as tiebreaker
        ROW_NUMBER() OVER (
            PARTITION BY Country, Year
            ORDER BY 
                CASE WHEN Status != '' THEN 1 ELSE 2 END,      -- Prioritize rows with Status
                CASE WHEN Lifeexpectancy != '' THEN 1 ELSE 2 END,  -- Then consider Life expectancy
                CASE WHEN GDP > 0 THEN 1 ELSE 2 END,           -- Then consider GDP
                Row_ID                                         -- Use Row_ID as final tiebreaker
        ) as row_num
    FROM worldlifexpectancy
)
-- Delete all duplicate rows (keeping only row_num = 1)
DELETE FROM worldlifexpectancy 
WHERE Row_ID IN (
    SELECT Row_ID 
    FROM DuplicatesCTE 
    WHERE row_num > 1
);

-- =============================================================================
-- SECTION 3: DATA STANDARDIZATION AND CLEANING
-- =============================================================================
-- Purpose: Standardize values and formats across all columns
-- Dependencies: Deduplication complete
-- Expected Runtime: 2-3 minutes
-- =============================================================================

-- 3. Standardize Status values
/*
 * Normalizes the Status field to ensure consistency
 * Valid values: 'Developing', 'Developed', 'Unknown'
 * Empty values are converted to 'Unknown'
 */
UPDATE worldlifexpectancy
SET Status = CASE 
    WHEN Status = '' THEN 'Unknown'
    WHEN Status IN ('Developing', 'Developed') THEN Status
    ELSE 'Unknown'
END;

-- 4. Clean and standardize Life Expectancy values
/*
 * Validates and standardizes Life Expectancy values
 * - Converts empty strings to NULL
 * - Removes invalid values (> 100)
 * - Ensures decimal format with one decimal place
 */
UPDATE worldlifexpectancy t1
JOIN (
    SELECT Country, Year, 
        CASE 
            WHEN Lifeexpectancy = '' THEN NULL           -- Convert empty strings to NULL
            WHEN CAST(Lifeexpectancy AS DECIMAL(5,1)) > 100 THEN NULL  -- Remove impossible values
            ELSE CAST(Lifeexpectancy AS DECIMAL(5,1))    -- Convert to consistent decimal format
        END as clean_life_expectancy
    FROM worldlifexpectancy
) t2
ON t1.Country = t2.Country AND t1.Year = t2.Year    -- Match records by Country and Year
SET t1.Lifeexpectancy = t2.clean_life_expectancy;

-- =============================================================================
-- SECTION 4: MISSING VALUE HANDLING
-- =============================================================================
-- Purpose: Handle NULL values and interpolate missing data where appropriate
-- Dependencies: Standardized data format
-- Expected Runtime: 2-3 minutes
-- =============================================================================

-- 5. Fill missing Life Expectancy values using interpolation
/*
 * Uses window functions to interpolate missing Life Expectancy values
 * Calculates average based on surrounding years for the same country
 * Only fills NULL values, preserving existing valid data
 */
UPDATE worldlifexpectancy t1
JOIN (
    SELECT Country, Year,
        -- Calculate moving average using surrounding years
        -- Window: 1 year before and 1 year after current record
        AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))) OVER (
            PARTITION BY Country              -- Group by country
            ORDER BY Year                     -- Order by year for proper interpolation
            ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING  -- Define 3-year window
        ) as interpolated_life_expectancy
    FROM worldlifexpectancy
    WHERE Lifeexpectancy IS NOT NULL         -- Only consider valid values for interpolation
) t2
ON t1.Country = t2.Country AND t1.Year = t2.Year
SET t1.Lifeexpectancy = t2.interpolated_life_expectancy
WHERE t1.Lifeexpectancy IS NULL;            -- Only update missing values

-- =============================================================================
-- SECTION 5: DATA VALIDATION AND QUALITY SCORING
-- =============================================================================
-- Purpose: Implement quality checks and scoring system
-- Dependencies: Cleaned and standardized data
-- Expected Runtime: 1-2 minutes
-- =============================================================================

-- 6. Clean numeric columns
/*
 * Validates and cleans numeric columns using logical bounds:
 * - AdultMortality: 0-1000 range
 * - GDP: Must be positive
 * - BMI: 0-100 range
 * Invalid values are converted to NULL
 */
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
/*
 * Adds columns for tracking data quality and updates
 * - data_quality_score: Integer score based on completeness
 * - last_updated: Timestamp of last modification
 */
ALTER TABLE worldlifexpectancy
ADD COLUMN data_quality_score INT,
ADD COLUMN last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- 8. Calculate data quality score
/*
 * Implements a scoring system (0-100) based on:
 * - Life expectancy presence (20 points)
 * - Valid adult mortality (20 points)
 * - Valid GDP (20 points)
 * - Valid BMI (20 points)
 * - Valid schooling data (20 points)
 */
UPDATE worldlifexpectancy
SET data_quality_score = (
    -- Award 20 points for each valid critical field
    CASE WHEN Lifeexpectancy IS NOT NULL THEN 20 ELSE 0 END +          -- Life expectancy check
    CASE WHEN AdultMortality IS NOT NULL AND AdultMortality > 0 THEN 20 ELSE 0 END +  -- Adult mortality check
    CASE WHEN GDP IS NOT NULL AND GDP > 0 THEN 20 ELSE 0 END +         -- GDP check
    CASE WHEN BMI IS NOT NULL AND BMI BETWEEN 10 AND 100 THEN 20 ELSE 0 END +  -- BMI check
    CASE WHEN Schooling > 0 THEN 20 ELSE 0 END                         -- Schooling check
);

-- =============================================================================
-- SECTION 6: PERFORMANCE OPTIMIZATION
-- =============================================================================
-- Purpose: Create indexes and optimize table structure for query performance
-- Dependencies: All data cleaning steps complete
-- Expected Runtime: 3-5 minutes depending on table size
-- =============================================================================

-- 9. Create indexes for better performance
/* 
 * Creates optimized indexes for improved query performance
 * Implements best practices for index creation including:
 * - Appropriate column selection
 * - Prefix length limitations
 * - Composite indexes for related columns
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

-- =============================================================================
-- SECTION 7: REPORTING AND ANALYSIS VIEWS
-- =============================================================================
-- Purpose: Create summary views for data quality assessment
-- Dependencies: Quality scoring complete
-- Expected Runtime: < 1 minute
-- =============================================================================

-- 10. Create summary view
/*
 * Creates a statistical summary view with:
 * - Date range per country
 * - Average life expectancy
 * - Data quality metrics
 * - Record counts
 * Useful for quick data quality assessment and reporting
 */
CREATE OR REPLACE VIEW vw_life_expectancy_summary AS
SELECT 
    Country,
    Status,
    MIN(Year) as start_year,                 -- First year of data for country
    MAX(Year) as end_year,                   -- Last year of data for country
    -- Calculate average life expectancy with 1 decimal precision
    ROUND(AVG(CAST(Lifeexpectancy AS DECIMAL(5,1))), 1) as avg_life_expectancy,
    -- Round average data quality score to whole number
    ROUND(AVG(data_quality_score), 0) as avg_data_quality,
    COUNT(*) as record_count                 -- Total records per country
FROM worldlifexpectancy
GROUP BY Country, Status;                    -- Group statistics by country and development status