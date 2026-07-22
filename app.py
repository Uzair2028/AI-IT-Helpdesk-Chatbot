import streamlit as st
import os

from chatbot import ask_helpdesk
from ticket_system import (
    initialize_database,
    create_ticket,
    get_all_tickets
)

from embeddings import create_embeddings


# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="TechNova AI Helpdesk",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Initialize
# -----------------------------

initialize_database()


if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("🏢 TechNova AI")

    st.success("🟢 Knowledge Base Active")


    st.markdown("---")


    st.subheader("📚 Knowledge Base")

    documents = []

    if os.path.exists("docs"):

        documents = [
            file for file in os.listdir("docs")
            if file.endswith(".txt")
        ]


    st.metric(
        "Documents",
        len(documents)
    )


    st.write("Files:")

    for doc in documents:
        st.write("📄", doc)


    st.markdown("---")


    # -----------------------------
    # Rebuild Knowledge Base
    # -----------------------------

    st.subheader("🔄 Update Knowledge Base")


    if st.button("Rebuild Index"):

        with st.spinner(
            "Creating embeddings..."
        ):

            create_embeddings()


        st.success(
            "Knowledge Base Updated!"
        )


    st.markdown("---")


    # -----------------------------
    # Tickets
    # -----------------------------

    st.subheader("🎫 Recent Tickets")


    tickets = get_all_tickets()


    if tickets:

        for ticket in tickets[:5]:

            st.write(
                f"#{ticket[0]} - {ticket[2]}"
            )

    else:

        st.info(
            "No tickets created"
        )



# -----------------------------
# Main UI
# -----------------------------

st.title(
    "🤖 TechNova AI IT Helpdesk"
)


st.caption(
    "Enterprise RAG Chatbot powered by FAISS + Groq + Sentence Transformers"
)



# -----------------------------
# Display Chat History
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )



# -----------------------------
# Chat Input
# -----------------------------

question = st.chat_input(
    "Ask your IT question..."
)


if question:


    # User message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    with st.chat_message("user"):

        st.markdown(question)



    # AI Response

    with st.chat_message("assistant"):

        with st.spinner(
            "Searching knowledge base..."
        ):

            try:

                answer, sources = ask_helpdesk(
                    question
                )


            except Exception as e:

                answer = (
                    "❌ Something went wrong.\n\n"
                    f"{e}"
                )

                sources = []


        st.markdown(answer)


        if sources:

            st.markdown("---")

            st.write(
                "📄 Sources:"
            )

            for source in sources:

                st.success(source)



    # Save assistant message

    final_response = answer


    if sources:

        final_response += (
            "\n\n📄 Sources:\n"
        )

        for s in sources:

            final_response += (
                f"- {s}\n"
            )


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_response
        }
    )



# -----------------------------
# Ticket Creation
# -----------------------------

st.markdown("---")


st.subheader(
    "🎫 Create IT Support Ticket"
)


ticket_issue = st.text_input(
    "Describe your issue"
)


if st.button(
    "Create Ticket"
):

    if ticket_issue:

        ticket_id = create_ticket(
            ticket_issue
        )


        st.success(
            f"Ticket #{ticket_id} created successfully!"
        )

    else:

        st.warning(
            "Please enter an issue."
        )