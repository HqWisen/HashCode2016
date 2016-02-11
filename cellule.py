class Cellule:
  def __init__(self):
    self.maison = None # maison warehouse or 
    self.drones = []

  def setMaison(self, maison):
    self.maison = maison
  def getMaison(self):
    return self.maison
	def moveIn(self,drone):
    self.drones.append(drone)

  def isIn(self,truc):
    return truc in self.trucs