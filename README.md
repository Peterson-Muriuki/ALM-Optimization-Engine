#  ALM Optimization Engine

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.34-orange)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

##  Project Overview

The **ALM (Asset-Liability Management) Optimization Engine** is a Python-based platform designed to:

- Model **liabilities** with present value and duration calculations.
- Optimize **asset allocation** for diversified portfolios.
- Measure **risk metrics** including **Volatility, Sharpe Ratio, VaR, and CVaR**.
- Visualize results interactively using **Streamlit**.
- Export outputs for reporting and further analysis.

This project is ideal for risk managers, finance analysts, and students learning quantitative asset-liability modeling.

## Project Structure

ALM-Optimization-Engine/
│
├─ data/
│ ├─ raw/
│ │ ├─ asset_prices.csv
│ │ ├─ liability_cashflows.csv
│ │ ├─ market_returns_daily.csv
│ │ ├─ market_returns_monthly.csv
│ │ └─ yield_curve.csv
│
├─ src/
│ ├─ alm_engine.py
│ ├─ liability_model.py
│ ├─ asset_optimizer.py
│ └─ risk_metrics.py
│
├─ app.py # Streamlit interactive app
├─ main.py # Run the ALM engine from CLI
└─ README.md

##  Features

### Liability Modeling
- Computes **Present Value (PV)** and **Duration** from cashflow data.
- Handles multiple liability structures.

### Diversified Asset Optimization
- Uses **CVXPY** to maximize risk-adjusted returns.
- Supports **long-only portfolios** with constraints.
- Calculates **optimal weights** for multiple asset classes.

### Risk Metrics
- Portfolio **Volatility**
- **Sharpe Ratio**
- **5% Value-at-Risk (VaR)**
- **Conditional Value-at-Risk (CVaR)**

### Visualization & Export
- Interactive **Streamlit dashboard**:
  - Line charts of **PV vs Time**
  - **Portfolio weights** bar chart
  - **Risk metrics** summary
- Export results to **CSV or Excel**

##  Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ALM-Optimization-Engine.git
cd ALM-Optimization-Engine

=== ALM Engine Summary ===
Liability PV: 1,697,217.72
Liability Duration: 10.90
Optimal Asset Weights: {'Equity_A': 0.25, 'Equity_B': 0.35, 'Bond_A': 0.20, 'Bond_B': 0.20}
Portfolio Volatility: 0.0063
Portfolio Sharpe Ratio: 0.218
Portfolio 5% VaR: -0.0092
Portfolio 5% CVaR: -0.0118

License

This project is licensed under the MIT License. 

Author

Peterson Muriuki
pitmuriuki@gmail.com
 | +254 729 303 852
LinkedIn: https://www.linkedin.com/in/peterson-muriuki-5857aaa9/
 | GitHub: https://github.com/Peterson-Muriuki
