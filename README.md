# Python A/B Testing Analysis

A complete end-to-end A/B test analysis using **Python**, **Pandas**, **Matplotlib**, and **SciPy**.

## What this project covers

1. **Data Cleaning** with Pandas  
2. **Conversion Rate** calculation for Version A vs Version B  
3. **Bar Chart** visualization  
4. **Statistical Testing** (independent t-test + proportion z-test)  
5. **Clear Recommendation** based on the results

## Dataset

- 500 users randomly assigned to Version A or Version B
- Binary conversion outcome (`converted`: 0 or 1)
- Balanced groups (250 users each)

## Key Results

| Metric                    | Value     |
|---------------------------|-----------|
| Version A Conversion Rate | 14.0%     |
| Version B Conversion Rate | 17.6%     |
| Relative Lift of B        | +25.7%    |
| p-value (t-test)          | ≈ 0.27    |

**Conclusion**: Although Version B shows a higher conversion rate, the difference is **not statistically significant**. More data is recommended before rolling out Version B.

## How to run

1. Clone this repository
2. Open `AB_Test_Analysis.ipynb` in JupyterLab / Jupyter Notebook / VS Code / Google Colab
3. Make sure `ab_data.csv` is in the same folder
4. Run all cells

```bash
git clone https://github.com/folasunkanmi/python-ab-testing.git
cd python-ab-testing
jupyter lab
```

## Requirements

- Python 3.8+
- pandas
- matplotlib
- scipy
- statsmodels (optional, for proportion z-test)

```bash
pip install pandas matplotlib scipy statsmodels
```

## Author

**Folasunkanmi** – Data Analyst & Aspiring Data Scientist  
[GitHub Profile](https://github.com/folasunkanmi)
