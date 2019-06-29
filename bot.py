#!/usr/bin/env python3
# Work with Python 3

import json

import discord

with open("auth.json") as data_file:
    auth = json.load(data_file)

TOKEN = auth["token"]

client = discord.Client()


@client.event
async def on_message(msg):
    # We want the bot to not answer to messages that have no content
    # (example only attachment messages)
    if not msg.content:
        return
    # Bot ignore all system messages
    if msg.type is not discord.MessageType.default:
        return

    if msg.author.id == 515058677640855552:
        message = "p xbt bitmex"
        await msg.channel.send(message)


@client.event
async def on_ready():
    print(f"Logged in as: {client.user.name} {{{client.user.id}}}")


client.run(TOKEN)
