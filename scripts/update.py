import json
import random
import glob
import os

rain_words = ["雨","小雨","霧雨","しとしと","降り","湿"]

sentences = []

for file in glob.glob("aozora/*.txt"):
    try:
        with open(file,encoding="shift_jis",errors="ignore") as f:
            text = f.read()
            for line in text.split("。"):
                if any(word in line for word in rain_words):
                    sentences.append(line+"。")
    except:
        pass

if sentences:
    result = {
        "sentence": random.choice(sentences),
        "author": "青空文庫",
        "work": ""
    }

    os.makedirs("data",exist_ok=True)

    with open("data/rain.json","w",encoding="utf-8") as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
