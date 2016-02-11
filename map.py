class Map:
  def __init__(self, R, C):
    self.R = R
    self.C = C
    self.matrix = [[Cellule() for i in range(C)] for i in range(R)]
    print(self.matrix)