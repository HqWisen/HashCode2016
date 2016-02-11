class Delivery:
  
  # Delivery.number
  
  def __init__(self, position, productTypeList):
    self.position = position
    self.productTypeList = productTypeList
    
  def getPosition(self):
    return self.position