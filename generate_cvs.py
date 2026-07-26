#!/usr/bin/env python3
"""Generate polished one-page TR and ENG CVs for Batuhan Taşdemir."""

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Flowable,
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUT_DIR = Path(__file__).resolve().parent

INK = HexColor("#14201C")
MUTED = HexColor("#4A5A54")
ACCENT = HexColor("#0F766E")
LINE = HexColor("#D5DDD8")
SOFT = HexColor("#EEF3F0")

FONT_REG = "CVSans"
FONT_BOLD = "CVSans-Bold"
pdfmetrics.registerFont(TTFont(FONT_REG, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont(FONT_BOLD, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
registerFontFamily("CVSans", normal=FONT_REG, bold=FONT_BOLD)


def tr_upper(text: str) -> str:
    return text.replace("i", "İ").replace("ı", "I").upper()


class SectionLabel(Flowable):
    def __init__(self, text, width):
        super().__init__()
        self.text = tr_upper(text)
        self._width = width
        self.height = 14

    def wrap(self, availWidth, availHeight):
        return self._width, self.height

    def draw(self):
        self.canv.setFillColor(ACCENT)
        self.canv.rect(0, 3, 3, 9, fill=1, stroke=0)
        self.canv.setFillColor(INK)
        self.canv.setFont(FONT_BOLD, 9)
        self.canv.drawString(10, 5, self.text)


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=18,
            textColor=INK,
            leading=22,
            spaceAfter=2,
        ),
        "role": ParagraphStyle(
            "Role",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=10,
            textColor=ACCENT,
            leading=13,
            spaceAfter=6,
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=8.2,
            textColor=MUTED,
            leading=11,
            spaceAfter=0,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=8.6,
            textColor=INK,
            leading=11.5,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        ),
        "h_job": ParagraphStyle(
            "HJob",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=9.2,
            textColor=INK,
            leading=12,
        ),
        "h_org": ParagraphStyle(
            "HOrg",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=8.4,
            textColor=ACCENT,
            leading=11,
            spaceAfter=2,
        ),
        "date": ParagraphStyle(
            "Date",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=8,
            textColor=MUTED,
            leading=11,
            alignment=TA_LEFT,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=8.3,
            textColor=INK,
            leading=11,
            leftIndent=10,
            bulletIndent=0,
            spaceAfter=1.5,
        ),
        "skill": ParagraphStyle(
            "Skill",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=8.2,
            textColor=INK,
            leading=11,
            spaceAfter=2,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=7.8,
            textColor=MUTED,
            leading=10,
        ),
    }


CONTENT = {
    "en": {
        "filename": "Batuhan_Tasdemir_CV_ENG.pdf",
        "role": "Computer Engineer · Full-Stack Developer",
        "meta": (
            "Ankara, Türkiye  ·  +90 507 611 05 69  ·  batuhanmedine2003@hotmail.com<br/>"
            "linkedin.com/in/batuhantasdemir03  ·  github.com/CaptainBlc  ·  captainblc.github.io"
        ),
        "summary": (
            "Computer Engineering senior at TED University with hands-on experience in C#, C++, "
            "Python, and Flutter. I build end-to-end management systems and practical full-stack "
            "tools—connecting reliable backends, clear interfaces, and maintainable architecture."
        ),
        "sections": {
            "experience": "Experience",
            "projects": "Projects",
            "education": "Education",
            "skills": "Skills",
            "certs": "Certificates",
            "languages": "Languages",
        },
        "experience": [
            {
                "title": "Game Developer Intern",
                "org": "FRANTIC GAMES",
                "date": "Jul 2025 – Aug 2025",
                "bullets": [
                    "Built modular Unity systems in C# with Scriptable Objects for scalable, decoupled gameplay data.",
                    "Implemented AI pathfinding and state-machine logic for dynamic in-game behaviors.",
                    "Delivered game-loop and UI/HUD features with a focus on UX polish and performance.",
                ],
            },
            {
                "title": "Software Programmer Intern",
                "org": "INFODIF Software & IT Technologies",
                "date": "Jun 2024 – Aug 2024",
                "bullets": [
                    "Developed Python/C++ backend modules for real-time object detection and data processing.",
                    "Built a SpaCy NER pipeline to extract and classify entities from unstructured text.",
                    "Engineered C++ solvers (chess/sudoku) with attention to algorithmic complexity and memory use.",
                ],
            },
        ],
        "projects": [
            {
                "title": "Leta-Takip — Session & Finance Desktop App",
                "link": "github.com/CaptainBlc/Leta-Takip",
                "text": (
                    "Python/Tkinter operations panel for counseling practices: scheduling, billing, "
                    "cash ledger, staff payouts, and rotating SQLite backups."
                ),
            },
            {
                "title": "OptiLumen — Hybrid AI Image Enhancement",
                "link": "github.com/CaptainBlc/optilumens",
                "text": (
                    "TED University CMPE 491 marketing site and project surface for a hybrid AI "
                    "image-enhancement system (HTML/CSS/JS)."
                ),
            },
            {
                "title": "NovaStore — Flutter Mini Catalog",
                "link": "github.com/CaptainBlc/NovaStoreMobil",
                "text": (
                    "Flutter e-commerce catalog with login, filtered product grid, detail flows, "
                    "and theme-driven UI (internship capstone module)."
                ),
            },
            {
                "title": "NLP NER Tool",
                "link": "github.com/CaptainBlc/named_Entity",
                "text": (
                    "SpaCy-based named-entity recognition workflow to automate extraction and "
                    "categorization from raw text corpora."
                ),
            },
        ],
        "education": {
            "title": "B.Sc. Computer Engineering (English)",
            "org": "TED University",
            "date": "2022 – 2026 (Expected)",
            "bullets": [
                "50% admission scholarship · Full English curriculum",
                "Coursework: Data Structures & Algorithms, OOP, DBMS, Software Engineering, Computer Networks",
            ],
        },
        "skills": [
            ("Languages", "C#, Python, C++, Java, SQL, Dart, HTML/CSS"),
            ("Frameworks & AI", ".NET, Unity, Flutter, SpaCy, OpenCV, SQLite"),
            ("Concepts", "OOP, Design Patterns, REST APIs, Agile/Scrum, UML, RDBMS"),
            ("Tools", "Git, GitHub, Visual Studio, JetBrains Rider, Figma"),
        ],
        "certs": [
            "Software Engineering: Implementation and Testing",
            "Software Engineering: Software Design and Project Management",
            "Software Engineering: Modeling Software Systems using UML",
        ],
        "languages": "Turkish (Native) · English (C1–C2, professional working proficiency)",
        "footer": "References available upon request.",
    },
    "tr": {
        "filename": "Batuhan_Tasdemir_CV_TR.pdf",
        "role": "Bilgisayar Mühendisi · Full-Stack Geliştirici",
        "meta": (
            "Ankara, Türkiye  ·  +90 507 611 05 69  ·  batuhanmedine2003@hotmail.com<br/>"
            "linkedin.com/in/batuhantasdemir03  ·  github.com/CaptainBlc  ·  captainblc.github.io"
        ),
        "summary": (
            "TED Üniversitesi Bilgisayar Mühendisliği son sınıf öğrencisiyim. C#, C++, Python ve "
            "Flutter ile uçtan uca yönetim sistemleri ve pratik full-stack çözümler geliştiriyorum; "
            "güvenilir backend mantığını anlaşılır arayüzlerle birleştiriyorum."
        ),
        "sections": {
            "experience": "Deneyim",
            "projects": "Projeler",
            "education": "Eğitim",
            "skills": "Beceriler",
            "certs": "Sertifikalar",
            "languages": "Diller",
        },
        "experience": [
            {
                "title": "Oyun Geliştirici Stajyeri",
                "org": "FRANTIC GAMES",
                "date": "Tem 2025 – Ağu 2025",
                "bullets": [
                    "C# ve Unity ile Scriptable Objects kullanarak modüler, ölçeklenebilir oyun sistemleri tasarladım.",
                    "Dinamik nesne davranışları için AI pathfinding ve state-machine mantığı geliştirdim.",
                    "Oyun döngüsü ve UI/HUD sistemlerini kullanıcı deneyimi ve performans odaklı tamamladım.",
                ],
            },
            {
                "title": "Yazılım Programcısı Stajyeri",
                "org": "INFODIF Yazılım ve Bilişim Teknolojileri",
                "date": "Haz 2024 – Ağu 2024",
                "bullets": [
                    "Python ve C++ ile gerçek zamanlı nesne tespiti ve veri işleme backend modülleri geliştirdim.",
                    "SpaCy ile yapılandırılmamış metinden varlık çıkaran özel bir NER aracı oluşturdum.",
                    "C++ ile satranç/sudoku çözücüleri tasarlayarak algoritmik karmaşıklık ve bellek yönetimine odaklandım.",
                ],
            },
        ],
        "projects": [
            {
                "title": "Leta-Takip — Seans & Finans Masaüstü Uygulaması",
                "link": "github.com/CaptainBlc/Leta-Takip",
                "text": (
                    "Danışmanlık kurumları için Python/Tkinter operasyon paneli: seans planlama, "
                    "borç/ödeme, kasa defteri, personel hakedişi ve döngüsel SQLite yedekleme."
                ),
            },
            {
                "title": "OptiLumen — Hibrit AI Görüntü İyileştirme",
                "link": "github.com/CaptainBlc/optilumens",
                "text": (
                    "TED Üniversitesi CMPE 491 kapsamında hibrit AI görüntü iyileştirme sistemi "
                    "için HTML/CSS/JS pazarlama sitesi ve proje yüzeyi."
                ),
            },
            {
                "title": "NovaStore — Flutter Mini Katalog",
                "link": "github.com/CaptainBlc/NovaStoreMobil",
                "text": (
                    "Giriş, kategori filtreli ürün ızgarası ve detay akışlarıyla Flutter e-ticaret "
                    "katalog uygulaması (staj bitirme modülü)."
                ),
            },
            {
                "title": "NLP NER Aracı",
                "link": "github.com/CaptainBlc/named_Entity",
                "text": (
                    "SpaCy tabanlı varlık tanıma iş akışı; ham metinden otomatik çıkarma ve "
                    "kategorilendirme."
                ),
            },
        ],
        "education": {
            "title": "Lisans, Bilgisayar Mühendisliği (İngilizce)",
            "org": "TED Üniversitesi",
            "date": "2022 – 2026 (Beklenen)",
            "bullets": [
                "%50 giriş bursu · Tamamen İngilizce müfredat",
                "Dersler: Veri Yapıları & Algoritmalar, OOP, VTYS, Yazılım Mühendisliği, Bilgisayar Ağları",
            ],
        },
        "skills": [
            ("Diller", "C#, Python, C++, Java, SQL, Dart, HTML/CSS"),
            ("Framework & AI", ".NET, Unity, Flutter, SpaCy, OpenCV, SQLite"),
            ("Kavramlar", "OOP, Tasarım Desenleri, REST API, Agile/Scrum, UML, RDBMS"),
            ("Araçlar", "Git, GitHub, Visual Studio, JetBrains Rider, Figma"),
        ],
        "certs": [
            "Yazılım Mühendisliği: Uygulama ve Test",
            "Yazılım Mühendisliği: Yazılım Tasarımı ve Proje Yönetimi",
            "Yazılım Mühendisliği: UML ile Yazılım Sistemlerini Modelleme",
        ],
        "languages": "Türkçe (Anadil) · İngilizce (C1–C2, profesyonel çalışma yetkinliği)",
        "footer": "Referanslar talep halinde sunulur.  ·  08.2003  ·  B Sınıfı Ehliyet  ·  Askerlik: Muafiyet yok",
    },
}


def job_block(s, job):
    header = Table(
        [[Paragraph(job["title"], s["h_job"]), Paragraph(job["date"], s["date"])]],
        colWidths=[125 * mm, 50 * mm],
    )
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    parts = [header, Paragraph(job["org"], s["h_org"])]
    for b in job["bullets"]:
        parts.append(Paragraph(f"• {b}", s["bullet"]))
    parts.append(Spacer(1, 5))
    return KeepTogether(parts)


def project_block(s, project):
    title = Paragraph(
        f"<b>{project['title']}</b>  <font color='#4A5A54'>— {project['link']}</font>",
        s["skill"],
    )
    body = Paragraph(project["text"], s["bullet"])
    return KeepTogether([title, body, Spacer(1, 3)])


def build(lang: str):
    data = CONTENT[lang]
    s = styles()
    path = OUT_DIR / data["filename"]

    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=12 * mm,
        title=f"Batuhan Taşdemir CV ({lang.upper()})",
        author="Batuhan Taşdemir",
    )

    story = []
    story.append(Paragraph("BATUHAN TAŞDEMİR", s["name"]))
    story.append(Paragraph(data["role"], s["role"]))
    story.append(Paragraph(data["meta"], s["meta"]))
    story.append(Spacer(1, 6))
    story.append(
        HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=0, spaceAfter=8)
    )
    story.append(Paragraph(data["summary"], s["body"]))

    story.append(SectionLabel(data["sections"]["experience"], 178 * mm))
    story.append(Spacer(1, 4))
    for job in data["experience"]:
        story.append(job_block(s, job))

    story.append(SectionLabel(data["sections"]["projects"], 178 * mm))
    story.append(Spacer(1, 4))
    for project in data["projects"]:
        story.append(project_block(s, project))

    story.append(Spacer(1, 2))
    story.append(SectionLabel(data["sections"]["education"], 178 * mm))
    story.append(Spacer(1, 4))
    edu = data["education"]
    edu_header = Table(
        [[Paragraph(edu["title"], s["h_job"]), Paragraph(edu["date"], s["date"])]],
        colWidths=[125 * mm, 50 * mm],
    )
    edu_header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.append(edu_header)
    story.append(Paragraph(edu["org"], s["h_org"]))
    for b in edu["bullets"]:
        story.append(Paragraph(f"• {b}", s["bullet"]))

    story.append(Spacer(1, 6))
    story.append(SectionLabel(data["sections"]["skills"], 178 * mm))
    story.append(Spacer(1, 4))
    for label, value in data["skills"]:
        story.append(Paragraph(f"<b>{label}:</b> {value}", s["skill"]))

    story.append(Spacer(1, 4))
    story.append(SectionLabel(data["sections"]["certs"], 178 * mm))
    story.append(Spacer(1, 4))
    for c in data["certs"]:
        story.append(Paragraph(f"• {c}", s["bullet"]))

    story.append(Spacer(1, 4))
    story.append(SectionLabel(data["sections"]["languages"], 178 * mm))
    story.append(Spacer(1, 3))
    story.append(Paragraph(data["languages"], s["skill"]))

    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=0, spaceAfter=4))
    story.append(Paragraph(data["footer"], s["small"]))

    # subtle top bar via onFirstPage
    def draw_chrome(canvas, _doc):
        canvas.saveState()
        canvas.setFillColor(ACCENT)
        canvas.rect(0, A4[1] - 4 * mm, A4[0], 4 * mm, fill=1, stroke=0)
        canvas.setFillColor(SOFT)
        canvas.rect(0, 0, A4[0], 6 * mm, fill=1, stroke=0)
        canvas.restoreState()

    doc.build(story, onFirstPage=draw_chrome, onLaterPages=draw_chrome)
    print(f"Wrote {path}")


if __name__ == "__main__":
    build("en")
    build("tr")
