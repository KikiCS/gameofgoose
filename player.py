class Player:
    def __init__(self):
        self.index = 1
        self.can_move_next_turn = True

    def move(self, index):
        self.index = index
