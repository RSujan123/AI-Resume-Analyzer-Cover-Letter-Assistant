from sklearn.feature_extraction.text import CountVectorizer
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

def extract_keywords(text, num_keywords=10):
    text = clean_text(text)
    vectorizer = CountVectorizer(stop_words='english', max_features=num_keywords)
    vectorizer.fit([text])
    keywords = vectorizer.get_feature_names_out()
    return list(keywords)

def find_missing_keywords(resume_text, job_text):
    resume_text = clean_text(resume_text)
    job_keywords = extract_keywords(job_text)
    missing = [kw for kw in job_keywords if kw not in resume_text]
    return missing
