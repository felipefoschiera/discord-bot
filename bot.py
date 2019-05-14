import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import datetime
from pytz import timezone
import pytz

Client = discord.Client()
client = commands.Bot(command_prefix="#")
 
@client.event
async def on_ready():
    print("Ready!")
    print("I am running on", client.user.name)
    print("With the ID:", client.user.id)

@client.event
async def on_message(message):
    # if message.content.upper().startswith('!PING'):
    #     userID = message.author.id
    #     await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith("!TIME"):

        br_east_time = timezone("Brazil/East")
        london_time = timezone("Europe/London")
        dubai_time = timezone("Asia/Dubai")
        china_time = timezone("Asia/Shanghai")
        current_time = br_east_time.localize(datetime.datetime.now())

        brazil_curtime = current_time.strftime("%H:%M:%S - %d of %b (GMT %Z)")
        london_curtime = current_time.astimezone(london_time).strftime("%H:%M:%S - %d of %b (%Z)")
        dubai_curtime = current_time.astimezone(dubai_time).strftime("%H:%M:%S - %d of %b (GMT %Z)")
        china_curtime = current_time.astimezone(china_time).strftime("%H:%M:%S - %d of %b (GMT +08)")
        msgSend = "Brazil Time: " + brazil_curtime + "\n\n"
        msgSend += "London Time: " + london_curtime + "\n\n"
        msgSend += "Dubai Time: " + dubai_curtime + "\n\n"
        msgSend += "China Time: " + china_curtime + "\n\n" 
        await client.send_message(message.channel, msgSend)
client.run("-")
