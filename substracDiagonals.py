# Get the sum of the two main diagonals
# and substract the two values.
# The result should be an integer.

def subsDiagonals(array):

	diag1=0
	diag2=0

	size=len(array)-1

	for r, row in enumerate(array):
		diag1 += array[r][r]
		diag2 += array[r][size-r]

	print diag1, diag2

	subtraction = abs(diag1 - diag2)
	
	return subtraction

testArray = [
	[2,2,3,4],
	[4,5,6,0],
	[7,8,9,8],
	[2,5,3,2]
]

print subsDiagonals(testArray)