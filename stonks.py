import discord
import os
from wazirx_sapi_client.rest import Client
import shib

wazirClient = Client()
wazirClient = Client(api_key=os.getenv('api_key'), secret_key=os.getenv('secret_key'))

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$shib'):
        await message.channel.send(shib.shibPrice())

client.run(os.getenv('TOKEN'))
