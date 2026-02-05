import re
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP

def split_into_sections(text: str):
    pattern = r"\n?\s*(\d+\.\s+[^\n]+)\n+"
    parts = re.split(pattern, text)

    sections = []
    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        body = parts[i + 1].strip()
        full_section = title + "\n" + body

        if len(full_section) > 300:
            sections.append(full_section)

    return sections

def chunk_sections(sections):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    docs = []
    for sec in sections:
        docs.extend(splitter.create_documents([sec]))
    return docs
