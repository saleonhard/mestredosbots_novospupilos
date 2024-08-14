"""
Mestre Dos Bots - Worker de Saudação - Arquivo Main

Descrição:
Este script faz parte do projeto "Mestre Dos Bots", sendo responsável por saudar novos seguidores 
no Twitter com mensagens personalizadas e salvar frases criativas dos seguidores. O bot também interage 
com a API do Google Sheets para armazenar e gerenciar dados.

Objetivo:
Este projeto foi criado para fins de aprendizagem, visando aprimorar habilidades em programação, 
automação de tarefas com bots, e integração com APIs como Twitter e Google Sheets.

Dependências:
- Python 3.x
- tweepy: Biblioteca para interagir com a API do Twitter.
- gspread: Biblioteca para manipular planilhas do Google Sheets.
- oauth2client: Biblioteca para autenticação via OAuth 2.0.
- Outros módulos personalizados: gerador_meme, pop, keys.

Como usar:
1. Configure suas credenciais da API do Twitter e do Google Sheets.
2. Coloque suas credenciais no arquivo `keys.py` e `credenciais.json` (ou use variáveis de ambiente).
3. Execute o script em um ambiente configurado, como o Heroku, para que ele rode continuamente.

Autor: Leonardo Aquino
Data de Criação: 20/09/2020

Licença:
Distribuído sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário.

"""


import tweepy
import time, datetime
from keys import *
from gerador_meme import *
import random
import string
import os
import gspread
from pop import *
from oauth2client.service_account import ServiceAccountCredentials


nada = False

# Usando as credenciais do Google Drive API
scope = ["https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
client = gspread.authorize(creds)

# Abrindo planilha.
sheet = client.open("Mestre Dos Bots").worksheet("Frases Pupilos")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


while True:

    saudar()
    print("🕵 Analisando timeline...")
    ultimo_verificado = int(sheet.acell("E2").value)
    rpy = api.user_timeline(
        "@mestredosbots", since_id=ultimo_verificado, tweet_mode="extended", count=40
    )
    nada = False

    for r in reversed(rpy):
        if r.id != ultimo_verificado:
            if r.full_text.startswith("RT @") == True:
                print("\n🔄 Retweet encontrado!")
                tmp = (datetime.datetime.utcnow() - r.created_at).seconds / 60
                print("⌚ Tempo: ", tmp)
                if tmp >= 60:
                    print("⏳ Dentro do prazo!")
                    ultimo_verificado = sheet.update("E2", str(r.id))
                    likes = r.retweeted_status.favorite_count
                    print("👍 Curtidas: ", likes)
                    if likes >= 100:
                        print("👀 Número de curtudas válido")
                        id = r.retweeted_status.id_str
                        print("	Retweet ID:", id)
                        print("📝 Texto: ", r.retweeted_status.full_text)
                        id = api.get_status(
                            id=id, tweet_mode="extended"
                        ).in_reply_to_status_id
                        print("	ID Resposta:", id)
                        tweet = api.get_status(id=id, tweet_mode="extended")
                        user = tweet.author.screen_name
                        txt = tweet.full_text
                        print("	Tweet Menção: ", txt)
                        txt = txt.replace("#seupupilodisse", "")

                        if txt == "":

                            id = api.get_status(
                                id=id, tweet_mode="extended"
                            ).in_reply_to_status_id
                            tweet = api.get_status(id=id, tweet_mode="extended")
                            txt = tweet.full_text
                            user = tweet.author.screen_name
                            txt = txt.replace("#seupupilodisse", "")
                        if "https://t.co/" in txt:
                            txt = txt[:-23]
                        linha = str(sheet.acell("E5").value)
                        sheet.update("A" + linha, txt)
                        sheet.update("B" + linha, "@" + str(user))
                        sheet.update("C" + linha, False)

                        qnt = int(sheet.acell("E8").value)
                        print("💩 Frase salva para analise!")
                        if qnt < 100:
                            sheet.update("E8", int(qnt) + 1)

                        if linha != "100":
                            sheet.update("E5", int(linha) + 1)
                        else:
                            sheet.update("E5", 2)

                    else:
                        print("Número de curtidas inválido\nFrase não selecionada 😢")
                else:
                    print("⌛ Fora do prazo!")
                    break

            else:
                nada = True

    time.sleep(10)

    if nada:
        print("	Nenhum retweet encontrado 😓")
    print("_______________________________________")
