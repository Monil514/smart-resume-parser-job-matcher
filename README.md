# 📄 Smart Resume Parser & Job Matcher

An AI-powered web application that analyzes resumes and matches them against job descriptions using NLP techniques. The system extracts relevant skills, identifies skill gaps, and generates a compatibility score to help recruiters and job seekers make faster, data-driven decisions.

---

## 🚀 Features

* 📤 Upload resume in **PDF format**
* 🧠 Extract skills from resume using NLP & keyword matching
* 📝 Analyze job description requirements
* ❌ Identify **missing skills**
* 📊 Generate **compatibility score (%)**
* 🎨 Clean, modern **Streamlit UI**
* ⌨️ Supports **Enter key submission**

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Web UI
* **spaCy** – NLP processing
* **Scikit-learn** – TF-IDF & cosine similarity
* **pdfplumber** – PDF text extraction
* **Regex** – Pattern-based parsing

---

## 🧠 How It Works

1. User uploads a resume (PDF)
2. Resume text is extracted
3. Skills are detected from resume and job description
4. Resume & JD are vectorized using **TF-IDF**
5. **Cosine similarity** is used to calculate match score
6. Missing skills are highlighted

---

## 🧱 Project Architecture

```
User
 │
 ▼
Streamlit UI
 │
 ├── Resume Upload (PDF)
 │        │
 │        ▼
 │   PDF Text Extractor
 │        │
 │        ▼
 │   Resume Skill Parser
 │
 ├── Job Description Input
 │        │
 │        ▼
 │   JD Skill Extractor
 │
 └── TF-IDF Vectorizer
          │
          ▼
   Cosine Similarity Engine
          │
          ▼
   Match Score + Missing Skills
```

---

## 📂 Project Structure

```
smart-resume-matcher/
│
├── app.py
├── requirements.txt
├── README.md
│
├── parser/
│   └── resume_parser.py
│
├── matcher/
│   └── job_matcher.py
│
├── utils/
│   └── pdf_reader.py
│
└── data/
    └── skills.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/smart-resume-parser-job-matcher.git
cd smart-resume-parser-job-matcher
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

## 🌍 Real‑World Applications

* 🏢 Applicant Tracking Systems (ATS)
* 👨‍💼 HR automation tools
* 🎓 Campus placement systems
* 🔍 Resume screening platforms
* 💼 Job portals

---

## 🔮 Future Enhancements

* Use **embeddings (Sentence Transformers)** for better accuracy
* Resume improvement suggestions
* PDF download of analysis
* Multi-resume comparison
* Database integration

---

