import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



@bot.command()
async def tukettigimesyalardanneyapabilirim(ctx):
        
    fikirler = [
        "Plastik şişelerden kalemlik yapabilirsin.",
        "Eski yoğurt kaplarında saksı yapabilirsin.",
        "Pet şişeleri keserek kuşlar için yemlik yapabilirsin.",
        "Pet şişeden oyuncak yapabilirsin",
        "Eski tişörtlerden bez çanta yapabilirsin.",
        "plastik şişeden evcil hayvanıza su kabı ve yemek kabı yapabilirsin.",
        "karton ile cetvel yapabilirsin.",
        "karton ile geri dönüşüm kutusu yapabilirsin."
    ]
    await ctx.send(f"Fikir : {random.choice(fikirler)}")

bot.run("token yazınız")
