from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters

from help import *
from chatgpt import *


def main():
    application = ApplicationBuilder().token(f'{token}').build()

    """  START/HELP  """
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', start))

    """  chatgpt  """
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("chatgpt", chatgpt_satrt)],
            states={
                chatgpt_command: [
                    MessageHandler(
                        (filters.TEXT & ~filters.COMMAND), chatgpt_continue)
                ],
                chatgpt_apikey: [
                    MessageHandler(
                        (filters.TEXT & ~filters.COMMAND), get_apikey)
                ]
            },
            fallbacks=[
                CommandHandler("cancel", cancel),
                CommandHandler("renew", renew)
            ],
        )
    )

    application.run_polling()  # 不终止tg-bot


if __name__ == '__main__':
    token = ''
    main()
