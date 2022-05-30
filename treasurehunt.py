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
tie2 = 1
key1 = 0
key2 = 0
whine = 0

room = [[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]]


#descriptions of rooms
room[0][0][0] = "This part of the castle seems more run down than the other parts you\'ve seen. Long scratches run down the walls and the brickwork seems patchy in some places, leading to gusts of wind coming through.\nThere is a off-white door to your east and a door to your south."
room[0][1][0] = "This hallway is lined with pictures of great Lords of the castle, starting with the great \'Lord Rutherford\' and ending with the obviously inbred \'Lord Edwin\'"
room[0][2][0] = "Yet another part of the wall, but this part has an entrance into the castle to the North and more wall to the South."
room[0][3][0] = "You stand upon the wall, and you feel something watching you. The wind ruffles your hair and you feel what could be long fingers run across your scalp. There is a small stairway to the east that seems to call to you..."
room[0][4][0] = "You didn't heed the writing on the wall and now you appear to be paying the price. You slip on a slime-coated stair and fall down the rest of the way, landing in a pit of man-eating slugs. The last thing you feel is the slugs chewing on your eyeballs as you are covered in their mucus."
room[1][0][0] = """You come to a room with cushioned walls, ripped in places where it appears someone tried to tear out. A skeleton lies in the center and you walk towards it until you see it has a key around its neck.
You grab the key and note that the skeleton does not appear to be strictly human."""
room[1][1][0] = """You escape the confines of flesh and step into an infinite void of black. Two eyes open slowly, quizzically. \"How did you get here…\" It asks, a rotten stench pooling from its mouth. 
\"No matter, you appear like a good snack!\" Savage teeth rip you apart. 
We don't like cheaters here """
room[1][2][0] = """You step out onto the wall of a castle, the wind howling like a madman. However, the temperature's not too bad
There doesn't seem to be a way off except for directly West and East"""
room[1][3][0] = "This is a test"
room[1][4][0] = "You descend into a drippy stone staircase, the steps coated with what looks like mucus and the walls covered in warnings. It looks like if you continue further down this dark deep staircase there may be dangerous consequences."
room[2][0][0] = ""
room[2][1][0] = """You open the door and step out onto a small rocky platform. You notice much too late that the entire area,
other than the place you are now standing, is covered in boiling lava. You turn back, only to have the door into the original room vanish
before your very eyes. The lava rises, and you roast alive."""
room[2][2][0] = "You find yourself back in the laviously decorated room you began in. The same doors are available to you: North, South, East, and West" 
room[2][3][0] = "You walk through the door and find yourself in a small room that appears to be more of a maintenance hallway than a grand entrance. There's a door to the east and south."
room[2][4][0] = """You find yourself on a seemingly endless stairway, one end going into the deepest dark of the west castle and the other leading up and to the north"""
room[3][0][0] = """You come upon a gigantic figure sitting in the center of the path, hands upon his knees in a pose as if he were waiting for you. 
Joints creak as he turns his head to look at you, caked mud and grime falling off him in clumps. 
His voice sounds as if mountains could speak, \"Hello young traveller. I suppose you are here to get the key I keep over yonder \" He waves off to the East.
\"However, due to protocol and the such, I cannot simply allow you to have it. Let's play a game of roshambo to see if you may escape, shall we? I haven't seen another living soul in ages.\" 
The game is simple. When prompted, provide an answer of rock, paper, or scissors. Paper beats rock, rock beats scissors, and scissors beats paper
\"If you win, you may recieve the key. If you lose, you do not.\""""
room[3][1][0] = "The door creaks open and you find yourself outside, with a path leading forward before you, flowers lining it. It seems like a garden that no one has tended for a while, as it runs wild and free all along the path."
room[3][2][0] = """It's a hallway, but even so it is yet another magnificent feature of wherever you are. The carpet is luscious and thick, the chandeliers huge and well-lit, and magnificent paintings line the walls. You casually wonder who or what lived in this place, and where they went.
There are another four doors in here, but the Eastern door seems to lead to stairs, while the Northern has scratches of dirt and grass on the carpet in front of it."""
room[3][3][0] = "The hallways here are tight, but you can still navigate them. There is a cast-iron door to your east that appears to have not been used for quite some time, and a darker hallway leading to the south."
room[3][4][0] = "It grows darker and darker as you walk down the hallway, but suddenly you enter upon a huge cavern, with long glowing vines hanging from the ceiling. Fireflies hum and propogate through the dark, liting up every corner. You spot a sparkle to the east, but the scenery is so pretty you might simply want to stay and admire it for a minute."
room[4][0][0] = "You walk to the shed and retrieve an old copper key off of a hook."
room[4][1][0] = """Walking through the doorway, you are startled to find yourself atop a high tower, looking down at a series of courtyards below.
To the North-East you can see a giant figure sitting in one of them seemingly guarding a small storage shed directly to your North, likely used for housing keys.
There is no other exit off of the tower other than the way you came."""
room[4][2][0] = """You pause at this landing, out of breath after climbing so many flights of stairs.
There is a small window, out of which you can see a dense green forest. Jagged mountains box the whole view in, white peaks touching the scattered cloud.
You read a small inscription below the window: \"We love to look at that which we cannot have\" 
The stairs continue upwards to the North and down to the East."""
room[4][3][0] = """You push the heavy metal door aside, eahring the creaks of rust and disuse screech against your hands. You stumble out onto a sandy pit, bones scattered in undiginified fashion throughout.
At the back of the pit is a huge beast, panting for the kill. Almost before you can react it leaps up and runs towards you, teeth bared. You grab up a sword still grasped by boney fingers and evade the first attack, but it simply loops back around, foam glistening.
Please enter rock, paper, or scissors to see if you can successfully kill the beast."""
room[4][4][0] = """You find a hidden alcove in the wall, hidden by some vines. Inside is a brilliant diamond key, which you take for later. """

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
	if whine == 1:
		key1 = 1
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
		elif Position[0] == 1 and Position[1] == 1:
			print(room[Position[0]][Position[1]][0])
			death()
		elif Position[0] == 3 and Position[1] == 0:
			if key1 == 0:
				print(room[Position[0]][Position[1]][0])
			else:
				print("The giant looks fondly down upon you and wishes you good luck on your journey")
			while tie == 1:
				match1 = Battle()
				if match1 == 1:
					print("The giant looks surprised, but not too hurt. He smiles and allows you to move along your way to the small shed to his East")
					tie = 0
					whine = 1
				elif match1 == 0:
					print("The giant looks rather sad, but not surprised. He gives you the grandest of condolences, and then crushes you under his fist.")
					tie = 1
					death()
					break
				elif match1 == 2:
					print("You tie, and the giant asks for another go.")
					tie = 1
		elif Position[0] == 4 and Position[1] == 0:
			print(room[4][0][0])
			key1 = 1
		elif Position[0] == 1 and Position[1] == 0:
			print(room[Position[0]][Position[1]][0])
			key2 = 1
		elif Position[0] == 4 and Position[1] == 3: 
			if tie2 == 1:
				print(room[Position[0]][Position[1]][0])
			else:
				print("The sandy pit is empty, except for the last vestiges of green blood left in the center of the room.")
			while tie2 == 1:
				match1 = Battle()
				if match1 == 1:
					print("The beast is vanquished. slide under it and slice it open, green blood spurting from the cut. You watch as it dissolves into the sand and throw the sowrd away as it does so too. You are now free to go.")
					tie2 = 0
				elif match1 == 0:
					print("The beast dodges your attack and comes in for the killing blow, biting your head clean off.")
					tie2 = 1
					death()
					break
				elif match1 == 2:
					print("You successfully block, but do not kill the beast, prompting it to come in for another attack.")
		elif Position[0] == 4 and Position[1] == 4:
			print(room[Position[0]][Position[1]][0])
			key3 = 1
		elif Position[0] == 0 and Position[1] == 4:
			print(room[Position[0]][Position[1]][0])
			death()
		elif Position[0] == 2 and Position[1] == 0:
			if key1 == 1 and key2 == 1 and key3 == 1:
				print("You put the keys into the keyholes and the gates slowly creak open and you finally escape the castle. As you walk away into the forest you take one last look at the castle you were stuck in, dominating teh skyline. It seems almost forlorn from the outside, nonthreatening. You shrug and go on your way, back home")
				stillPlaying = False
				break
			else:
				print("You come to two huge gates blocking your way. You can see the path into the forest past it, but you cannot budge the gates. You see three keyholes in the gate, most likely for three keys.")
				print("Good job" + name)
		else:
			print(room[Position[0]][Position[1]][0])
		

	cwtw = 0





