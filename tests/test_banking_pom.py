import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

doc = Document()

# Page Margins
for s in doc.sections:
    s.top_margin = Inches(0.65)
    s.bottom_margin = Inches(0.65)
    s.left_margin = Inches(0.65)
    s.right_margin = Inches(0.65)

def add_p_bottom_border(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '9CA3AF')
    pBdr.append(bottom)
    pPr.append(pBdr)

# Base Font
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(10)
style.font.color.rgb = RGBColor(31, 41, 55)

# Header
p_name = doc.add_paragraph()
p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_name.paragraph_format.space_after = Pt(2)
r_name = p_name.add_run("PREM KUMAR")
r_name.bold = True
r_name.font.size = Pt(18)

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_after = Pt(4)
r_title = p_title.add_run("QA ENGINEERING TEAM LEAD | SENIOR STAFF QA AUTOMATION ENGINEER")
r_title.bold = True
r_title.font.size = Pt(11)
r_title.font.color.rgb = RGBColor(37, 99, 235)

p_contact = doc.add_paragraph()
p_contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_contact.paragraph_format.space_after = Pt(6)
p_contact.add_run("India | Open to Global Remote / Contractor\n")
p_contact.add_run("Email: ").bold = True
p_contact.add_run("premqa191@gmail.com | ")
p_contact.add_run("Phone: ").bold = True
p_contact.add_run("+91 9110572376 | ")
p_contact.add_run("LinkedIn: ").bold = True
p_contact.add_run("linkedin.com/in/premqa191 | ")
p_contact.add_run("GitHub: ").bold = True
p_contact.add_run("github.com/premqa191")
add_p_bottom_border(p_contact)

def add_heading(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text.upper())
    r.bold = True
    r.font.size = Pt(11.5)
    r.font.color.rgb = RGBColor(17, 24, 39)
    add_p_bottom_border(p)
    return p

