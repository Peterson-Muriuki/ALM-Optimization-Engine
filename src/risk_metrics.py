import numpy as np

class RiskMetrics:
    def __init__(self, returns):
        self.returns = np.array(returns)

    def volatility(self):
        return np.std(self.returns, ddof=1)

    def sharpe_ratio(self, risk_free=0.0):
        return (np.mean(self.returns) - risk_free) / self.volatility()

    def var(self, alpha=0.05):
        return np.percentile(self.returns, 100*alpha)

    def cvar(self, alpha=0.05):
        var_alpha = self.var(alpha)
        return self.returns[self.returns <= var_alpha].mean()
