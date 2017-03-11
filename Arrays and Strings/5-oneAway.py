# There are three types of edits that can be performed
# on strings: insert a character, remove a character, 
# or replace a character. Given two strings, write a 
# function to check if they are one edit (or zero edits) 
# away.

from collections import Counter
from pprint import pprint as pp

def oneAway(w1,w2):

	d1 = Counter(x for x in w1)
	d2 = Counter(x for x in w2)

	if len(w1) >= len(w2):
		difference = d1-d2
	else:
		difference = d2-d1

	if len(difference)==1 and difference.values()[0]<2:
		return True
	else:
		return False



test=[('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'), ('pale', 'bake'), ('paaale', 'ple')]

pp( [(t1,t2, oneAway(t1,t2)) for t1,t2 in test] )