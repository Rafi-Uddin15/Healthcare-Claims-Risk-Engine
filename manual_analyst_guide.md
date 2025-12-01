# Manual Analyst Guide: Healthcare Claims Risk Engine (Detailed Tutorial)

This guide provides a click-by-click tutorial for performing the analysis using **Excel** and **Power BI**. No coding is required.

---

## Part 1: Excel Analysis (The "RCM Analyst" Role)

### Step 1: Prepare the Data (VLOOKUP/XLOOKUP)
**Goal**: Join Patient Data (`Train_Beneficiarydata.csv`) into Claims Data (`Train_Inpatientdata.csv`).

1.  **Open Files**:
    *   Open Excel.
    *   Go to `File > Open` and browse to `d:/Health Care`.
    *   **Important**: In the file dialog, change the dropdown above the "Open" button from "All Excel Files" to **"All Files (*.*)"** or **"Text Files (*.prn; *.txt; *.csv)"**. Otherwise, Excel hides CSV files.
    *   Select `Train_Inpatientdata.csv` and click Open.

2.  **Add Columns in Inpatient Data**:
    *   Go to the `Train_Inpatientdata.csv` window.
    *   Right-click on Column B header and select **Insert** to create a new column.
    *   Name cell `B1`: **Gender**.
    *   Right-click on Column C header and select **Insert**.
    *   Name cell `C1`: **State**.

3.  **Write the Formula (VLOOKUP)**:
    *   Click on cell **B2** (under Gender).
    *   Type this formula:
        ```excel
        =VLOOKUP(A2, '[Train_Beneficiarydata.csv]Train_Beneficiarydata'!$A:$D, 4, FALSE)
        ```
    *   *Explanation*:
        *   `A2`: The ID we are looking for (BeneID).
        *   `'[Train_Beneficiarydata.csv]...'`: The other file where the data lives.
        *   `4`: The column number in the other file that has Gender (Column D is the 4th column).
        *   `FALSE`: We want an exact match.
    *   Press **Enter**. You should see a number (1 or 2).

4.  **Fill Down**:
    *   Double-click the small green square (fill handle) at the bottom-right corner of cell **B2**. This copies the formula down to all 40,000+ rows.

### Step 2: Find Fraud (Pivot Tables)
**Goal**: Identify providers who charge too much.

1.  **Insert Pivot Table**:
    *   Click anywhere inside your data in `Train_Inpatientdata.csv`.
    *   Go to the **Insert** tab > Click **PivotTable**.
    *   Click **OK** (New Worksheet).

2.  **Configure Pivot Table**:
    *   On the right side (**PivotTable Fields** pane):
    *   Drag **Provider** to the **Rows** area.
    *   Drag **InscClaimAmtReimbursed** to the **Values** area.
        *   *Check*: It should say "Sum of Insc...". If it says "Count", click the arrow > Value Field Settings > Select **Sum**.
    *   Drag **ClaimID** to the **Values** area.
        *   *Check*: It should say "Count of ClaimID".

3.  **Calculate Average**:
    *   Drag **InscClaimAmtReimbursed** to the **Values** area *again* (so it appears twice).
    *   It will probably say "Sum of InscClaimAmtReimbursed2".
    *   Click the little arrow next to it > **Value Field Settings**.
    *   Select **Average**.
    *   Click **OK**.
    *   *Result*: You now have a column for "Average Reimbursement".

4.  **Analyze**:
    *   Click the arrow next to "Row Labels" (Provider).
    *   Select **More Sort Options** > **Descending (Z to A)** by **Average of InscClaimAmtReimbursed**.
    *   The top providers are your "High Risk" targets.

### Step 3: Deep Dive (Conditional Formatting)
**Goal**: Highlight claims that took too long to process.

1.  **Calculate Duration**:
    *   Go back to your main data sheet (`Train_Inpatientdata`).
    *   Add a new column at the end called **Duration**.
    *   Formula in cell (e.g., Z2): `=H2 - G2` (assuming H is ClaimEndDt and G is ClaimStartDt).
    *   *Note*: Ensure columns G and H are formatted as **Date**.

2.  **Highlight Long Claims**:
    *   Select the entire **Duration** column (click the letter header).
    *   Go to **Home** tab > **Conditional Formatting** > **Highlight Cells Rules** > **Greater Than**.
    *   Type **10**.
    *   Select **Light Red Fill with Dark Red Text**.
    *   Click **OK**.
    *   *Result*: Any claim taking longer than 10 days is now red.

---

## Part 2: Power BI Dashboard (The "Storyteller" Role)

### Step 1: Load Data
1.  Open **Power BI Desktop**.
2.  Click **Get Data** > **Text/CSV**.
3.  Select `d:/Health Care/Train_Inpatientdata.csv`. Click **Load**.
4.  Repeat for `d:/Health Care/Train_Beneficiarydata.csv`.

### Step 2: Create Relationships (The Model)
1.  Click the **Model View** icon (3rd icon on the left sidebar).
2.  Find the `BeneID` field in the **Inpatient** box.
3.  Drag and drop it onto the `BeneID` field in the **Beneficiary** box.
4.  *Result*: A line connects them. This is a "One-to-Many" relationship.

### Step 3: Build Visuals
1.  Click the **Report View** icon (1st icon on the left).

**Visual A: Map of Costs**
1.  In the **Visualizations** pane, click the **Map** icon (globe).
2.  Drag **State** (from Beneficiary table) to **Location**.
3.  Drag **InscClaimAmtReimbursed** (from Inpatient table) to **Bubble Size**.
4.  *Result*: Bigger bubbles = more expensive states.

**Visual B: Top Fraud Providers**
1.  Click empty white space to deselect the map.
2.  Click the **Clustered Bar Chart** icon.
3.  Drag **Provider** (Inpatient) to **Y-Axis**.
4.  Drag **InscClaimAmtReimbursed** (Inpatient) to **X-Axis**.
5.  **Filter**:
    *   In the **Filters** pane (next to Visualizations), expand **Provider**.
    *   Change "Filter type" to **Top N**.
    *   Type **5**.
    *   Drag **InscClaimAmtReimbursed** to the "By value" box.
    *   Click **Apply filter**.

**Visual C: Slicer**
1.  Click empty space.
2.  Click the **Slicer** icon (funnel with list).
3.  Drag **Gender** (Beneficiary) to **Field**.
4.  *Result*: You can now click "1" (Male) or "2" (Female) to filter the whole dashboard.

---

## Final Output
You now have:
1.  **Excel**: A spreadsheet with joined data, highlighted long claims, and a Pivot Table showing top spenders.
2.  **Power BI**: An interactive dashboard connecting patients to claims.
