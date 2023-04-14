from pokemon import deck


def main():
    pokemon_deck = deck.generate_pokemon_deck()

    for card in pokemon_deck:
        print(card)


if __name__ == '__main__':
    main()
