# GilBot

Gilbot é um serviço de bot do telegram no qual perguntas recebidas via voz ou arquivo de audio são respondidas com o que a wikipedia souber sobre o assunto.

## Como usar

- Para usar esse bot como seu, basta replicar esse repositório, criar um arquivo `.env` na raiz do repositório com o seguinte conteúdo:

  ```
  bot_token=[SEU_TOKEN]
  ```

  No qual `[SEU_TOKEN]` é o token retornado pelo Bot Father.

- Depois disso, precisamos criar a imagem:

  ```bash
  docker build -t gilbot:latest .
  ```

  Quando desejar rodar o bot, basta executar os seguintes comandos:

  ```bash

  docker run --env-file ./.env --name gilbot --rm -d gilbot:latest
  ```

- Para parar, basta executar:

  ```bash
  docker stop gilbot
  ```

---

## Licença

[ISC](./LICENSE)

```

```
