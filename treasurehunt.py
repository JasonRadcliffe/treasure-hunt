#This is a shared programming exercise developed by the students of BFA Computer Club
#March 2022

print ("Treasure Hunt Python Program\n\nThe main commands are \"walk [direction]\", \"pick up\", \"use\", and \"exit\"")

print ("Welcome, explorer. You find yourself in the basement of an ancient and spooky looking castle.	")
print ("The room you are in has thick red carpet, and 4 doors, one on each wall")
print ("You are approached by an elderly man in a suit who asks:\n\n")
print("I am waiting to pass along instructions to one who is worthy.\nWhat is your first name, explorer?")

name = input(":")

approvedNamesList = ["Jason", "Andrew", "Tom", "Flintlock", "Ian"]
approved = False

for testName in approvedNamesList:
	if testName == name:
		approved = True
		print("The old man silently hands you a safety deposit box and vanishes. Inside you find a letter with this text:")
		print("Not all who wander are lost, but you should definitely not wander North.")
		print("You open the letter and find a small key inside")
		small_key = 0

if approved == False:
	print("The old man simply vanishes without saying anything. Hmm...")

stillPlaying = True

while stillPlaying == True:
	print("What do you do next?")
	nextCommand = input(":")

	if nextCommand == "walk North":
		print("you walk through the door to the North")
		print("You find yourself in a long, dark hallway.")
		print("There is no sound, and as you go father along the darker it becomes.")
		print("Should you walk foward or walk back?")
		nasnwer = input(":")
		if nasnwer == "walk forward":
			print("You continue further into the darkness, unafraid of what might lurk in the shadows.")
			
		elif nasnwer == "walk back":
			print("You walk back to the starting room.")
			break

	elif nextCommand == "walk East":
		print("you walk through the door to the East")
		#
		#ENTER CODE HERE
		#
	
	elif nextCommand == "walk South":
		print("you walk through the door to the South")
		#
		#ENTER CODE HERE
		#
	
	elif nextCommand == "walk West":
		print("you walk through the door to the West")
		#
		#ENTER CODE HERE
		#

	elif nextCommand == "exit":
		stillPlaying = False
		break


	print("You hear a loud \"POP!\" and to your surprise you find yourself back in the original room.") 



