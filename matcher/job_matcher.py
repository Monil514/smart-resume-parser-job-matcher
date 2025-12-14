from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_with_jd(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)


def extract_jd_skills(jd_text, skills_list):
    jd_text = jd_text.lower()
    jd_skills = []

    for skill in skills_list:
        if skill in jd_text:
            jd_skills.append(skill)

    return list(set(jd_skills))
