import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_master_qa_resume():
    doc = docx.Document()

    # 1. Page Margins (ATS Standard: 0.6 inches)
    for section in doc.sections:
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.6)
        section.right_margin = Inches(0.6)

    # Section Header Helper
    def add_section_header(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(title)
        run.bold = True
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0, 0, 0)

    # Bullet Point Helper
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

    # --- HEADER SECTION ---
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
    run_title = p_title.add_run("Lead / Senior Staff QA Automation Engineer | Python, Distributed CI/CD & AI-Augmented Systems")
    run_title.bold = True
    run_title.font.name = 'Calibri'
    run_title.font.size = Pt(10)

    p_contact = doc.add_paragraph()
    p_contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_contact.paragraph_format.space_after = Pt(6)
    run_contact = p_contact.add_run("India (Open to Global Remote / Contractor) | +91 9110572376 | premqa191@gmail.com\nGitHub: github.com/premqa191 | LinkedIn: linkedin.com/in/premqa191")
    run_contact.font.name = 'Calibri'
    run_contact.font.size = Pt(9)

    # --- PROFESSIONAL SUMMARY (3 Power-Bullet Points) ---
    add_section_header("PROFESSIONAL SUMMARY")
    add_bullet("Enterprise Python & Framework Architecture: ", "20+ years hands-on expertise building production-grade test automation architectures (Python 3, AsyncIO, PyTest, Playwright) across distributed microservices and global remote platforms (Turing, Crossover, Testlio).")
    add_bullet("CI/CD Quality Gates & API Security: ", "Architect of automated GitHub Actions and Docker quality pipelines; expert in deep log diagnostics, REST API contract integrity (OAuth 2.0, JSON Schema), and zero-defect release verification.")
    add_bullet("AI-Augmented QA & Model Evaluation: ", "Proven practitioner in synthetic test data generation, prompt engineering, and LLM evaluation rubrics under strict 0.05% tolerance bounds, optimizing framework execution efficiency by 40%.")

    # --- CORE TECHNICAL EXPERTISE ---
    add_section_header("CORE TECHNICAL EXPERTISE")
    add_bullet("Languages & Frameworks: ", "Python 3 (Advanced OOP, PyTest, AsyncIO), Bash/Shell Scripting, SQL, JSON, YAML")
    add_bullet("CI/CD & DevOps Automation: ", "GitHub Actions (Custom workflows, runner orchestration), Docker, GitLab CI, Jenkins, Linux CLI")
    add_bullet("API & Integration Systems: ", "RESTful APIs, Postman, Requests, OAuth 2.0, Webhooks, JSON Schema Validation, Contract Testing (Pact)")
    add_bullet("Automation & Quality Systems: ", "Playwright, Selenium WebDriver, TestNG, Shift-Left Testing, Root-Cause Analysis, Edge-Case Boundary Testing, Calibrated Rubric Auditing")
    add_bullet("AI-Augmented QA & Developer Tooling: ", "Claude, ChatGPT, Cursor, GitHub Copilot, Prompt Engineering, Model Context Protocol (MCP) concepts, LLM Output Evaluation, Synthetic Test Data Generation")
    add_bullet("Version Control & Developer Workflow: ", "Git (Advanced PR reviews, trunk-based branching, git diff analysis, merge conflict resolution), Jira, TestRail")

    # --- PROFESSIONAL EXPERIENCE ---
    add_section_header("PROFESSIONAL EXPERIENCE")

    # Role 1: Yashvi Web Tech
    p_job1 = doc.add_paragraph()
    p_job1.paragraph_format.space_before = Pt(4)
    p_job1.paragraph_format.space_after = Pt(1)
    r1 = p_job1.add_run("Senior Staff Software Engineer & Automation Architect\n")
    r1.bold = True
    r1.font.name = 'Calibri'
    r1.font.size = Pt(10)
    r1_sub = p_job1.add_run("Yashvi Web Tech Pvt Ltd. (Enterprise Clients: Daimler, RJO) | Jan 2018 – Present")
    r1_sub.italic = True
    r1_sub.font.name = 'Calibri'
    r1_sub.font.size = Pt(9.5)

    add_bullet("Engineered Enterprise Test Infrastructure: ", "Architected and scaled production-grade automated testing pipelines and reproducible test environments using Python, PyTest, Playwright, and Selenium across multi-tier distributed applications.")
    add_bullet("CI/CD Pipeline Quality Gates: ", "Designed and optimized custom GitHub Actions and CI/CD quality gates, proactively isolating build regressions, payload diff discrepancies, and cloud deployment configuration mismatches.")
    add_bullet("REST API & Contract Integrity: ", "Developed extensible Python automation suites to validate REST API contracts, authenticating via OAuth 2.0 and inspecting payload schemas to eliminate data truncation and serialization defects prior to staging.")
    add_bullet("AI-Augmented Engineering: ", "Leveraged AI developer tools (Claude, ChatGPT, GitHub Copilot) to generate combinatorial edge-case suites, author synthetic verification datasets, and refactor legacy test frameworks for 40% higher execution efficiency.")
    add_bullet("Strict Calibration & Precision Audits: ", "Enforced systematic calibration audits and rubric scoring on release-critical transactions, verifying numerical tolerance bounds (0.05%) and zero-defect data transformations for global enterprise clients.")

    # Role 2: Tiarion Software
    p_job2 = doc.add_paragraph()
    p_job2.paragraph_format.space_before = Pt(4)
    p_job2.paragraph_format.space_after = Pt(1)
    r2 = p_job2.add_run("Software Automation Engineer & QA Specialist\n")
    r2.bold = True
    r2.font.name = 'Calibri'
    r2.font.size = Pt(10)
    r2_sub = p_job2.add_run("Tiarion Software (P) Ltd. | Apr 2015 – Dec 2017")
    r2_sub.italic = True
    r2_sub.font.name = 'Calibri'
    r2_sub.font.size = Pt(9.5)

    add_bullet("Modular Framework Modernization: ", "Built modular, hybrid automation frameworks (Python, Selenium, TestNG), reducing regression execution cycles by 35% across core enterprise product lines.")
    add_bullet("Backend API & Data Integrity: ", "Authored comprehensive automation scripts for API verification and data pipeline workflows, validating complex database state transitions against strict schema invariants.")
    add_bullet("Git Workflow & Release Governance: ", "Standardized Git branching strategies, rigorous code diff reviews, and defect triage workflows to guarantee release branch stability across continuous deployment sprints.")

    # Role 3: Like Ways Infocom
    p_job3 = doc.add_paragraph()
    p_job3.paragraph_format.space_before = Pt(4)
    p_job3.paragraph_format.space_after = Pt(1)
    r3 = p_job3.add_run("Senior Software Test Engineer\n")
    r3.bold = True
    r3.font.name = 'Calibri'
    r3.font.size = Pt(10)
    r3_sub = p_job3.add_run("Like Ways Infocom (P) Ltd. | Mar 2012 – Mar 2015")
    r3_sub.italic = True
    r3_sub.font.name = 'Calibri'
    r3_sub.font.size = Pt(9.5)

    add_bullet("Integration & Bottleneck Isolation: ", "Constructed automated and exploratory test suites for multi-service integration workflows, successfully isolating critical boundary defects and server-side latency bottlenecks.")
    add_bullet("Deep Log Diagnostics & Triage: ", "Diagnosed root causes of production issues directly from server execution logs, API payload dumps, and stack traces, accelerating engineering resolution speed by 30%.")

    # Role 4: Pline Technologies
    p_job4 = doc.add_paragraph()
    p_job4.paragraph_format.space_before = Pt(4)
    p_job4.paragraph_format.space_after = Pt(1)
    r4 = p_job4.add_run("Senior QA & Automation Specialist\n")
    r4.bold = True
    r4.font.name = 'Calibri'
    r4.font.size = Pt(10)
    r4_sub = p_job4.add_run("Pline Technologies & Six Sigma SoftSolutions | Aug 2003 – Feb 2012")
    r4_sub.italic = True
    r4_sub.font.name = 'Calibri'
    r4_sub.font.size = Pt(9.5)

    add_bullet("Enterprise Regression & Compliance: ", "Built automated regression suites, executed functional and API integration tests, and audited mission-critical system workflows against strict ISO 9001 and CMMI software quality standards.")

    # --- EDUCATION & CREDENTIALS ---
    add_section_header("EDUCATION & CREDENTIALS")
    add_bullet("Master of Business Administration (M.B.A.) - IT & Management: ", "AIMA-CME, New Delhi")
    add_bullet("Professional Credentials: ", "Testlio Certified QA Network Tester & Evaluator")
    add_bullet("Core Practices: ", "Continuous Integration & Delivery (CI/CD), Shift-Left Testing, REST API Contract Testing, Rubric Evaluation & Calibration, Git PR Workflows")

    doc.save("PREM_KUMAR_Master_Clean_Resume.docx")
    print("Master Resume generated successfully: PREM_KUMAR_Master_Clean_Resume.docx")

if __name__ == "__main__":
    create_master_qa_resume()