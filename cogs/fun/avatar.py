from discord.ext import commands
import discord


class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        memberAvatar = member.avatar.url

        avaEmbed = discord.Embed(title=f"{member.name}'s Avatar")
        avaEmbed.set_image(url=memberAvatar)

        await ctx.send(embed=avaEmbed)


async def setup(bot):
    await bot.add_cog(Avatar(bot))
    print("avatar cog loaded")
