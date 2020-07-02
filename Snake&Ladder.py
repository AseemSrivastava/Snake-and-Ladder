import pprint
import random



board = [	[100, 99, 98, 97, 96, 95, 94, 93, 92, 91],
			[81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
			[80, 79, 78, 77, 76, 75, 74, 73, 72, 71],
			[61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
			[60, 59, 58, 57, 56, 55, 54, 53, 52, 51],
			[41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
			[40, 39, 38, 37, 36, 35, 34, 33, 32, 31],
			[21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
			[20, 19, 18, 17, 16, 15, 14, 13, 12, 11],
			[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		]
dice = [1, 2, 3, 4, 5, 6]
player1 = input("Enter name of player1 ")
player2 = input("Enter name of player2 ")

player1Pos = int(0)
player2Pos = int(0)

count = random.randint(1, 2)

while player1Pos != 100 and player2Pos != 100:
	x = int(random.choice(dice))
	if count == 1:
		if player1Pos + x <= 100:
			player1Pos = player1Pos + x
			print( str(player1)+ " moves by " +str(x)+ " blocks")
		else:
			print("Position of " +player1+ " exceed 100... therefore not moving")
		count = 2
		print("Current Position of " +str(player1)+ " is " +str(player1Pos) )
		print("Current Position of " +str(player2)+ " is " +str(player2Pos) )
		print()

	elif count == 2:
		if player2Pos + x <= 100:
			player2Pos = player2Pos + x
			print( str(player2)+ " moves by " + str(x)+ " blocks")
		else:
			print("Position of " +player2+ " exceed 100... therefore not moving")
		count = 1
		print("Current Position of " +str(player1)+ " is " +str(player1Pos) )
		print("Current Position of " +str(player2)+ " is " +str(player2Pos) )
		print()

if player1Pos == 100:
	print(player1 + " wins")

elif player2Pos == 100:
	print(player2 + " wins")
 
