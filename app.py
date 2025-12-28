import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

if 'messages' not in st.session_state:
    st.session_state.messages = []

st.markdown("""
<style>
.stApp { background: #0f0f0f; color: white; }
.hero { text-align: center; padding: 2rem; }
.hero h1 { font-size: 3rem; background: linear-gradient(45deg, #00ff88, #00aaff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.section { margin: 2rem 0; }
.skill { background: #2a2a2a; color: #00ff88; padding: 0.5rem 1rem; margin: 0.25rem; border-radius: 20px; display: inline-block; }
.project { background: #1a1a1a; padding: 1.5rem; margin: 1rem 0; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>Harsh</h1>
    <p>AI Full Stack Developer | 2nd Year B.Tech IT Student</p>
</div>
""", unsafe_allow_html=True)

# About Section
st.markdown('<div class="section"><h2>About Me</h2><p>Passionate AI Full Stack Developer with focus on building intelligent web applications and scalable systems.</p></div>', unsafe_allow_html=True)

# Skills Section
st.markdown('<div class="section"><h2>Skills</h2>', unsafe_allow_html=True)
skills = ["HTML", "CSS", "JavaScript", "Python", "Flask", "AI APIs"]
for skill in skills:
    st.markdown(f'<span class="skill">{skill}</span>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
st.markdown('<div class="section"><h2>Projects</h2>', unsafe_allow_html=True)
projects = [
    "AI Resume Builder - AI-powered resume creation tool",
    "To-Do List Web App - Modern task management application", 
    "AI-Powered Portfolio Website - Dynamic portfolio with AI chatbot"
]
for project in projects:
    st.markdown(f'<div class="project">{project}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Chatbot Section
st.markdown('<div class="section"><h2>AI Assistant</h2>', unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about Harsh's skills, projects, or background"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        system_prompt = """You are Harsh's portfolio assistant. Only answer about Harsh, his skills (HTML, CSS, JavaScript, Python, Flask, AI APIs), projects (AI Resume Builder, To-Do List Web App, Portfolio Website), and background. Redirect unrelated questions."""
        
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)
            
    except Exception as e:
        st.error(f"Error: {str(e)}")
