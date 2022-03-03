import configparser
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

 
config = configparser.ConfigParser()
config.sections()
config.read('conf/gilbot.conf')
bot = telebot.TeleBot(config['DEFAULTS']['bot_token'])


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, f'Oi, {message.chat.first_name}! \U0001F601')


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "Não vou ajudar não")



@bot.message_handler(commands=['about'])
def handle_about(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "Não fiz ainda")



@bot.message_handler(content_types=['voice', 'audio']) # ou audio ?
def handle_audio(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id,"Ouça isso novamente, "+message.chat.first_name)

    if message.voice:
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        bot.send_voice(message.chat.id, downloaded_file) # ou send audio
    else:
        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        bot.send_audio(message.chat.id, downloaded_file) # ou send audio



@bot.message_handler(content_types=['text'])
def handle_audio(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id,"Manda em audio ai, "+message.chat.first_name)
    bot.send_message(message.chat.id, f"Tu falou: <i>{message.text}</i>.\n Foi poético.",  parse_mode="HTML")

print('GilBot ativado')
bot.polling()
