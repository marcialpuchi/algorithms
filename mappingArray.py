# ['A','B','B'],  'A'=>[ ((0,0)), ((2,0),(2,1)) ]
# ['B','B','C'],  'B'=>[ ((0,1),(0,2),(1,0),(1,1)) ]
# ['A','A','C']   'C'=>[ ((1,2),(2,2)) ]


from collections import defaultdict
from pprint import pprint as pp

def findAdjacent(matrix, pos, elements, unique):

	row = pos[0]
	col = pos[1]

	rows = len(matrix)
	cols = len(matrix[0])

	category = matrix[row][col]

	if pos in elements:
		return elements

	elements.add(pos)
	unique.add(pos)

	if row > 0 and matrix[row-1][col] == category:
			# above
			pos = (row-1,col)
			elements = findAdjacent(matrix, pos, elements, unique)
			
	if row < rows-1 and matrix[row+1][col] == category:
			# below
			pos = (row+1,col)
			elements = findAdjacent(matrix, pos, elements, unique)

	if col > 0 and matrix[row][col-1] == category:
			#it has elements to the left
			pos = (row,col-1)
			elements = findAdjacent(matrix, pos, elements, unique)

	if col < cols-1 and matrix[row][col+1] == category:
			#it has elements to the right
			pos = (row,col+1)
			elements = findAdjacent(matrix, pos, elements, unique)

	return elements


def mapArray(entry):
	
	unique=set()
	result = {}
	row_group=defaultdict(list)

	for r, row in enumerate(entry):
		for c, col in enumerate(row):

			current = col
			pos = (r,c)

			if pos not in unique:
				unique.add(pos)

				if current not in result.keys():
					result[current]=[]
					
				result[current].append(findAdjacent(entry, pos, set(), unique))

	return result

pp(mapArray([['A','B','B'],['B','B','C'],['A','A','C']]))