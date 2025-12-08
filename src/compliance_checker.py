class ComplianceChecker:
    def __init__(self, solvency_ratio=2.0, min_solvency=1.5):
        self.solvency_ratio = solvency_ratio
        self.min_solvency = min_solvency

    def check(self):
        compliant = self.solvency_ratio >= self.min_solvency
        return compliant

if __name__ == "__main__":
    checker = ComplianceChecker()
    print("Compliant:", checker.check())
