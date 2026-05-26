import numpy as np
from fastembed import TextEmbedding
from config import FASTEMBED_MODEL_NAME, DOCUMENTS_PATH
from logging_config import logger   
def _cosine_similarity(vec1:np.ndarray, vec2:np.ndarray) -> float:
    """Calculate the cosine similarity between two vectors."""
    norm1=np.linalg.norm(vec1)
    norm2=np.linalg.norm(vec2)
    return np.dot(vec1, vec2) / (norm1 * norm2) if norm1 and norm2 else 0.0
def _read_text():
    documents = DOCUMENTS_PATH.read_text(encoding="utf-8").splitlines()
    logger.debug(f"Read {len(documents)} documents from {DOCUMENTS_PATH}")
    return documents
def _embed_documents(documents, model):
    embeddings = model.embed(documents) #generator of embeddings
    logger.debug(f"Generated embeddings for {len(documents)} documents")
    return embeddings
def _find_most_similar_document(query: str, model) -> str:
    documents = _read_text()
    document_embeddings:np.ndarray = np.array(list(_embed_documents(documents, model)))
    query_embedding:np.ndarray = np.array(list(model.embed([query]))[0]) #embedding for the query
    logger.debug(f"Generated embedding for query: '{query}'")
    logger.debug(f"Document embeddings shape: {document_embeddings.shape}, Query embedding shape: {query_embedding.shape}")
    similarities = [_cosine_similarity(query_embedding, doc_emb) for doc_emb in document_embeddings]
    most_similar_index = np.argmax(similarities)
    logger.debug(f"Most similar document index: {most_similar_index}, similarity: {similarities[most_similar_index]:.4f}")
    return documents[most_similar_index]
def main():
    model = TextEmbedding(FASTEMBED_MODEL_NAME)
    query = "Travelling to Africa"
    most_similar_document = _find_most_similar_document(query, model)
    print("Most similar document:", most_similar_document)
if __name__ == "__main__":
    main()