import pandas as pd
import numpy as np
import cvxpy as cp

class AssetOptimizer:
    def __init__(self, asset_file="data/raw/asset_prices.csv"):
        self.asset_file = asset_file
        self.assets = pd.read_csv(asset_file)
        self.assets.columns = self.assets.columns.str.strip()

    def optimize(self):
        if self.assets.empty:
            print("Warning: Asset data is empty.")
            return {}

        # Drop non-numeric columns (e.g., dates)
        numeric_assets = self.assets.select_dtypes(include=[np.number])
        returns = numeric_assets.pct_change().dropna()

        mu = returns.mean().values
        Sigma = np.cov(returns.T)

        n = len(mu)
        w = cp.Variable(n)
        ret = mu @ w
        risk = cp.quad_form(w, Sigma)

        prob = cp.Problem(cp.Maximize(ret - 0.5*risk),
                          [cp.sum(w) == 1,
                           w >= 0])
        prob.solve()

        # Map weights to asset names
        return dict(zip(numeric_assets.columns, w.value))

