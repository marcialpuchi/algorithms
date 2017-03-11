def pathFinder(maze, pos, r, c, exit, count=0):
	row = pos[0]
	col = pos[1]

	# print '@', pos

	#~~~~~~~~~~~ Check if reached exit ~~~~~~~~~~
	if pos==exit:
		return count

	#~~~~~~~~~~~ Mark current position as a wall ~~~~~~~~~~~
	maze[row][col]=1

	# ~~~~~~~~~~~~~~ Gather Posible Branches ~~~~~~~~~~~
	# print 'posible branches:'
	branches = []

	# up
	if row > 0 and maze[row-1][col] == 0:
		pos = (row-1,col)
		branches.append(pos)
		# print 'U', pos

	# down	
	if row < r-1 and maze[row+1][col] == 0:
		pos = (row+1,col)
		branches.append(pos)
		# print 'D', pos

	# left
	if col > 0 and maze[row][col-1] == 0:
		pos = (row,col-1)
		branches.append(pos)
		# print 'L', pos

	# right
	if col < c-1 and maze[row][col+1] == 0:
		pos = (row,col+1)
		branches.append(pos)
		# print 'R', pos

	# ~~~~~~~~~~~~ Check branches ~~~~~~~~~~~~~~~~
	# print 'maze:',maze
	# print 'continue?'
	# raw_input()

	best=-1

	for branch in branches:
		move = pathFinder(maze, branch, r, c, exit, count+1)
		
		# print 'branch result', branch, move 

		if best==-1 or move < best:
			best = move

		# print 'best', best

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