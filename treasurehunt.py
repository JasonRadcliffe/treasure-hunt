#This is a shared programming exercise developed by the students of BFA Computer Club
#March 2022

print ("Treasure Hunt Python Program\n\nThe main commands are \"walk [direction]\", \"pick up\", \"use\", \"map\", and \"exit\"")

print ("Welcome, explorer. You find yourself in the basement of an ancient and spooky looking castle.	")
print ("The room you are in has thick red carpet, and 4 doors, one on each wall")
print ("You are approached by an elderly man in a suit who asks:\n\n")
print("I am waiting to pass along instructions to one who is worthy.\nWhat is your first name, explorer?")

name = input(":")
Position = [ 2 , 2]
cwtw = 0


room = [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]]


#descriptions of rooms
room[0][0][0] = ""
room[0][1][0] = ""
room[0][2][0] = ""
room[0][3][0] = ""
room[0][4][0] = ""
room[1][0][0] = ""
room[1][1][0] = ""
room[1][2][0] = """You open the door to find a magnificent courtyard, the walls decorated with banners of red and gold. Walking to the center, you find only one door beyond,
leading to the West."""
room[1][3][0] = ""
room[1][4][0] = ""
room[2][0][0] = ""
room[2][1][0] = """You open the door and step out onto a small rocky platform. You notice much too late that the entire area,
other than the place you are now standing, is covered in boiling lava. You turn back, only to have the door into the original room vanish
before your very eyes. The lava rises, and you roast alive."""
room[2][2][0] = "You find yourself back in the laviously decorated room you began in. The same doors are available to you: North, South, East, and West" 
room[2][3][0] = ""
room[2][4][0] = ""
room[3][0][0] = ""
room[3][1][0] = ""
room[3][2][0] = ""
room[3][3][0] = ""
room[3][4][0] = ""
room[4][0][0] = ""
room[4][1][0] = ""
room[4][2][0] = ""
room[4][3][0] = ""
room[4][4][0] = ""

#whether/not you can walk through certain doors
# 1 = North, 2 = East 3 = South 4 = West
room[0][0][1] = 0
room[0][0][2] = 1
room[0][0][3] = 1
room[0][0][4] = 0
room[0][1][1] = 1
room[0][1][2] = 0
room[0][1][3] = 1
room[0][1][4] = 0
room[0][2][1] = 1
room[0][2][2] = 1
room[0][2][3] = 1
room[0][2][4] = 0
room[0][3][1] = 1
room[0][3][2] = 1
room[0][3][3] = 0
room[0][3][4] = 0
room[0][4][1] = 0
room[0][4][2] = 1
room[0][4][3] = 0
room[0][4][4] = 0
room[1][0][1] = 0
room[1][0][2] = 0
room[1][0][3] = 0
room[1][0][4] = 1
room[1][1][1] = 0
room[1][1][2] = 0
room[1][1][3] = 0
room[1][1][4] = 0
room[1][2][1] = 0
room[1][2][2] = 1
room[1][2][3] = 0
room[1][2][4] = 1
room[1][3][1] = 0
room[1][3][2] = 0
room[1][3][3] = 0
room[1][3][4] = 1
room[1][4][1] = 0
room[1][4][2] = 1
room[1][4][3] = 0
room[1][4][4] = 1
room[2][0][1] = 0
room[2][0][2] = 1
room[2][0][3] = 0
room[2][0][4] = 0
room[2][1][1] = 0
room[2][1][2] = 0
room[2][1][3] = 1
room[2][1][4] = 0
room[2][2][1] = 1
room[2][2][2] = 1
room[2][2][3] = 1
room[2][2][4] = 1
room[2][3][1] = 1
room[2][3][2] = 1
room[2][3][3] = 1
room[2][3][4] = 0
room[2][4][1] = 1
room[2][4][2] = 0
room[2][4][3] = 0
room[2][4][4] = 1
room[3][0][1] = 0
room[3][0][2] = 1
room[3][0][3] = 1
room[3][0][4] = 1
room[3][1][1] = 1
room[3][1][2] = 0
room[3][1][3] = 1
room[3][1][4] = 0
room[3][2][1] = 1
room[3][2][2] = 1
room[3][2][3] = 1
room[3][2][4] = 1
room[3][3][1] = 1
room[3][3][2] = 1
room[3][3][3] = 1
room[3][3][4] = 1
room[3][4][1] = 1
room[3][4][2] = 1
room[3][4][3] = 0
room[3][4][4] = 0
room[4][0][1] = 0
room[4][0][2] = 0
room[4][0][3] = 0
room[4][0][4] = 1
room[4][1][1] = 0
room[4][1][2] = 0
room[4][1][3] = 1
room[4][1][4] = 0
room[4][2][1] = 1
room[4][2][2] = 0
room[4][2][3] = 0
room[4][2][4] = 1
room[4][3][1] = 0
room[4][3][2] = 0
room[4][3][3] = 0
room[4][3][4] = 1
room[4][4][1] = 0
room[4][4][2] = 0
room[4][4][3] = 0
room[4][4][4] = 1

def Walk_North(): 
	Position[1] -= 1

def Walk_South(): 
	Position[1] += 1

def Walk_East(): 
	Position[0] += 1

def Walk_West(): 
	Position[0] -= 1


def death():
	Position[0] = 2
	Position[1] = 2

        

approvedNamesList = ["Jason", "Andrew", "Tom", "Flintlock", "Ian" , "Human"]
approved = False

for testName in approvedNamesList:
	if testName == name:
		approved = True
		print("The old man silently hands you a safety deposit box and vanishes. Inside you find a letter with this text:")
		print("Not all who wander are lost, but you should definitely not wander North.")

if approved == False:
	print("The old man simply vanishes without saying anything. Hmm...")

stillPlaying = True

while stillPlaying == True:
	print("What do you do next?")
	nextCommand = input(":")
	nextCommand = nextCommand.lower()
	if nextCommand == "walk north":
		if room[Position[0]][Position[1]][1] == 1:
			Walk_North()
			print("You walk through the door to the North")
		else:
			print("You cannot walk that way")
			cwtw = 1

	elif nextCommand == "walk east":
		if room[(Position[0])][Position[1]][2] == 1:
			Walk_East()
			print("You walk through the door to the East")
		else:
			print("You cannot walk that way")
			cwtw = 1

	elif nextCommand == "walk south":
		if room[(Position[0])][Position[1]][3] == 1:
			Walk_South()
			print("You walk through the door to the South")
		else:
			print("You cannot walk that way")
			cwtw = 1

	elif nextCommand == "walk west":
		if room[(Position[0])][Position[1]][4] == 1:
			Walk_West()
			print("You walk through the door to the West")
		else:
			print("You cannot walk that way")
			cwtw = 1

	elif nextCommand == "exit":
		stillPlaying = False
		break
	elif nextCommand == "map":
		print("You are at position " + str(Position[0]) + "," + str(Position[1]))
	elif nextCommand == "return":
		Position = [2,2]
	else:
		print("Sorry, please repeat")
	if cwtw == 0:
		if Position[0] == 2 and Position[1] == 1:
			print(room[2][1][0])
			death()
		else:
			print(room[Position[0]][Position[1]][0])
	cwtw = 0






