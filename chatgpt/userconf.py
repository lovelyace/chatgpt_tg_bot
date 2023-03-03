class UserConf():
    def __init__(self):
        self.chat_history = {}
        self.openai_key = {}

    def save_user_chat(self, tg_id, message):
        message = {"role": "user", "content": message}
        try:
            self.chat_history[tg_id].append(message)
        except KeyError:
            self.chat_history[tg_id] = [message]

    def save_bot_chat(self, tg_id, message):
        message = {"role": "assistant", "content": message}
        self.chat_history[tg_id].append(message)


chat = UserConf()
