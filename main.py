from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import subprocess

from dotenv import load_dotenv
import os
import random

load_dotenv()

# добавляем возможность извлекать id стикеров из файла
def load_sticker_ids(file):
    with open(file, "r") as f:
        sticker_ids = [line.strip() for line in f]
    return sticker_ids

def main():
    api = os.environ.get("API")
    chat_id = os.getenv("CHAT_ID")

    sticker_file = "/home/ubuntu/faf_tg_bot/ids"
    sticker_ids = load_sticker_ids(sticker_file)

    updater = Updater(api, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.command & Filters.regex('^/play'), lambda update, context: play(update, context, chat_id, sticker_ids)))    
    dp.add_handler(MessageHandler(Filters.command & Filters.regex('^/notplay'), notplay))
    dp.add_handler(MessageHandler(Filters.command & Filters.regex('^/whoplaytoday'), whoplaytoday))
    dp.add_handler(MessageHandler(Filters.command & Filters.regex(r'.*@'), unknown))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    updater.start_polling()
    updater.idle()

def play(update, context: CallbackContext, chat_id, sticker_ids):
    user_id = update.message.from_user.id
#   user_name = update.message.from_user.username
    first_name = update.message.from_user.first_name
# last_name - при необходимости
    last_name = update.message.from_user.last_name
    file = open("/home/ubuntu/faf_tg_bot/get.md", "w")
#   file.write(f"{user_name} не будет играть.")
    file.write(f"{first_name} будет играть.")
    file.close()
    subprocess.run(["/home/ubuntu/faf_tg_bot/run.sh"])
# отправляем рандомный стикер из списка
    sticker_id = random.choice(sticker_ids)
    context.bot.send_sticker(chat_id, sticker_id)

def notplay(update, context: CallbackContext):
    user_id = update.message.from_user.id
#   user_name = update.message.from_user.username
    first_name = update.message.from_user.first_name
# last_name - при необходимости
    last_name = update.message.from_user.last_name
    file = open("/home/ubuntu/faf_tg_bot/get.md", "w")
#   file.write(f"{user_name} не будет играть.")
    file.write(f"{first_name} не будет играть.")
    file.close()
    subprocess.run(["/home/ubuntu/faf_tg_bot/not_run.sh"])

def whoplaytoday(update, context: CallbackContext):
    user_id = update.message.from_user.id
#   user_name = update.message.from_user.username
    first_name = update.message.from_user.first_name
# last_name - при необходимости
    last_name = update.message.from_user.last_name
    subprocess.run(["/home/ubuntu/faf_tg_bot/who_play.sh"])

def unknown(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Такой комманды не существует. Вот список доступных комманд:\n"
             "/play - буду играть\n"
             "/notplay - не буду играть\n"
             "/whoplaytoday - кто играет сегодня?"
    )

if __name__ == '__main__':
    main()
