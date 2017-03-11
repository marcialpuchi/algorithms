# Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutations(w1, w2):

	if ''.join(sorted(w1)) == ''.join(sorted(w2)):
		return True
	else:
		return False

test=[('hello', 'ollhe'), ('abc','dca'), ('zdk', 'kdf'), ('cat', 'tac')]
print [(w1,w2,checkPermutations(w1,w2)) for w1,w2 in test]