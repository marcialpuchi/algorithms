# Given an image represented by an NxN matrix, where each pixel 
# in the image is 4 bytes, write a method to rotate the image by 
# 90 degrees. can you do this in place?

def rotateMatrix(matrix):

	n = len(matrix)-1

	rMatrix = [['' for c in r] for r in matrix]

	for r, row in enumerate(matrix):
		for c, col in enumerate(row):
			
			current = col
			rMatrix[n-c][r] = col


	return rMatrix


test = [
	['R','R','G','B'],
	['R','B','B','R'],
	['G','R','G','G'],
	['R','R','B','G'],
]

print rotateMatrix(test)