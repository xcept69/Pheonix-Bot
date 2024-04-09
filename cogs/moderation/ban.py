from discord.ext import commands
import discord


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(aliases=["murder", "uninstall"])
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if not (ctx.author.guild_permissions.ban_members):
            await ctx.send("You do not have the permissions to run this command!")
            return
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned!")


async def setup(bot):
    await bot.add_cog(Ban(bot))
    print("Ban cog loaded")
