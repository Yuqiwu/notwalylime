import json

s = open("s", "r")
doc = s.read()

dic = json.loads(doc)

final = []
for episode in dic["_embedded"]["episodes"]:
    final.append(episode)

