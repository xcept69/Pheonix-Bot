import discord
import os
from discord.ext import commands, tasks
from src.utils.constants import TOKEN, WAVELINK_PASS, WAVELINK_URI
from itertools import cycle
import wavelink

ts = 0
tm = 0
th = 0
td = 0


class Pheonix(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="p!", intents=discord.Intents.all())

    async def on_ready(self):
        await load_cog()
        print("Pheonix™ is ready to use!")
        print("-------------------------")
        status_swap.start()
        uptimeCounter.start()
    
    async def setup_hook(self) -> None:
        nodes = [wavelink.Node(uri=f"{WAVELINK_URI}", password=f"{WAVELINK_PASS}")]

        # cache_capacity is EXPERIMENTAL. Turn it off by passing None
        await wavelink.Pool.connect(nodes=nodes, client=self, cache_capacity=100)

    async def on_wavelink_node_ready(
        self, payload: wavelink.NodeReadyEventPayload
    ) -> None:
        print(f"Wavelink Node connected: {payload.node!r} | Resumed: {payload.resumed}")

    async def on_wavelink_track_start(
        self, payload: wavelink.TrackStartEventPayload
    ) -> None:
        player: wavelink.Player | None = payload.player
        if not player:
            # Handle edge cases...
            return

        original: wavelink.Playable | None = payload.original
        track: wavelink.Playable = payload.track

        embed: discord.Embed = discord.Embed(title="Now Playing")
        embed.description = f"**{track.title}** by `{track.author}`"

        if track.artwork:
            embed.set_image(url=track.artwork)

        if original and original.recommended:
            embed.description += f"\n\n`This track was recommended via {track.source}`"

        if track.album.name:
            embed.add_field(name="Album", value=track.album.name)

        await player.home.send(embed=embed)


bot = Pheonix()

bot.remove_command("help")


status = cycle(
    [
        "p!help",
        "Itz Panda OP",
        "@itz.pheonix",
        "https://discord.gg/UEttZCZPFE",
        "Itz Panda is THE GOAT",
    ]
)


@tasks.loop(seconds=15)
async def status_swap():
    await bot.change_presence(activity=discord.Game(next(status)))


@tasks.loop(seconds=2.0)
async def uptimeCounter():
    global ts, tm, th, td
    ts += 2
    if ts == 60:
        ts = 0
        tm += 1
        if tm == 60:
            tm = 0
            th += 1
            if th == 24:
                th = 0
                td += 1


async def load_cog():
    modules = ["core", "fun", "moderation", "music"]
    for module in modules:
        for fn in os.listdir("cogs/" + module):
            if fn.endswith(".py"):
                await bot.load_extension(f"cogs.{module}.{fn[:-3]}")


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)


@bot.command()
async def sync(ctx: commands.Context):
    await ctx.send("Syncing Slash Commands")
    synced = await bot.tree.sync()
    if len(synced) > 0:
        for cmd in synced:
            await ctx.send(f"Synced {cmd}")
        await ctx.send(f"Synced {len(synced)} Commands Globally!")
    else:
        await ctx.send("No Slash Commands to Register.")


@bot.hybrid_command(name="shutdown")
async def shutdown(ctx: commands.Context):
    if int(ctx.author.id) not in [786926252811485186, 1085081038952337508]:
        await ctx.send("Owner only Command")
        return
    await ctx.send("Going to sleep")
    await bot.close()


if __name__ == "__main__":
    bot.run(TOKEN)
