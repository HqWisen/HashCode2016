class Drone:

	# Drone.load
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
		items = warehouse.unload(productType,quantity)
		if not productType in self.products:
			self.products[productType] = items
		else:
			self.products[productType] += items

	def unload(self,warehouse,productType,qty):
		items = warehouse.load(productType,quantity)
		
			
	def move(self,cellule):
		self.position = position

	def addOrders(self,orders):
		self.orders.extend(orders)

	def wait():
		pass

	def run():
		eval("self."+self.currentCommand[0]+self.currentCommand[1])

	def isIn(self,cellule):
		return self in cellule.drones

	def idle(self,warehouse):
		# wait
		items = warehouse.check(productType)
		if items < self.currentOrder:
			self.load(warehouse,self.currentOrder[0],self.currentOrder[1])