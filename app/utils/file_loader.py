from pypdf import PdfReader


def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def load_document(path):
    if path.endswith(".pdf"):
        return load_pdf(path)
    elif path.endswith(".txt"):
        return load_txt(path)
    else:
        return None