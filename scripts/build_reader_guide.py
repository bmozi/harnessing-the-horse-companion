#!/usr/bin/env python3
# © 2026 John Briggs - MIT licensed
"""Build the public reader quick-start PDF from its versioned JSON source."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "release-assets" / "reader-quick-start.json"
OUTPUT_DIR = ROOT / "output" / "pdf"

NAVY = colors.HexColor("#11263D")
TEAL = colors.HexColor("#168C8C")
ORANGE = colors.HexColor("#EF8B32")
INK = colors.HexColor("#243447")
MUTED = colors.HexColor("#607384")
PALE = colors.HexColor("#EAF4F3")
LIGHT = colors.HexColor("#F3F6F8")
WHITE = colors.white


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "cover_title": ParagraphStyle(
            "CoverTitle", parent=base["Title"], fontName="Helvetica-Bold",
            fontSize=34, leading=38, textColor=WHITE, alignment=TA_CENTER,
            spaceAfter=14,
        ),
        "cover_subtitle": ParagraphStyle(
            "CoverSubtitle", parent=base["Normal"], fontName="Helvetica",
            fontSize=18, leading=24, textColor=colors.HexColor("#BCE0DE"),
            alignment=TA_CENTER, spaceAfter=24,
        ),
        "cover_promise": ParagraphStyle(
            "CoverPromise", parent=base["Normal"], fontName="Helvetica",
            fontSize=13, leading=20, textColor=WHITE, alignment=TA_CENTER,
        ),
        "title": ParagraphStyle(
            "PageTitle", parent=base["Heading1"], fontName="Helvetica-Bold",
            fontSize=24, leading=29, textColor=NAVY, spaceAfter=7,
        ),
        "kicker": ParagraphStyle(
            "Kicker", parent=base["Normal"], fontName="Helvetica",
            fontSize=11.5, leading=16, textColor=MUTED, spaceAfter=15,
        ),
        "step_label": ParagraphStyle(
            "StepLabel", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=10.5, leading=14, textColor=TEAL,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["BodyText"], fontName="Helvetica",
            fontSize=10.2, leading=14.3, textColor=INK,
        ),
        "bullet": ParagraphStyle(
            "Bullet", parent=base["BodyText"], fontName="Helvetica",
            fontSize=10.2, leading=14, leftIndent=13, firstLineIndent=-8,
            bulletIndent=0, textColor=INK, spaceAfter=4,
        ),
        "callout": ParagraphStyle(
            "Callout", parent=base["BodyText"], fontName="Helvetica-Bold",
            fontSize=10.4, leading=15, textColor=NAVY,
        ),
        "small": ParagraphStyle(
            "Small", parent=base["BodyText"], fontName="Helvetica",
            fontSize=8.5, leading=11, textColor=MUTED,
        ),
        "table_head": ParagraphStyle(
            "TableHead", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=8.8, leading=11, textColor=WHITE,
        ),
        "table_body": ParagraphStyle(
            "TableBody", parent=base["Normal"], fontName="Helvetica",
            fontSize=8.2, leading=10.3, textColor=INK,
        ),
    }


def footer(canvas: Any, doc: Any, version: str) -> None:
    canvas.saveState()
    width, _ = letter
    canvas.setStrokeColor(colors.HexColor("#CCD8DF"))
    canvas.line(doc.leftMargin, 0.48 * inch, width - doc.rightMargin, 0.48 * inch)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.29 * inch, f"Harnessing the Horse - Reader Quick Start v{version}")
    canvas.drawRightString(width - doc.rightMargin, 0.29 * inch, str(doc.page))
    canvas.restoreState()


def cover(canvas: Any, doc: Any, data: dict[str, Any], st: dict[str, ParagraphStyle]) -> None:
    width, height = letter
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, width, height, stroke=0, fill=1)
    canvas.setFillColor(TEAL)
    canvas.rect(0, height - 0.18 * inch, width, 0.18 * inch, stroke=0, fill=1)
    canvas.setFillColor(ORANGE)
    canvas.rect(0, 0, width, 0.12 * inch, stroke=0, fill=1)
    canvas.restoreState()


def step_table(items: list[list[str]], st: dict[str, ParagraphStyle]) -> Table:
    rows = [
        [Paragraph(label, st["step_label"]), Paragraph(text, st["body"])]
        for label, text in items
    ]
    table = Table(rows, colWidths=[1.12 * inch, 5.62 * inch], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (0, -1), PALE),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD8DD")),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#DCE5E9")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return table


def artifact_table(rows: list[list[str]], st: dict[str, ParagraphStyle]) -> Table:
    converted = []
    for index, row in enumerate(rows):
        style = st["table_head"] if index == 0 else st["table_body"]
        converted.append([Paragraph(cell, style) for cell in row])
    table = Table(converted, colWidths=[1.18 * inch, 1.62 * inch, 3.94 * inch], repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("BACKGROUND", (0, 1), (-1, -1), WHITE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CBD8DD")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return table


def callout(text: str, st: dict[str, ParagraphStyle]) -> Table:
    box = Table([[Paragraph(text, st["callout"])]], colWidths=[6.74 * inch])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFF3E8")),
        ("BOX", (0, 0), (-1, -1), 0.8, ORANGE),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return box


def build() -> Path:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    version = data["version"]
    output = OUTPUT_DIR / f"Harnessing-the-Horse-Reader-Quick-Start-v{version}.pdf"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    st = styles()
    doc = SimpleDocTemplate(
        str(output), pagesize=letter, rightMargin=0.63 * inch,
        leftMargin=0.63 * inch, topMargin=0.58 * inch, bottomMargin=0.66 * inch,
        title=f"{data['title']} - {data['subtitle']}", author="John Briggs",
        subject="A practical orientation to the Harnessing the Horse companion repository",
    )

    story: list[Any] = [
        Spacer(1, 1.55 * inch),
        Paragraph(data["title"], st["cover_title"]),
        Paragraph(data["subtitle"], st["cover_subtitle"]),
        Spacer(1, 0.18 * inch),
        Table([[Paragraph(data["promise"], st["cover_promise"])]],
              colWidths=[5.75 * inch], style=TableStyle([
                  ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#183954")),
                  ("BOX", (0, 0), (-1, -1), 0.8, TEAL),
                  ("LEFTPADDING", (0, 0), (-1, -1), 20),
                  ("RIGHTPADDING", (0, 0), (-1, -1), 20),
                  ("TOPPADDING", (0, 0), (-1, -1), 18),
                  ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
              ]), hAlign="CENTER"),
        Spacer(1, 1.18 * inch),
        Paragraph(f"Companion release v{version} | August 24, 2026", st["cover_subtitle"]),
        Paragraph("John Briggs", st["cover_promise"]),
        PageBreak(),
    ]

    for page_index, page in enumerate(data["pages"]):
        story.extend([
            Paragraph(page["title"], st["title"]),
            Paragraph(page["kicker"], st["kicker"]),
        ])
        if "image" in page:
            image_path = ROOT / page["image"]
            img = Image(str(image_path))
            max_width = 6.74 * inch
            max_height = 2.82 * inch if "steps" in page else 3.72 * inch
            scale = min(max_width / img.imageWidth, max_height / img.imageHeight)
            img.drawWidth = img.imageWidth * scale
            img.drawHeight = img.imageHeight * scale
            img.hAlign = "CENTER"
            story.extend([img, Spacer(1, 0.13 * inch)])
        if "table" in page:
            story.extend([artifact_table(page["table"], st), Spacer(1, 0.16 * inch)])
        if "steps" in page:
            story.extend([step_table(page["steps"], st), Spacer(1, 0.15 * inch)])
        if "bullets" in page:
            bullets = [Paragraph(f"- {item}", st["bullet"]) for item in page["bullets"]]
            story.extend([KeepTogether(bullets), Spacer(1, 0.1 * inch)])
        story.append(callout(page["callout"], st))
        if page_index < len(data["pages"]) - 1:
            story.append(PageBreak())

    story.extend([
        Spacer(1, 0.16 * inch),
        Paragraph("Continue with the stable resources", st["step_label"]),
    ])
    for label, url in data["links"]:
        story.append(Paragraph(f'<link href="{url}" color="#168C8C"><u>{label}</u></link> - {url}', st["small"]))
    story.extend([
        Spacer(1, 0.12 * inch),
        Paragraph("Written content © 2026 John Briggs. Licensed under CC BY-NC-SA 4.0.", st["small"]),
    ])

    doc.build(
        story,
        onFirstPage=lambda canvas, built_doc: cover(canvas, built_doc, data, st),
        onLaterPages=lambda canvas, built_doc: footer(canvas, built_doc, version),
    )
    return output


if __name__ == "__main__":
    print(build())
