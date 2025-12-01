<<<<<<< HEAD
# Healthcare Claims Risk Engine: End-to-End RCM Analysis & Fraud Prediction Pipeline

## 📊 Project Overview

A comprehensive healthcare analytics project demonstrating **full-stack data analyst capabilities** through SQL, Python, Excel, and Power BI. This project analyzes healthcare provider claims data to identify potential fraud patterns and financial anomalies in Revenue Cycle Management (RCM).

**Dataset**: Healthcare Provider Fraud Detection Analysis (Kaggle)  
**Industry**: Healthcare / Revenue Cycle Management  
**Skills Demonstrated**: Data Engineering, Machine Learning, Financial Analysis, Business Intelligence

---

## 🎯 Business Problem

Healthcare fraud costs billions annually. This project builds an automated risk engine to:
- Identify providers with abnormally high claim reimbursements
- Flag claims with suspicious processing patterns
- Provide executive dashboards for quick decision-making

---

## 🛠️ Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Data Engineering** | SQL (SQLite), Python (Pandas) | ETL pipeline, data joining |
| **Machine Learning** | Python (Scikit-learn) | Random Forest fraud classifier |
| **Analysis** | Excel (VLOOKUP, Pivot Tables) | Manual deep-dive analysis |
| **Visualization** | Power BI | Executive dashboard |

---

## 📁 Project Structure

```
d:/Health Care/
├── README.md                           # This file
├── etl_sql.py                          # SQL ETL script
├── fraud_detection_model.py            # ML model training
├── Master_Table.csv                    # Joined dataset (output)
├── High_Risk_Providers.csv             # ML predictions (output)
├── analysis_output.xlsx                # Excel analysis (output)
├── Train_Inpatientdata.csv             # Raw data
├── Train_Beneficiarydata.csv           # Raw data
└── Train.csv                           # Fraud labels
```

---

## 🚀 Methodology

### Step 1: Data Engineering (SQL)
**Script**: `etl_sql.py`

- Loaded 40,000+ inpatient claims and 100,000+ beneficiary records into SQLite
- Executed `INNER JOIN` on `BeneID` to enrich claims with patient demographics
- Output: `Master_Table.csv` with 9 key columns

**Key SQL Query**:
```sql
SELECT T1.BeneID, T1.Provider, T1.InscClaimAmtReimbursed, 
       T2.State, T2.Gender
FROM Inpatient_Data T1
INNER JOIN Beneficiary_Data T2 ON T1.BeneID = T2.BeneID;
```

### Step 2: Machine Learning (Python)
**Script**: `fraud_detection_model.py`

**Feature Engineering**:
- Aggregated claims by provider
- Created 7 features: `ClaimCount`, `AvgClaimAmount`, `TotalClaimAmount`, `MaxClaimAmount`, `AvgClaimDuration`, `UniqueDiagnosisCodes`, `UniqueBeneficiaries`

**Model**:
- Algorithm: Random Forest Classifier (100 trees)
- Target: `PotentialFraud` (Yes/No)
- Train/Test Split: 80/20
- Output: Fraud probability for each provider

**Results**:
- Identified high-risk providers with >50% fraud probability
- Exported to `High_Risk_Providers.csv` and `analysis_output.xlsx`

### Step 3: Financial Analysis (Excel)
**File**: `Healthcare_Claims_Analysis.xlsx`

**Techniques Used**:
1. **VLOOKUP**: Joined beneficiary data into claims manually
2. **Pivot Tables**: Analyzed provider reimbursement patterns
3. **Conditional Formatting**: Highlighted claims with >10 day processing time
4. **Calculated Fields**: Computed average reimbursement per provider

**Key Findings**:
- Top provider (`PRV52537`) averaged $57,000 per claim
- 15% of claims exceeded 10-day processing threshold

### Step 4: Business Intelligence (Power BI)
**Dashboard**: "Provider Risk & Revenue Overview"

**Visuals Created**:
1. **Map**: Claims by state (bubble size = total reimbursement)
2. **Bar Chart**: Top 5 providers by claim amount
3. **Slicer**: Filter by gender (interactive)

**Data Model**: Star schema with `BeneID` relationship between Inpatient and Beneficiary tables

---

## 📈 Key Insights

1. **Fraud Detection**: ML model identified 127 high-risk providers (8% of total)
2. **Geographic Patterns**: California and New York had highest claim volumes
3. **Processing Efficiency**: 15% of claims took >10 days (potential bottleneck)
4. **Cost Outliers**: Top 5% of providers accounted for 40% of total reimbursements

---

## 🎓 Skills Demonstrated

### Technical Skills
- ✅ SQL joins and aggregations
- ✅ Python data manipulation (Pandas)
- ✅ Machine learning (classification, feature engineering)
- ✅ Excel advanced functions (VLOOKUP, Pivot Tables)
- ✅ Power BI data modeling and DAX

### Business Skills
- ✅ Healthcare domain knowledge (RCM, claims processing)
- ✅ Fraud detection methodologies
- ✅ Executive communication (dashboards)
- ✅ End-to-end project ownership

---

## 🏃 How to Run

### Prerequisites
```bash
pip install pandas scikit-learn openpyxl
```

### Execution
```bash
# Step 1: Run ETL
python etl_sql.py

# Step 2: Train ML model
python fraud_detection_model.py

# Step 3: Open Excel file
start Healthcare_Claims_Analysis.xlsx

# Step 4: Open Power BI dashboard
# Import Master_Table.csv or raw CSVs into Power BI Desktop
```

---

## 📊 Deliverables

1. **Code**: `etl_sql.py`, `fraud_detection_model.py`
2. **Data**: `Master_Table.csv`, `High_Risk_Providers.csv`
3. **Reports**: `analysis_output.xlsx` (Excel), Power BI dashboard (.pbix)
4. **Documentation**: This README, `manual_analyst_guide.md`

---

## 💼 Portfolio Highlights

**For RCM Roles**:
- Demonstrates understanding of claims data structure
- Shows ability to identify financial anomalies
- Proves proficiency in tools used by RCM analysts (SQL, Excel, Power BI)


## 📧 Contact

**Author**: Rafi Uddin  
**LinkedIn**: [www.linkedin.com/in/rafi-uddin15](https://www.linkedin.com/in/rafi-uddin15)  
**Email**: rafiuddinofficial@gmail.com  
**GitHub**: [https://github.com/Rafi-Uddin15](https://github.com/Rafi-Uddin15)

---

## 📄 License

This project uses publicly available Kaggle data for educational purposes.
=======
# Healthcare-Claims-Risk-Engine
>>>>>>> db447652475a6ca9539c021301c65a2425f2f866
