import discord
from discord.ext import commands
import os
import random

bot = commands.Bot(commands.when_mentioned_or('='))
bot.remove_command(name="help")


@bot.event
async def on_ready():
    print("PoDeTer a la pêche")
    await bot.change_presence(activity=discord.Game(name="V1.2 | =help"))


@bot.command(pass_context=True)
async def help(ctx):
    await ctx.message.channel.purge(limit=1)
    ecolor = discord.Colour(value=0xc27c0e)
    e = discord.Embed(title="Liste des commandes banales :", description="Préfix : = \n\n", colour=ecolor)
    e.add_field(name=bot.get_command(name="help"), value="La commande d'aide", inline=False)
    e.add_field(name=bot.get_command(name="pomme"), value="Répond 'De Terre' ", inline=False)
    e.add_field(name=bot.get_command(name="info"), value="Donne les infos", inline=False)
    e.add_field(name=bot.get_command(name="coucou"), value="Dit coucou a tout le monde", inline=False)
    e.add_field(name=bot.get_command(name="non"), value="Dit non", inline=False)
    e.add_field(name=bot.get_command(name="pdp"), value="Donne la photo de profil", inline=False)
    e.add_field(name=bot.get_command(name="mc"), value='Dit la même chose que toi (mc = même chose)\n _Ps : Attention si votre msg a des espaces mettez des guillemets , ex : "Je vous aime"' , inline=False)
    e.add_field(name=bot.get_command(name="search"), value="Pour faire une recherche sur internet\n Ps : Attention les espaces entres les mots doivent être remplacer par des +", inline=False)
    e.add_field(name=bot.get_command(name="youtube"), value="Pour faire une recherche Youtube\n Ps : Attention les espaces entres les mots doivent être remplacer par des +", inline=False)
    e.add_field(name=bot.get_command(name="ah"), value="Ah !", inline=False)
    e.add_field(name=bot.get_command(name="vent"), value="Mesure le niveau du vent entre les messages", inline=False)
    em = discord.Embed(title="Liste des commandes modératrices :", colour=discord.Colour.dark_blue())
    em.add_field(name=bot.get_command(name="clean"), value="Efface les msg", inline=False)
    em.add_field(name=bot.get_command(name="nick"), value="Change le pseudo ", inline=False)
    em.add_field(name=bot.get_command(name="kick"), value="kick une personne", inline=False)
    em.add_field(name=bot.get_command(name="ban"), value="ban une personne", inline=False)
    eg = discord.Embed(title="Liste des commandes de jeu google:", colour=discord.Colour.greyple())
    eg.add_field(name=bot.get_command(name="googame"), value="Liste des commandes de jeu google", inline=False)
    eg.add_field(name=bot.get_command(name="snake"), value="Un petit jeu snake", inline=False)
    eg.add_field(name=bot.get_command(name="pacman"), value="PacMan PacMan PacMan !", inline=False)
    eg.add_field(name=bot.get_command(name="atari_breakout"), value="Le célèbre breakout sur atari", inline=False)
    eg.add_field(name=bot.get_command(name="quizz_mc"), value="Un quizz sur minecraft", inline=False)
    await ctx.message.channel.send(embed=e)
    await ctx.message.channel.send(embed=em)
    await ctx.message.channel.send(embed=eg)


@bot.command(pass_context=True)
async def pomme(ctx):
    await ctx.message.channel.purge(limit=1)
    await ctx.message.channel.send("Pomme")
    pommecolor = discord.Colour(value=0xe74c3c)
    e1 = discord.Embed(title="De terre", colour=pommecolor)
    await ctx.message.channel.send(embed=e1)


@bot.command(pass_context=True)
async def info(ctx):
    await ctx.message.channel.purge(limit=1)
    color_info = discord.Colour(value=0x3498db)
    info_e = discord.Embed(title="INFORMATION", description="Voici toutes les informations sur le bot et le créateur", colour=color_info)
    info_e.set_author(name="Oanliju (Maviis)", url=" https://discord.gg/n77aRXf", icon_url="https://i.pinimg.com"
                                                                                          "/originals/bc/7b/e6"
                                                                                          "/bc7be61f0a88d1d61f2c4913436f390a.jpg")
    info_e.add_field(name="\n\nInformation du Créateur\n\n", value="\n\n**Son Nom :** Oanliju\n**Son discord :** [JeanPaul c'est mon discord](https://discord.gg/n77aRXf)", inline=False)
    info_e.add_field(name="\n\nInofrmation du Bot\n\n", value="\n\n**Son Nom :** PoDeTer \n **Son Language :** Python\n**Créateur** : Oanliju#2557\n**Aider par :** Astremy#2316 ")
    await ctx.message.channel.send(embed=info_e)


