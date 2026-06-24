from pypdf import PdfReader


def extract_text_from_pdf(file):

    text = ""

    try:

        pdf = PdfReader(file)

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:

        return f"Error reading PDF: {e}"