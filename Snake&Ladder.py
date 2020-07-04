import pprint
import random
import time

class my_dictionary(dict):

	def __init__(self):
		self = dict()

	def add(self, key, value):
		self[key] = value

board = [	100, 99, 98, 97, 96, 95, 94, 93, 92, 91,
			81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
			80, 79, 78, 77, 76, 75, 74, 73, 72, 71,
			61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
			60, 59, 58, 57, 56, 55, 54, 53, 52, 51,
			41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
			40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
			21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
			20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
			1, 2, 3, 4, 5, 6, 7, 8, 9, 10
		]
	
dice = ( 1, 2, 3, 4, 5, 6 )
player1 = input( "Enter name of player1 " )
player2 = input( "Enter name of player2 " )



player1Pos = int(0)
player2Pos = int(0)

snake = my_dictionary()

count = 0
while(count != 5):
	start = random.choice(board)
	end = random.choice(board)
	if start > end and start != 100:
		if start not in snake.keys() and start not in snake.values():
			if end not in snake.keys() and end not in snake.keys():
				snake.add(start, end)
				count = count + 1

print( "These are the starting position of snakes generated and where they will end" )
print( snake )
time.sleep(5)
print()

ladder = my_dictionary()

count = 0
while(count != 5):
	start = (random.choice(board))
	end = random.choice(board)
	if start < end and end != 100:
		if start not in snake.keys() and start not in snake.values():
			if end not in snake.keys() and end not in snake.values():
				if start not in ladder.keys() and start not in ladder.values():
					if end not in ladder.keys() and ladder not in ladder.values():
						ladder.add(start, end)
						count = count + 1
		


print( "These are the starting position of ladders generated and where they will end" )
print( ladder )
time.sleep(5)
print()
count = random.randint(1, 2)

try:
	ch = int(input("Press 1 for Auto Completion otherwise press any key to watch moves of every step "))
except ValueError:
	ch = int(2)

print()
time.sleep(2)
if( ch == 1 ):

	while player1Pos != 100 and player2Pos != 100:
		x = int(random.choice(dice))
		if count == 1:
			print( "Number occurred on dice "+str(x) )
			if player1Pos + x <= 100:
				player1Pos = player1Pos + x
				print( str(player1)+ " moves by " +str(x)+ " blocks" )
				if snake.get(player1Pos) != None:
					print( "Oh no!!! "+player1+ " found a snake!!! at position "+str(player1Pos)+" ....Moving down" )
					player1Pos = snake.get(player1Pos)
				elif ladder.get(player1Pos) != None:
					print( "Hurray!!! "+player1+ " found a ladder!!! at position "+str(player1Pos)+" ...Moving up" )
					player1Pos = ladder.get(player1Pos)
			else:
				print( "Position of " +player1+ " exceed 100... therefore not moving" )
			count = 2
		
			print( "Current Position of " +str(player1)+ " is " +str(player1Pos) )
			print( "Current Position of " +str(player2)+ " is " +str(player2Pos) )
			print()

		elif count == 2:
			print( "Number occurred on dice "+str(x) )
			if player2Pos + x <= 100:
				player2Pos = player2Pos + x
				print( str(player2)+ " moves by " + str(x)+ " blocks")
				if snake.get(player2Pos) != None:
					print("Oh no!!! "+player2+ " found a snake!!! at position "+str(player2Pos)+" ....Moving down")
					player2Pos = snake.get(player2Pos)
				elif ladder.get(player2Pos) != None:
					print("Hurray!!! "+player2+ " found a ladder!!! at position "+str(player2Pos)+" ...Moving up")
					player2Pos = ladder.get(player2Pos)
			else:
				print("Position of " +player2+ " exceed 100... therefore not moving")
			count = 1
			print("Current Position of " +str(player1)+ " is " +str(player1Pos) )
			print("Current Position of " +str(player2)+ " is " +str(player2Pos) )
			print()



else: 
	while player1Pos != 100 and player2Pos != 100:
		x = int(random.choice(dice))
		if count == 1:
			input( player1+ " Press Enter to roll the dice" ) 
			print( "Number occurred on dice "+str(x) )
			if player1Pos + x <= 100:
				player1Pos = player1Pos + x
				print( str(player1)+ " moves by " +str(x)+ " blocks" )
				if snake.get(player1Pos) != None:
					print( "Oh no!!! "+player1+ " found a snake!!! at position "+str(player1Pos)+" ....Moving down" )
					player1Pos = snake.get(player1Pos)
				elif ladder.get(player1Pos) != None:
					print( "Hurray!!! "+player1+ " found a ladder!!! at position "+str(player1Pos)+" ...Moving up" )
					player1Pos = ladder.get(player1Pos)
			else:
				print( "Position of " +player1+ " exceed 100... therefore not moving" )
			count = 2
		
			print( "Current Position of " +str(player1)+ " is " +str(player1Pos) )
			print( "Current Position of " +str(player2)+ " is " +str(player2Pos) )
			print()

		elif count == 2:
			input( player2+ " Press Enter to roll the dice" ) 
			print( "Number occurred on dice "+str(x) )
			if player2Pos + x <= 100:
				player2Pos = player2Pos + x
				print( str(player2)+ " moves by " + str(x)+ " blocks")
				if snake.get(player2Pos) != None:
					print("Oh no!!! "+player2+ " found a snake!!! at position "+str(player2Pos)+" ....Moving down")
					player2Pos = snake.get(player2Pos)
				elif ladder.get(player2Pos) != None:
					print("Hurray!!! "+player2+ " found a ladder!!! at position "+str(player2Pos)+" ...Moving up")
					player2Pos = ladder.get(player2Pos)
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
 
