from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import subprocess

from dotenv import load_dotenv
import os
load_dotenv()

def main():
    api = os.environ.get("API")
    updater = Updater(api, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.command & Filters.regex('^/play'), play))
    dp.add_handler(MessageHandler(Filters.command & Filters.regex('^/notplay'), notplay))
    dp.add_handler(MessageHandler(Filters.command & Filters.regex('^/whoplaytoday'), whoplaytoday))
    updater.start_polling()
    updater.idle()

def play(update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username
    file = open("./get.md", "w")
    file.write(f"{user_name} будет играть.")
    file.close()
    subprocess.run(["./run.sh"])

def notplay(update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username
    file = open("./get.md", "w")
    file.write(f"{user_name} не будет играть.")
    file.close()
    subprocess.run(["./not_run.sh"])

def whoplaytoday(update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username
    subprocess.run(["./who_play.sh"])

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