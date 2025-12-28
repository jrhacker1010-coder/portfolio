import streamlit as st

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Harshanth | AI Full Stack Developer",
    page_icon="⚡",
    layout="wide",
)

# =============================
# CUSTOM CSS (PREMIUM UI)
# =============================
st.markdown("""
<style>
body {
    background-color: #0b0f19;
}
.main-title {
    font-size: 60px;
    font-weight: 800;
    background: linear-gradient(90deg, #6366f1, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    font-size: 22px;
    color: #c7d2fe;
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 0 30px rgba(99,102,241,0.15);
}
.skill {
    display: inline-block;
    background: linear-gradient(135deg, #4f46e5, #06b6d4);
    padding: 10px 16px;
    margin: 6px;
    border-radius: 20px;
    font-weight: 600;
}
.project-card {
    background: rgba(255,255,255,0.04);
    padding: 20px;
    border-radius: 14px;
    border-left: 4px solid #6366f1;
}
.footer {
    text-align: center;
    color: #94a3b8;
    padding: 30px;
}
</style>
""", unsafe_allow_html=True)

# =============================
# HERO SECTION
# =============================
st.markdown("<div class='main-title'>Harshanth</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI Full Stack Developer · 2nd Year B.Tech IT</div>", unsafe_allow_html=True)

st.write("""
I design and build **scalable full-stack applications** with a strong focus on  
**clean UI, performance, and AI integration**.
""")

st.markdown("---")

# =============================
# ABOUT ME
# =============================
st.header("🧠 About Me")

st.markdown("""
<div class="card">
I am a second-year Information Technology student passionate about building
modern web applications and intelligent systems.  
I enjoy turning ideas into **real-world digital products** using clean
architecture and modern development practices.
</div>
""", unsafe_allow_html=True)

# =============================
# SKILLS
# =============================
st.header("🛠 Technical Skills")

skills = [
    "HTML", "CSS", "JavaScript",
    "Python", "Flask", "Streamlit",
    "AI APIs", "Full Stack Development",
    "Git & GitHub"
]

st.markdown("<div class='card'>", unsafe_allow_html=True)
for skill in skills:
    st.markdown(f"<span class='skill'>{skill}</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# =============================
# PROJECTS
# =============================
st.header("🚀 Featured Projects")

projects = [
    ("AI Resume Builder",
     "An AI-powered web application that generates professional resumes dynamically."),
    
    ("To-Do List Web App",
     "A clean and efficient task management application with persistent storage."),
    
    ("AI-Powered Portfolio Website",
     "A modern portfolio platform showcasing skills, projects, and professional profile.")
]

for title, desc in projects:
    st.markdown(f"""
    <div class="project-card">
        <h3>{title}</h3>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

# =============================
# EDUCATION
# =============================
st.header("🎓 Education")

st.markdown("""
<div class="card">
<b>B.Tech – Information Technology</b><br>
2nd Year Undergraduate Student<br>
Focus: Software Engineering & AI Systems
</div>
""", unsafe_allow_html=True)

# =============================
# CONTACT
# =============================
st.header("📬 Contact")

st.markdown("""
<div class="card">
📧 Email: harsh@email.com<br>
🔗 GitHub: https://github.com/<br>
🔗 LinkedIn: https://linkedin.com/in/
</div>
""", unsafe_allow_html=True)

# =============================
# FOOTER
# =============================
st.markdown("""
<div class="footer">
© 2025 Harshanth ·current status 
</div>
""", unsafe_allow_html=True)


