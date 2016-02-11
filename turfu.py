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
    self.parseFirstSection();
    self.parseSecondSection();
    self.f.close()
    
  def parseFirstSection(self):
    line = self.lines[0].split()
    rows = int(line[0])
    cols = int(line[1])
    Drone.number = int(line[2])
    T = int(line[3])
    Drone.load = int(line[4])
  
  def parseSecondSection(self):
    line = self.lines[1].split()
    numberOfProduct = int(line[0])
    productWeightList = self.lines[2].split()
    self.convertSeqToInt(productWeightList)
    numberOfWarehouse = int(self.lines[3])
    warehouseIndexLine = 2;
    warehouseList = []
    for i in range(numberOfWarehouse):
      warehouseIndexLine += 2
      position = self.lines[warehouseIndexLine].split()
      self.convertSeqToInt(position)
      warehouseList.append(Warehouse(position))
      productList = self.lines[warehouseIndexLine+1].split()
      self.convertSeqToInt(productList)
      warehouseList[i].setProductList(productList)
    orderIndexLine = warehouseIndexLine + 2
    numberOfOrder = int(self.lines[orderIndexLine])
    orderIndexLine = orderIndexLine - 2
    for i in range(numberOfOrder):
      orderIndexLine += 3
      deliveryPosition = self.lines[orderIndexLine].split()
      self.convertSeqToInt(deliveryPosition)
      numberOfProducts = int(self.lines[orderIndexLine+1])
      productTypeList = self.lines[orderIndexLine+2].split()
      self.convertSeqToInt(productTypeList)
      
  def convertSeqToInt(self, L):
    for i in range(len(L)):
      L[i] = int(L[i]);
      
if __name__ == "__main__":
  parser = Parser("busy_day.in");

  
  