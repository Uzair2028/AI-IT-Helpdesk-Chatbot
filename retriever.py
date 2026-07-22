import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL


embedding_model = SentenceTransformer(EMBEDDING_MODEL)


index = faiss.read_index("vector_store/faiss.index")


with open("vector_store/metadata.pkl", "rb") as f:
    all_chunks = pickle.load(f)


def retrieve_context(query, k=3):

    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(query_embedding, k)

    results = []

    for idx in indices[0]:
        results.append(all_chunks[idx])

    return results