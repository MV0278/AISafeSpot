# AI SafeSpot – Women Safety Risk Prediction System

## Overview

AI SafeSpot is a machine learning-based system that predicts women safety risk using crime statistics. It helps identify high-risk areas and provides insights through an interactive dashboard with real-time predictions and visualizations.

## Features

* Predicts safety risk based on crime data
* Classifies risk as Low, Moderate, or High
* Interactive user interface for input and analysis
* Visualizations including charts and safety map
* Supports both manual input and state-based analysis

## Tech Stack

* Python
* Scikit-learn (Machine Learning)
* FastAPI (Backend API)
* Streamlit (Frontend UI)
* Pandas, NumPy (Data Processing)
* Matplotlib, Seaborn, Plotly (Visualization)
* Folium (Map Visualization)
* Jupyter Notebook (Model Training)

## Project Structure

AI-SafeSpot/

├── backend/
│   └── api.py

├── frontend/
│   ├── app.py
│   └── AI-SafeSpot-UI.html

├── model/
│   └── safety_model.pkl

├── data/
│   └── CrimesOnWomenData.csv

├── notebooks/
│   └── train_model.ipynb

├── requirements.txt
└── README.md

## Installation & Setup

1. Clone the repository

git clone https://github.com/MV0278/AI-SafeSpot.git
cd AI-SafeSpot

2. Create virtual environment

python -m venv venv

Activate:

venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

## Running the Application

Run Backend

cd backend
uvicorn api:app --reload

Backend runs at:
http://127.0.0.1:8000

Run Frontend (new terminal)

cd frontend
streamlit run app.py

Frontend runs at:
http://localhost:8501

## How It Works

1. Crime data is used to train a machine learning model
2. The trained model is saved as safety_model.pkl
3. Frontend collects user input
4. Backend API processes input and predicts risk
5. Result is displayed as a safety score and category

## Example Output

* Low Risk (0.2)
* Moderate Risk (0.5)
* High Risk (0.8)

## Future Improvements

* Real-time data integration
* GPS-based location tracking
* Mobile application
* Advanced ML models for higher accuracy
* Interactive heatmap visualization




