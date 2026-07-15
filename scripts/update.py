import json
import random

with open("data/rain_library.json",encoding="utf-8") as f:
    library=json.load(f)

quote=random.choice(library)

with open("data/latest.json","w",encoding="utf-8") as f:
    json.dump(quote,f,ensure_ascii=False,indent=2)
