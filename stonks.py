import discord
import os

from discord import channel
from wazirx_sapi_client.rest import Client
import mod
from discord.ext import commands

wazirClient = Client()
wazirClient = Client(api_key=os.getenv('api_key'), secret_key=os.getenv('secret_key'))

client = discord.Client()

bot = commands.Bot(command_prefix = '$')

@bot.command()
async def test(mes):
    await mes.channel.send("Testing 1, 2, 3...")

@bot.command()
async def price(com, cur, ticker):
    await com.channel.send(mod.tickerPrice(cur, ticker))

@bot.command()
async def alert(com, cur, ticker, alertPrice):
    await com.channel.send(mod.PriceBreakoutAlertAdd(cur, ticker, alertPrice))
    mod.PriceBreakoutCheckingLoop()

print(mod.alertList)

# client.run(os.getenv('TOKEN'))
bot.run((os.getenv('DISC_TOKEN')))
