from discord.ext import commands
from discord import Embed
from discord_components import Button, ButtonStyle, DiscordComponents
from variables import TOKEN, DATA_PATH

BOT = commands.Bot(command_prefix="!")  # Сам бот

'''Выполняется при запуске'''
@BOT.event
async def on_ready():
    DiscordComponents(BOT)  # Подключение кнопок
    print(f"Logged in as {BOT.user.name}({BOT.user.id})")  # Вывод в консоль, что бот запустился
    

'''Проверка, жив бот или что-то обрабатыает'''
@BOT.command()
async def ping(ctx):
    await ctx.send("pong")

'''Основное меню для пользователей'''
@BOT.command()
async def menu(ctx):
    embed = Embed()  # Основной держатель инфорамции
    embed.title = "Welcome to Viego Helper!"  # Назввание
    embed.description = "Choose one of the commands to go!"  # Описание
    embed.set_thumbnail(url=f"{DATA_PATH}/viego_avatar.jpg")  # Аватар Виего
    # Отправка сообщения с держателем и тремя кнопками вида [[random_agents][all_agents]][exit]
    await ctx.send(embed=embed, components=[[Button(label="Choose a random agent", style=ButtonStyle.gray, custom_id="random_agents"), 
                                             Button(label="All VALORANT agents", style=ButtonStyle.gray, custom_id="all_agents")],
                                             [Button(label="Exit the bot", style=ButtonStyle.red, custom_id="exit")]])
    interaction = await BOT.wait_for("button_click")  # Ждём, пока пользователь нажмёт кнопку
    # Если эта кнопка была не выход, заходим в обработку
    while interaction.component.custom_id != "exit":
        content = await ctx.invoke(BOT.get_command(interaction.component.custom_id))  # Выполняем команду бота в зависимости от того, что нажал пользователь
        await interaction.respond(content=content, ephemeral=False)  # Возвращаем результат как ответ бота, видимый всем
        interaction = await BOT.wait_for("button_click")  # Ожидаем новое нажатие кнопки
    # Если кнопка была выход, благодарим за использование бота 
    await interaction.respond(content="Thanks for using Viego Helper!")


if __name__ == "__main__":
    BOT.load_extension("cogs.agent")  # Подключение держателей команд (каждый прописывается отдельно)
    BOT.run(TOKEN)  # Запуск бота