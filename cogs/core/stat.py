from discord.ext import commands
import discord
import psutil
from src.main import td, th, tm, ts


class Stat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx):
        global ts, tm, th, td
        statusEmbed = discord.Embed(title="Pheonix™ Stats!")
        statusEmbed.add_field(name="Days:", value=td, inline=False)
        statusEmbed.add_field(name="Hours:", value=th, inline=False)
        statusEmbed.add_field(name="Minutes:", value=tm, inline=False)
        statusEmbed.add_field(name="Seconds:", value=ts, inline=False)
        statusEmbed.add_field(
            name="CPU:", value=f"{psutil.cpu_percent()}%", inline=False
        )
        statusEmbed.add_field(
            name="RAM:", value=f"{psutil.virtual_memory()[2]}%", inline=False
        )
        await ctx.send(embed=statusEmbed)


async def setup(bot):
    await bot.add_cog(Stat(bot))
    print("stat cog loaded")
