from redbot.core import commands

class VoiceRecognition(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active = False

    # [p] means command prefix
    # when user uses [p]toggle
    @commands.command()
    async def toggle(self, ctx):
        if len(self.bot.voice_clients) == 0:
            self.active = True
            author = ctx.message.author
            channel = author.voice.channel
            await channel.connect()
            await ctx.send("Voice recognition enabled.")
        elif ctx.author.voice.channel == ctx.voice_client.channel:
            self.active = not self.active
            await ctx.send("Voice recognition enabled." if self.active else "Voice recognition disabled.")
        else:
            await ctx.send("You are not in the same voice channel as me.")

    # when user uses [p]exit
    @commands.command()
    async def exit(self, ctx):
        if len(self.bot.voice_clients) == 0:
            await ctx.send("I am not in a voice channel.")
        elif ctx.author.voice.channel == ctx.voice_client.channel:
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("You are not in the same voice channel as me.")
        