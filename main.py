from discord.ext import commands
from discord import Embed
from discord_components import Button, ButtonStyle, DiscordComponents
from variables import TOKEN, DATA_PATH

BOT = commands.Bot(command_prefix="!")

@BOT.event
async def on_ready():
    DiscordComponents(BOT)
    print(f"Logged in as {BOT.user.name}({BOT.user.id})")

@BOT.event
async def on_button_click(interaction):
    await interaction.send(content=BOT.invoke(BOT.get_command(interaction.component.custom_id)))
    

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
                                             Button(label="All VALORANT agents", style=ButtonStyle.gray, custom_id="all_agents")]])


if __name__ == "__main__":
    BOT.load_extension("cogs.agent")
    BOT.run(TOKEN)