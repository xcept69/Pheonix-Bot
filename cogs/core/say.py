from discord.ext import commands

# import discord


class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, saymsg=None):
        if saymsg == None:
            return await ctx.send("You must tell me a message to say!")
        await ctx.send(saymsg)


async def setup(bot):
    await bot.add_cog(Say(bot))
    print("say cog loaded")
