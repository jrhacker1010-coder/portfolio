import streamlit as st
import os
from groq import Groq

st.set_page_config(page_title="Harsh | AI Portfolio", layout="wide")

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are an AI assistant for Harsh's portfolio website.

ONLY answer questions related to:
- Harsh's education
- Harsh's skills
- Harsh's projects
- Harsh as an AI Full Stack Developer

Profile:
Name: Harsh
Role: AI Full Stack Developer
Education: B.Tech IT (2nd Year)
Skills: HTML, CSS, JavaScript, Python, Flask, AI APIs
Projects:
- AI Resume Builder
- To-Do List Web App
- Portfolio Website

If the user asks anything unrelated, politely redirect them.
"""

# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

st.sidebar.title("🤖 Portfolio Chatbot")
user_input = st.sidebar.text_input("Ask about my portfolio")

# MAIN UI
st.title("👋 Hi, I'm Harsh")
st.subheader("AI Full Stack Developer | 2nd Year B.Tech IT")

st.write("This is my portfolio with a Groq-powered AI chatbot.")

# CHATBOT LOGIC
if user_input and user_input.strip():
    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input.strip()}
            ],
            temperature=0.4,
            max_tokens=512
        )

        reply = completion.choices[0].message.content
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("AI", reply))

    except Exception as e:
        st.error("Groq API error. Please try again.")
        st.stop()

# DISPLAY CHAT
for role, msg in st.session_state.chat:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")
