import configparser
import telebot
from utils.handle_message import question_to_answer
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# configura o bot
config = configparser.ConfigParser()
config.sections()
config.read('gilbot.conf')
bot = telebot.TeleBot(config['DEFAULTS']['bot_token'])




# lida com a mensagem 'start'
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, f'Oi, {message.chat.first_name}! \U0001F601')

# lida com a mensagem 'stop'
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "Não vou ajudar não")


# lida com a mensagem 'about'
@bot.message_handler(commands=['about'])
def handle_about(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, "Gilbot é um serviço de bot do telegram no qual perguntas recebidas via voz ou arquivo de audio são respondidas com o que a wikipedia souber sobre o assunto.")


# lida com mensagens de voz ou audio, carro chefe do bot
@bot.message_handler(content_types=['voice', 'audio'])
def handle_audio(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")

    if message.voice:
        print('Mensagem de voz')
        file_info = bot.get_file(message.voice.file_id)
        answer = question_to_answer(None, file_info.file_path)

        # downloaded_file = bot.download_file(file_info.file_path)
        bot.send_voice(message.chat.id, answer) 
    else:
        print('Mensagem de audio')
        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        bot.send_audio(message.chat.id, downloaded_file)


# lida com mensagens de texto, informando que só consegue conversar por voz
@bot.message_handler(content_types=['text'])
def handle_audio(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id,"Manda em audio ai, "+message.chat.first_name)
    bot.send_message(message.chat.id, f"Tu falou: <i>{message.text}</i>.\n Foi poético.",  parse_mode="HTML")

print('GilBot ativado')

def start_pooling():
    bot.polling()
