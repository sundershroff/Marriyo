import requests
import json
jsondec = json.decoder.JSONDecoder()
data = requests.get("http://51.20.61.70:3000/pm_myid/9FGWGK0RQUL").json()[0]
level = jsondec.decode(data["level_education"])
print(level)
print(type(level))
print(level[0])
for x in jsondec.decode(level[0]):
    print(x)