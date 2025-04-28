from fpdf import FPDF

# Function to generate a PDF from the resume content
def generate_pdf(resume_text):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, resume_text)
    
    pdf.output("generated_resume.pdf")
