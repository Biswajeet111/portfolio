import re

certs = [
    ("Completion Certificate _ SkillsBuild.pdf", "IBM AI Fundamentals", "IBM"),
    ("Completion Certificate _ SkillsBuild1.pdf", "AI-Powered Chatbots", "IBM"),
    ("Completion Certificate _ SkillsBuild2.pdf", "AI Ticket Routing & Recommendation", "IBM"),
    ("Completion Certificate _ SkillsBuild3.pdf", "Knowledge Management & Customer Analytics", "IBM"),
    ("Completion Certificate _ SkillsBuild4.pdf", "AI-Enabled Customer Service", "IBM"),
    ("Digital Sticker_IBM Granite Models for Software Development.png", "IBM Granite Models", "IBM"),
    ("I have completed Java Course - Mastering the Fundamentals on Scaler Topics.pdf", "Mastering Java Fundamentals", "Scaler"),
    ("Infosys_DataScience_Cert.pdf", "Data Science Certification", "Infosys"),
    ("microsoft gen ai.pdf", "Microsoft Generative AI", "Microsoft"),
    ("microsoft copilot.pdf", "Microsoft Copilot", "Microsoft"),
    ("MS cyber.pdf", "Microsoft Cybersecurity", "Microsoft"),
    ("c++ Cert.pdf", "C++ Programming Certification", "C++"),
    ("Ai_nextGen.pdf", "Generative AI Foundations", "AI"),
    ("automation.pdf", "Automation Fundamentals", "Automation"),
    ("Infosys_Presentation.pdf", "Presentation Skills", "Infosys"),
    ("Infosys_TimeManagement.pdf", "Time Management", "Infosys"),
    ("CERT_VT.pdf", "Vocational Training", "Vocational Training"),
    ("Certificate.pdf", "General Certification", "Certification"),
    ("DOC-20250108-WA0000..pdf", "Achievement Document (1)", "Achievement"),
    ("DOC-20250119-WA0004..pdf", "Achievement Document (2)", "Achievement"),
    ("5fbc0cc4-3b79-4740-af32-0b4c6238e909.pdf", "Specialized Certification", "Certification"),
    ("42c2c0024f54ded6918588cd32d25436125126667982c2f5e17b9c68547cbcc2.png", "Verified Credential", "Credential"),
    ("Screenshot 2026-03-25 175125.png", "Python Programming for Agentic AI", "Achievement"),
    ("Screenshot 2026-03-25 175312.png", "India AI Impact Buildathon", "Achievement"),
    ("Screenshot 2026-03-25 175349.png", "HACKSAGON 2026", "Achievement"),
    ("Screenshot 2026-03-25 175456.png", "GEN AI NASSCOM", "Achievement")
]

grid_html = '\n<div class="projects-grid">\n'

for f, title, tag in certs:
    is_png = f.lower().endswith(".png")
    icon = "fa-image" if is_png else "fa-file-pdf"
    encoded_f = f.replace(" ", "%20")
    
    media_html = f'''
        <div style="margin-bottom: 20px; border-radius: 8px; overflow: hidden; border: 1px solid var(--border-color); background: #fff; height: 250px;">
            {'<img src="Certificates/' + encoded_f + '" alt="' + title + '" style="width: 100%; height: 100%; object-fit: cover;">' if is_png else '<embed src="Certificates/' + encoded_f + '#toolbar=0&navpanes=0&scrollbar=0" type="application/pdf" width="100%" height="100%" style="border:none;" title="' + title + '">'}
        </div>'''
    
    card_html = f'''
    <div class="project-card">
        <div class="project-header" style="margin-bottom: 10px;">
            <i class="fa-solid {icon} folder-icon"></i>
            <div class="project-links">
                <a href="Certificates/{encoded_f}" target="_blank" title="Open Full View"><i class="fa-solid fa-arrow-up-right-from-square"></i></a>
            </div>
        </div>
        {media_html}
        <h3 class="project-title" style="font-size: 1.3rem; margin-bottom: 8px;">{title}</h3>
        <p class="project-desc" style="font-size: 0.95rem; margin-bottom: 15px;">
            {title} earned and correctly framed for direct visibility.
        </p>
        <div class="project-tech">
            <span class="tech-pill">{tag}</span>
        </div>
    </div>
    '''
    grid_html += card_html

grid_html += '\n</div>\n'

with open(r"e:\portfolio\index.html", "r", encoding="utf-8") as file:
    content = file.read()

# Replace the specific block
pattern = re.compile(r'<section id="certifications">.*?</section>', re.DOTALL)
replacement = f'''<section id="certifications">
    <div class="container reveal">
        <h2 class="section-title">My <span>Certifications</span></h2>
        {grid_html}
    </div>
</section>'''

new_content = pattern.sub(replacement, content)

with open(r"e:\portfolio\index.html", "w", encoding="utf-8") as file:
    file.write(new_content)

print("INJECTION SUCCESSFUL")
