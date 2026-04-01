import json
import random
import glob
import os

rain_words = ["雨","小雨","霧雨","しとしと","降り","湿"]

sentences = []

for file in glob.glob("aozora/*.txt"):
    try:
        # ←ここ追加（作者・作品取得）
        filename = os.path.basename(file)
        name = os.path.splitext(filename)[0]

        if "_" in name:
            author, work = name.split("_", 1)
        else:
            author = "青空文庫"
            work = name

        with open(file,encoding="shift_jis",errors="ignore") as f:
            text = f.read()
            for line in text.split("。"):
                if any(word in line for word in rain_words):
                    sentences.append({
                        "sentence": line + "。",
                        "author": author,
                        "work": work
                    })

    except:
        pass

if sentences:
    result = random.choice(sentences)

    os.makedirs("data",exist_ok=True)

    with open("data/rain.json","w",encoding="utf-8") as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
