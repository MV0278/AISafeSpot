import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
import pandas as pd
import plotly.graph_objects as go

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI SafeSpot",
    page_icon="🛡️",
    layout="wide"
)

# ---------- CUSTOM STYLING ----------
st.markdown("""
<style>

.stApp {
    background-image:
        linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
        url("https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
}

h1 {
    font-size: 48px;
    font-weight: 800;
    text-align: center;
}

.block-container {
    background-color: rgba(0,0,0,0.45);
    padding: 25px;
    border-radius: 15px;
}

.stButton > button {
    background: linear-gradient(90deg,#ff512f,#dd2476);
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🛡️ AI SafeSpot")
st.markdown("### Intelligent Women Safety Risk Prediction System")

st.markdown("---")

# ---------- LOAD DATA ----------
data = pd.read_csv("../data/CrimesOnWomenData.csv")

# clean column names
data.columns = data.columns.str.strip()

# ---------- INPUT MODE ----------
mode = st.radio(
    "Choose Input Method",
    ["Select State (Recommended)", "Manual Input"]
)

# ---------- LAYOUT ----------
col1, col2 = st.columns([1,1])

# ---------- INPUT SECTION ----------
with col1:

    st.subheader("📊 Crime Statistics Input")

    # default values
    rape = kidnapping = dowry = assault = minor = dv = trafficking = 0

    if mode == "Select State (Recommended)":

        states = data["State"].unique()
        selected_state = st.selectbox("Select State", states)

        state_data = data[data["State"] == selected_state]

        # dataset column names
        rape = int(state_data["Rape"].sum())
        kidnapping = int(state_data["K&A"].sum())
        dowry = int(state_data["DD"].sum())
        assault = int(state_data["AoW"].sum())
        minor = int(state_data["AoM"].sum())
        dv = int(state_data["DV"].sum())
        trafficking = int(state_data["WT"].sum())

        st.success("Crime statistics automatically loaded from dataset")

        st.write("Rape:", rape)
        st.write("Kidnapping:", kidnapping)
        st.write("Dowry:", dowry)
        st.write("Assault:", assault)

    else:

        rape = st.number_input("Rape cases", min_value=0)
        kidnapping = st.number_input("Kidnapping cases", min_value=0)
        dowry = st.number_input("Dowry deaths", min_value=0)
        assault = st.number_input("Assault cases", min_value=0)
        minor = st.number_input("Assault on minors", min_value=0)
        dv = st.number_input("Domestic violence", min_value=0)
        trafficking = st.number_input("Women trafficking", min_value=0)

    # ---------- PREDICT BUTTON ----------
    predict = st.button("🔍 Predict Safety Risk")

    if predict:

        url = "http://127.0.0.1:8000/predict"

        params = {
            "rape": rape,
            "kidnapping": kidnapping,
            "dowry": dowry,
            "assault": assault,
            "minor": minor,
            "dv": dv,
            "trafficking": trafficking
        }

        response = requests.post(url, params=params)

        result = response.json()

        score = result["risk_score"]

        st.markdown("### 🔐 Predicted Risk Score")

        if score < 0.3:
            st.success(f"Low Risk Area ({score:.2f})")

        elif score < 0.6:
            st.warning(f"Moderate Risk Area ({score:.2f})")

        else:
            st.error(f"High Risk Area ({score:.2f})")

        # ---------- RISK GAUGE ----------
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "Risk Level"},
            gauge={
                'axis': {'range': [0, 1]},
                'bar': {'color': "red"},
                'steps': [
                    {'range': [0, 0.3], 'color': "green"},
                    {'range': [0.3, 0.6], 'color': "yellow"},
                    {'range': [0.6, 1], 'color': "red"}
                ]
            }
        ))

        st.plotly_chart(fig)

# ---------- MAP SECTION ----------
with col2:

    st.subheader("🗺️ Safety Map")

    map = folium.Map(location=[22.5937,78.9629], zoom_start=5)

    cities = [
        ("Delhi",28.6139,77.2090,"High Risk","red"),
        ("Mumbai",19.0760,72.8777,"Moderate Risk","orange"),
        ("Chennai",13.0827,80.2707,"Moderate Risk","orange"),
        ("Bangalore",12.9716,77.5946,"Low Risk","green")
    ]

    for city,lat,lon,risk,color in cities:

        folium.CircleMarker(
            location=[lat,lon],
            radius=10,
            popup=f"{city} - {risk}",
            color=color,
            fill=True
        ).add_to(map)

    st_folium(map, width=None, height=500)

st.markdown("---")

# ---------- DATA INSIGHTS ----------
st.subheader("📊 Crime Risk Analysis")

data["Total_Crime"] = data.iloc[:,3:].sum(axis=1)

top_states = (
    data.groupby("State")["Total_Crime"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.write("### Top 10 High Risk States")
st.bar_chart(top_states)

st.write("### State Safety Ranking")

state_table = (
    data.groupby("State")["Total_Crime"]
    .sum()
    .sort_values()
)

st.dataframe(state_table)

st.write("### Crime Trend Over Years")

trend = data.groupby("Year")["Total_Crime"].sum()

st.line_chart(trend)

st.markdown("---")

st.caption("AI SafeSpot • Women Safety Risk Prediction System")