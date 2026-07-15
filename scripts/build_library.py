import json
import glob
import os

rain_words = ["雨","小雨","霧雨","しとしと","降り","湿"]

library = []

for file in glob.glob("aozora/*.txt"):

    try:

        filename = os.path.basename(file)
        name = os.path.splitext(filename)[0]

        if "_" in name:
            author, work = name.split("_",1)
        else:
            author = "不明"
            work = name

        with open(file,encoding="shift_jis",errors="ignore") as f:

            text = f.read()

            for line in text.split("。"):

                line=line.strip()

                if len(line)<15:
                    continue

                if any(word in line for word in rain_words):

                    library.append({

                        "sentence":line+"。",
                        "author":author,
                        "work":work

                    })

    except:
        pass


os.makedirs("data",exist_ok=True)

with open("data/rain_library.json","w",encoding="utf-8") as f:
    json.dump(library,f,ensure_ascii=False,indent=2)

print(len(library))
