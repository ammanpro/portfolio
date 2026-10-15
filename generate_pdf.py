import sys
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_JUSTIFY, TA_CENTER

def create_resume_pdf(filename="Ammar_resume.pdf"):
    # Target A4 with clean 0.45-inch (32pt) margins to maximize readable space while looking elegant
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=34,
        rightMargin=34,
        topMargin=32,
        bottomMargin=32
    )

    content_width = A4[0] - 68  # 595.27 - 68 = 527.27 pt

    styles = getSampleStyleSheet()

    # Custom Color Palette
    C_PRIMARY = colors.HexColor('#0f172a')     # Slate 900
    C_ACCENT = colors.HexColor('#0284c7')      # Sky 600
    C_BODY = colors.HexColor('#334155')        # Slate 700
    C_MUTED = colors.HexColor('#64748b')       # Slate 500
    C_LINE = colors.HexColor('#cbd5e1')        # Slate 300
    C_BG_CARD = colors.HexColor('#f8fafc')     # Slate 50

    # Typography Styles
    name_style = ParagraphStyle(
        'ResumeName',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=22,
        textColor=C_PRIMARY,
        spaceAfter=2
    )

    title_style = ParagraphStyle(
        'ResumeTitle',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=C_ACCENT,
        spaceAfter=5
    )

    contact_style = ParagraphStyle(
        'ResumeContact',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=C_MUTED
    )

    section_heading_style = ParagraphStyle(
        'SectionHeading',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=C_PRIMARY,
        spaceBefore=0,
        spaceAfter=0
    )

    body_style = ParagraphStyle(
        'ResumeBody',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=C_BODY,
        alignment=TA_LEFT
    )

    summary_style = ParagraphStyle(
        'ResumeSummary',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=C_BODY,
        alignment=TA_JUSTIFY
    )

    bullet_style = ParagraphStyle(
        'ResumeBullet',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=C_BODY,
        leftIndent=11,
        firstLineIndent=-8,
        spaceAfter=2
    )

    role_title_style = ParagraphStyle(
        'RoleTitle',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11.5,
        textColor=C_PRIMARY
    )

    date_style = ParagraphStyle(
        'RoleDate',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=C_ACCENT,
        alignment=TA_RIGHT
    )

    company_sub_style = ParagraphStyle(
        'CompanySub',
        fontName='Helvetica-Oblique',
        fontSize=8.2,
        leading=10.5,
        textColor=C_MUTED,
        spaceAfter=3
    )

    story = []

    # 1. HEADER SECTION
    header_data = [
        [
            Paragraph("ABDUL AMMAR", name_style),
            Paragraph("<b>Email:</b> shaikammar011@gmail.com<br/><b>Phone:</b> +91 7893175137", ParagraphStyle('HRight', fontName='Helvetica', fontSize=8.5, leading=11, textColor=C_BODY, alignment=TA_RIGHT))
        ],
        [
            Paragraph("SOFTWARE DEVELOPER INTERN", title_style),
            Paragraph("<b>GitHub:</b> github.com/ammanpro<br/><b>Location:</b> Hyderabad, India", ParagraphStyle('HRight2', fontName='Helvetica', fontSize=8.5, leading=11, textColor=C_BODY, alignment=TA_RIGHT))
        ]
    ]

    header_table = Table(header_data, colWidths=[content_width * 0.55, content_width * 0.45])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=2, color=C_ACCENT, spaceBefore=2, spaceAfter=8))

    def make_section_header(title_text):
        t_data = [[
            Paragraph(f"<b>{title_text.upper()}</b>", section_heading_style)
        ]]
        t = Table(t_data, colWidths=[content_width])
        t.setStyle(TableStyle([
            ('LINEBELOW', (0, 0), (-1, -1), 1, C_LINE),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ]))
        return t

    # 2. PROFESSIONAL SUMMARY
    story.append(make_section_header("Professional Summary"))
    story.append(Spacer(1, 3))
    summary_p = (
        "Software Developer Intern at <b>Infer Labs</b>, working on the <b>iNexus</b> enterprise application platform. "
        "Familiar with <b>React, JavaScript, Python, FastAPI, PostgreSQL, and Git</b>. Use AI-assisted development tools "
        "such as <b>Claude Code</b> and <b>Antigravity</b> to understand existing code, troubleshoot issues, and assist with "
        "development tasks. Have knowledge of AWS cloud services, Linux operating systems and commands, and monitoring "
        "tools such as Prometheus and Grafana. Familiar with manual software testing and API testing using Swagger. "
        "Passionate about exploring AI tools and discovering ways to automate repetitive tasks, streamline workflows, "
        "and improve productivity. Interested in improving software development skills and gaining practical experience "
        "in backend development, cloud computing, DevOps, and software testing."
    )
    story.append(Paragraph(summary_p, summary_style))
    story.append(Spacer(1, 7))

    # 3. TECHNICAL SKILLS
    story.append(make_section_header("Technical Skills"))
    story.append(Spacer(1, 3))

    skills_data = [
        [
            Paragraph("<b>Programming:</b> Python, JavaScript, SQL, Bash", body_style),
            Paragraph("<b>Cloud Computing:</b> AWS (EC2, VPC, S3, Load Balancing)", body_style)
        ],
        [
            Paragraph("<b>Frontend:</b> React, Vite, HTML5, CSS3", body_style),
            Paragraph("<b>Operating Systems:</b> Linux, CLI Operations, Shell Scripting", body_style)
        ],
        [
            Paragraph("<b>Backend & APIs:</b> FastAPI, REST APIs", body_style),
            Paragraph("<b>Monitoring Tools:</b> Prometheus, Grafana", body_style)
        ],
        [
            Paragraph("<b>Database & ORM:</b> PostgreSQL, SQLAlchemy", body_style),
            Paragraph("<b>Software Testing:</b> Manual Testing, Swagger API, Troubleshooting", body_style)
        ],
        [
            Paragraph("<b>AI Dev Tools:</b> Claude Code, Antigravity", body_style),
            Paragraph("<b>Version Control & Others:</b> Git, GitHub, API Integration", body_style)
        ]
    ]

    skills_table = Table(skills_data, colWidths=[content_width * 0.48, content_width * 0.52])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 7))

    # 4. WORK EXPERIENCE
    story.append(make_section_header("Work Experience"))
    story.append(Spacer(1, 3))

    exp_header = [
        [
            Paragraph("<b>Software Developer Intern</b> &bull; <font color='#0284c7'><b>Infer Labs</b></font>", role_title_style),
            Paragraph("May 8, 2026 – Present", date_style)
        ]
    ]
    t_exp_head = Table(exp_header, colWidths=[content_width * 0.70, content_width * 0.30])
    t_exp_head.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(t_exp_head)
    story.append(Paragraph("Platform: iNexus Enterprise Suite &mdash; iPersonnel & iPayroll Modules &bull; Hyderabad, India", company_sub_style))

    exp_bullets = [
        "Work on the enterprise iNexus application, including its iPersonnel and iPayroll modules for workforce and payroll operations.",
        "Explore and understand existing frontend and backend codebases to accelerate feature development and bug fixes.",
        "Develop and maintain responsive frontend UI components and functionality with <b>React and JavaScript</b>.",
        "Use <b>Python and FastAPI</b> to understand backend APIs, business workflows, and application logic.",
        "Explore <b>PostgreSQL</b> database models, relational schema design, and <b>SQLAlchemy</b> ORM relationships.",
        "Use <b>Claude Code and Antigravity</b> to understand complex code, investigate issues, and assist with implementation.",
        "Manage branches, pull requests, and collaborative code changes effectively using <b>Git and GitHub</b>.",
        "Perform manual testing across application flows to check functionality and identify edge-case issues.",
        "Conduct API testing using <b>Swagger</b> to examine API endpoints, dispatch payloads, and validate responses.",
        "Develop knowledge of <b>AWS cloud services</b> (EC2, VPC, S3) and Linux server administration commands.",
        "Build familiarity with telemetry and system observability tools, including <b>Prometheus and Grafana</b>."
    ]

    for b in exp_bullets:
        story.append(Paragraph(f"&bull;  {b}", bullet_style))

    story.append(Spacer(1, 6))

    # 5. PROJECT EXPERIENCE
    story.append(make_section_header("Project Experience"))
    story.append(Spacer(1, 3))

    proj_header = [
        [
            Paragraph("<b>iNexus – Enterprise Application Platform</b>", role_title_style),
            Paragraph("Full-Stack Enterprise", date_style)
        ]
    ]
    t_proj_head = Table(proj_header, colWidths=[content_width * 0.70, content_width * 0.30])
    t_proj_head.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(t_proj_head)
    story.append(Paragraph("<b>Technologies:</b> React, JavaScript, Python, FastAPI, PostgreSQL, SQLAlchemy, Git", company_sub_style))

    proj_bullets = [
        "Work directly on the iPersonnel and iPayroll modules facilitating employee workforce tracking and payroll processing.",
        "Understand how frontend interfaces connect to backend REST APIs and relational database layers.",
        "Explore payroll computation workflows and their structural dependencies on employee-management data.",
        "Investigate code and integration issues using modern development tools and AI-assisted coding workflows.",
        "Support application testing and investigate API and frontend-backend integration issues."
    ]

    for b in proj_bullets:
        story.append(Paragraph(f"&bull;  {b}", bullet_style))

    story.append(Spacer(1, 6))

    # 6. EDUCATION & INTERESTS (2-Column Grid)
    edu_interests_data = [
        [
            Paragraph("<b>EDUCATION</b>", section_heading_style),
            Paragraph("<b>PROFESSIONAL INTERESTS</b>", section_heading_style)
        ],
        [
            Paragraph(
                "<b>Bachelor of Technology (B.Tech) – Civil Engineering</b><br/>"
                "Srinivasa Ramanujan Institute of Technology (SRIT)<br/>"
                "<font color='#64748b'><b>Graduated: 2023</b></font>",
                body_style
            ),
            Paragraph(
                "&bull; <b>AI & Workflow Automation:</b> Automating repetitive manual tasks.<br/>"
                "&bull; <b>AI-Assisted Development:</b> Claude Code & Antigravity acceleration.<br/>"
                "&bull; <b>Continuous Learning:</b> Backend engineering, cloud, and DevOps.",
                body_style
            )
        ]
    ]

    edu_table = Table(edu_interests_data, colWidths=[content_width * 0.48, content_width * 0.52])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LINEBELOW', (0, 0), (0, 0), 1, C_LINE),
        ('LINEBELOW', (1, 0), (1, 0), 1, C_LINE),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 3),
        ('BOTTOMPADDING', (0, 1), (-1, 1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(edu_table)

    # Build PDF
    doc.build(story)
    print("SUCCESS: Ammar_resume.pdf generated successfully.")

if __name__ == "__main__":
    create_resume_pdf("Ammar_resume.pdf")
