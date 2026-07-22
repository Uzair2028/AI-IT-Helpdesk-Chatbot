import os
from langchain_text_splitters import RecursiveCharacterTextSplitter


DOCS_FOLDER = "docs"


def load_documents():

    documents = []

    for file in os.listdir(DOCS_FOLDER):

        if file.endswith(".txt"):

            path = os.path.join(
                DOCS_FOLDER,
                file
            )

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:

                text = f.read()


            documents.append(
                {
                    "text": text,
                    "source": file
                }
            )


    return documents



def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )


    chunks = []


    for doc in documents:

        split_texts = splitter.split_text(
            doc["text"]
        )


        for chunk in split_texts:

            chunks.append(
                {
                    "text": chunk,
                    "source": doc["source"]
                }
            )


    return chunks



def load_and_split():

    documents = load_documents()

    chunks = split_documents(
        documents
    )

    return chunks



if __name__ == "__main__":

    chunks = load_and_split()

    print(
        "Total chunks:",
        len(chunks)
    )


    print(
        chunks[0]
    )