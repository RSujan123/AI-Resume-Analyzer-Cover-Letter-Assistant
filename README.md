# 🧠 AI Resume Analyzer & Cover Letter Assistant (Flask + NLP)

An intelligent web application that evaluates resumes against job descriptions, identifies skill gaps, and generates personalized cover letters — built with Flask, NLP, and interactive charts.

---

## 🚀 Features

- ⚡ **Resume-Job Match Scoring** using TF-IDF and cosine similarity  
- 🔍 **Keyword Gap Detection** to highlight missing resume terms  
- 📈 **Visual Score Feedback** with animated doughnut and bar charts (Chart.js)  
- 🧠 **Automatic Skill Extraction** from resumes using a curated skills list  
- ✍️ **Dynamic Cover Letter Generator** with real data integration  
- 📥 **Downloadable Cover Letter** as `.txt` file  
- ✅ **Two-Step User Flow**: evaluate first, generate letter next  

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask  
- **Frontend**: HTML, CSS, JavaScript (Chart.js)  
- **NLP & Logic**: Scikit-learn (TF-IDF), PDFMiner  
- **Templating**: Jinja2  
- **File Handling**: Resume and JD as `.pdf` uploads  

---

## 📂 Project Structure

```
resume-evaluator/
├── app.py                          # Main Flask app logic
├── resume_parser.py                # Extracts text from PDFs
├── resume_matcher.py               # Calculates match score using TF-IDF
├── keyword_suggester.py            # Identifies missing keywords
├── skill_extractor.py              # Pulls skills from resume using dictionary
├── skills_list.txt                 # List of technical & soft skills
├── cover_template.txt              # Template for auto-filled cover letters
├── static/
│   └── style.css                   # Yellow-black themed UI
├── templates/
│   └── index.html                  # Frontend form & result page
```

---

## 📦 Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

2. **Install Required Packages**

```bash
pip install flask scikit-learn pdfminer.six
```

3. **Run the Application**

```bash
python app.py
```

4. **Visit the App**

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

### 🔹 Step 1: Resume & Job Description Upload
- Extracts plain text from uploaded PDFs  
- Calculates **match score** using TF-IDF + cosine similarity  
- Detects **missing keywords** from job description  

### 🔹 Step 2: Cover Letter Generation
- User enters name, company, and job role  
- App auto-fills a professional letter using:
  - Extracted resume skills  
  - Job-specific details  
- Letter is downloadable as `.txt`  

---

## 📈 Visuals

- **Doughnut Chart**: Shows match vs. gap percentage  
- **Bar Chart**: Displays keyword match vs. missing count  

All powered by Chart.js for smooth UI integration.

---

## 🧪 Sample Skills List (`skills_list.txt`)

```
python
java
c++
html
css
javascript
react
node.js
django
flask
sql
mysql
mongodb
git
linux
aws
azure
docker
kubernetes
tensorflow
pandas
numpy
excel
communication
teamwork
leadership
```

---

## 🧠 NLP Algorithms Used

- **TF-IDF Vectorizer**: Converts resume & JD into numerical vectors  
- **Cosine Similarity**: Measures how close the vectors are  
- **Keyword Matching**: Finds which expected skills are missing  

---

## 📥 Download Feature

- Users can download the generated cover letter as a `.txt` file using Flask’s `send_file()` function.

---

## 💼 Use Cases

- Job seekers analyzing and improving their resumes  
- Career counselors giving feedback  
- ATS optimization demonstration  
- Academic or portfolio NLP projects  

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Sujan Chintu**  
💼 [LinkedIn](https://linkedin.com/in/your-profile)  
💻 [GitHub](https://github.com/your-username)  
📧 sujanchintu@example.com

---

> Feel free to fork this project, customize the skills list, or deploy it online using Render/Fly.io!
