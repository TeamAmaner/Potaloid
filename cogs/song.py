import discord
from discord.ext import commands

from lib.youtube import YTDLSource


class Song(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.system = bot.system


    @commands.command()
    async def play(self, ctx, url):
        player = await YTDLSource.from_url(url, loop=self.bot.loop)
        vc = await discord.VoiceChannel.connect(ctx.author.voice.channel)
        vc.play(player)
        # vc.play(discord.FFmpegPCMAudio('【公式】 レミングミング／かいりきベア feat.flower-4oCuGeHWzCo.wav'))










def setup(bot):
    bot.add_cog(Song(bot))
