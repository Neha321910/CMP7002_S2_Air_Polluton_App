import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_data.csv", parse_dates=["datetime"])
    return df

df = load_data()

# --- Page Config ---
st.set_page_config(page_title="Beijing Air Quality Dashboard", layout="wide")

st.title("Beijing Air Quality Analysis Dashboard")
st.markdown("CMP7005 – From Data to Application Development")

# --- Sidebar Navigation ---
page = st.sidebar.radio("Navigate", ["Data Overview", "EDA", "Prediction Model"])

# ------------------------
# Data Overview Section
# ------------------------
if page == "Data Overview":
    st.header("Raw Data Preview")
    st.write(df.head())

    st.subheader("Column List")
    st.write(df.columns.tolist())

    st.subheader("Statistical Summary")
    st.write(df.describe())

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

# ------------------------
# EDA Section
# ------------------------
elif page == "EDA":
    st.header("Exploratory Data Analysis")

    # PM2.5 Histogram
    st.subheader("PM2.5 Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(df["PM2.5"], bins=50, kde=True, ax=ax1, color="salmon")
    ax1.set_title("Distribution of PM2.5")
    st.pyplot(fig1)

    # Correlation Heatmap (only numeric)
    st.subheader("Correlation Heatmap (numeric features only)")
    numeric_df = df.select_dtypes(include='number')
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax2)
    ax2.set_title("Feature Correlation Matrix")
    st.pyplot(fig2)

    # PM2.5 Boxplot by Station
    st.subheader("PM2.5 by Station")
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=df, x="station", y="PM2.5", palette="Set2", ax=ax3)
    ax3.set_title("PM2.5 Distribution Across Stations")
    st.pyplot(fig3)

    # Wind Speed vs PM2.5
    st.subheader("Wind Speed vs PM2.5 Scatter")
    fig4, ax4 = plt.subplots()
    sns.scatterplot(data=df, x="WSPM", y="PM2.5", hue="station", alpha=0.5, ax=ax4)
    ax4.set_title("Wind Speed vs PM2.5")
    st.pyplot(fig4)

# ------------------------
# Prediction Section
# ------------------------
elif page == "Prediction Model":
    st.header("Predict PM2.5 using Linear Regression")

    features = ["PM10", "SO2", "NO2", "CO", "O3", "TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
    X = df[features]
    y = df["PM2.5"]

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train model
    model = LinearRegression()
    model.fit(X_scaled, y)
    y_pred = model.predict(X_scaled)

    st.subheader("Actual vs Predicted PM2.5")
    result_df = pd.DataFrame({
        "datetime": df["datetime"],
        "Actual PM2.5": y,
        "Predicted PM2.5": y_pred
    }).set_index("datetime")

    st.line_chart(result_df.head(500))

    st.subheader("Feature Coefficients")
    st.write(pd.DataFrame({
        "Feature": features,
        "Coefficient": model.coef_
    }))
