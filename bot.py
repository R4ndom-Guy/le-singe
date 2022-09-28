from secrets import choice
import discord
from discord.ext import commands
import random 
import re

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client()
bot = commands.Bot(command_prefix="!", intents=default_intents)

@bot.event
async def on_ready():
    print("{0.username} est en ligne !")

@bot.event
async def on_member_join(member):
    print(f"Un espèce rare est arrivé : {member.display_username}")

@bot.command(name="info")
async def information(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    numberOfPerson = server.member_count
    message = f"Le {server} a une population de **{numberOfPerson}** espèces **rares**, **{numberOfTextChannels}** où on dit de la **merde**, **{numberOfVoiceChannels}** où on **crie** comme des singes !"
    await ctx.send(message)

@bot.command(name="joke")
async def blague(ctx):
    joke = [
        "Quelle mamie fait peur aux voleurs ? **Mamie Traillette**.",
        "J'ai une blague sur les magasins Mais elle a pas **supermarché**",
        "Pourquoi est-ce c'est difficile de conduire dans le Nord ? Parce que les voitures arrêtent **PAS DE CALER**.",
        "Deux lions discutent « T’as une belle crinière », « Arrête, tu vas me faire **rugir** »",
        "Pourquoi est-ce qu'on dit que les bretons sont tous frères et sœurs ? Parce qu’ils n’ont **Quimper**.",
        "Pourquoi est-ce qu'on met tous les crocos en prison ? Parce que les crocos **dealent**.",
        "Pourquoi dit-on que les poissons travaillent illégalement ? Parce qu’ils n’ont pas de **FISH** de paie",
        "Quel est le bar préféré des espagnols ? Le Bar-celone",
        "Pourquoi est-ce que les mexicains mangent-ils aux toilettes ? Parce qu’ils aiment **manger épicé**",
        "Que faisaient les dinosaures quand ils n'arrivaient pas à se décider? Des **tirageosaures**",
        "Qu'est-ce qu'un tennisman adore faire ? Rendre des services" ,
        "Que se passe-t-il quand 2 poissons s'énervent ? Le thon monte" 
        ]
    hasard = random.choices(joke)
    embed_joke = discord.Embed(title="Blague à deux balles Pan-Pan", description=hasard, colour=discord.Color.random())
    await ctx.send(embed=embed_joke)

@bot.command(name="wiki")
async def search(ctx, message):
    embed_wiki = discord.Embed(title="RECHERCHE WIKIPEDIA", description="Lien Wikipédia -> https://fr.wikipedia.org/w/index.php?search=" + message, colour=discord.Color().random())
    await ctx.send(embed=embed_wiki)


@bot.command("ban")
async def ban(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"**{user}** a été ban pour la raison suivante : **{reason}**")

@bot.command(name="kick")
async def kick(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"**{user}** a été kick pour la raison suivante : **{reason}**")



bot.run("MTAyNDczNDIwOTM1MDMxNjA4Mg.G5P-t3.WC-Zhj2QAXUFpUjlovdvhV0UJ7ADFMFmuG5Gfk")

