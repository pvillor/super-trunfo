from .deck import generate_pokemon_deck, split_deck, get_random_attr


def play():
    pokemon_deck = generate_pokemon_deck()

    p1_deck, p2_deck = split_deck(pokemon_deck)

    for index, p1_card in enumerate(p1_deck):
        print()
        p2_card = p2_deck[index]
        attr_to_compare = get_random_attr(p1_deck[0])

        print('p1_card -> ', p1_card)
        print('p2_card -> ', p2_deck[index])
        print('attr_to_compare -> ', attr_to_compare)

        if p1_card[attr_to_compare] > p2_card[attr_to_compare]:
            print(f"{p1_card['name']} WINS")
        elif p2_card[attr_to_compare] > p1_card[attr_to_compare]:
            print(f"{p2_card['name']} WINS")
        else:
            print('DRAW!')
