# Given a string, write a function to check if it is a permutation 
# of a palin- drome. A palindrome is a word or phrase that is the 
# same forwards and backwards. A permutation is a rearrangement of 
# letters.

from collections import Counter

def palindromePermutation(text):

	count = Counter()
	text = text.translate(None, " ").lower()
	check = Counter()

	for w in text:
		count[w]+=1

	for k,v in count.items():
		if v%2==0:
			check['even']+=1
		else:
			check['odd']+=1

	if len(text) % 2 == 0 and check['odd']==0:
		return True
	elif len(text) % 2 != 0 and check['odd']==1:
		return True
	else:
		return False



test=["Tact Coa", "Taco cat", "atco cta", "house mouse"]

print [(t,palindromePermutation(t)) for t in test]