def read_card_pool(filename):
    card_pool = {}
    with open(filename, 'r') as file:
        card_list = []
        for line in file:
            card_list.append(line.strip())

    POOL_SIZE = len(card_list)
    for i in range(POOL_SIZE):
        card = card_list[i]
        card = card.split(' ')
        number_of_cards = int(card[0])
        name_of_card = " ".join(card[1:])
        card_pool[i] = (name_of_card, number_of_cards)

    return card_pool


def color_symbols(CARDS, cardName):
    colors = [CARDS[cardName]['manaCost'].count('W'),
              CARDS[cardName]['manaCost'].count('U'),
              CARDS[cardName]['manaCost'].count('B'),
              CARDS[cardName]['manaCost'].count('R'),
              CARDS[cardName]['manaCost'].count('G')]  # WUBRG
    return colors


def land_symbols(CARDS, cardName):
    colors = [CARDS[cardName]['colorIdentity'].count('W'),
              CARDS[cardName]['colorIdentity'].count('U'),
              CARDS[cardName]['colorIdentity'].count('B'),
              CARDS[cardName]['colorIdentity'].count('R'),
              CARDS[cardName]['colorIdentity'].count('G')]  # WUBRG
    return colors


def colorsymbols_in_deck(CARDS, decklist):
    colors = [0, 0, 0, 0, 0]
    lands = [0, 0, 0, 0, 0]
    for card in decklist:
        card = card.lower()
        if is_land(CARDS, str(card).lower()):
            lands = list(map(sum, zip(lands, land_symbols(CARDS, card))))
        else:
            colors = list(map(sum, zip(colors, color_symbols(CARDS, card))))
    return lands, colors


def is_land(CARDS, cardName):
    if 'manaCost' in CARDS[cardName].keys():
        return False
    else:
        return True
