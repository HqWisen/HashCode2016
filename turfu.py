class Warehouse:
  def __init__(self):
    pass

class ProductType:
  def __init__(self, _id, weight):
    self._id = _id;
    self.weight = weight    
  def getWeight():
    return self.weight
  def setWeight(weight):
    self.weight = weight

class Product:
  def __init__(self, ptype):
    self.ptype = ptype;
class Order:
  def __init__(self):
    pass


class Cellule:
  def __init__(self):
    pass
  
class Map:
  def __init__(self, R, C):
    self.R = R
    self.C = C
    self.matrix = [[Cellule() for i in range(C)] for i in range(R)]
    print(self.matrix)
  
class Parser:
  def __init__(self, fileName):
    self.f = open(fileName)
    self.lines = self.f.readlines()
    print(self.lines)
    self.f.close()
    
if __name__ == "__main__":
  parser = Parser("busy_day.in");

  
  