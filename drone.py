from math import abs,sqrt

class Drone:

    # Drone.weight
    # Drone.number
    # static
    
    def __init__ (self,manager,position):
        
        self.manager = manager
        self.products = {}
        self.load = 0
        self.position = position
        self.currentCommand = ["wait",params]
        self.currentOrder = [None,0]
        self.historique = []
        self.currentStep = 0

    def load(self,warehouse,productType,qty):
        items = warehouse.unload(productType,qty)
        if not productType.getId() in self.products:
            self.products[productType.getId()] = items
        else:
            self.products[productType.getId()] += items

    def unload(self,warehouse,productType,qty):
        warehouse.load(productType,qty)
        self.products[productType.getId()] -= qty

    def deliver(self,position,productType,qty):
        if self.position == position:
            return True
        else:
            if self.currentStep == 0:
                self.getCoord()
            self.go(position)

    def getCoord(self,position):
        x,y = position
        dx,dy = self.position
        dist = sqrt( abs(x - dx)**2  + abs(y - dy)**2 )
        if dist%int(dist) > 0:
            dist = int(dist) + 1
        self.currentStep = dist

    def go(self,position):
        if self.currentStep:
            self.currentStep -= 1
        
        if self.currentStep == 0:
            self.position = position

    def move(self,maison):
        self.position = position

#    def addOrders(self,orders):
#        self.orders.extend(orders)

    def run(self):
        res = False
        if self.currentCommand != "wait"
            res = eval("self."+self.currentCommand[0]+"("+self.currentCommand[1]+")")
        return res

    def isIn(self,position):

        #
        return self in cellule.drones

    def idle(self,warehouse):
        items = warehouse.check(self.currentOrder[0])
        if items < self.currentOrder[1]:
            self.load(warehouse,self.currentOrder[0],self.currentOrder[1])
            return True
        return False

    def setCommand(self,task,params):

        # a voir
        self.currentCommand[0] = task
        self.currentCommand[1] = "("
        for i in params
        :
            self.currentCommand[1] += params+","
        self.currentCommand[1] = self.currentCommand[1][:-1] + ")"

    def getHistory(self):
        return self.historique