import telebot
from utils.handle_message import question_to_answer
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# configura o bot
bot = telebot.TeleBot(os.environ.get('bot_token'))


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
    bot.reply_to(message, f"Envie alguma dúvida em áudio ou em mensagem de texto que eu irei te ajudar \U0001F601. Capricha na pergunta, {message.chat.first_name}")


# lida com a mensagem 'about'
@bot.message_handler(commands=['about'])
def handle_about(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    #bot.reply_to(message, "Gilbot é um serviço de bot do telegram no qual perguntas recebidas via voz ou arquivo de áudio são respondidas com o que a wikipedia souber sobre o assunto. " +
    #                        "O bot foi desenvolvido durante o segundo período de 2021 para a disciplina de Telecomunicações, ministrada pelo professor Fernando Gil Vianna. ")
    about = "Gilbot é um serviço de bot do telegram no qual perguntas recebidas via voz ou arquivo de áudio são respondidas com o que a wikipedia souber sobre o assunto. O bot foi desenvolvido durante o segundo período de 2021 para a disciplina de Telecomunicações, ministrada pelo professor Fernando Gil Vianna."
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Entre em contato com os desenvolvedor:', url ='telegram.me/Danyel_C')) #url='telegram.me/DanyelC'))
    keyboard.add(telebot.types.InlineKeyboardButton('Entre em contato com os desenvolvedor:', url ='telegram.me/cmarquesluizgustavo'))
    keyboard.add(telebot.types.InlineKeyboardButton('Entre em contato com os desenvolvedor:', url ='telegram.me/Gustavo32123'))
    bot.send_message(message.chat.id,about,reply_markup=keyboard)

# lida com mensagens de voz ou audio, carro chefe do bot
@bot.message_handler(content_types=['voice', 'audio'])
def handle_audio(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id,"Fala que eu te escuto!")
    
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