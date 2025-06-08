import os
from flask import Flask, request, render_template, send_file
from resume_parser import extract_text_from_pdf
from resume_matcher import calculate_match_score
from keyword_suggester import find_missing_keywords
from skill_extractor import extract_skills_from_resume  # ✅ NEW

app = Flask(__name__)

def generate_cover_letter(template_path, context):
    with open(template_path, "r") as file:
        template = file.read()
    for key, value in context.items():
        template = template.replace(f"{{{{ {key} }}}}", value)
    return template

@app.route("/", methods=["GET", "POST"])
def home():
    match_score = None
    missing_keywords = []
    cover_letter = None
    extracted_skills = []

    if request.method == "POST":
        action = request.form.get("action")

        if action == "match":
            resume = request.files["resume"]
            jobdesc = request.files["jobdesc"]
            resume.save("resume.pdf")
            jobdesc.save("jobdesc.pdf")

            resume_text = extract_text_from_pdf("resume.pdf")
            job_desc_text = extract_text_from_pdf("jobdesc.pdf")

            match_score = calculate_match_score(resume_text, job_desc_text)
            missing_keywords = find_missing_keywords(resume_text, job_desc_text)

        elif action == "generate":
            applicant_name = request.form["applicant_name"]
            hiring_manager = request.form["hiring_manager"]
            job_title = request.form["job_title"]
            company_name = request.form["company_name"]

            # ✅ Extract skills from resume
            resume_text = extract_text_from_pdf("resume.pdf")
            extracted_skills = extract_skills_from_resume(resume_text)
            skills_string = ", ".join(extracted_skills) if extracted_skills else "relevant skills"

            context = {
                "applicant_name": applicant_name,
                "hiring_manager": hiring_manager,
                "job_title": job_title,
                "company_name": company_name,
                "skills": skills_string,
                "experience_highlights": "full-stack development, REST API integration"
            }

            cover_letter = generate_cover_letter("cover_template.txt", context)

    return render_template("index.html",
                           match_score=match_score,
                           missing_keywords=missing_keywords,
                           cover_letter=cover_letter,
                           extracted_skills=extracted_skills)

@app.route("/download")
def download_cover_letter():
    cover_letter_text = request.args.get("text", "")
    file_path = "generated_cover_letter.txt"
    with open(file_path, "w") as f:
        f.write(cover_letter_text)
    return send_file(file_path, as_attachment=True)
if __name__ == "__main__":
    app.run(port=5000)

