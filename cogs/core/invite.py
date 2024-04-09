from discord.ext import commands
import discord


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        invEmbed = discord.Embed(
            title="Invite Pheonix™",
            description=" [Invite](https://discord.com/oauth2/authorize?commands_id=1226890427987398676&permissions=8&scope=bot)",
            color=0x5493F7,
        )
        invEmbed.add_field(name="", value="")
        invEmbed.set_author(name=ctx.author.display_name)
        invEmbed.set_thumbnail(
            url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg"
        )
        await ctx.send(embed=invEmbed)


async def setup(bot):
    await bot.add_cog(Invite(bot))
    print("invite cog loaded")
