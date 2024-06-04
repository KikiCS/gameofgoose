from player import Player


class Casella:
    def trigger(self, player: Player):
        pass


class Teleport(Casella):
    def __init__(self, casella_target: int):
        self.casella_target = casella_target

    def trigger(self, player: Player):
        player.move(self.casella_target)


class Teleport6(Teleport):
    def __init__(self):
        super().__init__(casella_target=12)

    def trigger(self, player: Player):
        super().trigger(player=player)
        print("Sali sul ponte e vai alla casella 12!")


class Teleport42(Teleport):
    def __init__(self):
        super().__init__(casella_target=39)

    def trigger(self, player: Player):
        super().trigger(player=player)
        print("Ti perdi nel labirinto e torni alla casella 39!")


class Teleport58(Teleport):
    def __init__(self):
        super().__init__(casella_target=1)

    def trigger(self, player: Player):
        super().trigger(player=player)
        print("Oh no! Lo scheletro ti fa tornare alla casella di partenza!")


class CasellaBloccaGiocatore(Casella):
    def trigger(self, player: Player):
        player.can_move_next_turn = False
        print("Locanda! Le gozzoviglie ti bloccano per un turno!")


class Board:
    def __init__(self, num_caselle: int = 63):
        self.num_caselle = num_caselle
        self.board = [Casella()] * (self.num_caselle + 1)

        self.board[6] = Teleport6()
        self.board[42] = Teleport42()
        self.board[58] = Teleport58()

        self.board[19] = CasellaBloccaGiocatore()

    def move_player(self, player: Player, steps: int):
        player.index = min(player.index + steps, self.num_caselle)
        self.board[player.index].trigger(player)

    def game_is_over(self, player: Player):
        return player.index == self.num_caselle
