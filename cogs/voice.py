from discord.ext import commands


'''Держатель для команд, связанных с голосовым чатом'''
class VoiceCog(commands.Cog):
    '''Инициализация держателя'''
    def __init__(self, bot):  
        self.bot = bot
    
    '''Подключение к голосовому чату'''
    @commands.command(pass_context=True)
    async def connect(self, ctx):  
        if (n := ctx.author.voice):
            await self.bot.connect(n.channel)
            self.voice_channel
        else:
            await ctx.send("You are not connected to any of the voice channels. You need to connect to one of them.")
    
    '''Отключение от голосового чата'''
    @commands.command(pass_context=True)
    async def disconnect(self, ctx):  
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
        else:
            await ctx.send("I am not connected to any of the voice channels.")


def setup(bot):
    bot.add_cog(VoiceCog(bot))