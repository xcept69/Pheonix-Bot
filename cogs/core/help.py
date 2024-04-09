from discord.ext import commands
import discord


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        helpEmbed = discord.Embed(
            title="Pheonix™ Help Panel",
            description="> p!commands - Lists all commands \n \n > Check out my owner's profile [here](https://discord.com/users/1085081038952337508) \n \n > Join my support server [here](https://discord.gg/UEttZCZPFE)",
            color=0x5493F7,
        )
        helpEmbed.set_author(name=ctx.author.display_name)
        helpEmbed.set_thumbnail(
            url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg"
        )
        await ctx.send(embed=helpEmbed)

    @commands.command()
    async def support(self, ctx):
        supportEmbed = discord.Embed(title="Support Server", color=0x5493F7)
        supportEmbed.add_field(
            name="Join our support server for help!",
            value="[Support Server](https://discord.gg/UEttZCZPFE)",
        )
        supportEmbed.set_author(name=ctx.author.display_name)
        supportEmbed.set_thumbnail(
            url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg"
        )
        await ctx.send(embed=supportEmbed)

    @commands.command()
    async def info(self, ctx):
        infoEmbed = discord.Embed(
            title="Pheonix™ Info",
            description="**Created by: @itz.pheonix** \n > The Discord bot to make server management and moderation easy!",
            color=0x5493F7,
        )
        infoEmbed.add_field(
            name="Join our support server for help!",
            value="[Support Server](https://discord.gg/UEttZCZPFE)",
        )
        infoEmbed.set_author(name=ctx.author.display_name)
        infoEmbed.set_thumbnail(
            url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg"
        )
        await ctx.send(embed=infoEmbed)


async def setup(bot):
    await bot.add_cog(Help(bot))
    print("help cog loaded")