@bot.command(pass_context=True)
async def non(ctx):
    await ctx.message.channel.purge(limit=1)
    e4 = discord.Embed(title="Non ! <:non:578130152140308481> ", colour=discord.Colour.dark_blue())
    await ctx.message.channel.send(embed=e4)


@bot.command(pass_context=True)
async def ah(ctx):
    await ctx.message.channel.purge(limit=1)
    e4 = discord.Embed(title="Ah ! <:ah:578130126705917982> <:ah:578130126705917982> <:ah:578130126705917982>", colour=discord.Colour.dark_blue())
    await ctx.message.channel.send(embed=e4)


@bot.command(pass_context=True)
async def vent(ctx):
    await ctx.message.channel.purge(limit=1)
    ml = ["vent", "vent lvl 10", "vent lvl 100000", "Tornade", "Cyclone", "tourbillion", "Ouragan"]
    color = [discord.Colour.blue(), discord.Colour.light_grey(), discord.Colour.dark_orange(), discord.Colour.gold(), discord.Colour.dark_purple(), discord.Colour.green()]
    e = discord.Embed(title="Wind levels", description=random.choice(ml))
    await ctx.message.channel.send(embed=e)


@bot.command(pass_context=True)
async def test(ctx):
    await ctx.message.channel.purge(limit=1)
    await ctx.message.channel.send("test")

    
@bot.command(pass_context=True)
async def coucou(ctx):
    await ctx.message.channel.purge(limit=1)
    e3 = discord.Embed(title="COUCOU", description="Tout le monde", colour=discord.Colour.greyple())
    await ctx.message.channel.send(embed=e3)
    

@bot.command(pass_context=True)
async def pdp(ctx):
    await ctx.message.channel.purge(limit=1)
    if len(ctx.message.mentions) > 0:
        perso = ctx.message.mentions[0]
    else:
        perso = ctx.author
    epdp = discord.Embed(title="Photo de profil", description="voici la photo de profil de" + perso.mention, colour=discord.Colour.orange())
    epdp.set_image(url=perso.avatar_url + "?size=2048")
    await ctx.message.channel.send(embed=epdp)


@bot.command(pass_context=True)
async def clean(ctx, arg):
    if ctx.author.guild_permissions.manage_messages:
        if len(arg) > 0 and arg.isdigit:
            await ctx.message.channel.purge(limit=int(arg)+1)
            if int(arg) <= 1:
                await ctx.message.channel.send(arg + " Message a été supprimé", delete_after=3)
            else:
                await ctx.message.channel.send(arg + " Messages ont été supprimés", delete_after=3)
        else:
            await ctx.message.channel.send("Un nombre pas des lettres")
    else:
        ctx.message.channel.send("Dommage , vous n'avez pas les permissions")


@bot.command(pass_context=True)
async def nick(ctx, arg):
    await ctx.message.channel.purge(limit=1)
    if ctx.message.author.guild_permissions.change_nickname:
        if len(ctx.message.mentions) > 0 and len(arg) > 1:
            await ctx.message.mentions[0].edit(nick=arg.join(ctx.message.content.split(" ")[2:]))
            await ctx.message.channel.send(content="Le pseudo " + ctx.message.mentions[0].name + " a été changé par " + ctx.message.mentions[0].nick, delete_after=3)
    else:
        await ctx.message.channel.send("Vous n'avez pas les permissions !")


@bot.command(pass_context=True)
async def mc(ctx, arg):
    await ctx.message.channel.purge(limit=1)
    if ctx.message.author.guild_permissions.send_messages:
        emc = discord.Embed(description="**" + arg + "**", color=discord.Colour.dark_green())
        emc.set_author(name=ctx.message.author.name, icon_url=ctx.author.avatar_url)
        await ctx.message.channel.send(embed=emc)


