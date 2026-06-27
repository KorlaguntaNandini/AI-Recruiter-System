from parser import extract_text_from_pdf
from ranker import get_score
import openpyxl

candidates = ["sample.pdf"]

job = """
Machine Learning Engineer required.
Skills: Python, Machine Learning, SQL, Data Science, Deep Learning.
"""

results = []

for file in candidates:
    resume = extract_text_from_pdf(file)
    score = get_score(resume, job)
    results.append((file, score))

results.sort(key=lambda x: x[1], reverse=True)

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Ranking"

ws.append(["Candidate", "Score"])

for r in results:
    ws.append([r[0], r[1]])

wb.save("ranking_output.xlsx")

print("Excel file created: ranking_output.xlsx")