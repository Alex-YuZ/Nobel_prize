import json
import helper

def load_nobel_prizes(filename='prize.json'):
    with open(filename) as infile:
        contents = json.load(infile)
    return contents