import pandas as pd
import sqlite3
import os

# Define file paths
BASE_DIR = "d:/Health Care"
INPATIENT_FILE = os.path.join(BASE_DIR, "Train_Inpatientdata.csv")
BENEFICIARY_FILE = os.path.join(BASE_DIR, "Train_Beneficiarydata.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "Master_Table.csv")

def run_etl():
    print("Step 1: SQL (Data Engineering) - ETL Process Started")
    
    # 1. Load CSVs into Pandas DataFrames
    print(f"Loading {INPATIENT_FILE}...")
    try:
        df_inpatient = pd.read_csv(INPATIENT_FILE)
        print(f"Loaded Inpatient Data: {df_inpatient.shape}")
    except FileNotFoundError:
        print(f"Error: File not found at {INPATIENT_FILE}")
        return

    print(f"Loading {BENEFICIARY_FILE}...")
    try:
        df_beneficiary = pd.read_csv(BENEFICIARY_FILE)
        print(f"Loaded Beneficiary Data: {df_beneficiary.shape}")
    except FileNotFoundError:
        print(f"Error: File not found at {BENEFICIARY_FILE}")
        return

    # 2. Create in-memory SQLite database
    print("Creating in-memory SQLite database...")
    conn = sqlite3.connect(':memory:')
    
    # 3. Write DataFrames to SQL tables
    print("Writing data to SQL tables...")
    df_inpatient.to_sql('Inpatient_Data', conn, index=False)
    df_beneficiary.to_sql('Beneficiary_Data', conn, index=False)
    
    # 4. Execute the Join Query
    print("Executing SQL Join Query...")
    query = """
    SELECT
        T1.BeneID,
        T1.Provider,
        T1.ClaimID,
        T1.InscClaimAmtReimbursed,
        T1.ClmDiagnosisCode_1,
        T1.ClaimStartDt,
        T1.ClaimEndDt,
        T2.State,
        T2.Gender,
        T2.DOB
    FROM Inpatient_Data T1
    INNER JOIN Beneficiary_Data T2 ON T1.BeneID = T2.BeneID;
    """
    
    try:
        df_master = pd.read_sql_query(query, conn)
        print(f"Query executed successfully. Result shape: {df_master.shape}")
        
        # 5. Export to CSV
        print(f"Saving results to {OUTPUT_FILE}...")
        df_master.to_csv(OUTPUT_FILE, index=False)
        print("ETL Process Completed Successfully.")
        
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_etl()
