import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'creator':
        await client.send_message(message.channel,'@itayshimada The creator of me!')
    if message.content == 'help':
        await client.send_message(message.channel,'DM the owner! @itayshimada')
    if message.content == 'despacito?':
        em = discord.Embed(description='LLLLOLLLL WHY THOOOO')
        em.set_image(url='https://i.ytimg.com/vi/IT78CB8F614/hqdefault.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'here?':
        await client.send_message(message.channel,'i think so')
    if message.content == 'despacito power!':
        await client.send_message(message.channel,'you cant use a power thats stronger then you!')
    if message.content == 'prefix':
        await client.send_message(message.channel,'i have no prefix. just type the command')
    if message.content == 'default':
        em = discord.Embed(description='A DEFAULT BRAIN')
        em.set_image(url='https://i.kym-cdn.com/photos/images/original/001/404/468/698.gif')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('ping'):
        await client.send_message(message.channel,'Hello <@%s>'  %(message.author.id))
    if message.content.startswith('random'):
        randomlist = ["sup","hy","why i am alive","please stop","i have more commands. type commands so you can see them"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == 'commands':
        await client.send_message(message.channel,'```creator | help | despacito? | here? | despacito power! | prefix | default | ping | random | commands (this command)```')
client.run('NTI1ODU1OTEyNTE5MjcwNDAx.Dv8tKQ.GUhoyyjRXw_4wBvE5sLsfegBXkw')
