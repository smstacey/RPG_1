ROW = 5
COL = 5

xPlayer = 3
yPlayer = 3
player = "$"

grid = [[' ', ' ', ' ', ' ', ' ', ' '], 
		[' ', ' ', ' ', ' ', ' ', ' '], 
		[' ', ' ', ' ', ' ', ' ', ' '], 
		[' ', ' ', ' ', ' ', ' ', ' '], 
		[' ', ' ', ' ', ' ', ' ', ' '], 
		[' ', ' ', ' ', ' ', ' ', ' ']]


grid[ROW-yPlayer][COL-xPlayer] = player

while True:
	for i in grid:
		print(i)

	print("xPlayer:", xPlayer, "yPlayer:", yPlayer, "\n", "COL:", COL, "ROW:", ROW)
	move = input("Move your character: ")
	grid[ROW-yPlayer][COL-xPlayer] = ' '

	if move == "W" and yPlayer >= 0 and yPlayer <= ROW:
		yPlayer += 1
	elif move == "S" and yPlayer >= 0 and yPlayer <= ROW:
		yPlayer -= 1
	elif move == "A" and xPlayer >= 0 and xPlayer <= COL:
		xPlayer += 1
	elif move == "D" and xPlayer >= 0 and xPlayer <= COL:
		xPlayer -= 1

	grid[ROW-yPlayer][COL-xPlayer] = player












