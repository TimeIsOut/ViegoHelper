from discord.ext import commands
from random import choice
from json import loads
from requests import get
from variables import VAL_KEY


VAL_CONTENT = None
while VAL_CONTENT is None:
    content = get(f"https://ap.api.riotgames.com/val/content/v1/contents?api_key={VAL_KEY}")
    if content.status_code == 200:
        VAL_CONTENT = content.content
    


class AgentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.agents = [i['name'] for i in VAL_CONTENT['characters']]
    
    @commands.command()
    async def all_agents(self, ctx):
        output_agents = '\n'.join(self.agents)
        await ctx.send(f"List of VALORANT agents:\n{output_agents}")
    
    @commands.command()
    async def random_agents(self, ctx):
        await ctx.send(f"I chose you an agent. You need {choice(self.agents)}!")


def setup(bot):
    bot.add_cog(AgentCog(bot))