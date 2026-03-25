import os
import PyPDF2
import sys

cert_dir = r"e:\portfolio\Certificates"
for f in os.listdir(cert_dir):
    if f.lower().endswith(".pdf"):
        path = os.path.join(cert_dir, f)
        try:
            with open(path, "rb") as file_obj:
                reader = PyPDF2.PdfReader(file_obj)
                text = ""
                for i in range(min(1, len(reader.pages))):
                    text += reader.pages[i].extract_text() + " "
                clean_text = " ".join(text.replace("\n", " ").split())
                print(f"FILE: {f}")
                print(f"TEXT: {clean_text[:200]}")
                print("-" * 40)
        except Exception as e:
            print(f"FILE: {f} ERROR: {e}")
            print("-" * 40)
