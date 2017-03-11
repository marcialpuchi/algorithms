# Write an algorithm such that if an element in an MxN 
# matrix is 0, its entire row and column are set to 0.

def zeroMatrix(matrix):
	newMatrix=[[None for c in r] for r in matrix]
	rows=len(matrix)
	cols=len(matrix[0])

	for r,row in enumerate(newMatrix):
		for c,val in enumerate(row):
			eq=matrix[r][c]

			if val is None:
				if eq==0:
					for r2 in range(rows):
						newMatrix[r2][c]=0

					for c2 in range(cols):
						newMatrix[r][c2]=0
				else:
					newMatrix[r][c]=eq
			else:
				continue

	return newMatrix


test = [
	[0,1,1],
	[1,1,1],
	[1,1,0]
]

print(zeroMatrix(test))