from os import getenv
from requests import get
from json import loads
from random import choice
from discord.ext import commands

BOT = commands.Bot(command_prefix="!")
TOKEN = getenv("DISCORD_TOKEN")
VAL_CONTENT = loads(get(f"https://ap.api.riotgames.com/val/content/v1/contents?api_key={getenv('VAL_KEY')}"))
LOL_KEY = getenv("LOL_KEY")

class AgentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.agents = [i['name'] for i in VAL_CONTENT['characters']]
    
    @commands.command()
    async def all_agents(self, ctx):
        await ctx.send(f"List of VALORANT agents:\n{'\n'.join(self.agents)}")
    
    @commands.command()
    async def random_agent(self, ctx):
        await ctx.send(f"I chose you an agent. You need to pick {choice(self.agents)}!")


@BOT.event
async def on_ready():
    print(f"Logged in as {BOT.user.name}({BOT.user.id})")

@BOT.command()
async def ping(ctx):
    await ctx.send("pong")


if __name__ == "__main__":
    BOT.add_cog(AgentCog(BOT))
    BOT.run(TOKEN)