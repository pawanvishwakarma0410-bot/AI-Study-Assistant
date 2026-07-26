import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

from prompts import PROMPT_TEMPLATE

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY not found in .env file")
    st.stop()

client = Groq(api_key=api_key)

st.set_page_config(page_title="AI Study Assistant")

st.title("📚 AI Study Assistant")

st.write("Ask anything and choose an expert role.")

role = st.selectbox(
    "Choose Role",
    [
        "Teacher",
        "Software Engineer",
        "Career Counselor",
        "Doctor",
        "Java Professor",
        "Nutritionist"
    ]
)

question = st.text_area("Enter your Question")

if st.button("Generate Answer"):

    if question:

        prompt = PROMPT_TEMPLATE.format(
            role=role,
            question=question
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.subheader("Answer")
        st.write(response.choices[0].message.content)

    else:
        st.warning("Please enter a question.")