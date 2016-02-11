from cellule import *

class Carte:
  def __init__(self, R, C):
    self.R = R
    self.C = C
    self.matrix = [[Cellule() for i in range(C)] for i in range(R)]
  def setMaisonOn(self, maison):
    r, c = maison.getPosition()
    self.matrix[r][c].setMaison(maison)