import streamlit as st
import pandas as pd
import joblib

# Load artifacts
model = joblib.load("models/best_rf_model.pkl")
scaler = joblib.load("models/scaler_new.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

st.title("✈️ Flight Price Prediction")

# -----------------------------
# User Inputs
# -----------------------------

from_city = st.selectbox(
    "From",
    [
        "Aracaju (SE)",
        "Brasilia (DF)",
        "Campo Grande (MS)",
        "Florianopolis (SC)",
        "Natal (RN)",
        "Recife (PE)",
        "Rio de Janeiro (RJ)",
        "Salvador (BH)",
        "Sao Paulo (SP)"
    ]
)

destination = st.selectbox(
    "Destination",
    [
        "Aracaju (SE)",
        "Brasilia (DF)",
        "Campo Grande (MS)",
        "Florianopolis (SC)",
        "Natal (RN)",
        "Recife (PE)",
        "Rio de Janeiro (RJ)",
        "Salvador (BH)",
        "Sao Paulo (SP)"
    ]
)

flight_type = st.selectbox(
    "Flight Type",
    ["economic", "firstClass", "premium"]
)

agency = st.selectbox(
    "Agency",
    ["CloudFy", "FlyingDrops", "Rainbow"]
)

day = st.number_input("Day", min_value=1, max_value=31, value=1)
week_day = st.number_input("Week Day", min_value=1, max_value=7, value=1)
week_no = st.number_input("Week Number", min_value=1, max_value=53, value=1)

# -----------------------------
# Prediction
# -----------------------------


if st.button("Predict Price"):

    df = pd.DataFrame(columns=feature_columns)
    df.loc[0] = 0

    df["day"] = day
    df["week_day"] = week_day
    df["week_no"] = week_no

    if f"from_{from_city}" in df.columns:
        df[f"from_{from_city}"] = 1

    if f"destination_{destination}" in df.columns:
        df[f"destination_{destination}"] = 1

    if f"flightType_{flight_type}" in df.columns:
        df[f"flightType_{flight_type}"] = 1

    if f"agency_{agency}" in df.columns:
        df[f"agency_{agency}"] = 1

    prediction = model.predict(df)

    st.success(f"Predicted Flight Price : {prediction[0]:.2f}")