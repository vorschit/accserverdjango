import os
import pandas as pd
import json

with open('E:\Steam\steamapps\common\Assetto Corsa Competizione Dedicated Server\server\cfg\event.json', encoding='utf-16') as f:
    data_event_json = json.load(f)
    for i in data_event_json:
        print(i.get('track'))
#os.startfile("E:\Steam\steamapps\common\Assetto Corsa Competizione Dedicated Server\server\\accServer.exe")