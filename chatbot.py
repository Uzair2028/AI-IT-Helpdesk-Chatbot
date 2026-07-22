from groq import Groq

from config import GROQ_API_KEY, MODEL_NAME
from retriever import retrieve_context

client = Groq(api_key=GROQ_API_KEY)


def ask_helpdesk(question):

    results = retrieve_context(question)

    context = "\n\n".join(
        [item["text"] for item in results]
    )

    sources = list(set(
        item["source"] for item in results
    ))

    prompt = f"""
You are TechNova AI IT Helpdesk Assistant.

Rules:
- Answer ONLY using the provided context.
- If the answer is not available, reply:
"I couldn't find this information in the company knowledge base."
- Be concise and professional.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    answer = response.choices[0].message.content

    return answer, sources