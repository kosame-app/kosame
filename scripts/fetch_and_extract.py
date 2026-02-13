import random
import requests
import json
import re

URL = "https://www.aozora.gr.jp/cards/000148/files/773_14560.html"

html = requests.get(URL).text
body = re.split("<body.*?>", html, flags=re.DOTALL)[1]
body = re.split("</body>", body, flags=re.DOTALL)[0]

text = re.sub("<.*?>", "", body)
sentences = [s.strip() for s in text.split("。") if "雨" in s]

if not sentences:
    sentence = "今日は雨に関する一文が見つかりませんでした。"
else:
    sentence = random.choice(sentences)
data = {
    "sentence": sentence + "。",
    "author": "夏目漱石",
    "work": "こころ",
    "app": "kosame"
}

with open("data/latest.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
