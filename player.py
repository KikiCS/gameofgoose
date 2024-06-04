class Player:
    def __init__(self, name: str = "pippo"):
        self.name = name
        self.index = 1
        self.can_move_next_turn = True

    def move(self, index):
        self.index = index

    def __repr__(self):
        return self.name
