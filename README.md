# Project_3_EchoChain

## Objective
The objective of this project is to analyze laptop datasets using Python, PySpark, Databricks, and Power BI. The project includes data exploration, data cleaning, feature engineering, data transformation, and data analysis.

## Dataset
- products.csv
- refurbished_laptops.csv

## Technologies Used
- Python
- Pandas
- PySpark
- Databricks
- Power BI
- GitHub

## Project Structure

### 01_Dataset
- Contains original and processed datasets.

### 02_Databricks
- Contains Databricks notebooks and documentation.

### 03_PySpark
- Contains Python and PySpark scripts.

### 06_Documentation
- Contains project documents.

### 07_Progress
- Contains weekly progress reports.

### 09_Images
- Contains screenshots.

### 10_Reports
- Contains reports.

## Implemented Files

- 01_data_exploration.py
- 02_data_cleaning.py
- 03_feature_engineering.py
- 04_data_transformation.py
- 05_data_analysis.py
- 06_refurbished_data_exploration.py
- 07_refurbished_data_cleaning.py
- 08_refurbished_feature_engineering.py
- 09_refurbished_data_transformation.py
- 10_refurbished_data_aggregation.py

## Branch Information

- main : Final project code
- laxman : Development branch
- sahla-sharin : Refurbished dataset development

## Execution Steps

### Activate Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Required Libraries

```powershell
pip install pandas pyspark matplotlib openpyxl
```

### Run Scripts

```powershell
python 03_PySpark/01_data_exploration.py
python 03_PySpark/02_data_cleaning.py
python 03_PySpark/03_feature_engineering.py
python 03_PySpark/04_data_transformation.py
python 03_PySpark/05_data_analysis.py
python 03_PySpark/06_refurbished_data_exploration.py
python 03_PySpark/07_refurbished_data_cleaning.py
python 03_PySpark/08_refurbished_feature_engineering.py
python 03_PySpark/09_refurbished_data_transformation.py
python 03_PySpark/10_refurbished_data_aggregation.py
```

## Week 1 Work

- Repository setup
- Dataset collection
- Data exploration
- Data cleaning
- Feature engineering
- GitHub integration

## Week 2 Work

- Data transformation
- Data analysis
- Refurbished dataset processing
- Databricks implementation
- Added screenshots
- Updated documentation

## Week 3 Work

- Performed data transformation using Python and Pandas.
- Created transformed_products.csv.
- Performed data analysis on the transformed dataset.
- Explored the refurbished laptop dataset using PySpark.
- Cleaned the refurbished laptop dataset using PySpark.
- Uploaded cleaned and transformed datasets to Databricks.
- Created and queried Databricks tables.
- Verified data using PySpark operations and aggregations.
- Updated project documentation and screenshots.
- Synced project changes with GitHub.

# Sahla Sharin - Work Completed

## Databricks
- Connected GitHub repository with Databricks.
- Created the Databricks project folder.
- Completed the initial Databricks workspace setup.

---

## PySpark Tasks Completed

### 06_refurbished_data_exploration.py

- Loaded the refurbished laptops dataset.
- Explored the dataset structure.
- Displayed schema and sample records.
- Performed basic data exploration.

### 07_refurbished_data_cleaning.py

- Removed duplicate records.
- Checked and handled missing values.
- Cleaned the dataset for further processing.

### 08_refurbished_feature_engineering.py
Created new features:
- Laptop_Age
- Price_Category
- Storage_Category

### 09_refurbished_data_transformation.py
Completed:
- Screen size transformation.
- Data type conversion.
- Saved transformed dataset.

### 10_refurbished_data_aggregation.py
Performed:
- Average Price Analysis
- Grade-wise Analysis
- Storage Type Analysis
- Memory Type Analysis
- Maximum Price Analysis
- Minimum Price Analysis
- Top 10 Expensive Laptops
- Top 10 Cheapest Laptops

---

## Git Status
- All completed tasks committed successfully.
- All changes pushed to the `sahla-sharin` branch.