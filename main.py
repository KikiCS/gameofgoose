import random

NUM_CASELLE = 63
NUM_PLAYERS = 1

giocatore1_index = 1


def game_is_over():
    return giocatore1_index >= NUM_CASELLE


def lancio_i_dadi():
    return random.randint(1, 6) + random.randint(1, 6)


while not game_is_over():
    for player in range(NUM_PLAYERS):
        print(f"Il giocatore {player + 1} è alla casella {giocatore1_index}.")
        step = lancio_i_dadi()
        print(f"Lancia i dadi! Esce {step}!")
        giocatore1_index += step
        print(f"Il giocatore {player + 1} si sposta sulla casella {giocatore1_index}.")


print("Il gioco è finito!")
