from discord.ext import commands
from variables import TOKEN

BOT = commands.Bot(command_prefix="!")

@BOT.event
async def on_ready():
    print(f"Logged in as {BOT.user.name}({BOT.user.id})")

@BOT.command()
async def ping(ctx):
    await ctx.send("pong")


if __name__ == "__main__":
    BOT.load_extension("cogs.agent")
    BOT.run(TOKEN)