@bot.command(pass_context=True)
async def ban(ctx, arg):
    await ctx.message.channel.purge(limit=1)
    if ctx.message.author.guild_permissions.ban_members:
        if len(ctx.message.mentions) > 0:
            if ctx.message.mentions[0].dm_channel == None:
                await ctx.message.mentions[0].create_dm()
            await ctx.message.mentions[0].dm_channel.send("Vous avez été banni de " + ctx.message.guild.name + " par " + ctx.message.author + " La raison de votre ban est " + arg[1])
    await ctx.message.mentions[0].ban()


@bot.command(pass_context=True)
async def kick(ctx):
    await ctx.message.channel.purge(limit=1)
    if ctx.message.author.guild_permissions.kick_members:
        if len(ctx.message.mentions) > 0:
            membrek2 = ctx.message.mentions[0]
            if membrek2.dm_channel == None:
                await membrek2.create_dm()
            await membrek2.dm_channel.send("Vous avez été kické de " + ctx.message.guild.name + " par " + ctx.message.author.name)
    await membrek2.kick()


@bot.command(pass_context=True)
async def googame(ctx):
    await ctx.message.channel.purge(limit=1)
    e = discord.Embed(title="Liste des commandes de jeu:", description="Préfix : = \n\n", colour=discord.Colour.greyple())
    e.add_field(name=bot.get_command(name="snake"), value="Un petit jeu snake", inline=False)
    e.add_field(name=bot.get_command(name="pacman"), value="PacMan PacMan PacMan !", inline=False)
    e.add_field(name=bot.get_command(name="atari_breakout"), value="Le célèbre breakout sur atari", inline=False)
    e.add_field(name=bot.get_command(name="quizz_mc"), value="Un quizz sur minecraft", inline=False)
    await ctx.message.channel.send(embed=e)


@bot.command(pass_context=True)
async def snake(ctx):
    await ctx.message.channel.purge(limit=1)
    e = discord.Embed(title="Le célèbre Snake", description="[Snake](https://www.google.com/search?client=firefox-b-d&q=snake)", colour=discord.Colour.green())
    await ctx.message.channel.send(embed=e)


@bot.command(pass_context=True)
async def pacman(ctx):
    await ctx.message.channel.purge(limit=1)
    e = discord.Embed(title="PacMan PacMan PacMan!", description="[PacMan](https://www.google.com/search?client=firefox-b-d&q=pacman)", colour=discord.Colour.gold())
    await ctx.message.channel.send(embed=e)


@bot.command(pass_context=True)
async def atari_breakout(ctx):
    await ctx.message.channel.purge(limit=1)
    e = discord.Embed(title="Sur Atari y'avait eu un jeu comment il s'appellait ?!", description="[Breakout](https://elgoog.im/breakout/)", colour=discord.Colour.dark_grey())
    await ctx.message.channel.send(embed=e)


@bot.command(pass_context=True)
async def quizz_mc(ctx):
    await ctx.message.channel.purge(limit=1)
    e = discord.Embed(title="Connaissez vous vraiment Minecraft ?", description="[QuizMc](https://www.quizz.biz/quizz-297155.html)", colour=discord.Colour.dark_teal())
    await ctx.message.channel.send(embed=e)


@bot.command(pass_context=True)
async def search(ctx, arg):
    await ctx.message.channel.purge(limit=1)
    e = discord.Embed(title="Voici votre recherche Internet " + ctx.author.name + " : " + arg, colour=discord.Colour.dark_teal())
    e.add_field(name="Google :", value="[Google](https://www.google.com/search?client=firefox-b-d&q=" + arg + ")", inline=False)
    e.add_field(name="Bing :", value="[Bing](https://www.bing.com/search?q=" + arg + ")", inline=False)
    await ctx.message.channel.send(embed=e)


@bot.command(pass_context=True)
async def youtube(ctx, arg):
    await ctx.message.channel.purge(limit=1)
    e = discord.Embed(title="Voici votre recherche Youtube " + ctx.author.name + " : " + arg, description="[Youtube](https://www.youtube.com/results?search_query=" + arg + ")", colour=discord.Colour.dark_red())
    await ctx.message.channel.send(embed=e)


bot.run(os.getenv('TOKEN'))
