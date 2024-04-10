from typing import cast
from discord.ext import commands
import discord
import wavelink

class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx: commands.Context, *, query: str = None) -> None:
        """Play a song with the given query."""
        if query is None:
            embedVar = discord.Embed(
                title="Play Command Help",
                description="The `p!play` command allows you to play a song in the voice channel you're currently in. To use the command, type `p!play` followed by the name of the song you want to play. For example, p!play Despacito`.",
                color=discord.Color.blue()
            )
            await ctx.send(embed=embedVar)
            return

        if not ctx.guild:
            return

        player: wavelink.Player
        player = cast(wavelink.Player, ctx.voice_client)  # type: ignore

        if not player:
            try:
                player = await ctx.author.voice.channel.connect(cls=wavelink.Player)  # type: ignore
            except AttributeError:
                await ctx.send(
                    "Please join a voice channel first before using this command."
                )
                return
            except discord.ClientException:
                await ctx.send(
                    "I was unable to join this voice channel. Please try again."
                )
                return

        player.autoplay = wavelink.AutoPlayMode.enabled

        # Lock the player to this channel...
        if not hasattr(player, "home"):
            player.home = ctx.channel

        tracks: wavelink.Search = await wavelink.Playable.search(query)
        if not tracks:
            await ctx.send(
                f"{ctx.author.mention} - Could not find any tracks with that query. Please try again."
            )
            return

        if isinstance(tracks, wavelink.Playlist):
            # tracks is a playlist...
            added: int = await player.queue.put_wait(tracks)
            await ctx.send(
                f"Added the playlist **`{tracks.name}`** ({added} songs) to the queue."
            )
        else:
            track: wavelink.Playable = tracks[0]
            await player.queue.put_wait(track)
            embedVar = discord.Embed(
                title="Added to Queue",
                description=f"**{track}** has been added to the queue. Enjoy your music!",
                color=discord.Color.green()
            )
            await ctx.send(embed=embedVar)

        if not player.playing:
            # Play now since we aren't playing anything...
            await player.play(player.queue.get(), volume=30)
            embedVar = discord.Embed(
                title="Now Playing",
                description=f"Now playing: **{track}**. Enjoy your music!",
                color=discord.Color.green()
            )
            await ctx.send(embed=embedVar)

        # Optionally delete the invokers message...
        try:
            await ctx.message.delete()
        except discord.HTTPException:
            pass

async def setup(bot):
    await bot.add_cog(Play(bot))
    print("Music: Play loaded")