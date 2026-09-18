import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

from agent.graph import build_gift_agent

load_dotenv()

st.set_page_config(
    page_title="AI Gift Recommendation Agent",
    page_icon="🎁",
    layout="wide"
)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY is not configured.")
    st.stop()

client = genai.Client(api_key=api_key)
gift_agent = build_gift_agent(client)

st.title("🎁 AI Gift Recommendation Agent")
st.write(
    "Get personalized gift ideas based on the recipient, occasion, "
    "interests, relationship, and budget."
)

st.divider()
st.subheader("🎀 Enter Gift Details")

recipient = st.text_input(
    "Who is the gift for?",
    placeholder="Example: Best friend"
)

age = st.number_input(
    "Recipient age",
    min_value=1,
    max_value=100,
    value=20
)

occasion = st.selectbox(
    "Occasion",
    [
        "Birthday", "Anniversary", "Graduation", "Festival",
        "Wedding", "Farewell", "Thank You", "Just Because", "Other"
    ]
)

interests = st.text_area(
    "Interests / hobbies",
    placeholder="Example: Dance, music, books, skincare, photography"
)

budget = st.number_input(
    "Budget (₹)",
    min_value=100,
    max_value=100000,
    value=1000,
    step=100
)

relationship = st.text_input(
    "Your relationship with the person",
    placeholder="Example: Close friend"
)

preferences = st.text_area(
    "Gift preferences or restrictions",
    placeholder="Example: Avoid clothes. They like useful and personalized gifts."
)

delivery = st.selectbox(
    "Preferred gift type",
    ["Physical gift", "DIY / handmade", "Experience", "Digital gift", "Any"]
)

if st.button("🎁 Find Gift Ideas", type="primary"):
    if not recipient.strip():
        st.warning("Please enter who the gift is for.")
        st.stop()

    if not interests.strip():
        st.warning("Please enter the person's interests or hobbies.")
        st.stop()

    initial_state = {
        "recipient": recipient,
        "age": int(age),
        "occasion": occasion,
        "interests": interests,
        "budget": int(budget),
        "relationship": relationship,
        "preferences": preferences,
        "delivery": delivery,
        "recommendations": ""
    }

    with st.spinner("Finding thoughtful gift ideas..."):
        result = gift_agent.invoke(initial_state)

    st.success("Your gift recommendations are ready!")
    st.divider()
    st.subheader("🎁 Recommended Gifts")
    st.markdown(result["recommendations"])

    st.divider()
    st.caption(
        "These are AI-generated suggestions. Check current prices, "
        "availability, and suitability before purchasing."
    )
