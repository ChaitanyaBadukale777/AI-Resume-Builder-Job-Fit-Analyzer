import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to train and save the vectorizer
def train_and_save_vectorizer(data, model_path='models/vectorizer.pkl'):
    """
    Train a TF-IDF Vectorizer and save it to a file.
    
    Parameters:
    - data: List of text data (e.g., job descriptions or resumes)
    - model_path: Path to save the trained vectorizer model (default is 'models/vectorizer.pkl')
    """
    vectorizer = TfidfVectorizer(stop_words='english')
    vectorizer.fit(data)  # Train the vectorizer on the text data

    # Save the trained vectorizer to a file
    joblib.dump(vectorizer, model_path)
    print(f"Vectorizer model saved to {model_path}")

# Function to load the vectorizer (used for transforming job descriptions or resumes)
def load_vectorizer(model_path='models/vectorizer.pkl'):
    """
    Load a pre-trained vectorizer from a file.
    
    Parameters:
    - model_path: Path to the saved vectorizer model (default is 'models/vectorizer.pkl')
    
    Returns:
    - vectorizer: The loaded vectorizer model
    """
    vectorizer = joblib.load(model_path)
    return vectorizer

# Function to match resume with job description
def match_resume_with_job(resume, job_description, vectorizer_path='models/vectorizer.pkl'):
    """
    Match a resume with a job description by calculating cosine similarity.
    
    Parameters:
    - resume: The resume text
    - job_description: The job description text
    - vectorizer_path: Path to the saved vectorizer model (default is 'models/vectorizer.pkl')
    
    Returns:
    - match_score: Cosine similarity score between resume and job description
    """
    # Load the pre-trained vectorizer
    vectorizer = load_vectorizer(vectorizer_path)
    
    # Combine the resume and job description into a list for transformation
    documents = [resume, job_description]
    
    # Transform the documents (resume and job description) into vectors
    vectors = vectorizer.transform(documents)
    
    # Calculate the cosine similarity between the resume and the job description
    cosine_sim = cosine_similarity(vectors[0], vectors[1])
    
    # Return the cosine similarity score as the match score
    return cosine_sim[0][0]

# Example usage:
# Training and saving the vectorizer (this part can be run separately once to save the vectorizer)
if __name__ == "__main__":
    # Sample data for training (add real job descriptions here)
    job_descriptions = [
        "Software engineer with experience in Python and Java",
        "Data scientist with a background in machine learning and statistics"
        # Add more job descriptions or text data as needed
    ]
    
    # Train and save the vectorizer
    train_and_save_vectorizer(job_descriptions)
