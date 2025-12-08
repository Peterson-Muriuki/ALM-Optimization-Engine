from src.liability_model import LiabilityModel
from src.asset_optimizer import AssetOptimizer
from src.risk_metrics import RiskMetrics
import pandas as pd

class ALMEngine:
    def __init__(self):
        self.liabilities = LiabilityModel()
        self.optimizer = AssetOptimizer()
        self.asset_weights = None
        self.liability_pv = None
        self.liability_duration = None
        self.risk_metrics = None

    def run(self):
        print("[2/5] Modeling liabilities and assets...")
        # Liability
        self.liability_pv = self.liabilities.present_value()
        self.liability_duration = self.liabilities.duration()
        print(f"Liability PV: {self.liability_pv:.2f}")
        print(f"Liability Duration: {self.liability_duration:.2f}")

        # Asset optimization
        self.asset_weights = self.optimizer.optimize()
        print("Optimal asset weights calculated.")

        # Risk metrics
        numeric_assets = self.optimizer.assets.select_dtypes(include=[float, int])
        if not numeric_assets.empty:
            returns = numeric_assets.pct_change().dropna()
            if not returns.empty:
                self.risk_metrics = RiskMetrics(returns.mean(axis=1))
        else:
            print("Warning: Asset returns data is empty. Risk metrics skipped.")

    def summary(self):
        print("\n=== ALM Engine Summary ===")
        print(f"Liability PV: {self.liability_pv:.2f}")
        print(f"Liability Duration: {self.liability_duration:.2f}")
        print(f"Optimal Asset Weights: {self.asset_weights}")
        if self.risk_metrics:
            print(f"Portfolio Volatility: {self.risk_metrics.volatility():.4f}")
            print(f"Portfolio Sharpe Ratio: {self.risk_metrics.sharpe_ratio():.4f}")
            print(f"Portfolio 5% VaR: {self.risk_metrics.var():.4f}")
            print(f"Portfolio 5% CVaR: {self.risk_metrics.cvar():.4f}")
        else:
            print("Portfolio Volatility: N/A")
            print("Portfolio Sharpe Ratio: N/A")
            print("Portfolio 5% VaR: N/A")
            print("Portfolio 5% CVaR: N/A")
