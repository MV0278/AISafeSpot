# AI SafeSpot: Women Safety Risk Predictor

## Overview
AI SafeSpot is an AI-powered system that predicts women safety risk levels using crime data. It analyzes multiple crime factors and generates a risk score to help users understand safety conditions across regions.

---

## Features
- Predicts safety risk (Low / Moderate / High)
- Visualizes crime data trends
- Interactive safety map
- High-risk state analysis
- Real-time prediction using API

---

## How It Works
1. User inputs crime statistics or selects a state  
2. Frontend sends data to backend via API  
3. Backend processes data using machine learning logic  
4. Risk score (0–1) is generated  
5. Results are displayed with visual insights  

---

## Tech Stack
- Frontend: Streamlit  
- Backend: FastAPI  
- Machine Learning: Scikit-learn  
- Data Processing: Pandas, NumPy  
- Visualization: Plotly, Matplotlib, Seaborn  
- Maps: Folium  

---

## Dataset
The dataset contains crime statistics related to women safety in India.

Source: Kaggle – Crimes Against Women Dataset  
(Note: Dataset is not included due to size constraints)

---

## Risk Score Interpretation

| Score Range | Risk Level |
|------------|-----------|
| 0 – 0.3    | Low Risk |
| 0.3 – 0.6  | Moderate Risk |
| 0.6 – 1.0  | High Risk |

---

## Installation & Setup

### Clone the repository
```bash
git clone https://github.com/MV0278/AISafeSpot.git
cd AISafeSpot
