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
