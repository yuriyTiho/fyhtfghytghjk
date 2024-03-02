from random import *
import os
import discord
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='Y-', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesion como {bot.user}')

@bot.command()
async def mem(ctx):
    mem = choice(os.listdir("M2L1/img"))
    with open(f"M2L1/img/{mem}", 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run('MTIwMzM4Mjc3OTk1NDQ2Mjc0MA.GRuSpi._V5TzolTGU_OHIC6YuBqeJ_tF4wMZe_TN7dbws')