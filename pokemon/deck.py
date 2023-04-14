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
            'strength': 2,
            'agility': 4,
            'heigth': 1,
        }

        pokemon_cards.append(pokemon_dict)

    return pokemon_cards