def add_bullet(bold_pfx, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    if bold_pfx:
        r_b = p.add_run(bold_pfx)
        r_b.bold = True
        r_b.font.color.rgb = RGBColor(17, 24, 39)
    r_t = p.add_run(text)
    r_t.font.color.rgb = RGBColor(55, 65, 81)

def add_role(title, subtitle):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r1 = p.add_run(title + "\n")
    r1.bold = True
    r1.font.size = Pt(10.5)
    r2 = p.add_run(subtitle)
    r2.italic = True
    r2.font.size = Pt(9.5)
    r2.font.color.rgb = RGBColor(75, 85, 99)

# Summary
add_heading("Professional Summary")
p_s = doc.add_paragraph()
p_s.paragraph_format.line_spacing = 1.15
p_s.paragraph_format.space_after = Pt(4)
p_s.add_run("Hands-on QA Engineering Team Lead and Senior Staff QA Automation Engineer with 20+ years of enterprise experience in architecting robust automation frameworks, end-to-end test strategies, and scalable CI/CD pipelines. Deep technical specialization in Python, PyTest, Playwright, REST API validation, and shift-left quality methodologies across high-throughput distributed architectures. Proven track record leading defect triage, root-cause diagnostics, and strict calibration audits (0.05% tolerance) for tier-1 enterprise clients including Daimler and RJO. Adept at augmenting modern engineering teams with AI developer workflows, synthetic test generation, and continuous release governance.")

# Competencies
add_heading("Core Competencies")
add_bullet("Test Leadership & Strategy: ", "Quality Engineering Leadership, Test Strategy, Test Planning, Automation Roadmaps, Risk Analysis, Release Governance.")
add_bullet("Automation & Testing: ", "Shift-Left Testing, Functional Testing, Automated Regression Testing, Integration Testing, End-to-End Testing, Boundary & Edge-Case Testing.")
add_bullet("Architecture & API: ", "Test Framework Architecture, REST API Testing, Contract Testing (Pact), JSON Schema Invariant Validation, Database & SQL Verification.")
add_bullet("Diagnostics & Delivery: ", "Defect Triage, Root-Cause Analysis, CI/CD Quality Gates, Git PR Workflows, Calibrated Rubric Auditing, Continuous Improvement.")

# Technical Skills
add_heading("Technical Skills")
add_bullet("Languages & Scripting: ", "Python 3 (Advanced OOP, AsyncIO), Bash/Shell Scripting, SQL, JSON, YAML")
add_bullet("Test Automation Frameworks: ", "Playwright, PyTest, Selenium WebDriver, TestNG")
add_bullet("API & Integration Testing: ", "RESTful APIs, Postman, Requests, OAuth 2.0, Webhooks, JSON Schema Validation, Contract Testing (Pact)")
add_bullet("CI/CD & Cloud Infrastructure: ", "GitHub Actions (Custom workflows, runner orchestration), Docker, Jenkins, GitLab CI, Linux CLI, Cloud Test Execution (AWS)")
add_bullet("Version Control & Quality Management: ", "Git (Advanced PR reviews, trunk-based branching, git diff analysis, merge conflict resolution), Jira, TestRail")
add_bullet("AI-Augmented QA & Tooling: ", "Claude, ChatGPT, GitHub Copilot, Cursor, Prompt Engineering, LLM Output Evaluation, Model Context Protocol (MCP) concepts, Synthetic Test Data Generation")

# Professional Experience
add_heading("Professional Experience")
add_role("Senior Staff Software Engineer & Automation Architect", "Yashvi Web Tech Pvt Ltd. | Enterprise Clients: Daimler, RJO | 01/2018 – Present")
add_bullet("Enterprise Test Architecture: ", "Architected and scaled production-grade automated testing pipelines and reproducible test environments using Python, PyTest, Playwright, and Selenium across multi-tier distributed applications.")
add_bullet("CI/CD Quality Gates: ", "Designed and deployed customized GitHub Actions CI/CD quality gates, proactively isolating build regressions, payload discrepancies, and cloud deployment configuration mismatches.")
add_bullet("API & Contract Integrity: ", "Developed extensible Python automation test suites for REST API validation, implementing OAuth 2.0 authentication, schema invariant checks, and contract integrity to prevent data truncation before staging.")
add_bullet("Framework Optimization: ", "Refactored legacy automation test suites and operational workflows, improving overall execution efficiency by approximately 40%.")
add_bullet("Precision Audits & Calibration: ", "Enforced strict calibration audits and rubric validation scoring for release-critical transactions, verifying numerical tolerance bounds of 0.05% and zero-defect data transformations.")
add_bullet("Deep Diagnostics & Triage: ", "Accelerated engineering resolution by diagnosing complex failures directly from CI execution logs, API payload dumps, stack traces, and backend data states.")
add_bullet("AI-Augmented Engineering: ", "Leveraged AI developer tools (Claude, ChatGPT, GitHub Copilot) to generate combinatorial edge-case suites, author synthetic verification datasets, and optimize automation coverage.")
add_bullet("Shift-Left Governance: ", "Collaborated across cross-functional engineering teams to embed shift-left quality gates, conduct code reviews, and maintain zero-defect release cadences.")

# Page Break for Clean 2-Page Fit
doc.add_page_break()

add_role("Software Automation Engineer & QA Specialist", "Tiarion Software (P) Ltd. | 04/2015 – 12/2017")
add_bullet("Modular Framework Modernization: ", "Built modular, hybrid test automation frameworks using Python, Selenium, and TestNG across core enterprise product lines.")
add_bullet("Regression Acceleration: ", "Authored comprehensive automated regression and functional test suites, reducing regression execution cycles by approximately 35%.")
add_bullet("Data Pipeline & Backend Validation: ", "Developed automated scripts for backend data-processing pipelines and REST API verification, validating database state transitions against defined schema invariants.")
add_bullet("Integration Testing: ", "Conducted multi-service backend validation to detect data serialization discrepancies, edge-case bottlenecks, and schema violations.")
add_bullet("Git Governance: ", "Standardized team Git branching models, trunk-based deployment flows, pull request diff reviews, and release governance protocols to stabilize sprint branches.")

add_role("Senior Software Test Engineer", "Like Ways Infocom (P) Ltd. | 03/2012 – 03/2015")
add_bullet("Integration & Bottleneck Isolation: ", "Constructed automated and exploratory test suites for multi-service integration workflows, isolating critical boundary defects and latency bottlenecks.")
add_bullet("High-Availability Releases: ", "Executed functional, integration, regression, and backend validation across enterprise applications to ensure high-availability releases.")
add_bullet("Root-Cause Diagnostics: ", "Diagnosed root causes of mission-critical production issues from server execution logs, API payload dumps, and stack traces, driving a 30% reduction in defect turnaround time.")
add_bullet("Defect Triage: ", "Facilitated regular defect triage sessions with development teams to prioritize high-severity bugs and mitigate delivery risks.")

add_role("Senior QA & Automation Specialist", "Pline Technologies & Six Sigma SoftSolutions | 08/2003 – 02/2012")
add_bullet("Enterprise Regression & Compliance: ", "Built automated regression suites and executed functional and API integration tests for mission-critical enterprise workflows.")
add_bullet("Standards Compliance: ", "Validated application behavior and audited quality control processes against ISO 9001 and CMMI software quality standards.")
add_bullet("Verification & Defect Identification: ", "Conducted structured boundary testing, manual regression runs, and system integration verification to ensure robust production deployments.")

# Education
add_heading("Education")
add_bullet("Master of Business Administration (M.B.A.) – IT & Management: ", "AIMA-CME, New Delhi")
add_bullet("Bachelor of Science (B.Sc.) / Bachelor of Technology (B.Tech): ", "[University Name, City] — Satisfies corporate 4-year degree requirements")

# Credentials
add_heading("Professional Credentials & Certifications")
add_bullet("Testlio Certified QA Network Tester & Evaluator: ", "Specialized in exploratory, functional, and payment-flow usability testing across global distributed networks.")

# Methodologies
add_heading("Core Methodologies & Practices")
p_m = doc.add_paragraph()
p_m.paragraph_format.line_spacing = 1.15
p_m.paragraph_format.space_before = Pt(3)
p_m.add_run("Continuous Integration & Continuous Delivery (CI/CD) | Shift-Left Quality Engineering | REST API Contract Testing | Automated Test Architecture | Data Schema Calibration | Root-Cause Analysis | Defect Triage & Governance | Git PR Workflows | Microservices Integration Testing")

doc.save("Prem_Kumar_QA_Lead_Resume.docx")
print("Saved: Prem_Kumar_QA_Lead_Resume.docx")