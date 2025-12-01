# Power BI Desktop Setup Guide for Data Analysts

## Step 1: Download Power BI Desktop

### Option A: Microsoft Store (Recommended)
1. Open **Microsoft Store** on Windows.
2. Search for **"Power BI Desktop"**.
3. Click **Get** or **Install**.
4. Wait for installation to complete.

### Option B: Direct Download
1. Visit: [https://www.microsoft.com/en-us/download/details.aspx?id=58494](https://www.microsoft.com/en-us/download/details.aspx?id=58494)
2. Click **Download**.
3. Run the `.exe` file.
4. Follow the installation wizard (accept defaults).

---

## Step 2: Initial Setup

### First Launch
1. Open **Power BI Desktop** from Start Menu.
2. **Sign In** (Optional but recommended):
   - Click **Sign In** at top-right.
   - Use your Microsoft account (or create one).
   - *Why?* Enables publishing to Power BI Service and collaboration.

### Skip Sign-In (For Local Work Only)
- Click **Skip** if you only want to work locally.

---

## Step 3: Essential Settings for Data Analysts

### A. Data Load Settings
1. Go to **File** > **Options and settings** > **Options**.
2. Navigate to **Data Load**:
   - ✅ **Enable "Auto date/time"** (helps with time-based analysis).
   - ✅ **Enable "Type detection"** (auto-detects data types).

### B. Privacy Settings
1. In **Options** > **Privacy**:
   - Set **Privacy Level** to **"Ignore Privacy Levels"** (for local files).
   - *Note*: Only do this for trusted data sources.

### C. Regional Settings
1. In **Options** > **Regional Settings**:
   - Set **Locale** to your region (e.g., English (United States)).
   - Set **Data Format** to match your CSV files (usually auto-detected).

### D. Query Editor Settings
1. In **Options** > **Power Query Editor**:
   - ✅ **Enable "Column profiling based on entire dataset"** (not just top 1000 rows).

---

## Step 4: Install Key Visuals (Optional but Recommended)

### Custom Visuals from AppSource
1. In Power BI Desktop, click **Home** > **Get more visuals** (icon with three dots).
2. Search and install:
   - **"Chiclet Slicer"** (better filters).
   - **"Text Filter"** (search boxes).
   - **"Sankey Diagram"** (flow charts).

---

## Step 5: Verify Installation

### Test with Sample Data
1. Click **Get Data** > **Excel**.
2. Select any Excel file (or use `d:/Health Care/analysis_output.xlsx`).
3. Click **Load**.
4. Drag a field to the canvas to create a visual.

**Success!** If you see a chart, you're ready to go.

---

## Essential Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Get Data | `Ctrl + Alt + D` |
| Refresh Data | `F5` |
| Duplicate Page | `Ctrl + D` |
| Save | `Ctrl + S` |
| Publish to Service | `Ctrl + Shift + P` |

---

## Next Steps

You're now ready to build the **Healthcare Claims Risk Dashboard**!

Refer to the **Manual Analyst Guide** (`manual_analyst_guide.md`) for step-by-step instructions on creating the visuals.
