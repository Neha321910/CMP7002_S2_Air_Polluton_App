# 🌫️ Beijing Air Quality Analysis and Prediction App

## 📌 Project Overview

This project presents an end-to-end data science application developed for the **CMP7005 "From Data to Application Development"** reassessment. It focuses on analysing, visualising, and predicting air pollution levels in **Beijing, China**, using real-world datasets. A graphical user interface (GUI) was built using **Streamlit** to make the tool accessible for non-technical users.

---

## 📁 Dataset

- **Source**: [UCI Machine Learning Repository – Beijing Multi-Site Air Quality Data](https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data)
- **Files Used**:  
  - `PRSA_Data_Dongsi_20130301-20170228.csv`  
  - `PRSA_Data_Changping_20130301-20170228.csv`  
  - `PRSA_Data_Huairou_20130301-20170228.csv`  
  - `PRSA_Data_Guanyuan_20130301-20170228.csv`  

Each dataset contains hourly air quality measurements including PM2.5, PM10, SO2, NO2, CO, O3, temperature, pressure, wind direction/speed, and humidity.

---

## 🔧 Features

- 📊 **Data Cleaning & Preparation**  
  Missing values handled, data combined and enriched with datetime features.

- 📈 **Exploratory Data Analysis (EDA)**  
  - PM2.5 distribution  
  - Yearly pollution trends  
  - Correlation heatmap  
  - Seasonal effects on pollution

- 🤖 **Predictive Modelling**  
  - Linear Regression  
  - Model evaluation with R² and RMSE metrics  
  - Predictions based on meteorological conditions

- 💻 **Streamlit GUI**  
  - Upload dataset  
  - View visual analytics  
  - Run predictive model  
  - Interactive interface with user-friendly controls

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/air-quality-beijing.git
   cd air-quality-beijing
   ```
2. Create and activate virtual environment (optional)
   ```bash
   python -m venv venv
   venv\Scripts\activate     # For Windows
  
3. Install dependencies
   ```bash
   pip install -r requirements.txt
4. Run Streamlit App
   ```bash
   streamlit run app.py
📂 Repository Structure
├── CMP7005_Full_EDA_Model.ipynb     # Jupyter Notebook with data analysis and model
├── app.py                           # Streamlit GUI
├── data/                            # Raw and cleaned data files
├── figures/                         # Generated visualisations
├── requirements.txt                 # Project dependencies
└── README.md                        # Project documentation
