import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def pollutionsolution(ctx):
    await ctx.send(f'Hello, I am pollutionsolution, i am here to teach you ways to solve the pollution problem that may kill us all one day')

@bot.command()
async def lesson1(ctx):
    await ctx.send(f'I have a few different problems with pollution i can solve, for example, bikes are more useful than other transportations, bikes prevent air pollution since they do not use gas, maybe also use public transportation to make gas use be used less')

@bot.command()
async def lesson2(ctx):
    await ctx.send(f'For our next lesson, i recommend making recycle bins useful, the floor is not a giant trash can, but recycle bins should do the trick if you are lazy enough to not stand up from your chair when you have a bunch of trash on top of you, maybe portable recycle bins will help you with that')

@bot.command()
async def lesson3(ctx):
    await ctx.send(f'please, for the love of god, do NOT PUT TRASH IN THE WATER, USE ANY TRASH CAN THAT IS NEARBY OK? ok, basically, water pollution is quite bad, so you should drop your trash in trash cans nearby the beach so the trash does not end up in the sea, river or lake, unless you want to destroy us all, that is')

@bot.command()
async def lesson4(ctx):
    await ctx.send(f'did you know sound pollution exists? well, yeah, it does, try to not put something loud at full volume, it can damage the human ears and animal ears, since we are pretty sensible to hearing, i recommend putting a volume that does not destroy your ears, you will thank me later for that one, also, do not put loud volumes when you have headphones')

@bot.command()
async def lesson5(ctx):
    await ctx.send(f'please try not to use plastic bags, use bags that can be recycled instead, that way, less pollution is made, since plastic is a material that can last for more than 1000 years, so please, do not use plastic bags, use recycled bags instead')

@bot.command()
async def lesson6(ctx):
    await ctx.send(f'if you see trash on the floor, collect it and put it in a recycle bin or directly in the trash can if it can not be recycled, trust me, you will be helping the world like never before once you do that, I also recommend correcting people if they do not put their trash in the recycle bin or the trash can, hope they change when you said that')

bot.run("no token for you HAHAHAHAHAHAHA")
