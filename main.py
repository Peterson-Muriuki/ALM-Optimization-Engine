from src.data_loader import DataLoader
from src.alm_engine import ALMEngine
from src.compliance_checker import ComplianceChecker
import os

# Load data
print("[1/5] Loading market data...")
loader = DataLoader()
print("Data loaded successfully.")

# ALM modeling
print("\n[2/5] Modeling liabilities and assets...")
engine = ALMEngine()
engine.run()
engine.summary()

# Compliance check
print("\n[5/5] Checking regulatory compliance...")
checker = ComplianceChecker()
if checker.check():
    print("✓ PORTFOLIO IS COMPLIANT")
else:
    print("⚠ PORTFOLIO NOT COMPLIANT")

# Save outputs
os.makedirs("outputs/reports", exist_ok=True)
with open("outputs/reports/alm_summary.txt", "w") as f:
    f.write("ALM Summary\n")
    f.write(f"Liability PV: {engine.liability_pv}\n")
    f.write(f"Liability Duration: {engine.liability_duration}\n")
    f.write(f"Optimal Asset Weights: {engine.asset_weights}\n")
