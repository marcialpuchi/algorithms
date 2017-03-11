# Implement a method to perform basic string compression using 
# the counts of repeated characters. For example, the string 
# aabcccccaaa would become a2b1c5a3. If the "compressed" string
# would not become smaller than the original string, your method
# should return the original string.

from itertools import groupby


def strCompression(text):	
	compression = "".join(["{0}{1}".format(k, sum(1 for i in g)) for k, g in groupby(text)])

	if len(compression) > len(text):
		
		return text
	else:
		return compression


test=['aabcccccaaa', 'ababab']
print [ (t,strCompression(t)) for t in test]