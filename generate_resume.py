import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_prem_kumar_resume():
    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.6)
        section.right_margin = Inches(0.6)

    def add_section_header(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(title)
        run.bold = True
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0, 0, 0)

    def add_bullet(bold_prefix, text):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2.5)
        p.paragraph_format.line_spacing = 1.05
        
        run_bold = p.add_run(bold_prefix)
        run_bold.bold = True
        run_bold.font.name = 'Calibri'
        run_bold.font.size = Pt(9.5)
        
        run_text = p.add_run(text)
        run_text.font.name = 'Calibri'
        run_text.font.size = Pt(9.5)

    p_name = doc.add_paragraph()
    p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_name.paragraph_format.space_after = Pt(1)
    run_name = p_name.add_run("PREM KUMAR")
    run_name.bold = True
    run_name.font.name = 'Calibri'
    run_name.font.size = Pt(15)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(2)
    run_title = p_title.add_run("PRINCIPAL QA ARCHITECT & QUALITY ENGINEERING DELIVERY MANAGER")
    run_title.bold = True
    run_title.font.name = 'Calibri'
    run_title.font.size = Pt(10.5)

    p_contact = doc.add_paragraph()
    p_contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_contact.paragraph_format.space_after = Pt(6)
    run_contact = p_contact.add_run("India | Open to Global Remote / Contractor | Email: premqa191@gmail.com | Phone: +91 9110572376\nLinkedIn: linkedin.com/in/premqa191 | GitHub: github.com/premqa191")
    run_contact.font.name = 'Calibri'
    run_contact.font.size = Pt(9)

    add_section_header("PROFESSIONAL SUMMARY")
    add_bullet("Executive QA Leadership & Delivery Governance: ", "25+ years' enterprise experience directing global quality engineering, leading cross-functional teams of 12+ SDETs, and owning final Go/No-Go release sign-offs for tier-1 accounts including Daimler and RJO.")
    add_bullet("Resilient Multi-Cloud Architecture: ", "Architect of scalable Python, PyTest, and Playwright frameworks integrated with automated CI/CD quality gates across AWS, Azure, and GCP, reducing regression cycles by 35%.")
    add_bullet("High-Precision & AI-Augmented Systems: ", "Specialised in REST API contract verification, OWASP Top 10 security, strict numerical calibration audits (0.05% tolerance), and leveraging AI tooling (Claude, Copilot) to boost test efficiency by 40%.")

    add_section_header("CORE COMPETENCIES")
    add_bullet("Delivery Management & Client Governance: ", "Client Stakeholder Management, Go/No-Go Release Sign-offs, QA Delivery Governance, Agile/Scrum Delivery, Resource & Risk Planning.")
    add_bullet("Hands-on Test Architecture: ", "Test Automation Roadmaps, Framework Architecture, Shift-Left Quality, Automated Functional & Regression Testing, Boundary Validation.")
    add_bullet("API, Performance & Security: ", "RESTful Contract Testing (Pact), JSON Schema Invariant Validation, Performance/Load Testing (k6/JMeter), OWASP Top 10 API Security.")
    add_bullet("Cloud, DevOps & Leadership: ", "Multi-Cloud Test Infrastructure (AWS, Azure, GCP), CI/CD Quality Gates, Git PR Workflows, Defect Triage, Mentoring & Team Building (12+ Engineers).")

    add_section_header("TECHNICAL SKILLS")
    add_bullet("Languages & Frameworks: ", "Python 3 (Advanced OOP, AsyncIO), Playwright, PyTest, Selenium WebDriver, TestNG, Bash/Shell Scripting, SQL, JSON, YAML")
    add_bullet("API, Security & Performance: ", "RESTful APIs, Postman, Requests, OAuth 2.0, Webhooks, Contract Testing (Pact), OWASP Top 10, k6, Apache JMeter, Locust, Latency SLA Monitoring")
    add_bullet("Multi-Cloud & CI/CD: ", "AWS, Microsoft Azure, Google Cloud Platform (GCP), GitHub Actions, Docker, Jenkins, GitLab CI, Linux CLI")
    add_bullet("Management, Agile & Quality Tools: ", "Agile/Scrum, Sprint Ceremonies, Client Release Governance, Jira, Confluence, TestRail, Git (Advanced PR reviews, Trunk-based branching)")
    add_bullet("AI-Augmented QA & Developer Tooling: ", "Claude, ChatGPT, GitHub Copilot, Cursor, Prompt Engineering, LLM Output Evaluation, Model Context Protocol (MCP), Synthetic Test Data Generation")

    add_section_header("PROFESSIONAL EXPERIENCE")
    
    p_job1 = doc.add_paragraph()
    p_job1.paragraph_format.space_before = Pt(4)
    p_job1.paragraph_format.space_after = Pt(1)
    r1 = p_job1.add_run("Principal QA Architect & Quality Engineering Delivery Manager\n")
    r1.bold = True
    r1.font.name = 'Calibri'
    r1.font.size = Pt(10)
    r1_sub = p_job1.add_run("Yashvi Web Tech Pvt Ltd. | Enterprise Clients: Daimler, RJO | 01/2018 – Present")
    r1_sub.italic = True
    r1_sub.font.name = 'Calibri'
    r1_sub.font.size = Pt(9.5)
    
    add_bullet("Client Governance & Release Sign-offs: ", "Directed quality delivery for flagship enterprise accounts (Daimler, RJO); led technical stakeholder sessions and held complete authority over final Go/No-Go release sign-offs.")
    add_bullet("Engineering Leadership & Sprint Delivery: ", "Led and mentored a cross-functional team of 12 SDETs and QA engineers; drove Agile sprint ceremonies, backlog grooming, defect triage, and engineering career progression.")
    add_bullet("Enterprise Framework Architecture: ", "Architected and scaled production-grade test automation frameworks and reproducible test environments using Python, PyTest, Playwright, and Selenium across distributed microservices.")
    add_bullet("Multi-Cloud CI/CD Quality Gates: ", "Implemented automated CI/CD quality gates across AWS and Azure environments using GitHub Actions and GitLab CI, proactively isolating configuration mismatches and regressions.")
    add_bullet("Performance & API Security Engineering: ", "Conducted automated performance benchmarking using k6 and JMeter under peak enterprise loads; enforced REST API contract validation, OAuth 2.0 authentication, and OWASP Top 10 security checks.")
    add_bullet("Calibration Audits & AI Modernization: ", "Enforced strict calibration audits on release-critical transactions (0.05% numerical tolerance); leveraged Claude and GitHub Copilot to optimize test execution efficiency by 40%.")

    p_job2 = doc.add_paragraph()
    p_job2.paragraph_format.space_before = Pt(4)
    p_job2.paragraph_format.space_after = Pt(1)
    r2 = p_job2.add_run("Software Automation Engineer & QA Specialist\n")
    r2.bold = True
    r2.font.name = 'Calibri'
    r2.font.size = Pt(10)
    r2_sub = p_job2.add_run("Tiarion Software (P) Ltd. | 04/2015 – 12/2017")
    r2_sub.italic = True
    r2_sub.font.name = 'Calibri'
    r2_sub.font.size = Pt(9.5)

    add_bullet("Modular Automation Modernization: ", "Built modular hybrid test automation frameworks (Python, Selenium, TestNG), reducing regression execution cycles by 35% across continuous deployment sprints.")
    add_bullet("Backend Pipeline Validation: ", "Authored automated scripts for backend data pipelines and REST API verification, validating database state transitions against defined schema invariants.")
    add_bullet("Integration & Git Governance: ", "Conducted multi-service backend validation to detect serialization defects; standardized team Git branching models, PR diff reviews, and defect triage workflows.")

    p_job3 = doc.add_paragraph()
    p_job3.paragraph_format.space_before = Pt(4)
    p_job3.paragraph_format.space_after = Pt(1)
    r3 = p_job3.add_run("Senior Software Test Engineer\n")
    r3.bold = True
    r3.font.name = 'Calibri'
    r3.font.size = Pt(10)
    r3_sub = p_job3.add_run("Like Ways Infocom (P) Ltd. | 03/2012 – 03/2015")
    r3_sub.italic = True
    r3_sub.font.name = 'Calibri'
    r3_sub.font.size = Pt(9.5)

    add_bullet("Integration & Bottleneck Isolation: ", "Built automated and exploratory test suites for multi-service integration workflows, isolating critical boundary defects and server latency bottlenecks.")
    add_bullet("Diagnostics & Sprint Defect Triage: ", "Diagnosed root causes of production issues from server logs, API dumps, and stack traces, driving a 30% reduction in defect turnaround time during Agile iterations.")
    add_bullet("High-Availability Releases: ", "Executed functional, integration, regression, and backend validation across enterprise applications to ensure high-availability releases.")

    p_job4 = doc.add_paragraph()
    p_job4.paragraph_format.space_before = Pt(4)
    p_job4.paragraph_format.space_after = Pt(1)
    r4 = p_job4.add_run("Senior QA & Automation Specialist\n")
    r4.bold = True
    r4.font.name = 'Calibri'
    r4.font.size = Pt(10)
    r4_sub = p_job4.add_run("Pline Technologies & Six Sigma SoftSolutions | 08/2003 – 02/2012")
    r4_sub.italic = True
    r4_sub.font.name = 'Calibri'
    r4_sub.font.size = Pt(9.5)

    add_bullet("Enterprise Regression & Compliance: ", "Built automated regression suites and executed functional/API integration tests, auditing quality against ISO 9001 and CMMI software quality standards.")
    add_bullet("Boundary & System Verification: ", "Conducted structured boundary testing, manual regression runs, and system integration verification to ensure robust production deployments.")

    add_section_header("EDUCATION")
    add_bullet("Master of Business Administration (M.B.A.) – IT & Management: ", "AIMA-CME, New Delhi")

    add_section_header("PROFESSIONAL CREDENTIALS & CERTIFICATIONS")
    add_bullet("Testlio Certified QA Network Tester & Evaluator: ", "Specialised in exploratory, functional, and payment-flow usability testing across globally distributed networks.")

    add_section_header("CORE METHODOLOGIES & PRACTICES")
    p_meth = doc.add_paragraph()
    p_meth.paragraph_format.space_before = Pt(2)
    p_meth.paragraph_format.space_after = Pt(2)
    p_meth.paragraph_format.line_spacing = 1.1
    r_meth = p_meth.add_run("Agile / Scrum Delivery | Client Stakeholder Management & Go/No-Go Sign-offs | Continuous Integration & Continuous Delivery (CI/CD) | Shift-Left Quality Engineering | REST API Contract Testing | Performance & Load Testing | OWASP Security Testing | Multi-Cloud Architecture (AWS/Azure/GCP)")
    r_meth.font.name = 'Calibri'
    r_meth.font.size = Pt(9)

    doc.save("Prem_Kumar_Clean_Resume.docx")
    print("Resume successfully generated: Prem_Kumar_Clean_Resume.docx")

if __name__ == "__main__":
    create_prem_kumar_resume()