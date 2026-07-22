from memory import ChatMemory


memory = ChatMemory()


memory.add_message(
    "user",
    "Why VPN is not working?"
)


memory.add_message(
    "assistant",
    "Check your VPN credentials."
)


print(
    memory.get_history()
)


print("----------------")


print(
    memory.get_formatted_history()
)