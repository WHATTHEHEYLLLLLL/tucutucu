import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello! My name is Boombic, type $commands to view all possible commands, some commands are not gonna be said since they are only for the owner to use!')

@bot.command()
async def rules(ctx):
    await ctx.send(f'No swearing, No insulting, No pinging the owner of this server excessively, Have fun!')
