class ChatMemory:

    def __init__(self):
        self.history = []


    def add_message(self, role, content):

        self.history.append(
            {
                "role": role,
                "content": content
            }
        )


    def get_history(self):

        return self.history


    def clear_memory(self):

        self.history = []


    def get_formatted_history(self):

        conversation = ""

        for message in self.history:

            conversation += (
                f"{message['role']}: "
                f"{message['content']}\n"
            )

        return conversation