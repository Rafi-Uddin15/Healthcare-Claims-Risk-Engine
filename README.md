# 🏥 Healthcare Claims Risk Engine
### End-to-End RCM Analysis & Fraud Prediction Pipeline

![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-Data_Engineering-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-Fraud_Detection-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Financial_Analysis-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

---

## 💼 Business Case
In the US healthcare system, **Revenue Cycle Management (RCM)** is plagued by fraud and inefficiency. This project simulates a Risk Engine that analyzes **40,000+ inpatient claims** to:
1.  **Detect Fraud**: Automatically flag providers charging 500% above the average.
2.  **Optimize Revenue**: Identify claims stalled in processing (>10 days) to improve cash flow.
3.  **Visual Intelligence**: Provide executives with a live Power BI dashboard for geographic and financial oversight.

**Key Result**: Identified **$X Million** in potential fraud and 127 high-risk providers (8% of network).

---

## 🛠️ Technical Implementation

### 1. Data Engineering (SQL & Python)
*   **ETL Pipeline**: Built an automated script (`etl_sql.py`) to ingest raw CSVs into a **SQLite database**.
*   **Complex Joins**: Performed `INNER JOIN` operations to merge Claim Data with Beneficiary Demographics on `BeneID`.
*   **Data Cleaning**: Handled missing values (`NULL` in Deductibles) and standardized date formats for analysis.

### 2. Machine Learning for Fraud (Scikit-Learn)
Instead of simple rules, I trained a **Random Forest Classifier**:
*   **Feature Engineering**: Created aggregate metrics like `AvgClaimAmount` and `UniqueDiagnosisCodes` per provider.
*   **Anomaly Detection**: The model assigns a "Fraud Probability Score" (0-100%) to every provider.
*   **Outcome**: Providers with >50% probability are flagged for manual audit.

### 3. Financial Analysis (Excel)
Used for deep-dive auditing of specific flagged claims:
*   **Advanced Formulas**: `VLOOKUP` for cross-referencing NPIs, `INDEX-MATCH` for flexible lookups.
*   **Pivot Tables**: Analyzed Year-over-Year (YoY) claim volume growth.

### 4. Executive Dashboard (Power BI)
A fully interactive report containing:
*   **Geo-Map**: Claims distribution by State (Heatmap).
*   **KPI Cards**: Total Revenue, Fraud Risk Exposure, Avg Processing Time.
*   **Decomposition Tree**: Root cause analysis of high reimbursements.

---

## 📂 Repository Structure
```
.
├── etl_sql.py                  # Database creation and data loading
├── fraud_detection_model.py    # Random Forest ML model training
├── Master_Table.csv            # Cleaned, joined dataset ready for BI
├── High_Risk_Providers.csv     # List of flagged providers (Model Output)
├── Healthcare_Claims_Analysis.xlsx # Excel Audit File
└── README.md                   # Documentation
```

## 🚀 How to Run
1.  **Install Dependencies**:
    ```bash
    pip install pandas scikit-learn openpyxl
    ```
2.  **Run Pipeline**:
    ```bash
    python etl_sql.py
    python fraud_detection_model.py
    ```
3.  **View Results**: Open `Healthcare_Claims_Analysis.xlsx` or import `Master_Table.csv` into Power BI.

---
**Author**: Rafi Uddin | [LinkedIn](https://www.linkedin.com/in/rafi-uddin15)
