import random

POKEMON_NAMES = (
    'Bulbasaur',
    'Charmander',
    'Squirtle',
    'Pikachu',
    'Eevee',
    'Riolu'
)


def generate_pokemon_deck() -> list[dict]:
    # pokemon_cards = []

    # for pokemon_name in POKEMON_NAMES:
    #     pokemon_dict = {
    #         'name': pokemon_name,
    #         'strength': random.randint(1, 10),
    #         'agility': round(random.uniform(0, 10), 1),
    #         'heigth': round(random.uniform(0, 10), 2),
    #     }

    #     pokemon_cards.append(pokemon_dict)

    pokemon_cards = [
        {
            'name': pokemon_name,
            'strength': random.randint(1, 10),
            'agility': round(random.uniform(0, 10), 1),
            'heigth': round(random.uniform(0, 10), 2),
        }
        for pokemon_name in POKEMON_NAMES]

    return pokemon_cards


def split_deck(deck: list[dict]) -> tuple[list[dict], list[dict]]:
    half_deck = len(deck) // 2

    random.shuffle(deck)

    p1_deck = deck[:half_deck]
    p2_deck = deck[half_deck:]

    # print('p1 deck: ')
    # for card in p1_deck:
    #     print(card)

    # print()

    # print('p2_deck: ')
    # for card in p2_deck:
    #     print(card)

    return p1_deck, p2_deck


def get_random_attr(card: dict) -> str:
    card_keys = card.keys()
    # print(list(card_keys))
    card_keys = [key for key in card.keys() if key != 'name']
    # print(card_keys)

    # rand_int = random.randint(0, len(card_keys) - 1)
    # print(card_keys[rand_int])

    # print(random.choice(card_keys))

    return random.choice(card_keys)
