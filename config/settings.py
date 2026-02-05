# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Embeddings
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Vector DB
COLLECTION_NAME = "company_policy_v2"
TOP_K = 2

# LLM
LLM_MODEL_ID = "Qwen/Qwen-2B-Chat"
MAX_NEW_TOKENS = 120
TEMPERATURE = 0.7

# Prompt
QA_PROMPT = """
You must answer the question ONLY using the context below.

Rules:
- Every sentence must include a citation like [Doc X].
- Do NOT use outside knowledge.
- If the answer is not present, say:
"I don't know based on the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
