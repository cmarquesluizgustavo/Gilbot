from utils.speech_and_text import make_audio, check_cordialidade, get_answer, voice_to_text

# recebe a pergunta por voz ou texto e retorna a resposta via audio
def question_to_answer(text_question = None, voice_question = None, nome = "Estudante"):
    print('chegou')

    try:
        if not text_question:
            if not voice_question: raise Exception("Neither voice nor text received")
            text_question = voice_to_text(voice_question, nome)
    except Exception as e:
        print("o erro")
        print(e)
        errorResponse = 'Desculpe, não consegui compreender o que você disse. Poderia repetir?'
        return [make_audio(errorResponse), errorResponse]


    cordialidade      = check_cordialidade(text_question, nome)
    answer            = get_answer(text_question)
    resposta_completa = cordialidade + answer
    
    return [make_audio(resposta_completa), resposta_completa]
