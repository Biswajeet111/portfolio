import os
import PyPDF2

cert_dir = r"e:\portfolio\Certificates"
files = [
    "12c4ed65-33fc-4e82-8800-7aa3cdbd4e79.pdf",
    "5fbc0cc4-3b79-4740-af32-0b4c6238e909.pdf",
    "Certificate.pdf",
    "Completion Certificate _ SkillsBuild.pdf",
    "12c4ed65-33fc-4e82-8800-7aa3cdbd4e79.pdf"
]

for f in files:
    path = os.path.join(cert_dir, f)
    if os.path.exists(path):
        try:
            with open(path, "rb") as fp:
                reader = PyPDF2.PdfReader(fp)
                text = reader.pages[0].extract_text()
                print(f"FILE: {f}\nTEXT: {' '.join(text.split())[:300]}\n")
        except Exception as e:
            print(f"FILE: {f} ERROR: {e}\n")
    else:
        print(f"FILE: {f} NOT FOUND\n")
