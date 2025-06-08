def load_skills(file_path="skills_list.txt"):
    with open(file_path, "r") as f:
        return [skill.strip().lower() for skill in f.readlines()]

def extract_skills_from_resume(resume_text):
    resume_text = resume_text.lower()
    known_skills = load_skills()
    found_skills = [skill for skill in known_skills if skill in resume_text]
    return found_skills
