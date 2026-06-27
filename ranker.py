from sentence_transformers import SentenceTransformer, util
from utils import extract_skills

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_score(resume, job):

    emb1 = model.encode(resume, convert_to_tensor=True)
    emb2 = model.encode(job, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2).item() * 100

    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job)

    matched = []
    missing = []
    reasons = []

    for skill in job_skills:
        if skill in resume_skills:
            matched.append(skill)
            reasons.append(f"+ {skill} matched")
        else:
            missing.append(skill)
            reasons.append(f"- Missing {skill}")

    match_ratio = len(matched) / (len(job_skills) + 1)
    score += match_ratio * 20

    if score >= 80:
        confidence = "HIGH"
    elif score >= 50:
        confidence = "MEDIUM"
    else:
        confidence = "LOW"

    return round(score, 2), reasons, resume_skills, confidence, missing