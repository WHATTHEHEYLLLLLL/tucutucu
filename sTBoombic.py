import discord
from discord.ext import commands
from model import get_class

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
    await ctx.send(f'No swearing, No insulting, No pinging the owner of this server excessively, no spamming, no uploading or writing inappropiate images or messages Have fun!')

@bot.command()
async def check(ctx):
    if ctx.message.attachments: 
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(file_name)
            await ctx.send("El Archivo fue guardado Exitosamente!")

            try:
                class_name = get_class("keras_model.h5", "labels.txt", file_name)
                await ctx.send(class_name)

                if class_name[0] == "Fruta Fresca":
                    await ctx.send("Segun mis calculos, estos objetos son frutas frescas, so mejor detectando estas cuando hay mas de 5")
                elif class_name[0] == "Fruta Podrida":
                    await ctx.send("Segun mis calculos, estos objetos son frutas podridas, ew...")
                elif class_name[0] == "Vegetal Fresco":
                    await ctx.send("Segun mis calculos, estos objetos son vegetales frescos, so mejor detectando si hay mas de 5")
                elif class_name[0] == "Vegetal Podrido":
                    await ctx.send("Segun mis calculos, esto esta podrido")
            
            except:
                await ctx.send("Lamentablemente sucedio un error, verifica la imagen que enviaste e intentalo de nuevo mas tarde")
    else:
        await ctx.send("Oops! Olvidaste subir tu imagen, F...")

bot.run("Sorry, no token for you")
