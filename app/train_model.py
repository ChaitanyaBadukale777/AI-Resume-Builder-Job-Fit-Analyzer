from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# Example corpus (this should be your actual training data)
corpus = [
    "Looking for a data scientist with experience in AI and machine learning.",
    "We need a software engineer skilled in Python, Java, and SQL.",
    "A UX/UI designer with experience in web design and user testing."
]

# Initialize the vectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer to the corpus
vectorizer.fit(corpus)

# Save the vectorizer to a .pkl file
model_path = 'app/models/vectorizer.pkl'  # Path where you want to save the vectorizer
joblib.dump(vectorizer, model_path)

print("Vectorizer model saved to:", model_path)
