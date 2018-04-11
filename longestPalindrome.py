# Finding the longest palindrome in a given string
# Note: A palindrome is a words that reads the same
# 		either backwards or forwards.

def expandCenter(str, c, r, l):

	tmp=str[c]

	while r>=0 and l<len(str) and str[r]==str[l]:
		tmp=str[r:l+1]
		r-=1
		l+=1

	return tmp


def longestPalindrome(str):

	if str!=None and len(str)>0:
		longest=str[0:1]
	else:
		return 0

	for i, ch in enumerate(str):
		exp1=expandCenter(str,i, i-1, i+1)
		if len(longest) < len(exp1):
			longest = exp1
		
		exp2=expandCenter(str, i, i, i+1)
		if len(longest) < len(exp2):
			longest = exp2
		

	return longest

test = "jnasidsaofubsovbo12345654321erbvbqerob31240910412094102948128rq89r7890"

print "Result:",longestPalindrome(test)
