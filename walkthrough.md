# Healthcare Claims Risk Engine: Project Walkthrough

I have successfully built the "Healthcare Claims Risk Engine" pipeline. This project demonstrates end-to-end data analysis capabilities, from data engineering to machine learning and reporting.

## 1. Data Engineering (SQL)
**Script**: `etl_sql.py`
- **Action**: Loaded `Train_Inpatientdata.csv` and `Train_Beneficiarydata.csv` into an in-memory SQLite database.
- **Query**: Executed a `JOIN` to combine claims data with patient demographics (Gender, State, DOB).
- **Output**: Created `Master_Table.csv` containing the enriched dataset.

## 2. Fraud Detection (Python & ML)
**Script**: `fraud_detection_model.py`
- **Feature Engineering**:
    - Aggregated data by `Provider`.
    - Calculated metrics: `ClaimCount`, `AvgClaimAmount`, `AvgClaimDuration`, `UniqueDiagnosisCodes`.
- **Modeling**: Trained a **Random Forest Classifier** to predict `PotentialFraud`.
- **Output**:
    - `High_Risk_Providers.csv`: List of providers flagged as high risk (Probability > 0.5).
    - `analysis_output.xlsx`: Excel file with sheets for High Risk Providers, Feature Importance, and Sample Data.

## 3. Financial Analysis & Visualization
**Artifact**: `manual_analyst_guide.md`
- I have created a guide for the "Manual Analyst" role.
- **Next Steps for You**:
    - Open `analysis_output.xlsx` in Excel.
    - Create the Pivot Tables and Conditional Formatting as described in the guide.
    - Import the data into Power BI to build the "Provider Risk & Revenue Overview" dashboard.

## Files Created
- `d:/Health Care/Master_Table.csv` (Joined Data)
- `d:/Health Care/High_Risk_Providers.csv` (ML Predictions)
- `d:/Health Care/analysis_output.xlsx` (Excel Report)
- `d:/Health Care/etl_sql.py` (Source Code)
- `d:/Health Care/fraud_detection_model.py` (Source Code)
