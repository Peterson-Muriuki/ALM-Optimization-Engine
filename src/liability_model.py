import pandas as pd
import numpy as np

class LiabilityModel:
    def __init__(self, liability_file="data/raw/liability_cashflows.csv"):
        self.liability_file = liability_file
        self.liabilities = pd.read_csv(liability_file)

    def present_value(self, discount_rate=0.05):
        cashflows = self.liabilities['Cashflows']
        n = len(cashflows)
        pv = sum([cf / ((1 + discount_rate)**t) for t, cf in enumerate(cashflows, 1)])
        return pv

    def duration(self, discount_rate=0.05):
        cashflows = self.liabilities['Cashflows']
        n = len(cashflows)
        pv = self.present_value(discount_rate)
        dur = sum([t * cf / ((1 + discount_rate)**t) for t, cf in enumerate(cashflows, 1)]) / pv
        return dur

if __name__ == "__main__":
    lm = LiabilityModel()
    print("Present Value of Liabilities:", lm.present_value())
    print("Duration of Liabilities:", lm.duration())
