# ResuMate: AI Resume Builder 💼🤖

A Machine Learning-powered Streamlit web application that allows users to upload job descriptions and resumes (PDF/DOCX), and generates tailored resumes with a **job fit score** using advanced **NLP techniques** and **text similarity algorithms**.

---

## 🚀 Features

- 📄 Upload Job Descriptions and Resumes in **PDF/DOCX** format
- 🧠 Applies **NLP techniques** for resume-job matching
- 📊 Calculates a **Job Fit Score** using **text similarity** and **classification**
- 📈 Tracks live **user interactions** using **Google Sheets API**
- 🧾 Generates **tailored resumes** based on the uploaded job description

---

## 🔧 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **NLP**: SpaCy, NLTK, Sentence Transformers
- **Similarity Metrics**: Cosine Similarity, TF-IDF, BERT embeddings
- **APIs**: Google Sheets API
- **File Handling**: `pdfplumber`, `docx`, `PyMuPDF`

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/resumate.git
cd resumate

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```


```bash
streamlit run main_app.py
```

## 🤖 NLP & Similarity Matching


ResuMate leverages NLP techniques to analyze both job descriptions and resume content. It uses the following approaches:

- 🔍 **TF-IDF + Cosine Similarity** — to measure textual overlap and relevance between resume and job description.
- 🤖 **BERT Embeddings** *(optional for advanced matching)* — to capture semantic meaning beyond surface-level words.
- 🧠 **Text Classification** — to rank resumes based on suitability for a given job description.


## 📌 To-Do
 Add BERT-based semantic similarity

 Add user authentication

 Export tailored resume suggestions

 Deploy on Streamlit Cloud / Vercel

📷 Screenshots (Optional)
(Add screenshots or a screen recording of your app in action here)

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/) – For building the interactive web UI.
- [Google Sheets API](https://developers.google.com/sheets/api) – For tracking user interactions and analytics.
- [SpaCy](https://spacy.io/) – For natural language processing tasks.
- [NLTK](https://www.nltk.org/) – For classic NLP operations like tokenization and stemming.
- [HuggingFace Transformers](https://huggingface.co/transformers/) – For advanced NLP and BERT-based embeddings.


