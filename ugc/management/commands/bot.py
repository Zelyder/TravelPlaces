from django.core.management.base import BaseCommand
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater
from telegram.utils.request import Request
from django.conf import settings
from ugc.models import Profile, Message


def log_errors(f):

  def inner(*args, **kwargs):
    try:
      return f(*args, **kwargs)
    except Exception as e:

      error_message = f'Произошла ошибка: {e}'
      print(error_message)
      raise e
  return inner

@log_errors
def do_echo(update: Update, context: CallbackContext):
  chat_id = update.message.chat_id
  text = update.message.text

  profile, _ = Profile.objects.get_or_create(
    external_id = chat_id,
    defaults={
      'name': update.message.from_user.username,
    }
  )
  Message(
    profile=profile,
    text=text,
  ).save()

  reply_text = "Ваш ID = {}\n\n{}".format(chat_id, text)
  update.message.reply_text(
    text=reply_text,
  )

class Command(BaseCommand):
  help = 'Телеграм-бот'

  def handle(self, *args, **options):
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

    message_handler = MessageHandler(Filters.text, do_echo)
    updater.dispatcher.add_handler(message_handler)

    # Запустить бесконечную обработку входящих сообщений
    updater.start_polling()
    updater.idle()

def sendMessage(update: Update, text):
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