from discord.ext import commands
import discord


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

        serverinfoEmbed = discord.Embed(
            timestamp=ctx.message.created_at, color=ctx.author.color
        )
        serverinfoEmbed.add_field(name="Name", value=f"{ctx.guild.name}", inline=False)
        serverinfoEmbed.add_field(
            name="member Count", value=ctx.guild.member_count, inline=False
        )
        serverinfoEmbed.add_field(
            name="Verification Level",
            value=str(ctx.guild.verification_level),
            inline=False,
        )
        serverinfoEmbed.add_field(
            name="Highest Role", value=ctx.guild.roles[-2], inline=False
        )
        serverinfoEmbed.add_field(
            name="Number of Roles", value=str(role_count), inline=False
        )
        serverinfoEmbed.add_field(
            name="Bots", value=", ".join(list_of_bots), inline=False
        )
        serverinfoEmbed.set_thumbnail(
            url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg"
        )
        serverinfoEmbed.set_author(name=ctx.author.display_name)

        await ctx.send(embed=serverinfoEmbed)


async def setup(bot):
    await bot.add_cog(ServerInfo(bot))
    print("serverInfo cog loaded")
