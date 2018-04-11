"""
Problem: Print the shortest substring of input, that has all characters from alphabets

input: 
  string: "abbaac",
  alphabets: "acb"

Expected output: baac


tests:
  abbaac
  abbaacba
  abbaacb
  caxadcab
  dcab
  abbaabbaaaababbbaaaaaaab
  weerertert

Solutions:

Method 1:
  Generate all posible substring everytime we find a letter that is in the alphabet
  and keep track of the shortest.

  example:
    abbaac
     bbaac
      baac
       aacb
        acb
         cba
          ba
           a


Methd 2:
  Move through the word, letter by letter and remove the first letter when:
    1. Is the same as the last letter we found.
    2. Is the same as the second letter in the current substring.
    3. Is not cointained in the alphabet.

  example:
    abbaacba
    --baac
       -acb
         cba
"""

def findEndOfString(str, letters):
  alphabet = list(letters)

  for i, char in enumerate(str):

    if char in alphabet:
      alphabet.remove(char)

    if len(alphabet) <= 0:
      return str[:i+1]

  return -1


def shortestSubstring(str, alphabet):

  shortest = None

  print('test: ', str, alphabet)

  for i, char in enumerate(str):

    if char in alphabet:
      tmpSubstring = findEndOfString(str[i:], alphabet)

      if tmpSubstring != -1:
        if shortest is None or len(tmpSubstring) < len(shortest):
          shortest = tmpSubstring

  return shortest if shortest is not None else -1

##############################################################################

def removeDuplicatedFromStart(str, alphabet):
  if str[0] == str[-1] or str[0] == str[1] or str[0] not in alphabet:
    return removeDuplicatedFromStart(str[1:], alphabet)

  else:
    return str

def shortestSubstring2(str, alphabet):
  print('test: ', str, alphabet)
  currentSubstring = ''
  shortest = ''

  for ch in str:
    newSubstring = currentSubstring + ch

    if  len(currentSubstring) > 0 and currentSubstring[0] == ch:
      currentSubstring = removeDuplicatedFromStart(newSubstring, alphabet)

    else:
      currentSubstring = newSubstring

    currentSet = set(currentSubstring)
    if set(alphabet).issubset(currentSet):
      if shortest == '' or len(currentSubstring) < len(shortest):
        shortest = currentSubstring

  return shortest if shortest != '' else -1


##############################################################################

tests = [
  ('abbaac', 'abc'),
  ('abbaacba', 'abc'),
  ('abbaacb', 'abc'),
  ('caxadcab', 'abc'),
  ('weerertert', 'abc'),
  ('this is a test string', 'tis')
]

for str, alph in tests:
  print('result: ', shortestSubstring2(str, alph))
