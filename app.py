import streamlit as st
import json
from datetime import datetime

# Load daily challenges
with open("challenges.json", "r") as f:
    challenges = json.load(f)

# Get today's date
today = datetime.today().strftime("%Y-%m-%d")
day_index = datetime.today().day % len(challenges)

# Set page config
st.set_page_config(page_title="Growth Mindset", page_icon="🌱", layout="centered")

# Title
st.title("🌱 Growth Mindset Challenge")
st.caption("Built with 💚 using Streamlit")

st.markdown(f"### 📅 Today's Date: `{today}`")
st.divider()

# Show challenge
st.markdown("## 🧩 Your Challenge")
st.info(challenges[day_index])

# Activity Section
st.divider()
st.markdown("## ✍️ Today's Activity")

journal = st.text_area("📝 Reflect on this challenge. What did you learn or try?")
goal = st.text_input("🎯 Write one small goal for today:")
photo = st.file_uploader("📸 Upload a photo that shows your progress (optional)", type=["jpg", "png"])

# Mark complete
if "completed_days" not in st.session_state:
    st.session_state.completed_days = []

if st.button("✅ Submit Activity"):
    if today not in st.session_state.completed_days:
        st.session_state.completed_days.append(today)
        st.success("Awesome! Your activity is saved. Keep growing! 🌟")
    else:
        st.warning("You already submitted today's challenge.")

# Progress section
st.divider()
st.markdown("## 📅 Your Progress")
if st.session_state.completed_days:
    for d in st.session_state.completed_days:
        st.write(f"✔️ {d}")
else:
    st.write("No challenges completed yet. Start your journey today! 🚀")

# Quote of the day
st.divider()
st.markdown("## 💬 Quote of the Day")
quotes = [
    "Believe you can and you're halfway there.",
    "Progress, not perfection.",
    "Your only limit is you.",
    "Mistakes are proof that you're trying.",
    "Growth happens outside your comfort zone."
]
quote_index = datetime.today().day % len(quotes)
st.success(quotes[quote_index])
