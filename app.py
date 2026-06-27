import streamlit as st
from parser import extract_text_from_pdf
from ranker import get_score
import tempfile
import openpyxl

st.set_page_config(page_title="AI Recruiter System", layout="wide")

st.title("🧠 AI Recruiter System")
st.subheader("Explainable AI Resume Ranking Engine")

st.info("Bias-Free AI: This system evaluates candidates only on skills & experience, not personal attributes.")

job = st.text_area("📄 Enter Job Description", height=200)

uploaded_files = st.file_uploader(
    "📁 Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("🚀 Rank Candidates"):

    if not uploaded_files or not job:
        st.error("Please upload resumes and enter job description")

    else:
        results = []

        with st.spinner("AI analyzing resumes... 🤖"):

            for file in uploaded_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(file.read())
                    tmp_path = tmp.name

                resume_text = extract_text_from_pdf(tmp_path)

                score, reasons, skills, confidence, missing = get_score(resume_text, job)

                results.append({
                    "name": file.name,
                    "score": score,
                    "reasons": reasons,
                    "skills": skills,
                    "confidence": confidence,
                    "missing": missing
                })

        results.sort(key=lambda x: x["score"], reverse=True)

        st.success("Ranking Completed 🎯")

        st.write("## 🏆 Ranked Candidates")

        for i, r in enumerate(results, 1):

            st.markdown(f"""
            ## #{i} {r['name']}
            **Score:** {r['score']} | **Confidence:** {r['confidence']}
            """)

            st.write("### 🧠 Skills Found")
            st.write(", ".join(r["skills"]) if r["skills"] else "None")

            st.write("### 📌 Why this score")
            for reason in r["reasons"]:
                st.write(reason)

            st.write("### ❌ Why NOT selected (Skill gaps)")
            if r["missing"]:
                for m in r["missing"]:
                    st.error(f"Missing: {m}")
            else:
                st.success("No major skill gaps")

            st.write("---")

        # OPTIONAL: Excel export button
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Ranking"

        ws.append(["Candidate", "Score", "Confidence"])

        for r in results:
            ws.append([r["name"], r["score"], r["confidence"]])

        wb.save("ranking_output.xlsx")

        st.success("Excel file generated: ranking_output.xlsx")