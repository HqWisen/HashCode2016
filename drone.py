class Drone:
	def __init__ (self,products,load,grid,position):
		self.maxload = load
		self.weight = sum([i.weight() for i in range(products)])
		self.orders = [None]
		self.grid = grid
		self.position = position

	def load(self,warehouse):
		warehouse.load()

	def move(self,position):
		self.drone()

	def wait(self):


	def addOrders(self,orders):
		self.orders.extend(orders)

	def getNewpos(self,position):
		