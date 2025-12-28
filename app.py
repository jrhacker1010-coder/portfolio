import streamlit as st
import os
from groq import Groq

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Harsh | AI Full Stack Developer",
    page_icon="🤖",
    layout="wide"
)

# =============================
# GROQ CLIENT
# =============================

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# =============================
# SIDEBAR
# =============================
st.sidebar.title("🤖 AI Portfolio Chatbot")
st.sidebar.write("Ask about my skills, projects, or education")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.sidebar.text_input("Ask me anything about my portfolio")

# =============================
# CHATBOT LOGIC
# =============================

if user_input:
    system_prompt = """
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
Projects: AI Resume Builder, To-Do App, Portfolio Website

If the question is unrelated, politely redirect to portfolio topics.
"""

    if not user_input.strip():
        st.warning("Please ask something about my portfolio 😊")
    else:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.4,
            max_tokens=512
        )

        reply = completion.choices[0].message.content
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("AI", reply))


# =============================
# MAIN PAGE (PORTFOLIO)
# =============================
st.markdown("""
# 👋 Hi, I'm Harsh  
### AI Full Stack Developer | 2nd Year B.Tech IT Student

I build **full-stack web applications** with **AI-powered features**  
using modern tools and APIs.
""")

st.markdown("---")

# =============================
# ABOUT
# =============================
st.header("📌 About Me")
st.write("""
I am a second-year Information Technology student passionate about
building scalable web applications and integrating AI into real-world systems.
""")

# =============================
# SKILLS
# =============================
st.header("🛠 Skills")
cols = st.columns(3)
skills = [
    "HTML", "CSS", "JavaScript",
    "Python", "Flask", "AI APIs",
    "Full Stack Development"
]

for i, skill in enumerate(skills):
    cols[i % 3].success(skill)

# =============================
# PROJECTS
# =============================
st.header("🚀 Projects")

st.subheader("AI Resume Builder")
st.write("A web app that generates professional resumes using AI.")

st.subheader("To-Do List Web App")
st.write("Task management app using JavaScript and localStorage.")

st.subheader("AI-Powered Portfolio Website")
st.write("This portfolio itself includes an AI chatbot using Groq API.")

# =============================
# CONTACT
# =============================
st.header("📬 Contact")
st.write("""
📧 Email: harsh@email.com  
🔗 GitHub: https://github.com/yourusername  
🔗 LinkedIn: https://linkedin.com/in/yourusername
""")

# =============================
# CHAT HISTORY DISPLAY
# =============================
st.markdown("---")
st.header("💬 Chatbot Conversation")

for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")



