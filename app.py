import os
from datetime import date

import streamlit as st
from google import genai
from dotenv import load_dotenv

from agent.graph import build_exam_agent

load_dotenv()

st.set_page_config(
    page_title="AI Exam Recovery Agent",
    page_icon="🎓",
    layout="wide"
)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY is not configured.")
    st.stop()

client = genai.Client(api_key=api_key)
exam_agent = build_exam_agent(client)

st.title("🎓 AI Exam Recovery Agent")
st.write(
    "Create a realistic study recovery plan when your exam is approaching "
    "and you still have unfinished topics."
)

st.divider()
st.subheader("📋 Enter Your Exam Details")

exam_date = st.date_input(
    "Exam Date",
    min_value=date.today()
)

subjects = st.text_area(
    "Subjects",
    placeholder="Example:\nOperating Systems\nDBMS\nDAA"
)

completed_topics = st.text_area(
    "Topics / Units Already Completed",
    placeholder="Example:\nOS - Unit 1\nDBMS - Units 1 and 2"
)

remaining_topics = st.text_area(
    "Topics / Units Remaining",
    placeholder="Example:\nOS - Units 2, 3, 4, 5\nDBMS - Units 3, 4, 5"
)

hours_per_day = st.number_input(
    "How many hours can you study per day?",
    min_value=1.0,
    max_value=16.0,
    value=4.0,
    step=0.5
)

difficulty = st.selectbox(
    "Overall syllabus difficulty",
    ["Easy", "Moderate", "Difficult", "Very difficult"]
)

additional_info = st.text_area(
    "Additional Information",
    placeholder="Example: I have college from 9 AM to 4 PM."
)

study_days = max((exam_date - date.today()).days, 1)

st.info(f"📅 Approximately {study_days} study day(s) before the exam.")

if st.button("🚀 Create My Recovery Plan", type="primary"):

    if not subjects.strip():
        st.warning("Please enter your subjects.")
        st.stop()

    if not remaining_topics.strip():
        st.warning("Please enter your remaining topics.")
        st.stop()

    initial_state = {
        "exam_date": str(exam_date),
        "subjects": subjects,
        "completed_topics": completed_topics,
        "remaining_topics": remaining_topics,
        "hours_per_day": hours_per_day,
        "study_days": study_days,
        "difficulty": difficulty,
        "additional_info": additional_info,
        "recovery_plan": ""
    }

    with st.spinner("Analyzing your exam situation..."):
        result = exam_agent.invoke(initial_state)

    st.success("Your recovery plan is ready!")
    st.divider()
    st.subheader("📚 Your AI Exam Recovery Plan")
    st.markdown(result["recovery_plan"])

    st.divider()
    st.caption(
        "This is an AI-generated study aid. Adjust the plan to your "
        "actual schedule and academic requirements."
    )
