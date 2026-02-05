from ingestion.loader import load_text_file
from ingestion.splitter import split_into_sections, chunk_sections
from vectorstore.chroma_db import create_vectorstore
from ui.gradio_app import launch_ui

FILE_PATH = "companyPolicies.txt"

def main():
    text = load_text_file(FILE_PATH)
    sections = split_into_sections(text)
    docs = chunk_sections(sections)
    vectordb = create_vectorstore(docs)
    launch_ui(vectordb)

if __name__ == "__main__":
    main()