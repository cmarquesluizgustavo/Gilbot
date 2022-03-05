import utils.telegram_bot
import utils.wiki_requests
import utils.speech_and_text

# recebe a pergunta por voz ou texto e retorna a resposta via audio
def question_to_answer(text_question = None, voice_question = None, nome = "Estudante"):

    if not text_question:
        if not voice_question: raise Exception("Neither voice nor text received")
        text_question = voice_to_text(voice_question, nome)


    cordialidade      = check_cordialidade(text_question, nome)
    answer            = get_answer(text_question)
    resposta_completa = cordialidade + answer
    
    return [make_audio(resposta_completa), resposta_completa]

