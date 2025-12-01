import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import os

# Define file paths
BASE_DIR = "d:/Health Care"
MASTER_FILE = os.path.join(BASE_DIR, "Master_Table.csv")
TRAIN_LABELS_FILE = os.path.join(BASE_DIR, "Train.csv")
OUTPUT_HIGH_RISK = os.path.join(BASE_DIR, "High_Risk_Providers.csv")
OUTPUT_ANALYSIS = os.path.join(BASE_DIR, "analysis_output.xlsx")

def run_model():
    print("Step 2: Python (AI/ML) - Fraud Detection Model Started")
    
    # 1. Load Data
    print("Loading data...")
    try:
        df_master = pd.read_csv(MASTER_FILE)
        df_labels = pd.read_csv(TRAIN_LABELS_FILE)
        print(f"Master Table: {df_master.shape}, Labels: {df_labels.shape}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # 2. Data Cleaning & Feature Engineering
    print("Performing Feature Engineering...")
    
    # Calculate Claim Duration
    df_master['ClaimStartDt'] = pd.to_datetime(df_master['ClaimStartDt'])
    df_master['ClaimEndDt'] = pd.to_datetime(df_master['ClaimEndDt'])
    df_master['ClaimDuration'] = (df_master['ClaimEndDt'] - df_master['ClaimStartDt']).dt.days
    
    # Handle NaNs in Diagnosis Code (Fill with 'Unknown')
    df_master['ClmDiagnosisCode_1'] = df_master['ClmDiagnosisCode_1'].fillna('Unknown')
    
    # Aggregate by Provider
    provider_features = df_master.groupby('Provider').agg({
        'ClaimID': 'count',
        'InscClaimAmtReimbursed': ['mean', 'sum', 'max'],
        'ClaimDuration': 'mean',
        'ClmDiagnosisCode_1': 'nunique',
        'BeneID': 'nunique'
    })
    
    # Flatten MultiIndex columns
    provider_features.columns = [
        'ClaimCount', 
        'AvgClaimAmount', 'TotalClaimAmount', 'MaxClaimAmount',
        'AvgClaimDuration', 
        'UniqueDiagnosisCodes',
        'UniqueBeneficiaries'
    ]
    provider_features = provider_features.reset_index()
    
    # Merge with Labels
    df_merged = pd.merge(provider_features, df_labels, on='Provider', how='inner')
    
    # Encode Target
    df_merged['PotentialFraud'] = df_merged['PotentialFraud'].map({'Yes': 1, 'No': 0})
    
    print(f"Feature Matrix Shape: {df_merged.shape}")
    print(f"Fraud Distribution:\n{df_merged['PotentialFraud'].value_counts()}")

    # 3. Train Model
    print("Training Random Forest Model...")
    X = df_merged.drop(['Provider', 'PotentialFraud'], axis=1)
    y = df_merged['PotentialFraud']
    
    # Handle any remaining NaNs (e.g. if a provider had 0 claims? shouldn't happen with inner join)
    X = X.fillna(0)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    
    # 4. Evaluate
    print("Evaluating Model...")
    y_pred = rf.predict(X_test)
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Feature Importance
    importances = pd.DataFrame({
        'Feature': X.columns,
        'Importance': rf.feature_importances_
    }).sort_values(by='Importance', ascending=False)
    print("\nTop 5 Features:")
    print(importances.head())

    # 5. Identify High Risk Providers (Apply to full dataset for reporting)
    print("Identifying High Risk Providers...")
    df_merged['FraudProbability'] = rf.predict_proba(X)[:, 1]
    
    # Filter for High Risk (e.g., Probability > 0.5 or Actual Fraud = Yes)
    # Let's export the ones the model thinks are fraud, plus the actual labels for comparison
    high_risk_df = df_merged[df_merged['FraudProbability'] > 0.5].sort_values(by='FraudProbability', ascending=False)
    
    print(f"Found {len(high_risk_df)} high risk providers.")
    
    # 6. Export Results
    print(f"Saving High Risk Providers to {OUTPUT_HIGH_RISK}...")
    high_risk_df.to_csv(OUTPUT_HIGH_RISK, index=False)
    
    # Create Excel for Step 3
    print(f"Creating Excel Analysis file {OUTPUT_ANALYSIS}...")
    with pd.ExcelWriter(OUTPUT_ANALYSIS) as writer:
        high_risk_df.to_excel(writer, sheet_name='High_Risk_Providers', index=False)
        importances.to_excel(writer, sheet_name='Feature_Importance', index=False)
        df_merged.head(100).to_excel(writer, sheet_name='Model_Data_Sample', index=False)
    
    print("Model Training and Export Completed Successfully.")

if __name__ == "__main__":
    run_model()
