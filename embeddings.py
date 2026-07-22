import os
import faiss
import pickle

from sentence_transformers import SentenceTransformer

from document_loader import load_and_split
from config import EMBEDDING_MODEL


VECTOR_FOLDER = "vector_store"


def create_embeddings():

    print("Loading documents...")

    chunks = load_and_split()


    texts = [
        chunk["text"]
        for chunk in chunks
    ]


    print("Loading embedding model...")

    model = SentenceTransformer(
        EMBEDDING_MODEL
    )


    print("Creating embeddings...")

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )


    dimension = embeddings.shape[1]


    index = faiss.IndexFlatL2(
        dimension
    )


    index.add(
        embeddings
    )


    os.makedirs(
        VECTOR_FOLDER,
        exist_ok=True
    )


    faiss.write_index(
        index,
        f"{VECTOR_FOLDER}/faiss.index"
    )


    with open(
        f"{VECTOR_FOLDER}/metadata.pkl",
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )


    print("================================")
    print("Knowledge Base Updated ✅")
    print("Total chunks:", len(chunks))
    print("================================")



if __name__ == "__main__":

    create_embeddings()