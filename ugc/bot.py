from django.core.management.base import BaseCommand
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater, CommandHandler
from telegram.utils.request import Request
from django.conf import settings
from ugc.models import Profile, Message


def sendMessage(update: Update, context: CallbackContext):
  update.message.reply_text(
    text=text,
  )

def send(text):
# Подключение
  request = Request(
      connect_timeout=0.5,
      read_timeout=1.0,
    )
  bot = Bot(
      request=request,
      token=settings.TOKEN,
    )
  print(bot.get_me())
  # обработчики 
  updater = Updater(
    bot=bot,
    use_context=True,
  )
  
  updater.message.reply_text(
    text=text,
  )


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def start():
  updater = Updater(settings.TOKEN)

  updater.dispatcher.add_handler(CommandHandler('hello', hello))
  updater.start_polling()
  updater.idle()
