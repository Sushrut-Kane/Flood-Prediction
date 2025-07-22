
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("flood_predictor.pkl")

st.title("🌊 AI Flood Risk Predictor")

lat = st.number_input("Latitude", value=26.5)
lon = st.number_input("Longitude", value=92.3)
rain = st.number_input("Rainfall (mm)", value=100.0)
temp = st.number_input("Temperature (°C)", value=30.0)
humidity = st.number_input("Humidity (%)", value=75.0)
discharge = st.number_input("River Discharge (m³/s)", value=5000.0)
water_level = st.number_input("Water Level (m)", value=10.0)
elevation = st.number_input("Elevation (m)", value=50.0)

land_cover = st.selectbox("Land Cover", ['Urban', 'Forest', 'Agricultural', 'Water Body', 'Desert'])
soil_type = st.selectbox("Soil Type", ['Sandy', 'Clay', 'Loam', 'Silt', 'Peat'])

pop_density = st.number_input("Population Density", value=1000.0)
infrastructure = st.selectbox("Flood Control Infrastructure Present?", [0, 1])
historical_floods = st.selectbox("History of Floods?", [0, 1])

if st.button("Predict"):
    input_df = pd.DataFrame([{
        'Latitude': lat,
        'Longitude': lon,
        'Rainfall (mm)': rain,
        'Temperature (°C)': temp,
        'Humidity (%)': humidity,
        'River Discharge (m³/s)': discharge,
        'Water Level (m)': water_level,
        'Elevation (m)': elevation,
        'Land Cover': land_cover,
        'Soil Type': soil_type,
        'Population Density': pop_density,
        'Infrastructure': infrastructure,
        'Historical Floods': historical_floods
    }])

    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"Flood likely! (Risk: {proba:.2f})")
    else:
        st.success(f"No flood predicted. (Risk: {proba:.2f})")
#------------------------map------------------------------------
import pandas as pd
location_df = pd.DataFrame({
    'lat': [lat],  
    'lon': [lon]
})
st.map(location_df)
