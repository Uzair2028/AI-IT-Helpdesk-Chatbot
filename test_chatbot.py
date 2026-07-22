from chatbot import ask_helpdesk

answer, sources = ask_helpdesk(
    "Why is VPN authentication failing?"
)

print("\nAnswer:\n")
print(answer)

print("\nSources:\n")
print(sources)