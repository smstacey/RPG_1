import random

def displayInventory(inventory):
	counter = 0
	print("Inventory:")
	for i in inventory:
		counter += inventory[i]
		print(inventory[i], i)

	print("Total number of items:", counter)

def displayMap(grid):
	for i in grid:
		print(i)

def displayItem(xCoord, yCoord):
	item = "^"
	grid[yCoord][xCoord] = item

me = "$"
meX = 0	# must be [0, maxX)
meY = 3 # must be [0, maxY)

item = "^"
itemX = 0
itemY = 0

inventory = {}


# maxX and maxY are actually out of bounds, maxX - 1, maxY - 1 are the last possible indices of grid
minX = 0
minY = 0
maxX = 5
maxY = 5

grid = []

for i in range(maxY):
		grid.append([" "] * maxX)

grid[itemY][itemX] = item

while True:
	grid[meY][meX] = me
	displayInventory(inventory)

	displayMap(grid)

	move = str(input("Use your WASD keys to move: "))
	grid[meY][meX] = " "	# replaces the player with a blank spot so you don't have a trail of players on the grid

	if move.upper() == "W" and meY >= minY:
		if meY == minY:
			meY = maxY - 1
		else:
			meY -= 1
	elif move.upper() == "S" and meY <= maxY - 1:
		if meY == maxY - 1:
			meY = minY
		else:
			meY += 1
	elif move.upper() == "A" and meX >= minX:
		if meX == minX:
			meX = maxX - 1
		else:
			meX -= 1
	elif move.upper() == "D" and meX <= maxX- 1:
		if meX == maxX - 1:
			meX = minX
		else:
			meX += 1
	else:
		continue

	if meY == itemY and meX == itemX:
		if item not in inventory:
			inventory[item] = 1
		else:
			inventory[item] += 1

		while True:
			itemX = random.randrange(minX, maxX)
			itemY = random.randrange(minY, maxY)
			if itemX != meX and itemY != meY:
				displayItem(itemX, itemY)
				break
			else:
				continue






