from discord.ext import commands
import discord


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(aliases=["remove", "delete"])
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if not (ctx.author.guild_permissions.kick_members):
            await ctx.send("You do not have the permissions to run this command!")
            return
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked!")


async def setup(bot):
    await bot.add_cog(Kick(bot))
    print("Kick cog loaded")
