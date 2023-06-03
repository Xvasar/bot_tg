import telegram
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello, I'm a bot!")

def main():
    updater = Updater(token='YOUR_TOKEN_HERE', use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()

if __name__ == '__main__':
    main()
