import numpy as np

class RiskMetrics:
    def __init__(self, returns):
        self.returns = returns

    def volatility(self):
        return np.std(self.returns, ddof=1)

    def var(self, alpha=0.05):
        return np.percentile(self.returns, 100*alpha)

    def sharpe_ratio(self, risk_free=0.0):
        return (np.mean(self.returns) - risk_free) / self.volatility()

if __name__ == "__main__":
    sample_returns = np.random.normal(0.01, 0.05, 100)
    rm = RiskMetrics(sample_returns)
    print("Volatility:", rm.volatility())
    print("VaR (5%):", rm.var())
    print("Sharpe Ratio:", rm.sharpe_ratio())
