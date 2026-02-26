from fpdf import FPDF


class ProjectDoc(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Python Course: Professional Documentation", 0, 1, "C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, "L", True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 7, body)
        self.ln()


pdf = ProjectDoc()
pdf.add_page()

# Section 1
pdf.chapter_title("1. Overview")
pdf.chapter_body(
    "This documentation covers the 'py_course' repository, a structured Python learning path from core basics to modular application development. The project demonstrates proficiency in Python syntax, file handling, and modular software design."
)

# Section 2
pdf.chapter_title("2. Workflow & Architecture")
pdf.chapter_body(
    "The application follows a modular architecture:\n- Validation Layer: Ensures clean data entry using Regex.\n- Authentication Layer: Manages user lifecycle (Signup, Login, Activation).\n- Logic Layer: Handles CRUD operations for project management.\n- Storage Layer: Uses JSON files for persistent data storage."
)

# Section 3
pdf.chapter_title("3. Directory Structure")
pdf.set_font("Courier", "", 10)
structure = """
py_course/
|-- day01/ (Basic Logic)
|-- day02/ (Functions & Data Structures)
|-- day03/ (Main Application)
    |-- app.py (Main Runner)
    |-- modules/ (Logic Units)
    |-- data/ (JSON Files)
"""
pdf.multi_cell(0, 5, structure)

pdf.output("Professional_PyCourse_Doc.pdf")
print("PDF was generated successfully!")
