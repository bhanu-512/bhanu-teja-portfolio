from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Bhanu Teja Chintalakunta | Portfolio",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_path = Path(__file__).parent / "index.html"
st.iframe(html_path, width="stretch", height="content")
