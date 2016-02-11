class Drone:

    # Drone.weight
    # Drone.number
    # static
    
    def __init__ (self,manager,products,load,grid,cellule):
        
        self.manager = manager
        self.products = {}
        self.grid = grid
        self.weight = 0
        self.position = cellule
        self.currentCommand = ["wait","()"]
        self.currentOrder = [None,0]

    def load(self,warehouse,productType,qty):
        items = warehouse.unload(productType,qty)
        if not productType.getId() in self.products:
            self.products[productType.getId()] = items
        else:
            self.products[productType.getId()] += items

    def unload(self,warehouse,productType,qty):
        warehouse.load(productType,qty)
        self.products[productType.getId()] -= qty

    def deliver(self,warehouse,productType,qty):

    def go(self,cellule):
        

    def move(self,maison):
        self.position = position

    def addOrders(self,orders):
        self.orders.extend(orders)

    def wait():
        pass

    def run():
        res = eval("self."+self.currentCommand[0]+self.currentCommand[1])
        return res

    def isIn(self,cellule):
        return self in cellule.drones

    def idle(self,warehouse):
        self.wait()
        items = warehouse.check(self.currentOrder[0])
        if items < self.currentOrder[1]:
            self.load(warehouse,self.currentOrder[0],self.currentOrder[1])
            return True
        return False

    def setCommand(self,task,params):

        # a voir
        self.currentCommand[0] = task
        self.currentCommand[1] = "("
        for i in params:
            self.currentCommand[1] += params+","
        self.currentCommand[1] = self.currentCommand[1][:-1] + ")"
>>>>>>> 65d7870f3e9bc3f79564b3bd758fde938b854198