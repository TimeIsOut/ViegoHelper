from discord.ext import commands
from random import choice
from variables import VAL_CONTENT


class AgentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.agents = sorted([i['name'] for i in VAL_CONTENT['characters']])
    
    @commands.command()
    async def all_agents(self, ctx):
        output_agents = '\n'.join(self.agents)
        return f"List of VALORANT agents:\n{output_agents}"
    
    @commands.command()
    async def random_agents(self, ctx):
        return f"I chose you an agent. You need {choice(self.agents)}!"


def setup(bot):
    bot.add_cog(AgentCog(bot))