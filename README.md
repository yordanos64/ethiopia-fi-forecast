# Ethiopia Financial Inclusion Forecasting System
### 10 Academy Challenge - Week 11 Milestone Project

An interactive time-series forecasting system tracking Ethiopia's digital financial transformation trajectory across World Bank Global Findex benchmarks (2025–2027).

---

## 📊 Forecast Predictions Summary (2025 - 2027)

| Metric Focus | 2024 Baseline | 2025 Forecast | 2026 Forecast | 2027 Target Forecast |
| :--- | :---: | :---: | :---: | :---: |
| **Access** (Account Ownership %) | 49.00% | **52.12%** | **55.25%** | **58.38%** |
| **Usage** (Digital Payments %) | 35.00% | **39.50%** | **44.00%** | **48.50%** |

---

## ⚙️ Project Architecture Layout
```text
ethiopia-fi-forecast/
├── data/
│   ├── raw/             # Contains source data spreadsheets
│   └── processed/       # Stores clean datasets & enrichment proxies
├── src/
│   ├── data_enrichment.py   # Task 1 Enrichment Engine
│   └── time_series_model.py # Task 2 Trend Regression Predictor
├── dashboard/
│   └── app.py           # Task 3 Streamlit App Interface (Live)
└── tests/
    └── test_data_processing.py # Task 4 Automated Schema Validation
```

---

## 🎯 Key Strategic Market Insights
* **P2P Velocity Outpacing Infrastructure**: Interoperable peer-to-peer (P2P) transfers have successfully surpassed ATM physical cash withdrawals across Ethiopia.
* **Enabler Catalysts Injected**: Integrated national infrastructure trackers (such as Fayda ID national registration expansion and localized agent network density scaling) serve as key structural inputs for upcoming access growth loops.
