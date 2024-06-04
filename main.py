import random

from board import Board
from player import Player

NUM_CASELLE = 63


def lancio_i_dadi():
    return random.randint(1, 6) + random.randint(1, 6)


num_of_players = input("Quante persone vogliono giocare? (Inserisci un numero tra 2 e 6)\n")
NUM_PLAYERS = max(min(int(num_of_players), 6),2)

players = [Player() for n in range(NUM_PLAYERS)]
board = Board()
game_over = False

while not game_over:
    print("--- Nuovo turno! ---")
    for i, player in enumerate(players):
        print(f"Tocca al giocatore {i + 1}, è alla casella {player.index}.")
        input("Premi invio per tirare i dadi...")
        steps = lancio_i_dadi()
        print(f"Hai lanciato i dadi: esce {steps}!")
        board.move_player(player=player, steps=steps)
        print(f"Il giocatore {i +1} si sposta sulla casella {player.index}.")
        if board.game_is_over(player):
            print(f"Il giocatore {i +1} ha vinto!")
            game_over = True
            break


print("Il gioco è finito!")
