import pymupdf  # PyMuPDF

def extract_resume_text(pdf_file):
    """
    Extract text from an uploaded PDF resume.

    Args:
        pdf_file: Uploaded PDF file object.

    Returns:
        Extracted resume text as a string.
    """
    try:
        if pdf_file is None:
            raise ValueError("please upload a resume PDF.")
        resume_text = ""
        # fitz.open()	Opens the uploaded PDF file.
        with pymupdf.open(stream=pdf_file.read(),filetype="pdf") as document:
            if len(document) == 0:
                raise ValueError("the upload pdf is empty. ")
            for page in document:
                # page.get_text()	Extracts readable text from each page.
                resume_text += page.get_text() + "\n"
        resume_text = resume_text.strip()

        if not resume_text:
            raise ValueError("No text is found. The pdf may be scanned or Image based")
        return resume_text
    except ValueError:
        raise
    except Exception as e:
        raise RuntimeError(
            f"Failed to extract resume text: {e}"
        ) from e
    