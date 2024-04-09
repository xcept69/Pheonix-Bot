from discord.ext import commands
import discord


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(aliases=["p"])
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        pingEmbed = discord.Embed(title=f"Pong! Latency: {latency}ms", color=0x5493F7)
        pingEmbed.set_author(name=ctx.author.display_name)
        pingEmbed.set_thumbnail(
            url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg"
        )
        await ctx.send(embed=pingEmbed)


async def setup(bot):
    await bot.add_cog(Ping(bot))
    print("Ping cog loaded")
