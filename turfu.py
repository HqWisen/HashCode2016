class Warehouse:
  def __init__(self):
    pass

  
class ProductType:
  def __init__(self):
    pass

class Order:
  def __init__(self):
    pass


class Map:
  def __init__(self, R, C):
    self.R = R
    self.C = C
    self.matrix = [[None for i in range(C)] for i in range(R)]
    print(self.matrix)


if __name__ == "__main__":
  t = Map(2, 3);
