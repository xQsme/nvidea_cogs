from redbot.core import commands

class VoiceRecognition(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # [p] means command prefix
    # when user uses [p]join
    async def join(self, ctx):
        await ctx.send("I should join user's voice channel here")

    # when user uses [p]toggle
    async def toggle(self, ctx):
        await ctx.send("Voice recognition functionality should start/stop working here")

    # when user uses [p]leave
    async def leave(self, ctx):
        await ctx.send("I should leave voice channel here")