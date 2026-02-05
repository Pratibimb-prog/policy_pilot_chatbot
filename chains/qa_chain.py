from config.settings import QA_PROMPT, TOP_K
from llm.hf_llm import get_llm

def answer_question(question, vectordb):
    docs_with_scores = vectordb.similarity_search_with_score(
        question, k=TOP_K
    )
    docs_with_scores.sort(key=lambda x: x[1])

    docs = [doc for doc, _ in docs_with_scores]

    context = "\n\n".join(
        f"[Doc{i+1}] {doc.page_content.strip()}"
        for i, doc in enumerate(docs)
    )

    llm = get_llm()
    return llm.invoke(
        QA_PROMPT.format(context=context, question=question)
    ).strip()
