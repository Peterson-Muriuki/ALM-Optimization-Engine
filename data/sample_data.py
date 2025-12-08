import pandas as pd 
import numpy as np 
import os 
os.makedirs("data\\raw", exist_ok=True) 
dates = pd.date_range(start="2025-01-01", periods=100, freq="D") 
df_market_daily = pd.DataFrame(np.random.randn(100,5), columns=["Equity","Bonds","Cash","RealEstate","Commodities"], index=dates) 
df_market_daily.index.name = "Date" 
df_market_daily.to_csv("data\\raw\\market_returns_daily.csv") 
df_market_monthly = df_market_daily.resample('ME').sum() 
df_market_monthly.to_csv("data\\raw\\market_returns_monthly.csv") 
pd.DataFrame(np.random.randn(100,3), columns=["Asset1","Asset2","Asset3"]).to_csv("data\\raw\\asset_prices.csv", index=False) 
pd.DataFrame(np.random.randn(100,2), columns=["Liabilities","Cashflows"]).to_csv("data\\raw\\liability_cashflows.csv", index=False) 
pd.DataFrame(np.random.randn(10,2), columns=["Maturity","Yield"]).to_csv("data\\raw\\yield_curve.csv", index=False) 
print("Sample data generated successfully in data\\raw/") 
