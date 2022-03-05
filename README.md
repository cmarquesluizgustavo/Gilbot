# GilBot

Gilbot é um serviço de bot do telegram no qual perguntas recebidas via voz ou arquivo de audio são respondidas com o que a wikipedia souber sobre o assunto.

## Como usar

Para usar esse bot como seu, basta replicar esse repositório, criar um arquivo gilbot.conf na raiz do repositório com o seguinte conteúdo:

```
[DEFAULTS]
bot_token = [SEU_TOKEN]
```

No qual `[SEU_TOKEN]` é o token retornado pelo Bot Father.

Depois disso, basta executar o arquivo `main.py` com o comando:

```bash
python3 main.py
```

## Requisitos

- Python
- ffpmeg

---

## Licença

[ISC](./LICENSE)
