from discord.ext import commands
from random import choice
from variables import VAL_CONTENT


'''Команды, связанные с агентами протокола VALORANT'''
class AgentCog(commands.Cog):
    def __init__(self, bot):  # Инициализация держателя для команд
        self.bot = bot
        self.agents = sorted([i['name'] for i in VAL_CONTENT['characters']])
    
    @commands.command()
    async def all_agents(self, ctx):  # Вывод всех агентов протокола
        output_agents = '\n'.join(self.agents)
        return f"List of VALORANT agents:\n{output_agents}"
    
    @commands.command()
    async def random_agents(self, ctx):  # Выбор случайного агента
        return f"I chose you an agent. You need {choice(self.agents)}!"


'''ОБЯЗАТЕЛЬНО! Подключение держателя к основному боту.'''
def setup(bot):
    bot.add_cog(AgentCog(bot))