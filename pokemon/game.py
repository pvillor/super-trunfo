from .deck import generate_pokemon_deck, split_deck, get_random_attr


def play():
    pokemon_deck = generate_pokemon_deck()

    p1_deck, p2_deck = split_deck(pokemon_deck)

    random_attr = get_random_attr(p1_deck[0])
