from discord.ext import commands
import discord


class Dox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dox(self, ctx, member: discord.Member):
        if not (ctx.author.guild_permissions.ban_members):
            await ctx.send("You do not have the permissions to run this command!")
            return
        doxEmbed = discord.Embed(
            title="", description="Doxing member...", color=0x5493F7
        )
        doxEmbed.add_field(
            name="Succesfully doxxed member!",
            value="DNS: Clounfare \n Discord-DNS: Cloudfare_malware \n Device DNS: Default \n Discord-authority-crack: Succesful \n Inject: Clounfare-Malware",
        )
        doxEmbed.set_author(name=ctx.author.display_name)
        await ctx.send(embed=doxEmbed)
        await ctx.send(f"{member.mention} has been doxxed!")


async def setup(bot):
    await bot.add_cog(Dox(bot))
    print("dox cog loaded")
