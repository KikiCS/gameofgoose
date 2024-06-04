from player import Player


class Casella:
    def trigger(self, player: Player):
        pass


class Board:
    def __init__(self, num_caselle: int = 63):
        self.num_caselle = num_caselle
        self.board = [Casella()] * (self.num_caselle + 1)

    def move_player(self, player: Player, steps: int):
        player.index = min(player.index + steps, self.num_caselle)
        self.board[player.index].trigger(player)

    def game_is_over(self, player: Player):
        return player.index == self.num_caselle
