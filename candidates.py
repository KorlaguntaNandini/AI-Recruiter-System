from parser import extract_text_from_pdf
from ranker import get_score

candidates = [
    "sample.pdf",   # you can duplicate later for testing
]

job = """
Machine Learning Engineer required.
Skills: Python, Machine Learning, SQL, Data Science, Deep Learning.
"""

results = []

for file in candidates:
    resume = extract_text_from_pdf(file)
    score = get_score(resume, job)
    results.append((file, score))

# Sort by score
results.sort(key=lambda x: x[1], reverse=True)

print("\n========== AI CANDIDATE RANKING ==========")
for i, (name, score) in enumerate(results, 1):
    print(f"{i}. {name} → {score}")

print("=========================================\n")