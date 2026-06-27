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

# sort descending
results.sort(key=lambda x: x[1], reverse=True)

# create Excel file
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Ranking"

# headers
ws.append(["Candidate", "Score"])

# data
for r in results:
    ws.append([r[0], r[1]])

wb.save("ranking_output.xlsx")

print("Excel file created: ranking_output.xlsx")