class Warehouse:
  
  # Warehouse.number
  
  def __init__(self, position, productList):
    self.position = position
    self.productList = productList
  
  def getPosition(self):
    return self.position