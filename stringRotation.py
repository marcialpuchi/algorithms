# Given two strings, s1 and s2, write code to check if s2 
# is a rotation of s1 using only one call to isSubstring

def isSubstring(s1,s2):

	startIndex = -1

	for f, letter in enumerate(s1):
		i=s2.find(s1[:f])

		print s1[:f],i

		if i < 0:
			break
		else:
			startIndex=i

	p1=s2[startIndex:]
	p2=s2[:startIndex]

	final=p1+p2

	if final==s1:
		return True
	else:
		return False

print(isSubstring("wwwawwaww","wwwawwaww"))
