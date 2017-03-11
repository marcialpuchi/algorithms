# Given an array with a string of canditates,
# Find the candidate that has more repetitions.
# If two candidates have the same number of
# repetitions, print them in alphabetic order.

from collections import Counter;

def maxVotes(candicates):

	votes=Counter(candicates)
	maxVotes = 0
	winner = []

	for c, v in votes.iteritems():
		if v > maxVotes:
			maxVotes = v
			winner = [c]
		elif v==maxVotes:
			winner.append(c)

	print "Winner: " + str(sorted(winner))
	print "Votes: " + str(maxVotes)

votes=['john','john','john','Harry','Harry','Harry','Ed']

maxVotes(votes)