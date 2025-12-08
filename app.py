import streamlit as st
from src.alm_engine import ALMEngine
import pandas as pd

st.title("ALM Optimization Engine")

# File upload
liability_file = st.file_uploader("Upload Liability Cashflows CSV", type="csv")
asset_file = st.file_uploader("Upload Asset Prices CSV", type="csv")

if st.button("Run ALM Engine"):
    if liability_file is not None and asset_file is not None:
        # Save uploaded files temporarily
        liability_path = "data/raw/liability_cashflows.csv"
        asset_path = "data/raw/asset_prices.csv"
        with open(liability_path, "wb") as f:
            f.write(liability_file.getbuffer())
        with open(asset_path, "wb") as f:
            f.write(asset_file.getbuffer())

        # Run engine
        engine = ALMEngine()
        engine.run()
        st.subheader("ALM Engine Summary")
        st.write(f"Liability PV: {engine.liability_pv:.2f}")
        st.write(f"Liability Duration: {engine.liability_duration:.2f}")
        st.write("Optimal Asset Weights:", engine.asset_weights)
        if engine.risk_metrics:
            st.write(f"Portfolio Volatility: {engine.risk_metrics.volatility():.4f}")
            st.write(f"Portfolio Sharpe Ratio: {engine.risk_metrics.sharpe_ratio():.4f}")
            st.write(f"Portfolio 5% VaR: {engine.risk_metrics.var():.4f}")
            st.write(f"Portfolio 5% CVaR: {engine.risk_metrics.cvar():.4f}")
    else:
        st.warning("Please upload both liability and asset CSV files.")
