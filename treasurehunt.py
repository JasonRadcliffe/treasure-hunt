#This is a shared programming exercise developed by the students of BFA Computer Club
#March 2022

print ("Treasure Hunt Python Program\n\nThe main commands are \"walk [direction]\", \"pick up\", \"use\", and \"exit\"")

print ("Welcome, explorer. You find yourself in the basement of an ancient and spooky looking castle.	")
print ("The room you are in has thick red carpet, and 4 doors, one on each wall")
print ("You are approached by an elderly man in a suit who asks:\n\n")
print("I am waiting to pass along instructions to one who is worthy.\nWhat is your first name, explorer?")

name = input(":")
Position = [ 2 , 2]

Room = [[room1,1][room4][room7]
        [room2,2][room5][room8]
        [room3,3][room6][room9]

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

	if nextCommand == "walk North":
		Walk_North()
		print("you walk through the door to the North")
	elif nextCommand == "walk East":
		Walk_East()
		print("you walk through the door to the East")
		#
		#ENTER CODE HERE
		#
	
	elif nextCommand == "walk South":
		Walk_South()
		print("you walk through the door to the South")
		#
		#ENTER CODE HERE
		#
	
	elif nextCommand == "walk West":
		Walk_West()
		print("you walk through the door to the West")
		#
		#ENTER CODE HERE
		#

	elif nextCommand == "exit":
		stillPlaying = False
		break
	
	if Position[0] == 2 and Position[1] == 3:
                print("The area you walk into is densly wooded,\nsounds of animals surrounding you as you try to find your bearings in the wood.")
                print("You reach the center of the square, a small clearing with a stream running through it, the sun barely reaching it through the leaves.")






