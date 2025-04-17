import streamlit as st
import json
from datetime import datetime

# Load challenges
with open("challenges.json", "r") as f:
    challenges = json.load(f)

# Today's date
today = datetime.today().strftime("%Y-%m-%d")
index = datetime.today().day % len(challenges)

# Streamlit App
st.title("🌱 Growth Mindset Challenge")
st.subheader(f"Today's Date: {today}")

st.markdown("## 🧩 Your Challenge for Today")
st.info(challenges[index])

# Progress Tracking
st.markdown("## ✅ Mark as Complete")
if "completed" not in st.session_state:
    st.session_state.completed = []

if st.button("✅ I completed this challenge!"):
    if today not in st.session_state.completed:
        st.session_state.completed.append(today)
        st.success("Great job! Keep growing! 🌟")
    else:
        st.warning("You've already completed today's challenge.")

# Show completed days
st.markdown("## 📅 Your Progress")
if st.session_state.completed:
    st.write("You've completed challenges on:")
    for date in st.session_state.completed:
        st.write(f"✔️ {date}")
else:
    st.write("No challenges completed yet.")

# Motivational Quote
st.markdown("## 💬 Quote of the Day")
quotes = [
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only limit to our realization of tomorrow is our doubts of today."
]
quote_index = datetime.today().day % len(quotes)
st.success(quotes[quote_index])