
certs = [
    # HACKATHONS
    ("DOC-20250108-WA0000..pdf", "Code-A-Haunt 3.0 National Hackathon — Participation Certificate", "Participated in the Code-A-Haunt 3.0 national-level hackathon, demonstrating strong coding and problem-solving skills in a competitive environment.", "hackathon", ["Hackathon", "National"]),
    ("DOC-20250119-WA0004..pdf", "WEB-A-THON 2.0 University Hackathon — Participation Certificate", "Participated in WEB-A-THON 2.0, showcasing skills in web development, UI design, and strategic problem-solving.", "hackathon", ["Hackathon", "Web"]),
    ("Screenshot 2026-03-25 175312.png", "India AI Impact Buildathon — National AI Innovation Challenge", "Participated in a nationwide AI innovation challenge involving AI-based problem solving alongside 40,000+ participants.", "hackathon", ["AI", "National"]),
    ("Screenshot 2026-03-25 175349.png", "HACKSAGON 2026 — IEEE Ideation Phase Participant", "Participated in the IEEE Hacksagon 2026 ideation phase, contributing innovative technology ideas and collaborative strategies.", "hackathon", ["IEEE", "Ideation"]),
    
    # AI
    ("Ai_nextGen.pdf", "IBM AI NextGen Certification Program — IBM SkillsBuild", "Completed the IBM AI NextGen program, gaining knowledge of artificial intelligence fundamentals and real-world AI applications.", "ai", ["IBM", "AI"]),
    ("Digital Sticker_IBM Granite Models for Software Development.png", "IBM Granite Models for Software Development", "Learned to use IBM Granite AI models for code generation, AI-assisted development, and enterprise-level workflows.", "ai", ["IBM", "AI"]),
    ("Completion Certificate _ SkillsBuild1.pdf", "AI-Powered Chatbots Development", "Built knowledge of chatbot development, conversational AI design, and automated response systems.", "ai", ["IBM", "Chatbots"]),
    ("Completion Certificate _ SkillsBuild2.pdf", "AI-Powered Ticket Routing & Recommendation Systems", "Learned to design AI systems that automatically route tickets and provide intelligent recommendations.", "ai", ["IBM", "AI"]),
    ("Completion Certificate _ SkillsBuild3.pdf", "Knowledge Management Systems & Customer Analytics", "Developed skills in managing enterprise knowledge systems and analyzing customer behavior using AI.", "ai", ["IBM", "Analytics"]),
    ("Completion Certificate _ SkillsBuild4.pdf", "AI-Enabled Applications for Customer Service", "Built understanding of intelligent customer service systems powered by artificial intelligence.", "ai", ["IBM", "AI"]),
    ("Screenshot 2026-03-25 175125.png", "Python Programming for Agentic AI — Agentic AI Saksham", "Participated in a 2-day hands-on workshop focused on Python programming techniques used in building Agentic AI systems.", "ai", ["Python", "AI"]),
    ("Screenshot 2026-03-25 175456.png", "Generative AI Program — NASSCOM Skill Development", "Completed industry-aligned training in Generative AI, focusing on real-world applications and AI-driven solutions.", "ai", ["NASSCOM", "GenAI"]),
    ("microsoft gen ai.pdf", "Learn AI and Generative AI Basics — Microsoft", "Learned core AI and Generative AI concepts including model usage, real-world applications, and responsible AI practices.", "ai", ["Microsoft", "AI"]),
    ("Certificate.pdf", "Stock Market Using AI — Workshop Certification", "Explored AI-based stock analysis techniques, automated trading strategies, and financial prediction models.", "ai", ["AI", "Finance"]),
    
    # PROGRAMMING
    ("I have completed Java Course - Mastering the Fundamentals on Scaler Topics.pdf", "Java Programming — Mastering the Fundamentals", "Learned object-oriented programming concepts, Java syntax, and application development fundamentals.", "programming", ["Java", "OOP"]),
    ("c++ Cert.pdf", "C++ Course — Learn the Essentials", "Completed structured training covering C++ fundamentals, problem-solving, and core programming concepts.", "programming", ["C++"]),
    ("CERT_VT.pdf", "Vocational Training in Web Development — Tata Steel", "Completed hands-on web development training at Tata Steel, focusing on real-world software development practices.", "programming", ["Training", "Web"]),
    ("12c4ed65-33fc-4e82-8800-7aa3cdbd4e79.pdf", "Software Engineering Job Simulation — Forage", "Completed hands-on tasks involving architecture design, testing, security, and Agile development workflows.", "programming", ["Forage", "SWE"]),
    
    # TOOLS
    ("automation.pdf", "Certified Essentials Automation Professional — Automation Anywhere", "Gained expertise in robotic process automation (RPA), workflow automation, and enterprise automation tools.", "tools", ["Automation", "RPA"]),
    ("5fbc0cc4-3b79-4740-af32-0b4c6238e909.pdf", "Cybersecurity Analyst Job Simulation — Forage", "Learned identity management, access control systems, and cybersecurity architecture fundamentals.", "tools", ["Forage", "Cyber"]),
    ("Infosys_DataScience_Cert.pdf", "Introduction to Data Science — Infosys Springboard", "Learned core data science concepts including data analysis, visualization, and machine learning fundamentals.", "tools", ["Data Science", "Infosys"]),
    ("Infosys_Presentation.pdf", "High Impact Presentations — Infosys Springboard", "Developed strong presentation and communication skills for technical and professional settings.", "tools", ["Soft Skills", "Infosys"]),
    ("Infosys_TimeManagement.pdf", "Time Management — Infosys Springboard", "Learned productivity techniques to manage time effectively and improve workflow efficiency.", "tools", ["Soft Skills", "Infosys"]),
    ("microsoft copilot.pdf", "Get Started with Microsoft Copilot", "Learned to use Microsoft Copilot for AI-assisted coding, productivity automation, and workflow optimization.", "ai", ["Microsoft", "Copilot"]),
    ("MS cyber.pdf", "Cybersecurity Fundamentals — Microsoft", "Explored cybersecurity principles including threat awareness, secure systems, and digital safety fundamentals.", "tools", ["Microsoft", "Cyber"])
]

