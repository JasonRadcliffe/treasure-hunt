#This is a shared programming exercise developed by the students of BFA Computer Club
#March 2022

print ("Treasure Hunt Python Program\n\nThe main commands are \"walk [direction]\", \"pick up\", \"use\", and \"exit\"")

print ("Welcome, explorer. You find yourself in the basement of an ancient and spooky looking castle.	")
print ("The room you are in has thick red carpet, and 4 doors, one on each wall")
print ("You are approached by an elderly man in a suit who asks:\n\n")
print("I am waiting to pass along instructions to one who is worthy.\nWhat is your first name, explorer?")

name = input(":")
Position = [ 2 , 2]


room = [[[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0]],
        [[0],[0],[0],[0],[0]]]




room[0][0][0] = ""
room[0][1][0] = ""
room[0][2][0] = ""
room[0][3][0] = ""
room[0][4][0] = ""
room[1][0][0] = ""
room[1][1][0] = ""
room[1][2][0] = ""
room[1][3][0] = ""
room[1][4][0] = ""
room[2][0][0] = ""
room[2][1][0] = """You open the door and step out onto a small rocky platform. You notice much too late that the entire area,
other than the place you are now standing, is covered in boiling lava. You turn back, only to have the door into the original room vanish
before your very eyes. The lava rises, and you roast alive."""
room[2][2][0] = "You find yourself back in the laviously decoration room you began in. The same doors are available to you: North, South, East, and West" 
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


def Walk_North(): 
	Position[1] += 1

	#	print("your current position is:" + str(Position[0]) + "," + str(Position[1]))
	#	Walk_North() 
	#	print("your current position is:" + str(Position[0]) + "," + str(Position[1]))

def Walk_South(): 
	Position[1] -= 1

def Walk_East(): 
	Position[0] += 1

def Walk_West(): 
	Position[0] -= 1


def death():
        Position = [2,2]
        print(Position)

        

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
		Walk_North()
		print("you walk through the door to the North")
	elif nextCommand == "walk east":
		Walk_East()
		print("you walk through the door to the East")
		#
		#ENTER CODE HERE
		#
	
	elif nextCommand == "walk south":
		Walk_South()
		print("you walk through the door to the South")
		#
		#ENTER CODE HERE
		#
	
	elif nextCommand == "walk west":
		Walk_West()
		print("you walk through the door to the West")
		#
		#ENTER CODE HERE
		#

	elif nextCommand == "exit":
		stillPlaying = False
		break
	
	if Position[0] == 2 and Position[1] == 3:
                print(room[2][1][0])
                death()






