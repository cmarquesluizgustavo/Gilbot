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
        downloaded_file = bot.download_file(file_info.file_path)
        [answer, textAnwser] = question_to_answer(None, downloaded_file, message.chat.first_name)
        print('\n\n\n')
        print('----------------- RESPOSTA --------------------')
        print(textAnwser)
        print('----------------- FIM RESPOSTA --------------------')
        print('\n\n')
        bot.send_voice(message.chat.id, answer) 
    else:
        print('Mensagem de audio')
        file_info = bot.get_file(message.audio.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        [answer, textAnwser] = question_to_answer(None, downloaded_file, message.chat.first_name)
        print('\n\n\n')
        print('----------------- RESPOSTA --------------------')
        print(textAnwser)
        print('----------------- FIM RESPOSTA --------------------')
        print('\n\n')
        bot.send_audio(message.chat.id, answer)


# lida com mensagens de texto, informando que só consegue conversar por voz
@bot.message_handler(content_types=['text'])
def handle_text(message):
    print('Mensagem de texto')
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id,"Podia ter mandando em audio ein, "+message.chat.first_name)
    [_, textAnwser] = question_to_answer(message.text, None, message.chat.first_name)
    print('\n\n\n')
    print('----------------- RESPOSTA --------------------')
    print(textAnwser)
    print('----------------- FIM RESPOSTA --------------------')
    print('\n\n')
    bot.send_message(message.chat.id, f"{textAnwser}",  parse_mode="HTML")

print('GilBot ativado\n\n\n')

def start_pooling():
    bot.polling()
