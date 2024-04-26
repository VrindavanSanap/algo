#!/usr/bin/python3
import numpy as np
import re

from two_players_ttt import TicTacToe
from game_strings import game_instructions, quit_msg, welcome_msg, move_outof_range_msg

    
def play_game(ttt):
    print(welcome_msg)
    print(game_instructions)
    print(quit_msg)
    print(ttt)
    while (not ttt.is_game_over()):
        if (move := TicTacToe.get_player_move()):
            row, col = move
            ttt.make_move(row, col)
        print(ttt)
    print(ttt.result_str())


ttt = TicTacToe()
if __name__ == "__main__":
    play_game(ttt)
