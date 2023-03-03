import openai
from .userconf import chat


def chatgpt(tg_id, prompt):
    openai.api_key = chat.openai_key[tg_id]
    try:
        completions = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt
        )
        messages = completions.choices[0].message.content.strip()
        chat.save_bot_chat(tg_id, messages)
        return messages
    except Exception as messages:
        return messages
