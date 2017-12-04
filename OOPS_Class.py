# Class Decleration

class Home:	
	RoomNo = 19

# Method Decleration

	def __init__(self, Name, Role):				
		#super($Home, self).__init__()
		self.Name = Name
		self.Role = Role


# Object Declreation

Nag = Home("Nagarjuna", "Husband")				
shruthi = Home("shruthi", "Wife")

# Accession the Home calss

print(Nag.Name)
print(shruthi.Name)
print(Home.RoomNo)

		