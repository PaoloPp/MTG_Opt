import datetime

import config
from cards import read_card_pool

POPSIZE = 10
DECKSIZE = 40
CROSSOVER_RATE = 0.5
MUTATION_RATE = 0.5
NUMBER_OF_GENERATIONS = 200
MATCHES_PER_OPPONENT = '50'  # must be string!
CARD_POOL = read_card_pool('../AER-pool-3.txt') #DICT
CARD_POOL_SIZE = len(CARD_POOL)
CARD_DIRECTORY = config.CARD_DIR
FORGE_PATH = config.FORGE_DIR
DECKLIST_HEADER = '[metadata]\nName=candidate\n[Main]\n'
OPPONENTS = ["GB-sealed-opponent.dck", "UWg-sealed-opponent.dck", "RG-sealed-opponent1.dck",
             "BGw-sealed-opponent.dck", "UR-sealed-opponent.dck", "RW-sealed-opponent.dck"]
# OPPONENTS = ["GB-sealed-opponent.dck", "UWg-sealed-opponent.dck", "BGw-sealed-opponent.dck"]
# OPPONENTS = ["BGw-sealed-opponent.dck"]

EXPERIMENT_TIMESTAMP = datetime.datetime.now().strftime("%d%m%H%M")
EXPERIMENT_FOLDER = "results/" + EXPERIMENT_TIMESTAMP
TERMINATION_TRESHOLD = 50
# CARDS = read_cards_json()
