from discord.ext import commands
import discord


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def commands(self, ctx):
        cmdEmbed = discord.Embed(
            title="Pheonix™ Info",
            description="**Created by: @itz.pheonix** \n The Discord bot to make server management and moderation easy!",
            color=0x5493F7,
        )
        cmdEmbed.add_field(
            name="Utility",
            value="> p!serverinfo - Shows info about this server \n \n > p!info - Shows info about this bot \n \n > p!support - Shows a link to the support server \n \n > p!avatar - Displays the avatar of a user \n \n > p!ping - Shows the latency of the bot \n \n > p!say - Says a word that you want the bot to say \n \n > p!8ball - Helps you choose something / Answers your questions \n \n > p!help - Opens the help panel for the bot \n \n > p!invite - Sends a link that allows you to invite the bot to your server \n \n > p!stats - Shows the bot stats",
            inline=False,
        )
        cmdEmbed.add_field(
            name="Moderation",
            value="> p!kick - Kicks a member from the guild \n \n > p!ban - Bans a member from the guild \n \n > p!purge - Clears a certain amount of messages that you want the bot to",
        )
        cmdEmbed.set_author(name=ctx.author.display_name)
        cmdEmbed.set_thumbnail(
            url="https://i.pinimg.com/564x/6d/68/0a/6d680a201ec68ad79736345e113ef60d.jpg"
        )
        await ctx.send(embed=cmdEmbed)


async def setup(bot):
    await bot.add_cog(Commands(bot))
    print("commands cog loaded")
