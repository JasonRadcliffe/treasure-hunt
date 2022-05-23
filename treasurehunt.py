#This is a shared programming exercise developed by the students of BFA Computer Club
#March 2022

print ("Treasure Hunt Python Program\n\nThe main commands are \"walk [direction]\", \"pick up\", \"use\", \"map\", \"repeat\" and \"exit\"")

print ("Welcome, explorer. You find yourself in the basement of an ancient and spooky looking castle.	")
print ("The room you are in has thick red carpet, and 4 doors, one on each wall")
print ("You are approached by an elderly man in a suit who asks:\n\n")
print("I am waiting to pass along instructions to one who is worthy.\nWhat is your first name, explorer?")

import random
import time
random.seed(time.time())

name = input(":")
Position = [ 2 , 2]
cwtw = 0
d = 0
tie = 1


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
room[1][1][0] = """You escape the confines of flesh and step into an infinite void of black. Two eyes open slowly, quizzically. \"How did you get here…\" It asks, a rotten stench pooling from its mouth. 
\"No matter, you appear like a good snack!\" Savage teeth rip you apart. 
We don't like cheaters here """
room[1][2][0] = """You step out onto the wall of a castle, the wind howling like a madman. However, the temperature's not too bad
There doesn't seem to be a way off except for directly West and East"""
room[1][3][0] = ""
room[1][4][0] = ""
room[2][0][0] = ""
room[2][1][0] = """You open the door and step out onto a small rocky platform. You notice much too late that the entire area,
other than the place you are now standing, is covered in boiling lava. You turn back, only to have the door into the original room vanish
before your very eyes. The lava rises, and you roast alive."""
room[2][2][0] = "You find yourself back in the laviously decorated room you began in. The same doors are available to you: North, South, East, and West" 
room[2][3][0] = ""
room[2][4][0] = ""
room[3][0][0] = """You come upon a gigantic figure sitting in the center of the path, hands upon his knees in a pose as if he were waiting for you. 
Joints creak as he turns his head to look at you, caked mud and grime falling off him in clumps. 
His voice sounds as if mountains could speak, \"Hello young traveller. I suppose you are here to get the key I keep over yonder \" He waves off to the East.
\"However, due to protocol and the such, I cannot simply allow you to have it. Let's play a game of roshambo to see if you may escape, shall we? I haven't seen another living soul in ages.\" 
The game is simple. When prompted, provide an answer of rock, paper, or scissors. Paper beats rock, rock beats scissors, and scissors beats paper
\"If you win, you may recieve the key. If you lose, you do not.\""""
room[3][1][0] = ""
room[3][2][0] = """It's a hallway, but even so it is yet another magnificent feature of wherever you are. The carpet is luscious and thick, the chandeliers huge and well-lit, and magnificent paintings line the walls. You casually wonder who or what lived in this place, and where they went.
There are another four doors in here, but the Eastern door seems to lead to stairs, while the Northern has scratches of dirt and grass on the carpet in front of it."""
room[3][3][0] = ""
room[3][4][0] = ""
room[4][0][0] = "You walk to the shed "
room[4][1][0] = """Walking through the doorway, you are startled to find yourself atop a high tower, looking down at a series of courtyards below.
To the North-East you can see a giant figure sitting in one of them seemingly guarding a small storage shed directly to your North, likely used for housing keys.
There is no other exit off of the tower other than the way you came."""
room[4][2][0] = """You pause at this landing, out of breath after climbing so many flights of stairs.
There is a small window, out of which you can see a dense green forest. Jagged mountains box the whole view in, white peaks touching the scattered cloud.
You read a small inscription below the window: \"We love to look at that which we cannot have\" 
The stairs continue upwards to the North and down to the East."""
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

def Battle():
	outcome = 0
	play = input("Enter your selection:")
	play = play.lower()
	if play == "rock":
		best = 1
	elif play == "scissors":
		best = 2
	elif play == "paper":
		best = 3

	other = random.randint(1,3)
	if best == 1 and other == 2:
		outcome = 1
	elif best == 1 and other == 1:
		outcome = 2
	elif best == 1 and other == 3:
		outcome = 0
	elif best == 2 and other == 2:
		outcome = 2
	elif best == 2 and other == 1:
		outcome = 0
	elif best == 2 and other == 3:
		outcome = 1
	elif best == 3 and other == 1:
		outcome = 1
	elif best == 3 and other == 2:
		outcome = 0
	elif best == 3 and other == 3:
		outcome = 2
	return outcome








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
		cwtw = 1
	elif nextCommand == "return":
		Position = [2,2]
	elif nextCommand == "tp":
		x = input("x:")
		y = input("y:")
		Position[0] = int(x)
		Position[1] = int(y)
	elif nextCommand == "repeat":
		d += 1
	elif nextCommand == "battle":
		bob = Battle()
		print(bob)
	else:
		print("Sorry, please repeat")
		cwtw = 1
	if cwtw == 0:
		if Position[0] == 2 and Position[1] == 1:
			print(room[2][1][0])
			death()
		if Position[0] == 1 and Position[1] == 1:
			print(room[Position[0]][Position[1]][0])
			death()
		if Position[0] == 3 and Position[1] == 0:
			if tie == 1:
				print(room[Position[0]][Position[1]][0])
			else:
				print("The giant looks fondly down upon you and wishes you good luck on your journey")
			while tie == 1:
				match1 = Battle()
				if match1 == 1:
					print("The giant looks surprised, but not too hurt. He smiles and allows you to move along your way to the small shed to his East")
					tie = 0
					Position[0] = 4
					Position[1] = 0
				if match1 == 0:
					print("The giant looks rather sad, but not surprised. He gives you the grandest of condolences, and then crushes you under his fist.")
					tie = 0
					death()
				if match1 == 2:
					print("You tie, and the giant asks for another go.")
					tie = 1
		if Position[0] == 4 and Position[1] == 0:
			print(room[4][0][0])
			key1 = 1

		else:
			print(room[Position[0]][Position[1]][0])
			print("bob")


	cwtw = 0





