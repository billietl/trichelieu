#!/bin/env python3

import asyncio, os, random, re, time
import discord

token = os.environ['token']
taux_spam = 100

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
@asyncio.coroutine
def on_message(message):
    de_spam = random.randint(1,taux_spam)
    if (re.match(".*j'ai perdu.*", message.content, re.IGNORECASE) and message.author != client.user ):
        alerte = "Pas merci {}, à cause de toi j'ai perdu !".format(message.author.nick)
        print("# Sending on {}'s channel {} : {}".format(str(message.channel.server), str(message.channel), alerte))
        yield from client.send_message(message.channel, alerte)
    if (re.match(".*quel(le)? heure.*\?.*", message.content, re.IGNORECASE) or de_spam == 1):
        heure = time.localtime()
        de_perdu = random.randint(1,100)
        if de_perdu == 1:
            suite = "ET J'AI PERDU !"
        else:
            suite = "TOUT VA BIEN !"
        alerte = 'IL EST {} HEURES {} DU MATIN ! {}'.format(heure.tm_hour, heure.tm_min, suite)
        print("# Sending on {}'s channel {} : {}".format(str(message.channel.server), str(message.channel), alerte))
        yield from client.send_message(message.channel, alerte)

client.run(token)
