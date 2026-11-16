# Python A/B Testing Analysis

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Reproducible](https://img.shields.io/badge/Reproducible-Yes-brightgreen)](#reproducibility)

**A production-ready statistical evaluation of an A/B test comparing two product versions on conversion rate.**

**Author:** Folasunkanmi  
**Repository:** https://github.com/folasunkanmi/python-ab-testing

---

## Abstract

This project delivers a complete, reproducible A/B test analysis. It goes beyond a basic p-value by including:

- Rigorous **data validation**
- Conversion rates with **95% Wilson confidence intervals**
- **Two-proportion z-test** as the primary hypothesis test
- Effect size (Cohen’s h)
- **Power analysis** and required sample-size calculations
- Professional visualizations that show uncertainty
- Clear **business recommendations**

**Key result:** Version B converted at 17.6% vs 14.0% for Version A (+25.7% relative lift). The difference is **not statistically significant** (p ≈ 0.27). The experiment was underpowered.

---

## Project Structure

```
python-ab-testing/
├── AB_Test_Analysis.ipynb   # Full analysis notebook
├── ab_data.csv              # Raw experimental data (500 users)
├── requirements.txt         # Python dependencies
├── README.md                # This file
└── LICENSE                  # MIT License
```

---

## Quick Start

```bash
git clone https://github.com/folasunkanmi/python-ab-testing.git
cd python-ab-testing
pip install -r requirements.txt
jupyter lab AB_Test_Analysis.ipynb
```

---

## Key Findings

| Metric                        | Value                      |
|-------------------------------|----------------------------|
| Version A conversion rate     | 14.0% (95% CI: 11.1–17.5%) |
| Version B conversion rate     | 17.6% (95% CI: 14.3–21.5%) |
| Absolute difference           | +3.6 percentage points     |
| Relative lift                 | +25.7%                     |
| Two-proportion z-test p-value | 0.270                      |
| 95% CI for difference         | [−2.7 pp, +9.9 pp]         |
| Cohen’s h                     | ≈ 0.10 (small)             |
| Achieved power                | ~20%                       |

**Interpretation:** The observed lift is directionally positive but statistically inconclusive. The confidence interval for the difference includes zero, and the experiment lacked sufficient power.

---

## Methodology Highlights

1. **Data Validation** – Missing values, duplicates, invalid records, and group balance are explicitly checked.
2. **Confidence Intervals** – Wilson score intervals for individual rates; Wald interval for the difference.
3. **Primary Test** – Two-proportion z-test (most appropriate for binary conversion data).
4. **Effect Size** – Cohen’s h reported alongside the p-value.
5. **Power Analysis** – Achieved power calculated; required sample sizes provided for 5–25% relative lifts.
6. **Business Translation** – Clear go / no-go recommendation and design guidance for the next experiment.

---

## Business Recommendation

**Do not fully roll out Version B** on the basis of this test alone.

Recommended next steps:
- Re-run with a larger sample (see sample-size table in the notebook).
- Examine secondary metrics (revenue, retention, engagement).
- Consider segmentation and sequential testing frameworks for future experiments.

To detect a 10% relative lift with 80% power (α = 0.05) you would need approximately **8,000–9,000 users per group**.

---

## How to Cite

If you use this analysis or adapt the methodology, please cite:

```
Folasunkanmi. (2026). A/B Test Analysis: Conversion Rate Comparison 
[Jupyter Notebook]. GitHub. https://github.com/folasunkanmi/python-ab-testing
```

---

## Reproducibility

- [x] Raw data included
- [x] Complete executable notebook
- [x] Dependency list (`requirements.txt`)
- [x] Explicit statistical hypotheses
- [x] Confidence intervals reported
- [x] Power analysis included
- [x] Limitations documented

---

## License

MIT License – free to use, modify, and distribute with attribution.
