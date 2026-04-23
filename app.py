import streamlit as st
from data_processor import load_data, compute_kpis
 
# Page config
st.set_page_config(
    page_title="KPI Investigation Agent",
    layout="wide"
)
 
# Title
st.title("🚀 KPI Investigation Agent")
 
# Load data button
if st.button("Load Data"):
    df = load_data()
    st.session_state["df"] = df
 
# If data is loaded
if "df" in st.session_state:
    df = st.session_state["df"]
 
    # Compute KPIs
    kpis = compute_kpis(df)
 
    # Show dataset info
    st.subheader("📊 Dataset Overview")
    st.write("Rows, Columns:", df.shape)
 
    # Layout: 2 columns
    col1, col2 = st.columns(2)
 
    with col1:
        st.subheader("📈 Daily Trips")
        st.line_chart(kpis["daily_trips"])
 
    with col2:
        st.subheader("💰 Average Fare")
        st.metric("Avg Fare", round(kpis["avg_fare"], 2))
 
    # Trips by hour
    st.subheader("⏰ Trips by Hour")
    st.bar_chart(kpis["trips_by_hour"])
 
    # Top zones
    st.subheader("📍 Top Pickup Zones")
    st.write(kpis["top_zones"])
 
    # Optional debug (remove later)
    with st.expander("🔍 View Raw Data"):
        st.dataframe(df.head(50))