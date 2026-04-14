import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI SafeSpot", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

with open("AI-SafeSpot-UI.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=1800, scrolling=True)