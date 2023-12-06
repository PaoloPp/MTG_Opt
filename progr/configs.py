import card_parser as cp
import datetime

CARD_POOL_DIR = '/Users/paolopalmiero/Documents/Uni/MOTT/progetto/MTG_Opt/pools'
FORGE_DIR = ''
CARD_POOL = cp.read_card_pool(CARD_POOL_DIR + '/MY_POOL1.txt')
CARD_POOL_SIZE = len(CARD_POOL)
POPSIZE = 5
OPPONENTS = 5
#CROSSOVER_RATE = TBD
#MUTATION_RATE = TBD
NUMBER_OF_GENERATIONS = 200
MATCHES_PER_OPPONENT = '50' 

def set_timestamp():
    timestamp = datetime.datetime.now().strftime("%d%m%H%M")
    return timestamp