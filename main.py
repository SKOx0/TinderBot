# -*- coding: utf-8 -*-
import pynder
import re
import random

FBTOKEN = "##################"
FBID = "###################"

session = pynder.Session(FBID, FBTOKEN)
matches = session.matches()
users = session.nearby_users()


def cantadaCacaPalavras(match):
    match.message("Olá gata, prazer, estou com um problema e acho que só você pode resolver")
    match.message("Estou resolvendo um caça palavras, que tem a seguinte pergunta: ")
    match.message("Qual o número com 9 digitos(importante ressaltar) da garota cujo nome é {n}?".format(
        n=match.user.name.encode('utf-8')))
    match.message("tá muito dificil, pode me ajudar?")


def cantadaAmorPrimeiraVista(match):
    match.message("Você acredita em amor à primeira vista, ou devo passar por aqui mais uma vez?")


def cantadaTantoEmComun(match):
    porque = re.compile("(por que|porque|porquê|por quê)")
    match.message("Gata, a gente tem tanta coisa em comum")
    match.message("Por que eu tenho tinder, você também")
    match.message("Moro no brasil, você também")
    match.message("Moro no RJ, você também")
    match.message("Acho que nascemos um para o outro")


def cantadaPadeiro(match):
    porque = re.compile("(por que|porque|porquê|por quê)")
    match.message("Gata, você é padeira?")
    match.message("Por que seu pai é um sonho")


def cantadaDistancia(match):
    match.message("Defini para o tinder buscar até 100km")
    match.message("Mas parece que ele foi mais longe, e foi te buscar lá no céu")


def randomCatada():
    cantadaRandom = random.randint(0, 4)
    return cantadaRandom

while True:
    for match in matches:
        if not match.messages:
            if randomCatada() == 0:
                cantadaAmorPrimeiraVista(match)
            elif randomCatada() == 1:
                cantadaCacaPalavras(match)
            elif randomCatada() == 2:
                cantadaPadeiro(match)
            elif randomCatada() == 3:
                cantadaTantoEmComun(match)
            elif randomCatada() == 4 or match.user.distance_km >= "100":
                cantadaDistancia(match)
            print match.user.name

    for user in users:
        print user
        user.like()
        print user.like()

    session = pynder.Session(FBID, FBTOKEN)
    users = session.nearby_users()
    matches = session.matches()
pass
# session = pynder.Session(FBID, FBTOKEN)
# users = session.nearby_users()
