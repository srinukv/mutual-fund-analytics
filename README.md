# Mutual Fund Analytics Capstone Project

## Overview

This project was developed as part of the Bluestock Fintech Data Analytics Internship. The objective was to build an end-to-end mutual fund analytics platform covering data ingestion, cleaning, exploratory analysis, performance analytics, advanced risk metrics, and interactive dashboard development.

The project analyzes mutual fund schemes, NAV history, SIP inflows, AUM trends, investor behavior, portfolio allocations, and benchmark performance to generate actionable insights for investors and fund managers.

---

## Project Objectives

* Collect and validate mutual fund data
* Build a structured analytics database
* Perform exploratory data analysis
* Analyze fund performance metrics
* Calculate advanced risk measures
* Study investor behavior patterns
* Generate recommendations based on risk appetite
* Build an interactive Power BI dashboard

---

## Project Structure

```text
mutual_fund_analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── scripts/
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── create_database.py
│   ├── load_data.py
│   └── recommender.py
│
├── reports/
│
├── dashboard/
│
└── bluestock_mf.db
```

---

## Data Sources

* AMFI Mutual Fund Data
* MFAPI NAV Data
* Industry AUM Data
* SIP Inflow Data
* Investor Transaction Data
* Portfolio Holdings Data
* Benchmark Index Data

---

## Analytics Performed

### Exploratory Data Analysis

* AUM Growth Analysis
* SIP Trend Analysis
* Folio Growth Analysis
* Category Inflow Analysis
* State-wise SIP Distribution
* Sector Allocation Analysis

### Performance Analytics

* Daily Returns
* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Benchmark Comparison

### Advanced Analytics

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation Engine
* HHI Concentration Analysis

---

## Installation

```bash
git clone <repository-url>

cd mutual_fund_analytics

pip install -r requirements.txt
```

---

## Running the Project

### Data Processing

```bash
python scripts/data_ingestion.py

python scripts/data_cleaning.py

python scripts/create_database.py

python scripts/load_data.py
```

### Advanced Analytics

```bash
jupyter notebook notebooks/Advanced_Analytics.ipynb
```

### Fund Recommender

```bash
python scripts/recommender.py
```

---

## Key Deliverables

* EDA Analysis Notebook
* Performance Analytics Notebook
* Advanced Analytics Notebook
* Risk Reports
* Rolling Sharpe Visualizations
* Power BI Dashboard
* Final Report
* Presentation

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Plotly
* SQLite
* SQLAlchemy
* Jupyter Notebook
* Power BI

---

## Author

Venkata Srinivasarao Killadi

Bluestock Fintech Internship Project
