"""
Mestre Dos Bots - Worker de Saudação - Arquivo Sec

Autor: Leonardo Aquino
Data de Criação: 20/09/2020

Licença:
Distribuído sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário.

"""

import tweepy
import time
from keys import *
import random
import string
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Usando as credenciais do Google Drive API
scope = ["https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
client = gspread.authorize(creds)

# Abrindo planilha.
sheet = client.open("Mestre Dos Bots").sheet1

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
api2 = tweepy.API(auth2, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def saudar(last_seen_id=0):
    txt = ""
    ativo = "nao"

    print(" 🔎 Buscando novo pupilo...", flush=True)
    numf = api.me().followers_count
    print("	Qnt. de pupilos: ", numf)

    qntf = int(sheet.acell("A47").value)
    ultimouser = sheet.acell("A50").value
    new = numf - qntf
    print("	Qnt. de Novos pupilos: ", new)
    print("	Último pupilo: ", ultimouser)

    if new < 0:
        sheet.update("A47", str(numf))
        ultimo = api2.followers(screen_name="mestredosbots", count=1)
        for last in ultimo:
            username = last.screen_name
            print("	Último Pupilo Att: ", last.screen_name)
        sheet.update("A50", last.screen_name)
    else:
        if new > 0:
            ultimo = api2.followers(screen_name="mestredosbots", count=1)
            for last in ultimo:
                username = last.screen_name
                print("	Novo Último Pupilo: ", last.screen_name)
            if username != ultimouser:
                ativo = "sim"

    if new >= 1 and ativo == "sim":
        followers = api.followers(screen_name="mestredosbots", count=new)

        for follower in reversed(followers):
            local = ""
            sheet.update("A50", follower.screen_name)
            print("	Novo pupilo encotrado 😀\n")
            print("	User pupilo :", follower.screen_name)
            if follower.location != "":
                local = (
                    ' em busca do caminho  de volta ao (à) "' + follower.location + '"'
                )

            pupilo = random.randint(1, 6)
            print("	Pupilo: ", pupilo)
            if pupilo == 1:
                txt = (
                    "Olá, jovem @"
                    + str(follower.screen_name)
                    + ". Bem-vindo(a) ao Reino. Eu sou o Mestre dos Bots. Serei seu guia nessa sua jornada"
                    + local
                    + ". Assim como o Hank, você será um(a) Ranger. E lembre-se: use #MestreDosBots para me chamar e veja o que eu tenho a te dizer."
                )
                img = "./" + str(pupilo) + ".gif"

            else:
                if pupilo == 2:
                    txt = (
                        "Olá, jovem @"
                        + str(follower.screen_name)
                        + ". Bem-vindo(a) ao Reino. Eu sou o Mestre dos Bots. Serei seu guia nessa sua jornada"
                        + local
                        + ". Assim como a Diana , você será um(a) Acrobata. E lembre-se: use #MestreDosBots para me chamar."
                    )
                    img = "./" + str(pupilo) + ".gif"

                else:
                    if pupilo == 3:
                        txt = (
                            "Oi, jovem @"
                            + str(follower.screen_name)
                            + ". Bem-vindo(a) ao Reino. Eu sou o Mestre dos Bots. Serei seu guia nessa sua jornada"
                            + local
                            + ". Assim como o Presto, você será um(a) Mago(a). E lembre-se: use #MestreDosBots para me chamar."
                        )
                        img = "./" + str(pupilo) + ".gif"

                    else:
                        if pupilo == 4:
                            txt = (
                                "Saudação, jovem @"
                                + str(follower.screen_name)
                                + ". Bem-vindo(a) ao Reino. Eu sou o Mestre dos Bots. Serei seu guia nessa sua jornada"
                                + local
                                + ". Assim como a Sheila, você será um(a) Ladino(a). E lembre-se: use #MestreDosBots para me chamar."
                            )
                            img = "./" + str(pupilo) + ".gif"

                        else:
                            if pupilo == 5:
                                txt = (
                                    "Saudação, jovem @"
                                    + str(follower.screen_name)
                                    + ". Bem-vindo(a) ao Reino. Eu sou o Mestre dos Bots. Serei seu guia nessa sua jornada"
                                    + local
                                    + ". Assim como o Bobby, você será um(a) Bárbaro(a). E lembre-se: use #MestreDosBots para me chamar."
                                )
                                img = "./" + str(pupilo) + ".gif"

                            else:
                                txt = (
                                    "Oi, jovem @"
                                    + str(follower.screen_name)
                                    + ". Bem-vindo(a) ao Reino. Eu sou o Mestre dos Bots. Serei seu guia nessa sua jornada"
                                    + local
                                    + ". Assim como o Eric, você será um(a) Cavaleiro/Amazona. E lembre-se: use #MestreDosBots para me chamar."
                                )
                                img = "./" + str(pupilo) + ".gif"

            print("	Frase de resposta:", txt)

            time.sleep(15)
            api.update_with_media(img, status=txt, possible_sensitive=False)
            print(" ✅ Saudação realizada com sucesso!")
    else:
        print("	Nenhum novo pupilo 😢")

    sheet.update("A47", str(numf))
    print("_______________________________________")
