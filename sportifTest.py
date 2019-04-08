import sportif

#Define exceptions
class WeightError(Exception): pass
class TooLarge(Exception): pass
class NotIntegerError(Exception): pass
class InvalidSizeError(Exception): pass

class Athlete :
	def __init__(self,weight):
		
		if weight <= 0 :
			raise WeightError
			
		if weight > 200 :
			raise TooLarge
			
		self.__weight = weight

class Wife (Athlete) :
	def __init__(self, size, sport, name):
		
		if type(size) != int :
			raise NotIntegerError
	
		if size<0 :
			raise InvalidSizeError
		
			
		self.size = size 
		self.sport = sport 
		self.name = name
		

	def getSports(self):
		print("Miss.",self.name,"makes", self.sport)

	def getSize(self):
		print(self.name,"mesures", self.size, "meter")

class Male (Athlete) :
	def __init__(self,size,sport,age):
		
		self.size = size
		self.sport = sport
		self.age = age

	def add_one(self):
		self.age += 1 

	def getSize(self):
		print(self.name,"mesures", self.size, "meter")

	def his_age(self):
		self.add_one()
		print("Il a",self.age,"ans")
			


if __name__ == '__main__':
	Sport1 = Wife(1.76,"Rugby","Jor")
	Sport2 = Male(2.54, "Basket", 23)
	Sport1.getSports()
	Sport1.getSize()
	Sport2.his_age()

