import spacy

# Load pre-trained SpaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract skills from resume text
def extract_skills(resume_text):
    skills = []
    doc = nlp(resume_text)
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            skills.append(ent.text)
    return skills