def get_card(f, title, desc, cat, tags):
    is_png = f.lower().endswith(".png")
    encoded_f = f.replace(" ", "%20")
    tags_html = "".join([f'<span class="tech-pill">{t}</span>' for t in tags])
    media = f'<img src="Certificates/{encoded_f}" alt="{title}">' if is_png else f'<embed src="Certificates/{encoded_f}#toolbar=0&navpanes=0&scrollbar=0" type="application/pdf">'
    return f'''
                    <div class="project-card" data-category="{cat}">
                        <div class="project-header">
                            <i class="fa-solid fa-award folder-icon"></i>
                            <div class="project-links">
                                <a href="Certificates/{encoded_f}" target="_blank" title="View Document"><i class="fa-solid fa-arrow-up-right-from-square"></i></a>
                            </div>
                        </div>
                        <div class="preview-frame" onclick="openModal('Certificates/{encoded_f}', {str(not is_png).lower()})">
                            {media}
                            <div class="preview-overlay">
                                <i class="fa-solid fa-expand"></i>
                            </div>
                        </div>
                        <h3 class="project-title">{title}</h3>
                        <p class="project-desc">{desc}</p>
                        <div class="project-tech">
                            {tags_html}
                        </div>
                    </div>'''

cards_html = "\\n".join([get_card(*c) for c in certs])

section_html = f'''        <!-- CERTIFICATIONS -->
        <section id="certifications">
            <div class="container reveal">
                <h2 class="section-title">Professional <span>Certifications</span></h2>
                <div class="cert-counter"><i class="fa-solid fa-award"></i><span>25+ Verified Certifications</span></div>
                <div class="cert-filters">
                    <button class="filter-btn active" data-filter="all">All</button>
                    <button class="filter-btn" data-filter="ai">AI</button>
                    <button class="filter-btn" data-filter="programming">Programming</button>
                    <button class="filter-btn" data-filter="hackathon">Hackathons</button>
                    <button class="filter-btn" data-filter="tools">Tools</button>
                </div>
                <div class="projects-grid" id="cert-grid">
{cards_html}
                </div>
            </div>
        </section>'''

with open(r"e:\portfolio\index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
pattern = re.compile(r'<!-- CERTIFICATIONS -->.*?<!-- CONTACT -->', re.DOTALL)
new_content = pattern.sub(section_html + '\\n\\n        <!-- CONTACT -->', content)

with open(r"e:\portfolio\index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("SAFE SWAP COMPLETE")
