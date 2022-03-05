import random
import datetime
import subprocess
from io import BytesIO
from gtts import gTTS
import speech_recognition as sr

# Recebe um audio e transforma em texto
def voice_to_text(filepath, nome, language = "pt-BR"):
    transcoded_audio = transcode_to_wav(filepath, nome)
    audio_file = sr.AudioFile(transcoded_audio)

    r = sr.Recognizer()

    with audio_file as source:
        user_audio = r.record(source)

    text = r.recognize_google(user_audio, language = language)
    subprocess.run(['rm', transcoded_audio])

    return text

# Recebe um texto e transforma em audio
def make_audio(text, language = "pt-BR"):
    tts = gTTS(text, lang = language)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp


# Gera um arquivo de audio do tipo wav
def transcode_to_wav(voice_data, username = "Estudante"):
    time_identifier      = str(datetime.datetime.now()).split()[1].replace(":", ".")
    time_user_identifier = time_identifier + username
    src_filename  = f'/content/{time_user_identifier}-question.wav'
    dest_filename = f'/content/{time_user_identifier}-answer.wav'

    f = open(src_filename, "wb")
    f.write(voice_data)
    f.close()

    process = subprocess.run(['ffmpeg', '-i', src_filename, dest_filename])
    if process.returncode != 0:
        raise Exception("Unable to transcode")
    subprocess.run(['rm', src_filename])
    return dest_filename




# Adiciona um toque mais pessoal a resposta, em busca de soar menos robótico
def check_cordialidade(text, nome):
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
        adicionar_a_resposta.append("Mas qual a palavrinha mágica?")
    
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

    
    boa_pergunta = ["Boa pergunta", "Ótima pergunta", 
                    "Excelente pergunta", "Deixa eu te explicar"]
    adicionar_a_resposta.append(random.choice(boa_pergunta) +", " +  nome + ". ")
    


    cordialidades = ' '.join(adicionar_a_resposta)


    return cordialidades

# Recebe a pergunta e retorna a resposta, usando a wikipedia
def get_answer(pergunta):
    question_summon = ["o que é", "me explica", "me ajuda com"]
    for summon in question_summon:
        if summon in pergunta:
            search_key = pergunta.split(summon)[1]
            return wiki_get(search_key)
    return "Não captei sua dúvida"