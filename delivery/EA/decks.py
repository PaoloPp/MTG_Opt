import constants as ct


def genome_to_decklist(individual): #Convert a genome (rappresented with indexes) to a decklist
    deck_list = []
    for c in individual:
        deck_list.append(ct.CARD_POOL[c][0])
    return deck_list


def write_decklist(filename, decklist): #Saves the decklist to a txt file
    with open(filename, 'w') as file:
        file.write(ct.DECKLIST_HEADER)
        for card in decklist:
            file.write(card + '\n')
