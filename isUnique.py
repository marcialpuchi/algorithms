#  Implement an algorithm to determine if a string has all unique characters.

def isUnique(word):

	checker = {}

	for ch in word:
		if ch in checker.keys():
			return False
		else:
			checker[ch]=True

	return True


test=['hello', 'abc', 'asdas', 'ablcdef']

print [ (t, isUnique(t)) for t in test]