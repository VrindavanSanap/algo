#!/usr/bin/python3
import numpy as np
import re

from game_strings import game_instructions,quit_msg, welcome_msg, move_outof_range_msg

class TicTakToe:
    # 1 = X, -1 = Y
    # Game state

    def __init__(self, start_grid=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):

        self.grid = start_grid
        self.state = None  # None = Running, 1 = x won, -1 = o won, 0 = draw
        if self.is_valid_state():
            pass
        else:
            self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.itos = {1: "X", -1: "O"}

    def is_valid_state(self):

        if abs(self.get_sum()) > 1:
            return False
        return True

    def is_game_drawn(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    return False
        return True

    def update_state(self):
        if self.is_game_drawn():
            self.state = 0
        for row in self.grid:
            if abs(sum(row)) == 3:
                self.state = sum(row)/3

        for col in zip(*self.grid):
            if abs(sum(col)) == 3:
                self.state = sum(col)/3
        dia1 = [[0, 0], [1, 1], [2, 2]]
        dia2 = [[0, 2], [1, 1], [2, 0]]
        s1 = 0
        s2 = 0
        for i in range(3):
            s1 += self.grid[dia1[i][0]][dia1[i][1]]
            s2 += self.grid[dia2[i][0]][dia2[i][1]]

        if abs(s1) == 3:
            self.state = s1/3

        if abs(s2) == 3:
            self.state = s2/3

    def get_sum(self):
        return sum([sum(row) for row in self.grid])

    def make_move(self, r, c, m=None):

        if m == None:
            m = self.whos_turn()
        if self.grid[r][c] == 0:
            self.grid[r][c] = m
            if not self.is_valid_state():
                self.grid[r][c] = 0
                print("Invalid move")
        else:
            print("Spot is not empty")
            print()
        self.update_state()

    def whos_turn(self):
        if self.get_sum() == 1:
            return -1
        else:
            return 1

    def whos_turn_str(self):
        if self.whos_turn() == 1:
            return "X"
        if self.whos_turn() == -1:
            return "O"

    def __repr__(self):
        res = ""
        i = 0
        for r in range(3):
            for c in range(3):
                i += 1
                res += " "
                if self.grid[r][c] == 0:
                    res += str(i)
                else:
                    res += self.itos[self.grid[r][c]]
                res += " "
                if c < 2:
                    res += "|"
            res += "\n"
            if r < 2:
                res += " --------- "
            res += "\n"
        return res

    def is_game_over(self):
        return self.state != None

    def reset(self):
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.state = None

    def result_str(self):
        draw_msg = "Game Drawn!!!"
        running_msg = "Game is still running"

        def win_msg(winner):
            return f"Player [{winner}] is the Winner!!!"

        if self.state == None:
            return (running_msg)
        if self.state == 0:
            return (draw_msg)

        if self.state == 1:
            return win_msg(self.itos[1])

        if self.state == -1:
            return win_msg(self.itos[-1])

    @staticmethod
    def get_player_move():
        try:
            inp = input(f"Player {ttt.whos_turn_str()}, your move: ")
            inp = inp.strip()

            if inp == "q":
                print("Quiting!")
                exit(0)
            inp = re.sub(r'[^0-9\s]', '', inp)
            inp = int(inp) - 1
            if inp > 9:
                print(move_outof_range_msg)
                return False

            row = inp // 3
            col = inp % 3
            return row, col
        except Exception:
            print(Exception)
            return False

def play_game(ttt):
    print(welcome_msg)
    print(game_instructions)
    print(quit_msg)
    print(ttt)
    while (not ttt.is_game_over()):
        if (move := TicTakToe.get_player_move()):
            row, col = move
            ttt.make_move(row, col)
        print(ttt)
    print(ttt.result_str())


ttt = TicTakToe()
if __name__ == "__main__":
    play_game(ttt)
