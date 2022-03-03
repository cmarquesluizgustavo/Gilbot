import random
import datetime
from gtts      import gTTS
from playsound import playsound
import speech_recognition as sr

def voice_to_text(filepath = "/content/testee.wav", language = "pt-BR"):
    r          = sr.Recognizer()
    audio_file = sr.AudioFile(filepath)

    with audio_file as source:
        user_audio = r.record(source)

    text = r.recognize_google(user_audio, language = language)

    return text


def make_audio(text, language = "pt-BR"):
    tts = gTTS(text, lang = language)
    tts.save('/content/resposta.mp3')



def check_cordialidade(text, nome = "estudante"):
    now = datetime.datetime.now()
    text = text.lower()
    adicionar_a_resposta = []

    cordialidades_hora       = ["bom dia", "boa tarde", "boa noite"]
    
    cordialidades_pedido     = ["por favor", "por gentileza", 
                                "deixa eu te perguntar",  "me tira uma duvida"]

    cordialidade_cumprimento = ["tudo bem", "tudo beleza", "como vai", "fala professor", 
                                "fala gil", "fala gil bot", "fala bot", "tudo certo"]

    gentiliza   = False
    cumprimento = False

    for palavra in cordialidade_cumprimento:
        if palavra in text.lower():
            gentiliza = True

    for palavra in cordialidades_pedido:
        if palavra in text.lower():
            gentiliza = True

    if not gentiliza:
        adicionar_a_resposta.append("mas qual a palavrinha mágica?")
    
    if cumprimento:
        adicionar_a_resposta.append("Tudo bem sim, e você?")

    if now.hour > 8 and now.hour < 15:
        if cordialidades_hora[1] in text:
            adicionar_a_resposta.append(f"que {cordialidades_hora[1]} o que, bom dia.")

        elif cordialidades_hora[2] in text:
            adicionar_a_resposta.append(f"que {cordialidades_hora[2]} o que, bom dia.")
        
        else:
            adicionar_a_resposta.append("bom dia.")
    
    elif now.hour > 15:
        if cordialidades_hora[0] in text:
            adicionar_a_resposta.append(f"que {cordialidades_hora[0]} o que, boa tarde.")

        elif cordialidades_hora[1] in text:
            adicionar_a_resposta.append(f"que {cordialidades_hora[2]} o que, boa tarde.")
        
        else:
            adicionar_a_resposta.append("boa tarde.")

    elif now.hour > 21 or now.hour < 8:
        if cordialidades_hora[0] in text:
            adicionar_a_resposta.append(f"que {cordialidades_hora[0]} o que, boa noite.")

        elif cordialidades_hora[1] in text:
            adicionar_a_resposta.append(f"que {cordialidades_hora[1]} o que, boa noite.")

        else:
            adicionar_a_resposta.append("boa tarde.")

    
    boa_pergunta = ["boa pergunta ", "ótima pergunta ", 
                    "excelente pergunta ", "deixa eu te explicar "]
    adicionar_a_resposta.append(random.choice(boa_pergunta) +", " +  nome + ". ")
    


    cordialidades = ' '.join(adicionar_a_resposta)


    return cordialidades


def get_answer(pergunta):
    question_summon = ["o que é", "me explica", "me ajuda com"]
    for summon in question_summon:
        if summon in pergunta:
            search_key = pergunta.split(summon)[1]
            return search_key
    return "Não captei sua dúvida"


