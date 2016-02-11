from carte import *
from productType import *
from warehouse import *
from delivery import *
from drone import *
from droneManager import *

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
    # Creation de la carte
    self.carte = Carte(rows, cols) 
    Drone.number = int(line[2])
    T = int(line[3])
    Drone.weight = int(line[4])
  
  def parseSecondSection(self):
    line = self.lines[1].split()
    ProductType.number = int(line[0])
    productWeightList = self.lines[2].split()
    productTypeList = []
    for i in range(ProductType.number):
      productTypeList.append(ProductType(i, productWeightList[i]))
    self.convertSeqToInt(productWeightList)
    Warehouse.number = int(self.lines[3])
    warehouseIndexLine = 2;
    warehouseList = []
    for i in range(Warehouse.number):
      warehouseIndexLine += 2
      position = self.lines[warehouseIndexLine].split()
      self.convertSeqToInt(position)
      productList = self.lines[warehouseIndexLine+1].split()
      self.convertSeqToInt(productList)
      warehouseList.append(Warehouse(position, productList))
      
    orderIndexLine = warehouseIndexLine + 2
    Delivery.number = int(self.lines[orderIndexLine])
    orderIndexLine = orderIndexLine - 2
    deliveryList = []
    for i in range(Delivery.number):
      orderIndexLine += 3
      deliveryPosition = self.lines[orderIndexLine].split()
      self.convertSeqToInt(deliveryPosition)
      numberOfProducts = int(self.lines[orderIndexLine+1])
      productTypeList = self.lines[orderIndexLine+2].split()
      self.convertSeqToInt(productTypeList)
      deliveryList.append(Delivery(deliveryPosition, productTypeList))
    
    for i in range(Warehouse.number):
      self.carte.setMaisonOn(warehouseList[i])
    for i in range(Delivery.number):
      self.carte.setMaisonOn(deliveryList[i]) 
    self.droneManager = DroneManager(self.carte, Drone.number, warehouseList, deliveryList, productList)
    
  def convertSeqToInt(self, L):
    for i in range(len(L)):
      L[i] = int(L[i]);

  def getDroneManager(self):
    return self.droneManager
      
if __name__ == "__main__":
  parser = Parser("mother_of_all_warehouses.in");
  droneManager = parser.getDroneManager()
  droneManager.process()
  