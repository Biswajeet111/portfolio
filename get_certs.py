import os
import PyPDF2

def get_pdf_text(path):
    try:
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            t = ""
            for i in range(min(1, len(reader.pages))):
                t += reader.pages[i].extract_text() + " "
            return " ".join(t.split())[:300]
    except Exception as e:
        return str(e)

cert_dir = r"e:\portfolio\Certificates"
with open(r"e:\portfolio\cert_info.txt", "w", encoding="utf-8") as out:
    for f in os.listdir(cert_dir):
        path = os.path.join(cert_dir, f)
        if f.lower().endswith(".pdf"):
            out.write(f"PDF: {f}\nTEXT: {get_pdf_text(path)}\n{'-'*40}\n")
        else:
            out.write(f"OTHER: {f}\n{'-'*40}\n")
