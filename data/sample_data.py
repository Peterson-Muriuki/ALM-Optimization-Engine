import pandas as pd
import numpy as np
import os

# Ensure directories exist
os.makedirs("data/raw", exist_ok=True)

# -------------------------------
# 1. Generate Daily Market Returns
# -------------------------------
dates_daily = pd.date_range(start="2024-01-01", end="2024-12-31", freq="B")  # Business days
df_market_daily = pd.DataFrame({
    "Date": dates_daily,
    "Equity_Return": np.random.normal(0.0005, 0.01, len(dates_daily)),
    "Bond_Return": np.random.normal(0.0002, 0.002, len(dates_daily)),
})
df_market_daily.set_index("Date", inplace=True)
df_market_daily.to_csv("data/raw/market_returns_daily.csv")

# -------------------------------
# 2. Generate Monthly Market Returns
# -------------------------------
# Use 'ME' for month end frequency to avoid future warning
df_market_monthly = df_market_daily.resample('ME').sum()
df_market_monthly.to_csv("data/raw/market_returns_monthly.csv")

# -------------------------------
# 3. Generate Asset Prices
# -------------------------------
asset_names = ["Equity_A", "Equity_B", "Bond_A", "Bond_B"]
dates_prices = pd.date_range(start="2024-01-01", end="2024-12-31", freq="B")
prices = np.cumprod(1 + np.random.normal(0.0005, 0.01, (len(dates_prices), len(asset_names))), axis=0) * 100
df_asset_prices = pd.DataFrame(prices, columns=asset_names, index=dates_prices)
df_asset_prices.to_csv("data/raw/asset_prices.csv")

# -------------------------------
# 4. Generate Liability Cashflows
# -------------------------------
dates_liab = pd.date_range(start="2024-01-31", end="2025-12-31", freq="ME")
liabilities = np.random.uniform(50000, 200000, len(dates_liab))
df_liabilities = pd.DataFrame({"Date": dates_liab, "Cashflow": liabilities})
df_liabilities.to_csv("data/raw/liability_cashflows.csv", index=False)

# -------------------------------
# 5. Generate Yield Curve
# -------------------------------
maturities = [0.25, 0.5, 1, 2, 3, 5, 7, 10]  # in years
rates = np.random.uniform(0.02, 0.08, len(maturities))
df_yield_curve = pd.DataFrame({"Maturity": maturities, "Rate": rates})
df_yield_curve.to_csv("data/raw/yield_curve.csv", index=False)

print("Sample data generated in 'data/raw/'")
