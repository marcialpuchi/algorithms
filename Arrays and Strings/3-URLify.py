# Write a method to replace all spaces in a string with '%20: 
# You may assume that the string has sufficient space at the 
# end to hold the additional characters, and that you are given 
# the "true" length of the string.

def URLify(text):

	url = text.split(" ")

	while "" in url:
		url.remove("")

	return "%20".join(url)


test=' Mr John Smith  '
print URLify(test)