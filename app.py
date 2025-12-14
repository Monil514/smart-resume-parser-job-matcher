import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from parser.resume_parser import extract_skills, load_skills, get_missing_skills
from matcher.job_matcher import match_resume_with_jd, extract_jd_skills

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Resume Parser & Job Matcher",
    page_icon="📄",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.card {
    background-color: #1c1e26;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}
.skill-box {
    display: inline-block;
    background-color: #262730;
    color: white;
    padding: 6px 12px;
    margin: 4px;
    border-radius: 20px;
    font-size: 14px;
}
.missing-box {
    background-color: #402020;
}
.center {
    text-align: center;
}
.stButton > button {
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    padding: 10px 25px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 class='center'>📄 Smart Resume Parser & Job Matcher</h1>", unsafe_allow_html=True)
st.markdown("<p class='center'>AI-powered resume screening & job compatibility analysis</p>", unsafe_allow_html=True)
st.divider()

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])

with col2:
    job_description = st.text_area(
        "📝 Paste Job Description",
        height=180,
        placeholder="Paste the job description here..."
    )

analyze_btn = st.button("🚀 Analyze Resume")

# ---------------- PROCESS ----------------
if analyze_btn:
    if not uploaded_file:
        st.warning("⚠️ Please upload a resume PDF.")
    elif not job_description.strip():
        st.warning("⚠️ Please paste a job description.")
    else:
        with st.spinner("🔍 Analyzing resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)

            skills_list = load_skills()
            resume_skills = extract_skills(resume_text, skills_list)
            jd_skills = extract_jd_skills(job_description, skills_list)
            missing_skills = get_missing_skills(resume_skills, jd_skills)

            match_score = match_resume_with_jd(resume_text, job_description)

        st.divider()

        # ---------------- SKILLS SECTION ----------------
        col3, col4 = st.columns(2)

        with col3:
            st.markdown("<div class='card'><h3>✅ Resume Skills</h3>", unsafe_allow_html=True)
            if resume_skills:
                for skill in resume_skills:
                    st.markdown(f"<span class='skill-box'>{skill}</span>", unsafe_allow_html=True)
            else:
                st.info("No skills detected.")
            st.markdown("</div>", unsafe_allow_html=True)

        with col4:
            st.markdown("<div class='card'><h3>📌 Job Description Skills</h3>", unsafe_allow_html=True)
            if jd_skills:
                for skill in jd_skills:
                    st.markdown(f"<span class='skill-box'>{skill}</span>", unsafe_allow_html=True)
            else:
                st.info("No skills detected.")
            st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- MISSING SKILLS ----------------
        st.markdown("<div class='card'><h3>❌ Missing Skills</h3>", unsafe_allow_html=True)
        if missing_skills:
            for skill in missing_skills:
                st.markdown(f"<span class='skill-box missing-box'>{skill}</span>", unsafe_allow_html=True)
        else:
            st.success("🎉 No missing skills! Resume is a strong match.")
        st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- SCORE ----------------
        st.markdown("<div class='card center'>", unsafe_allow_html=True)
        st.markdown("## 📊 Compatibility Score")
        st.progress(match_score / 100)
        st.markdown(f"<h2>{match_score}% Match</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("👆 Upload a resume and paste a job description, then click **Analyze Resume**.")
