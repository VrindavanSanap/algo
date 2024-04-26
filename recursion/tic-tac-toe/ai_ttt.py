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
    while (True):
        if (move := ttt.get_player_move()):
            row, col = move
            ttt.make_move(row, col)
            print(ttt)
            for r, c in (ttt.all_possible_moves()):
                
                print(f"{ttt.row_col_to_n(r, c)}:{ttt.is_winning_move(r, c)}")
        if( ttt.is_game_over()):
            break
    print(ttt.result_str())


ttt = TicTacToe()
if __name__ == "__main__":
    play_game(ttt)
