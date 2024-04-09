import discord
import os
from discord.ext import commands, tasks
from src.utils.constants import TOKEN
from itertools import cycle

ts = 0
tm = 0
th = 0
td = 0


class Pheonix(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="p!", intents=discord.Intents.all())

    async def on_ready(self):
        await load_cog()
        print("Pheonix™ is ready to use!")
        print("-------------------------")
        status_swap.start()
        uptimeCounter.start()


bot = Pheonix()

bot.remove_command("help")


status = cycle(
    [
        "p!help",
        "Itz Panda OP",
        "@itz.pheonix",
        "https://discord.gg/UEttZCZPFE",
        "Itz Panda is THE GOAT",
    ]
)


@tasks.loop(seconds=15)
async def status_swap():
    await bot.change_presence(activity=discord.Game(next(status)))


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


async def load_cog():
    modules = ["core", "fun", "moderation", "music"]
    for module in modules:
        for fn in os.listdir("cogs/" + module):
            if fn.endswith(".py"):
                await bot.load_extension(f"cogs.{module}.{fn[:-3]}")


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)


@bot.command()
async def sync(ctx: commands.Context):
    await ctx.send("Syncing Slash Commands")
    synced = await bot.tree.sync()
    if len(synced) > 0:
        for cmd in synced:
            await ctx.send(f"Synced {cmd}")
        await ctx.send(f"Synced {len(synced)} Commands Globally!")
    else:
        await ctx.send("No Slash Commands to Register.")


@bot.hybrid_command(name="shutdown")
async def shutdown(ctx: commands.Context):
    if int(ctx.author.id) not in [786926252811485186, 1085081038952337508]:
        await ctx.send("Owner only Command")
        return
    await ctx.send("Going to sleep")
    await bot.close()


if __name__ == "__main__":
    bot.run(TOKEN)
