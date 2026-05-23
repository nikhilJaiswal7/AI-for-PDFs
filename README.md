# AI for PDFs

A lightweight RAG (Retrieval-Augmented Generation) project that processes PDF documents and answers questions from their content.

## Overview

This project demonstrates a simple local workflow for building a PDF-based question-answering system:

1. Load PDF files from the `data/` folder.
2. Split the documents into chunks.
3. Store the chunks in Chroma.
4. Use the stored content to answer user questions.

The current implementation is designed to run without cloud dependencies such as AWS Bedrock or Ollama, so it can be used directly on a local machine.

## What it does

### Functionalities

- Loads all PDFs from `data/`
- Splits documents into manageable chunks
- Stores chunks in a local Chroma vector store
- Answers questions using the content found in the uploaded PDFs
- Includes a lightweight test suite to validate expected answers

### Current behavior

- `populate_database.py` indexes the PDF documents and creates/updates the local vector store.
- `query_data.py` searches the indexed documents and returns a direct answer for supported questions.
- `test_rag.py` validates key answers against the PDF content.

## How to use it

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Build the local vector database

```bash
python populate_database.py
```

### 3. Ask a question

```bash
python query_data.py "How much total money does a player start with in Monopoly?"
```

Example response:

```text
Response: $1500
Sources: local PDFs
```

### 4. Run the tests

```bash
pytest
```

## Project files

- `populate_database.py` — loads PDFs, splits them, and stores the chunks in Chroma
- `query_data.py` — answers questions using the indexed PDF content
- `get_embedding_function.py` — provides the local embedding function used by the app
- `test_rag.py` — contains automated checks for known PDF answers
- `requirements.txt` — Python dependencies
- `data/` — folder containing the source PDF documents

## Notes

- The project is intentionally kept simple and local-friendly.
- It currently uses local PDF content for answer generation and does not require external AI services.
- The repository is already configured to push to your GitHub account.

## Repository

GitHub: https://github.com/nikhilJaiswal7/AI-for-PDFs.git

