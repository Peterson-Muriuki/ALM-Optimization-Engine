import pandas as pd
import os

class DataLoader:
    def __init__(self, data_path="data/raw"):
        self.data_path = data_path

    def load_market_daily(self):
        path = os.path.join(self.data_path, "market_returns_daily.csv")
        df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
        return df

    def load_market_monthly(self):
        path = os.path.join(self.data_path, "market_returns_monthly.csv")
        df = pd.read_csv(path, parse_dates=["Date"], index_col="Date")
        return df

    def load_assets(self):
        path = os.path.join(self.data_path, "asset_prices.csv")
        df = pd.read_csv(path)
        return df

    def load_liabilities(self):
        path = os.path.join(self.data_path, "liability_cashflows.csv")
        df = pd.read_csv(path)
        return df

    def load_yield_curve(self):
        path = os.path.join(self.data_path, "yield_curve.csv")
        df = pd.read_csv(path)
        return df

if __name__ == "__main__":
    loader = DataLoader()
    print("Loading market daily data...")
    print(loader.load_market_daily().head())
    print("\nLoading monthly data...")
    print(loader.load_market_monthly().head())
    print("\nLoading assets...")
    print(loader.load_assets().head())
    print("\nLoading liabilities...")
    print(loader.load_liabilities().head())
    print("\nLoading yield curve...")
    print(loader.load_yield_curve().head())
