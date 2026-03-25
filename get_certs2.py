import os
import pypdf # Using pypdf since PyPDF2 might be deprecated or behave differently
import sys

cert_dir = r"e:\portfolio\Certificates"
out_path = r"e:\portfolio\cert_texts.txt"

with open(out_path, "w", encoding="utf-8") as out:
    for f in os.listdir(cert_dir):
        path = os.path.join(cert_dir, f)
        if f.lower().endswith(".pdf"):
            try:
                reader = pypdf.PdfReader(path)
                t = ""
                for i in range(min(1, len(reader.pages))):
                    t += reader.pages[i].extract_text() + " "
                out.write(f"FILE: {f}\nTEXT: {' '.join(t.split())[:400]}\n{'-'*40}\n")
            except Exception as e:
                out.write(f"FILE: {f}\nERROR: {e}\n{'-'*40}\n")
        else:
            out.write(f"FILE: {f}\nFORMAT: IMAGE_OR_OTHER\n{'-'*40}\n")
