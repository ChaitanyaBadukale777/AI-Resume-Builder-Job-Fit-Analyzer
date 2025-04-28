import google.generativeai as genai

# Initialize Gemini with your API key
genai.configure(api_key="")

def generate_resume(job_desc_text):
    model = genai.GenerativeModel('gemini-1.5-pro')  # or 'gemini-pro' based on your access
    response = model.generate_content(
        f"Create a professional resume tailored to the following job description:\n\n{job_desc_text}\n\nThe resume should be well-structured, detailed, and highlight relevant skills and experiences."
    )
    return response.text
