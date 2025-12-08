from src.liability_model import LiabilityModel
from src.asset_optimizer import AssetOptimizer
from src.risk_metrics import RiskMetrics

class ALMEngine:
    def __init__(self):
        self.liabilities = LiabilityModel()
        self.optimizer = AssetOptimizer()
        self.asset_weights = None
        self.liability_pv = None
        self.liability_duration = None

    def run(self):
        # Liability modeling
        self.liability_pv = self.liabilities.present_value()
        self.liability_duration = self.liabilities.duration()

        # Asset optimization
        self.asset_weights = self.optimizer.optimize()

        # Risk metrics (example: on asset returns)
        returns = self.optimizer.assets.pct_change().dropna()
        self.risk_metrics = RiskMetrics(returns.mean(axis=1))

    def summary(self):
        print("=== ALM Engine Summary ===")
        print("Liability PV:", self.liability_pv)
        print("Liability Duration:", self.liability_duration)
        print("Optimal Asset Weights:", self.asset_weights)
        print("Portfolio Volatility:", self.risk_metrics.volatility())
        print("Portfolio Sharpe Ratio:", self.risk_metrics.sharpe_ratio())

if __name__ == "__main__":
    engine = ALMEngine()
    engine.run()
    engine.summary()
