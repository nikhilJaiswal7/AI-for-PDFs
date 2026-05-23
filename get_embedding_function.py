from langchain_core.embeddings import FakeEmbeddings


def get_embedding_function():
    return FakeEmbeddings(size=1536)
