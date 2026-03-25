import os
import PyPDF2
import sys

cert_dir = r"e:\portfolio\Certificates"
out_path = r"e:\portfolio\cert_texts.txt"

try:
    with open(out_path, "w", encoding="utf-8", errors="ignore") as out:
        for f in os.listdir(cert_dir):
            path = os.path.join(cert_dir, f)
            if f.lower().endswith(".pdf"):
                try:
                    with open(path, "rb") as fp:
                        reader = PyPDF2.PdfReader(fp)
                        t = ""
                        for i in range(min(1, len(reader.pages))):
                            t += reader.pages[i].extract_text() + " "
                        out.write(f"FILE: {f}\nTEXT: {' '.join(t.split())[:300]}\n{'-'*40}\n")
                except Exception as inner_e:
                    out.write(f"FILE: {f}\nERROR: {inner_e}\n{'-'*40}\n")
            else:
                out.write(f"FILE: {f}\nFORMAT: IMAGE_OR_OTHER\n{'-'*40}\n")
    print("DONE_SUCCESS")
except Exception as out_e:
    print("OUT_ERROR:", out_e)
