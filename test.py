from parser import extract_text_from_pdf
from ranker import get_score

# 1. Read resume
resume = extract_text_from_pdf("sample.pdf")

# 2. Sample job description
job = """
Machine Learning Engineer required.

Skills required:
Python, Machine Learning, Data Science, SQL, Deep Learning.

Responsibilities:
Build ML models, work with datasets, and deploy AI solutions.
"""

# 3. Get similarity score
score = get_score(resume, job)

# 4. Print result
print("\n========== AI RECRUITER RESULT ==========")
print("Match Score:", score)
print("=========================================\n")