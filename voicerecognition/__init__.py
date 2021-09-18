from .voicerecognition import VoiceRecognition

def setup(bot):
    bot.add_cog(VoiceRecognition(bot))