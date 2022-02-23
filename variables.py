from os import getenv
from requests import get
from json import loads



VAL_KEY = getenv('VALORANT_KEY')  # Переменная с ключом для Апи VALORANT
LOL_KEY = getenv('LOL_KEY')  # Переменная с ключом для Апи League of Legends
TOKEN = getenv("DISCORD_TOKEN")  # Переменная с ключом Discord
DATA_PATH = "https://raw.githubusercontent.com/TimeIsOut/ViegoHelperData/master"  # Пусь, где хранятся все файлы бота
BACKUP_VAR = {  # Переменная, если Апи VALORANT не отвечает (изменять вместе с разработкой).
    'characters': [
        {'name': 'Astra'},
        {'name': 'Breach'}, 
        {'name': 'Brimstone'}, 
        {'name': 'Chamber'}, 
        {'name': 'Cypher'}, 
        {'name': 'Jett'}, 
        {'name': 'KAY/O'}, 
        {'name': 'Killjoy'}, 
        {'name': 'Neon'}, 
        {'name': 'Omen'}, 
        {'name': 'Phoenix'}, 
        {'name': 'Raze'}, 
        {'name': 'Reyna'}, 
        {'name': 'Sage'}, 
        {'name': 'Skye'}, 
        {'name': 'Sova'}, 
        {'name': 'Viper'}, 
        {'name': 'Yoru'}], 
    'maps': [
        {'name': 'Ascent'},
        {'name': 'Bind'},
        {'name': 'Breeze'}, 
        {'name': 'Fracture'}, 
        {'name': 'Haven'}, 
        {'name': 'Icebox'}, 
        {'name': 'Split'}
    ]
}

'''Подключение и подгрузка данных VALORANT'''
content = get(f"https://ap.api.riotgames.com/val/content/v1/contents?api_key={VAL_KEY}")  # Запрос АПИ
if content.status_code == 200:  # Если поймал: 
    VAL_CONTENT = loads(content.content)  # Загрузка данных в словарь из JSON.
else:
    print("Backup plan! Loading variables...")  # Иначе выводим в консоль информацию о запасном плане
    VAL_CONTENT = BACKUP_VAR  # Подключаем переменную