from telegram.ext import Updater
from telegram.ext import CommandHandler
import config
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=config.CONFIGS['TOKEN'], use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")







start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()