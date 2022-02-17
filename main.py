import os
import discord
from discord.ext import commands

BOT = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@BOT.event
async def on_ready():
    print(f"Logged in as {BOT.user.name}({BOT.user.id})")

@BOT.command()
async def ping(ctx):
    await ctx.send("pong")


if __name__ == "__main__":
    BOT.run(TOKEN)