# AI IT Helpdesk Chatbot

An AI-powered IT Helpdesk Chatbot built using Retrieval-Augmented Generation (RAG) to answer employee IT support queries from enterprise knowledge base documents. The chatbot also includes an IT ticketing system and knowledge base management through a Streamlit interface.

## Features

- AI-powered IT support chatbot
- Retrieval-Augmented Generation (RAG)
- FAISS vector search
- Sentence Transformers embeddings
- Groq LLM integration
- Source citations
- Chat history
- IT support ticket creation
- SQLite ticket database
- Knowledge base rebuild

## Tech Stack

- Python
- Streamlit
- FAISS
- Sentence Transformers
- Groq API
- LangChain
- SQLite

## Project Structure

```
AI-IT-Helpdesk-Chatbot/
│── app.py
│── chatbot.py
│── embeddings.py
│── retriever.py
│── document_loader.py
│── ticket_system.py
│── docs/
│── faiss.index
│── metadata.pkl
│── tickets.db
│── requirements.txt
│── README.md
```

## Installation

```bash
git clone https://github.com/your-username/AI-IT-Helpdesk-Chatbot.git

cd AI-IT-Helpdesk-Chatbot

pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Sample Questions

- What are the password requirements?
- How often should employees change their passwords?
- What is the MFA policy?
- My VPN authentication failed. What should I do?
- How do I reset my password?

## Future Improvements

- PDF document upload
- Persistent chat history
- Ticket priority and status
- Admin dashboard
- User authentication

## Author

**Muhammad Uzair**
