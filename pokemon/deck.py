import random

POKEMON_NAMES = (
    'Bulbasaur',
    'Charmander',
    'Squirtle',
    'Pikachu',
    'Eevee'
)


def generate_pokemon_deck() -> list[dict]:
    pokemon_cards = []

    for pokemon_name in POKEMON_NAMES:
        pokemon_dict = {
            'name': pokemon_name,
            'strength': random.randint(1, 10),
            'agility': round(random.uniform(0, 10), 1),
            'heigth': round(random.uniform(0, 10), 2),
        }

        pokemon_cards.append(pokemon_dict)

    return pokemon_cards
