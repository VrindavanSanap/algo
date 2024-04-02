import numpy as np

class TicTakToe:
  # 1 = X, -1 = Y
  def __init__(self, start_state = [[0,0,0],[0,0,0],[0,0,0]]):

    self.state = start_state
    if self.is_valid_state():
        pass
    else:
      self.state= [[0,0,0],[0,0,0],[0,0,0]]

  def is_valid_state(self):

    if abs(self.get_sum()) > 1:
      return False
    return True

  def get_sum(self):
    return sum([sum(row) for row in self.state])


  def make_move(self, r ,c, m = None):

    if self.state[r][c] == 0:
      self.state[r][c] = m
      if not self.is_valid_state():
        self.state[r][c] = 0
        print("Invalid move")
    else:
      print("Spot is not empty")

  def whos_turn(self):
    if self.get_sum() == 1:
      return -1
    else:
      return 1

  def __repr__(self):
    res = ""
    for row in self.state:
        for cell in row:
            if cell == 1:
                res += 'X '
            elif cell == -1:
                res +='O '
            else:
                res +='- '
        res += "\n"
    return res

ttt = TicTakToe()
print(ttt)
ttt.make_move(1,1,1)
print(ttt)
print(ttt.whos_turn())
