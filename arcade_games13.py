class Character():
	name = "Link"
	sex = "Male"
	max_hit_points = 50
	current_hit_points = 50
	max_speed = 10
	armor_amount = 8

class Address():
	name = ""
	line1 = ""
	line2 = ""
	city = ""
	state = ""
	zip = ""

# create an address
homeAddress = Address()

# set the fields in the address
homeAddress.name = "John Smith"
homeAddress.line1 = "701 N. C Street"
homeAddress.line2 = "Carver Science Building"
homeAddress.city = "Indiana"
homeAddress.state = "IA"
homeAddress.zip = "20125"

#Create another address
vacationHomeAddress = Address()

#Set the fields in the address
vacationHomeAddress.name = "John Smith"
vacationHomeAddress.line1 = "1122 Main Street"
vacationHomeAddress.line2 = ""
vacationHomeAddress.city = "Santa Fe"
vacationHomeAddress.zip = "01824"

print("The client's main home is in " + homeAddress.city)
print("His home is in " + vacationHomeAddress.city + " " + vacationHomeAddress.zip)

# print and address to the screen
def printAddress(address):
	print(address.name)
	# if there is a line1 in the address, print it
	if(len(address.line1) > 0):
		print(address.line1)
# print line 2 
	if(len(address.line2) > 0):
		print(address.line2)
	print(address.city+", "+address.state+" "+address.zip)

printAddress(homeAddress)
printAddress(vacationHomeAddress)

class Dog():
	age = 0
	name = ""
	weight = 0

	def bark(self):
		print("Woof")

myDog = Dog()

myDog.name = "Chevy"
myDog.weight = 76
myDog.age = 3

myDog.bark()

class Person:
	name = ""
	money = 0

bob = Person()
bob.name = "Bob"
bob.money = 100

nancy = bob
nancy.name = "Nancy"


print(bob.name, "has", bob.money, "dollars.")
print(nancy.name, "has", nancy.money, "dollars.")

def giveMoney2(person):
	person.money += 100

giveMoney2(bob)
print(bob.money)
print(nancy.name)

def giveMoney1(money):
	money += 100

class Person:
	name = ""
	money = 0

bob = nancy
bob.name = "Bob"
bob.money = 100

giveMoney1(bob.money)
print(bob.money)

class Dog():
	name = ""
	
	#Constructor called when creating an object of this type
	def __init__(self):
		print("A new dog is born!")
#this creates the dog
myDog = Dog()
Chevy = Dog()

class NamedDog():
	name = ""
	def __init__(self, newName):
		self.name = newName

#This creates the dog
Blackjack = NamedDog("Blackjack")

#print name to verfiy it was set
print(Blackjack.name)

class Boat():
	tonnage = 0
	name = ""
	isDocked = True

	def dock(self):
		if self.isDocked:
			print("You are already docked.")
		else:
			self.isDocked = True
			print("Docking")

	def undock(self):
		if not self.isDocked:
			print("You aren't docked.")
		else:
			self.isDocked = False
			print("Undocking")

