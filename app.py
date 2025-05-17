import streamlit as st
import pandas as pd
import random
from io import StringIO

st.set_page_config(page_title="Used Car Price Predictor", layout="centered")

st.title("🚗 Used Car Price Predictor")

# Additional raw data cleaned and parsed
raw_data = """
Car Name,Company,Year,Price,Kms Driven,Fuel Type
Maruti Suzuki Wagon R LXi BS III,Maruti,2014,130000,37458,Petrol
Maruti Suzuki SX4 Celebration Diesel,Maruti,2016,970000,85960,Diesel
Audi A3 Cabriolet 40 TFSI,Audi,2015,3100000,12516,Petrol
Hyundai Eon D Lite Plus,Hyundai,2018,280000,35000,Petrol
Maruti Suzuki Zen Estilo LXI Green CNG,Maruti,2009,125000,0,Petrol
Mahindra Scorpio SLX,Mahindra,2008,285000,80000,Diesel
Hyundai Santro AE GLS Audio,Hyundai,2011,165000,45000,Petrol
Maruti Suzuki Swift Dzire Tour VDi,Maruti,2009,250000,51000,Diesel
Mahindra Scorpio S4,Mahindra,2015,865000,30000,Diesel
Mahindra Xylo D2 BS IV,Mahindra,2011,390000,48000,Diesel
Hyundai Santro,Hyundai,2003,60000,51000,Petrol
Chevrolet Beat LT Diesel,Chevrolet,2015,215000,90000,Diesel
Maruti Suzuki Swift Dzire VDi,Maruti,2015,475000,43000,Diesel
Mahindra XUV500 W8,Mahindra,2015,899000,53000,Diesel
Toyota Fortuner 3.0 4x4 MT,Toyota,2013,1499000,97000,Diesel
Maruti Suzuki Alto K10 VXi,Maruti,2013,240000,20000,Petrol
"""

df = pd.read_csv(StringIO(raw_data))

# Extract unique companies and fuel types for dropdowns
companies = sorted(df["Company"].unique())
fuel_types = sorted(df["Fuel Type"].unique())

# Sidebar inputs
with st.sidebar:
    st.header("Select Car Details")
    company = st.selectbox("Select Company", companies)
    year = st.slider("Select Manufacturing Year", 2000, 2025, 2015)
    fuel_type = st.selectbox("Select Fuel Type", fuel_types)
    kms_driven = st.number_input("Enter Kilometers Driven", min_value=0, max_value=300000, value=50000, step=1000)

# Predict button and logic
if st.button("Predict Price"):
    age = 2025 - year
    base_price_map = {
        "Hyundai": 600000,
        "Mahindra": 550000,
        "Maruti": 500000,
        "Ford": 650000,
        "Skoda": 700000,
        "Audi": 1200000,
        "Chevrolet": 450000,
        "Toyota": 1100000,
    }
    base_price = base_price_map.get(company, 500000)

    random_factor = random.uniform(0.85, 1.15)

    estimated_price = base_price * random_factor - (age * 25000) - (kms_driven * 2)
    estimated_price = max(50000, estimated_price)

    st.markdown("### Estimated Price :")
    st.success(f"₹{estimated_price:,.0f}")

# Developer credit
st.markdown("---")
st.markdown("<p style='text-align:center; font-size:14px; color:gray;'>Developed by Faiz Ahmad❤️</p>", unsafe_allow_html=True)
