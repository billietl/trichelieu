#!/bin/env python3

import asyncio, discord, random, re, time

token = ''
taux_spam = 100

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
@asyncio.coroutine
def on_message(message):
    de_spam = random.randint(1,taux_spam)
    if (re.match(".*quel(le)? heure.*\?.*", message.content, re.IGNORECASE) or de_spam == 1):
        heure = time.localtime()
        de_perdu = random.randint(1,100)
        if de_perdu == 1:
            suite = "ET J'AI PERDU !"
        else:
            suite = "TOUT VA BIEN !"
        alerte = 'IL EST {} HEURES {} DU MATIN ! {}'.format(heure.tm_hour, heure.tm_min, suite)
        yield from message.channel.send(alerte)

client.run(token)

