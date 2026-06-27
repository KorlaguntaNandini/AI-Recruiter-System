import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,@-]', '', text)
    return text.strip()


def extract_skills(text):
    skills_db = [
        "python", "machine learning", "deep learning", "nlp",
        "sql", "pandas", "numpy", "tensorflow", "pytorch",
        "data science", "streamlit", "flask", "scikit-learn"
    ]

    text_lower = text.lower()
    found = []

    for skill in skills_db:
        if skill in text_lower:
            found.append(skill)

    return found