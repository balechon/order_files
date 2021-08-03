import json

__config=None

def config():
    global __config
    if not __config:
        with open('directories.json','r',encoding="utf-8")as f:
            __config=json.load(f)
    
    return __config