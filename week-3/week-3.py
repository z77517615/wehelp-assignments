import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
clist=data["result"]["results"]
with open("data.csv","w",encoding="utf-8-sig") as file:
    for spot in clist:
        picture=spot["file"]
        picture=picture.split("https:")  
        file.write(spot["stitle"] +","+ spot["address"][5:8]+","+spot["longitude"]+","+spot["latitude"]+","+"https:"+picture[1]+"\n")

