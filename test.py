from board import Board, Teleport58
from player import Player


def test_end_of_game_for_Board_class():
    caselle = 60
    dummy_board = Board(caselle)
    dummy_player = Player()
    dummy_player.index = 50

    steps_to_win = caselle - dummy_player.index
    dummy_board.move_player(dummy_player, steps_to_win)

    assert dummy_board.game_is_over(dummy_player)


def test_teleport_to_the_start():
    caselle = 60
    dummy_board = Board(caselle)
    dummy_board.board[3] = Teleport58()
    dummy_player = Player()

    dummy_board.move_player(dummy_player, 2)

    assert dummy_player.index == 1


def test_endgame_rimbalzo():
    caselle = 63
    dummy_board = Board(caselle)
    dummy_player = Player()
    dummy_player.index = 60

    dummy_board.move_player(dummy_player, 5)

    assert dummy_board.game_is_over(dummy_player) is False
    assert dummy_player.index == 61


def test_normal_step():
    caselle = 63
    dummy_board = Board(caselle)
    dummy_player = Player()
    dummy_player.index = 10

    dummy_board.move_player(dummy_player, 5)

    assert dummy_board.game_is_over(dummy_player) is False
    assert dummy_player.index == 15


def test_game_ends():
    caselle = 63
    dummy_board = Board(caselle)
    dummy_player = Player()
    dummy_player.index = 60

    dummy_board.move_player(dummy_player, 3)

    assert dummy_board.game_is_over(dummy_player)
