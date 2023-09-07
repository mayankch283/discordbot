from http import client
import discord
import aiohttp
from discord.ext import commands
from datetime import datetime
import random

client = commands.Bot(command_prefix='+',intents=discord.Intents.all())
           
@client.command(name='meme')
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        x = 'https://www.reddit.com/r/memes/new.json?sort=hot'
        async with session.get(x) as resp:
            memes = await resp.json()
            
            y = random.randint(0,25)
            print(y)

            embed = discord.Embed(
                color= 0x00ff7f,
                description= memes["data"]["children"][y]['data']['title'],
                timestamp=datetime.utcnow()
            )

            embed.set_image(url = memes["data"]["children"][y]['data']['url'])
            await ctx.send(embed=embed)


@client.command(name='pmeme')
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        x = 'https://www.reddit.com/r/programmerhumour/new.json?sort=hot'
        async with session.get(x) as resp:
            memes = await resp.json()
            
            y = random.randint(0,25)
            print(y)

            embed = discord.Embed(
                color= 0x00ff7f,
                description= memes["data"]["children"][y]['data']['title'],
                timestamp=datetime.utcnow()
            )

            embed.set_image(url = memes["data"]["children"][y]['data']['url'])
            await ctx.send(embed=embed)

'''
@client.command(name='valomeme')
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        x = 'https://www.reddit.com/r/ValorantMemes/new.json?sort=hot'
        async with session.get(x) as resp:
            memes = await resp.json()
            
            y = random.randint(0,50)
            print(y)

            embed = discord.Embed(
                color= 0x00ff7f,
                description= memes["data"]["children"][y]['data']['title'],
                timestamp=datetime.utcnow()
            )

            embed.set_image(url = memes["data"]["children"][y]['data']['url'])
            await ctx.send(embed=embed)
'''

client.run('bot_token')
