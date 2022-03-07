from fastapi import FastAPI
from deta import Deta
import json
import random as Rand
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
a = "c00viw7z_4Rj2TKrz3WGG3"
deta = Deta(a+"xWuLkW711vRCifgJ4GR")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "I love you <3 Anu!"}


# Flutter Widgets
@app.get("/widgets/")
async def read_item(limit: int = -1, random: bool = False):
    with open('widgets.json', "r", encoding='utf-8') as json_file:
        allFacts = json.load(json_file, strict=False)
    countAllFacts = len(allFacts)
    if limit < 0 or limit >= countAllFacts:
        if random == False:
            return allFacts
        Rand.shuffle(allFacts)
        return allFacts
    if limit == 0:
        return []
    if random:
        Rand.shuffle(allFacts)
        requiredFacts = []
        for i in range(limit):
            requiredFacts.append(allFacts[i])
        return requiredFacts
    requiredFacts = []
    for i in range(limit):
        requiredFacts.append(allFacts[i])
    return requiredFacts