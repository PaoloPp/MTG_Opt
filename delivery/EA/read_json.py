import json
from pprint import pprint


def read_cards_json():
    with open("cards.json") as data_file:
        temp = json.load(data_file)
    cards = {}
    for k in temp:
        cards[str(k).lower()] = temp[k]
    return cards

