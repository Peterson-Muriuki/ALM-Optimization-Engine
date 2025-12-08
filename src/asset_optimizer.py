import pandas as pd
import numpy as np
import cvxpy as cp

class AssetOptimizer:
    def __init__(self, asset_file="data/raw/asset_prices.csv"):
        self.asset_file = asset_file
        self.assets = pd.read_csv(asset_file)

    def optimize(self):
        returns = self.assets.pct_change().dropna()
        mu = returns.mean().values
        Sigma = np.cov(returns.T)

        n = len(mu)
        w = cp.Variable(n)
        ret = mu @ w
        risk = cp.quad_form(w, Sigma)

        prob = cp.Problem(cp.Maximize(ret - 0.5 * risk),
                          [cp.sum(w) == 1,
                           w >= 0])
        prob.solve()

        return w.value

if __name__ == "__main__":
    optimizer = AssetOptimizer()
    weights = optimizer.optimize()
    print("Optimal Weights:", weights)
