from discord.ext import commands

# import discord


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Example(bot))
    print("Example cog loaded (does nothing)")
