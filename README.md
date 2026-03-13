# Dataset Quality Scorer

A Python-based tool to evaluate dataset quality using multiple data quality dimensions.  
This project analyzes datasets and generates a quality score along with risk levels and key issues.

## Features

- Dataset profiling
- Data quality scoring
- Risk assessment
- Detection of:
  - Missing values
  - Duplicate records
  - Invalid values
  - Outliers
- Automatic column type detection
- Detailed dataset quality report

## Quality Dimensions

The tool evaluates datasets based on four major dimensions:

### 1. Completeness
Checks for missing values across columns.

### 2. Validity
Detects invalid values based on column data types.

### 3. Duplicates
Identifies duplicate rows in the dataset.

### 4. Outliers
Detects extreme values in numeric columns using statistical methods.

## Final Score Calculation

The final dataset quality score is computed using weighted scores from all four dimensions:

Final Score =  
(Completeness × Weight) +  
(Duplicates × Weight) +  
(Validity × Weight) +  
(Outliers × Weight)

Additional override rules determine the final risk level.

## Risk Levels

| Score Range | Risk Level |
|-------------|------------|
| 80 – 100 | Low Risk |
| 50 – 79 | Medium Risk |
| 0 – 49 | High Risk |

## How It Works

1. Load dataset
2. Profile dataset structure
3. Detect column types
4. Evaluate quality dimensions
5. Calculate final score
6. Generate quality report

## Example Output

DATASET QUALITY SCORER

DATASET SUMMARY
Rows: 1000
Columns: 8

Numeric Columns: ['age', 'salary']
Categorical Columns: ['city']
Boolean Columns: ['is_active']
Datetime Columns: ['join_date']

Final Score: 82/100
Risk Level: LOW

DIMENSION SCORES
Completeness: 85 (Low)
Validity: 80 (Low)
Duplicates: 90 (Low)
Outliers: 75 (Moderate)

KEY ISSUES
Completeness:
Heavy missing values detected in:
salary


## Technologies Used

- Python
- Pandas
- NumPy

## Use Cases

- Data preprocessing
- Data quality auditing
- Machine learning dataset validation
- Data engineering pipelines

## Future Improvements

- Interactive HTML reports
- Visualization dashboard
- More advanced validation rules
- Support for large datasets
- Integration with data pipelines

## Author

Yash Rathva
