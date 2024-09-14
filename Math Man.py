import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def multiply(ctx, left: int, right: int):
    """Multiplies two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def subtract(ctx, left: int, right: int):
    """Subtracts two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def divide(ctx, left: int, right: int):
    """Divides two numbers together."""
    await ctx.send(left / right)

@bot.command()
async def sEcReT(ctx):
    await ctx.send(f'I am math man, i can help you with adding, subtracting, multiplying and diving numbers, you can make it by saying: $add, $subtract, $multiply or $divide, do not forget to put the numbers you want to do math with')
