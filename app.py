app.py
import streamlit as st

st.set_page_config(page_title="Smart Sleep Pattern Analyzer", layout="centered")
st.title("😴 AI-Based Smart Sleep Pattern Analyzer")
st.write("Analyze sleep quality using simple AI logic")

sleep_hours = st.slider("Hours of Sleep", 0, 12, 7)
screen_time = st.slider("Screen Time Before Bed (hours)", 0, 6, 2)
wakeups = st.slider("Number of Night Wake-ups", 0, 10, 1)

if st.button("Analyze Sleep"):
    score = 0
    if sleep_hours >= 7:
        score += 1
    if screen_time <= 2:
        score += 1
    if wakeups <= 2:
        score += 1

    if score == 3:
        st.success("✅ Sleep Quality: GOOD")
    elif score == 2:
        st.warning("⚠️ Sleep Quality: AVERAGE")
    else:
        st.error("❌ Sleep Quality: POOR")

    st.write("This result is generated using basic AI decision logic.")
