import pandas as pd

class LiabilityModel:
    def __init__(self, liability_file="data/raw/liability_cashflows.csv"):
        self.liability_file = liability_file
        self.liabilities = pd.read_csv(liability_file)
        self.liabilities.columns = self.liabilities.columns.str.strip()

    def present_value(self, discount_rate=0.05):
        cashflows = self.liabilities['Cashflow'].astype(float)
        pv = sum([cf / ((1 + discount_rate)**t) for t, cf in enumerate(cashflows, 1)])
        return pv

    def duration(self, discount_rate=0.05):
        cashflows = self.liabilities['Cashflow'].astype(float)
        pv = self.present_value(discount_rate)
        dur = sum([t * cf / ((1 + discount_rate)**t) for t, cf in enumerate(cashflows, 1)]) / pv
        return dur
