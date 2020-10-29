
class conexion :
	def __inint__ (self, origin, destiny, cost):
		self.origin = origin
		self.destiny = destiny
		self.cost = cost
		
	def show (self):
		print (self.origin, self.destiny, self.cost)



print ("uno")
luis = []
a = conexion()
a.__inint__ (0,1, 'a')
luis.append(a)
print ("perro")
a.show()
luis[0].show()


	
