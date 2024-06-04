import random

from board import Board
from dice import generate_dice_faces_diagram
from player import Player

NUM_CASELLE = 63


def lancio_i_dadi():
    return random.randint(1, 6), random.randint(1, 6)


num_of_players = input(
    "Quante persone vogliono giocare? (Inserisci un numero tra 2 e 6)\n"
)
NUM_PLAYERS = max(min(int(num_of_players), 6), 2)

players = [Player() for n in range(NUM_PLAYERS)]
board = Board()
game_over = False

while not game_over:
    print("--- Nuovo turno! ---")
    for i, player in enumerate(players):
        print(f"Tocca al giocatore {i + 1}, è alla casella {player.index}.")
        if not player.can_move_next_turn:
            print(
                f"Il giocatore {i + 1} è alla taverna e riprenderà a giocare il prossimo turno."
            )
            player.can_move_next_turn = True
            break
        input("Premi invio per tirare i dadi...")
        dice_values = lancio_i_dadi()
        ascii_dices = generate_dice_faces_diagram(dice_values)
        steps = sum(dice_values)
        print(f"\n{ascii_dices}")
        print(f"Esce {steps}!")
        board.move_player(player=player, steps=steps)
        print(f"Il giocatore {i +1} si sposta sulla casella {player.index}.")
        if board.game_is_over(player):
            print(f"Il giocatore {i +1} ha vinto!")
            game_over = True
            break


print("Il gioco è finito!")
