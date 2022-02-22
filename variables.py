from os import getenv
from requests import get
from json import loads



VAL_KEY = getenv('VALORANT_KEY')
LOL_KEY = getenv('LOL_KEY')
TOKEN = getenv("DISCORD_TOKEN")
DATA_PATH = "https://raw.githubusercontent.com/TimeIsOut/ViegoHelperData/master"
BACKUP_VAR = {
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

content = get(f"https://ap.api.riotgames.com/val/content/v1/contents?api_key={VAL_KEY}")
if content.status_code == 200:
    VAL_CONTENT = loads(content.content)
else:
    print("Backup plan! Loading variables...")
    VAL_CONTENT = BACKUP_VAR