from asyncio import gather
from code import interact
from discord.ext import commands
from discord import Embed
from discord_components import Button, ButtonStyle, DiscordComponents
from variables import TOKEN, DATA_PATH

BOT = commands.Bot(command_prefix="!")

@BOT.event
async def on_ready():
    DiscordComponents(BOT)
    print(f"Logged in as {BOT.user.name}({BOT.user.id})")
    

@BOT.command()
async def ping(ctx):
    await ctx.send("pong")

@BOT.command()
async def menu(ctx):
    embed = Embed()
    embed.title = "Welcome to Viego Helper!"
    embed.description = "Choose one of the commands to go!"
    embed.set_thumbnail(url=f"{DATA_PATH}/viego_avatar.jpg")
    await ctx.send(embed=embed, components=[[Button(label="Choose a random agent", style=ButtonStyle.gray, custom_id="random_agents"),
                                             Button(label="All VALORANT agents", style=ButtonStyle.gray, custom_id="all_agents")],
                                             [Button(label="Exit the bot", style=ButtonStyle.red, custom_id="exit")]])
    interaction = await BOT.wait_for("button_click")
    while interaction.component.custom_id != "exit":
        await gather(ctx.invoke(BOT.get_command(interaction.component.custom_id)), interaction.respond())
        interaction = await BOT.wait_for("button_click")
    await interaction.respond(content="Thanks for using Viego Helper!")

if __name__ == "__main__":
    BOT.load_extension("cogs.agent")
    BOT.run(TOKEN)