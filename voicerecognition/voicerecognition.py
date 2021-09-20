from redbot.core import commands

class VoiceRecognition(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active = False

    async def voiceMiddleware(self, ctx, error, success):
        if not hasattr(ctx.author.voice, 'channel'):
            await ctx.send("You are not in a voice channel.")
        elif len(self.bot.voice_clients) == 0:
            await error()
        elif ctx.author.voice.channel == ctx.voice_client.channel:
            await success()
        else:
            await ctx.send("We are not in the same voice channel.")

    # [p] means command prefix
    # when user uses [p]toggle
    @commands.command()
    async def toggle(self, ctx):
        async def error():
            self.active = True
            author = ctx.message.author
            channel = author.voice.channel
            await channel.connect()
            await ctx.send("Voice recognition enabled.")
        async def success():
            self.active = not self.active
            await ctx.send("Voice recognition enabled." if self.active else "Voice recognition disabled.")
        await self.voiceMiddleware(ctx, error, success)

    # when user uses [p]exit
    @commands.command()
    async def exit(self, ctx):
        async def error():
            await ctx.send("I am not in a voice channel.")
        async def success():
            await ctx.voice_client.disconnect()
        await self.voiceMiddleware(ctx, error, success)
        