import spacy

nlp = spacy.load("en_core_web_sm")

def load_skills():
    with open("data/skills.txt", "r") as f:
        return [line.strip().lower() for line in f.readlines()]

def extract_skills(text, skills_list):
    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


def get_missing_skills(resume_skills, jd_skills):
    return list(set(jd_skills) - set(resume_skills))
