import discord
from discord.ext import commands, tasks
import random
import json
import os
import asyncio
from io import BytesIO
from itertools import cycle
from discord.user import User
import psutil

ts = 0
tm = 0
th = 0
td = 0

client = commands.Bot(command_prefix="p!", intents=discord.Intents.all())

status = cycle([
    'p!help',
    'Itz Panda OP',
    '@itz.pheonix',
    'https://discord.gg/UEttZCZPFE',
    'Itz Panda is THE GOAT'
])

@tasks.loop(seconds=15)
async def status_swap():
    await client.change_presence(activity=discord.Game(next(status)))

@tasks.loop(seconds=2.0)
async def uptimeCounter():
    global ts, tm, th, td
    ts += 2
    if ts == 60:
        ts = 0
        tm += 1
        if tm == 60:
            tm = 0
            th += 1
            if th == 24:
                th = 0
                td += 1
@client.event
async def on_ready():
    print('Pheonix™ is ready to use!')
    print('-------------------------')
    status_swap.start()
    uptimeCounter.start()

@client.command(aliases=['p'])
async def ping(ctx):
    latency = round(client.latency * 1000)  #
    pingEmbed = discord.Embed(title=f'Pong! Latency: {latency}ms', color=0x5493f7)
    pingEmbed.set_author(name=ctx.author.display_name)
    pingEmbed.set_thumbnail(url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg")
    await ctx.send(embed=pingEmbed)

@client.command(aliases=['8ball', '8b'])
async def eightball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\n:8ball: says: {random.choice(responses)}')

@client.command(aliases=['remove', 'delete'])
async def kick(ctx, member:discord.Member, *, reason=None):
    if not(ctx.author.guild_permissions.kick_members):
        await ctx.send("You do not have the permissions to run this command!")
        return
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked!') 

@client.command(aliases=['murder', 'uninstall'])
async def ban(ctx, member:discord.Member, *, reason=None):
    if not(ctx.author.guild_permissions.ban_members):
        await ctx.send("You do not have the permissions to run this command!")
        return
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned!') 

@client.command(aliases=['purge'])
async def clear(ctx, amount=11):
    if not(ctx.author.guild_permissions.manage_messages):
        await ctx.send("You do not have the permissions to run this command!")
        return
    amount = amount+1
    if amount > 101:
        await ctx.send('Sorry but I can not delete more than 100 messages at a time.')
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Succesfully Cleared Messages!')

@client.command()
async def say(ctx , saymsg=None):
    if saymsg==None:
        return await ctx.send('You must tell me a message to say!')
    await ctx.send(saymsg)

@client.command()
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

    serverinfoEmbed = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    serverinfoEmbed.add_field(name='Name', value=f"{ctx.guild.name}", inline=False)
    serverinfoEmbed.add_field(name='member Count', value=ctx.guild.member_count, inline=False)
    serverinfoEmbed.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=False)
    serverinfoEmbed.add_field(name='Highest Role', value=ctx.guild.roles[-2], inline=False)
    serverinfoEmbed.add_field(name='Number of Roles', value=str(role_count), inline=False)
    serverinfoEmbed.add_field(name='Bots', value=', '.join(list_of_bots), inline=False)
    serverinfoEmbed.set_thumbnail(url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg")
    serverinfoEmbed.set_author(name=ctx.author.display_name)

    await ctx.send(embed = serverinfoEmbed)

client.remove_command("help")

@client.command()
async def help(ctx):
    helpEmbed = discord.Embed(title="Pheonix™ Help Panel", description="> p!commands - Lists all commands \n \n > Check out my owner's profile [here](https://discord.com/users/1085081038952337508) \n \n > Join my support server [here](https://discord.gg/UEttZCZPFE)", color=0x5493f7)
    helpEmbed.set_author(name=ctx.author.display_name)
    helpEmbed.set_thumbnail(url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg")
    await ctx.send(embed=helpEmbed)

@client.command()
async def support(ctx):
    supportEmbed = discord.Embed(title="Support Server", color=0x5493f7)
    supportEmbed.add_field(name="Join our support server for help!", value="[Support Server](https://discord.gg/UEttZCZPFE)")
    supportEmbed.set_author(name=ctx.author.display_name)
    supportEmbed.set_thumbnail(url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg")
    await ctx.send(embed=supportEmbed)

@client.command()
async def info(ctx):
    infoEmbed = discord.Embed(title="Pheonix™ Info", description="**Created by: @itz.pheonix** \n > The Discord bot to make server management and moderation easy!", color=0x5493f7)
    infoEmbed.add_field(name="Join our support server for help!", value="[Support Server](https://discord.gg/UEttZCZPFE)")
    infoEmbed.set_author(name=ctx.author.display_name)
    infoEmbed.set_thumbnail(url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg")
    await ctx.send(embed=infoEmbed)

@client.command()
async def avatar(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author

    memberAvatar = member.avatar.url

    avaEmbed = discord.Embed(title=f"{member.name}'s Avatar")
    avaEmbed.set_image(url = memberAvatar)

    await ctx.send(embed = avaEmbed)

@client.command()
async def commands(ctx):
    cmdEmbed = discord.Embed(title="Pheonix™ Info", description="**Created by: @itz.pheonix** \n The Discord bot to make server management and moderation easy!", color=0x5493f7)
    cmdEmbed.add_field(name="Utility", value="> p!serverinfo - Shows info about this server \n \n > p!info - Shows info about this bot \n \n > p!support - Shows a link to the support server \n \n > p!avatar - Displays the avatar of a user \n \n > p!ping - Shows the latency of the bot \n \n > p!say - Says a word that you want the bot to say \n \n > p!8ball - Helps you choose something / Answers your questions \n \n > p!help - Opens the help panel for the bot \n \n > p!invite - Sends a link that allows you to invite the bot to your server \n \n > p!stats - Shows the bot stats", inline=False)
    cmdEmbed.add_field(name="Moderation", value="> p!kick - Kicks a member from the guild \n \n > p!ban - Bans a member from the guild \n \n > p!purge - Clears a certain amount of messages that you want the bot to")
    cmdEmbed.set_author(name=ctx.author.display_name)
    cmdEmbed.set_thumbnail(url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg")
    await ctx.send(embed=cmdEmbed)

@client.command()
async def dox(ctx, member:discord.Member):
    if not(ctx.author.guild_permissions.ban_members):
        await ctx.send("You do not have the permissions to run this command!")
        return
    doxEmbed = discord.Embed(title="", description="Doxing member...", color=0x5493f7)
    doxEmbed.add_field(name="Succesfully doxxed member!", value="DNS: Clounfare \n Discord-DNS: Cloudfare_malware \n Device DNS: Default \n Discord-authority-crack: Succesful \n Inject: Clounfare-Malware")
    doxEmbed.set_author(name=ctx.author.display_name)
    await ctx.send(embed=doxEmbed)
    await ctx.send(f'{member.mention} has been doxxed!')

@client.command()
async def invite(ctx):
    invEmbed = discord.Embed(title="Invite Pheonix™", description=" [Invite](https://discord.com/oauth2/authorize?client_id=1226890427987398676&permissions=8&scope=bot)", color=0x5493f7)
    invEmbed.add_field(name="", value="")
    invEmbed.set_author(name=ctx.author.display_name)
    invEmbed.set_thumbnail(url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg")
    await ctx.send(embed=invEmbed)

@client.command()
async def stats(ctx):
    global ts, tm, th, td
    statusEmbed = discord.Embed(title="Pheonix™ Stats!")
    statusEmbed.add_field(name="Days:", value=td, inline=False)
    statusEmbed.add_field(name="Hours:", value=th, inline=False)
    statusEmbed.add_field(name="Minutes:", value=tm, inline=False)
    statusEmbed.add_field(name="Seconds:", value=ts, inline=False)
    statusEmbed.add_field(name="CPU:", value=f"{psutil.cpu_percent()}%", inline=False)
    statusEmbed.add_field(name="RAM:", value=f"{psutil.virtual_memory()[2]}%", inline=False)
    await ctx.send(embed=statusEmbed)


client.run('TOKEN')
