def pathFinder(maze, pos, r, c, exit, count=0):
	row = pos[0]
	col = pos[1]

	#~~~~~~~~~~~ Check if reached exit ~~~~~~~~~~
	if pos==exit:
		return count

	#~~~~~~~~~~~ Mark current position as a wall ~~~~~~~~~~~
	maze[row][col]=1

	# ~~~~~~~~~~~~~~ Gather Posible Branches ~~~~~~~~~~~
	branches = []

	# up
	if row > 0 and maze[row-1][col] == 0:
		pos = (row-1,col)
		branches.append(pos)
	
	# down	
	if row < r-1 and maze[row+1][col] == 0:
		pos = (row+1,col)
		branches.append(pos)

	# left
	if col > 0 and maze[row][col-1] == 0:
		pos = (row,col-1)
		branches.append(pos)
		
	# right
	if col < c-1 and maze[row][col+1] == 0:
		pos = (row,col+1)
		branches.append(pos)
		
	best=-1

	for branch in branches:
		move = pathFinder(maze, branch, r, c, exit, count+1)
		
		if best==-1 or move < best:
			best = move

	maze[row][col]=0
	return best


def mazePathfinder(maze, rows, columns, exitRow, exitCol):
	return pathFinder(maze, (0,0), rows, columns, (exitRow, exitCol),0)
	
maze = [
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,1],
	[0,0,0,0],
	[0,0,0,0]
]

print mazePathfinder(maze, 5, 4, 2, 3)