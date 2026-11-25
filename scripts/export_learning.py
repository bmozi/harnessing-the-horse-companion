#!/usr/bin/env python3
"""Export the public learning pilot as readable Markdown from its canonical JSON."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'learning/pilot.json').read_text())
for reference in data['references']:
 path=ROOT/'learning/reference'/f'{reference["slug"]}.md';path.parent.mkdir(parents=True,exist_ok=True)
 sources='\n'.join(f'- [{s["title"]}]({s["url"]})' for s in reference['sources'])
 path.write_text(f'# {reference["title"]}\n\n{reference["summary"]}\n\n{reference["body"]}\n## Source and further practice\n\nBook connection: {reference["book"]}.\n\n{sources}\n\nAuthor: John Briggs. Updated {data["updated"]}. This is original companion learning material; constructed examples are labeled.\n')
for number,lesson in enumerate(data['course']['lessons'],1):
 path=ROOT/'learning/verification'/f'{lesson["slug"]}.md';path.parent.mkdir(parents=True,exist_ok=True)
 options='\n'.join(f'{i+1}. {value}' for i,value in enumerate(lesson['options']))
 path.write_text(f'# Lesson {number}: {lesson["title"]}\n\n{lesson["summary"]}\n\n{lesson["body"]}\n## Retrieval check\n\n{lesson["question"]}\n\n{options}\n\n<details>\n<summary>Check your answer</summary>\n\nAnswer: {lesson["answer"]+1}. {lesson["feedback"]}\n\n</details>\n\n## Return later\n\n{lesson["retrieval"]}\n')
print('Exported three reference pages and four lessons')
