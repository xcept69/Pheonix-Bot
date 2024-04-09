from discord.ext import commands

# import discord


class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["purge"])
    async def clear(self, ctx, amount=11):
        if not (ctx.author.guild_permissions.manage_messages):
            await ctx.send("You do not have the permissions to run this command!")
            return
        amount = amount + 1
        if amount > 101:
            await ctx.send(
                "Sorry but I can not delete more than 100 messages at a time."
            )
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send("Succesfully Cleared Messages!")


async def setup(bot):
    await bot.add_cog(Purge(bot))
    print("purge cog loaded")
