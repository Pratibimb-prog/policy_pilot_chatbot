Policy-Pilot AI

Policy-Pilot AI is a local AI assistant designed to answer questions based on company policies. It uses a large language model (LLM) and vector-based document retrieval to provide accurate, context-aware responses.

This project is built with Python, Hugging Face Transformers, LangChain, and Gradio for a simple web interface.

Features

Intelligent Q&A: Ask questions about company policies and receive accurate answers.

Vector Search: Uses embeddings for fast document search and retrieval.

Local Deployment: Run the app locally on your machine with GPU acceleration.

Gradio Interface: Web-based GUI for interactive querying.

Hugging Face Models: Integrates open-source LLMs, with support for private models if you have access.
System Architecture
```mermaid
flowchart LR
    U[User] --> UI[Gradio UI]

    UI --> QH[Query Handler / QA Chain]

    QH --> EMQ["Embedding Model<br/>(Query)"]
    EMQ --> VS["Vector Store<br/>(FAISS / Chroma)"]

    VS --> R["Retriever<br/>(Top-k Policy Chunks)"]
    R --> QH

    QH --> LLM["Local LLM<br/>(HuggingFace Model on GPU)"]
    LLM --> UI

    %% Ingestion Pipeline
    subgraph Ingestion["Ingestion Pipeline (Offline)"]
        D[Policy Documents] --> TL[Text Loader]
        TL --> CH[Chunking]
        CH --> EMD["Embedding Model<br/>(Documents)"]
        EMD --> VS
    end
