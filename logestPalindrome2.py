# Finding the longest palindrome in a given string
# Note: A palindrome is a words that reads the same
#     either backwards or forwards.
def searchPalindrome(str, index):
  window = 0
  center = index
  leftWindow = index-1 
  rigthWindow = index+1

  while leftWindow >= 0 and rigthWindow < len(str):
    if str[leftWindow] == str[rigthWindow] or str[center-window] == str[center+window]:
      window += 1
      leftWindow -= 1
      rigthWindow += 1
    else:
      break

  print(str[leftWindow:rigthWindow])

  print('--result:', str[leftWindow + 1:rigthWindow])
  return str[leftWindow + 1:rigthWindow]


def searchOddPalindrome(str, index):
  window = 0
  leftWindow = index
  rigthWindow = index

  while leftWindow >= 0 and rigthWindow < len(str):
    if str[leftWindow] != str[rigthWindow]:
      break

    window += 1
    leftWindow -= 1
    rigthWindow += 1

  print('completed with', window, '--result:', str[leftWindow + 1:rigthWindow])
  return str[leftWindow + 1:rigthWindow]
  
def searchEvenPalindrome(str, index):
  window = 0
  leftWindow = index
  rigthWindow = index + 1

  while leftWindow >= 0 and rigthWindow < len(str):
    if str[leftWindow] != str[rigthWindow]:
      break

    window += 1
    leftWindow -= 1
    rigthWindow += 1

  print('completed with', window, ' --result:', str[leftWindow+1:rigthWindow])
  return str[leftWindow+1:rigthWindow]

def longestPalindrome(str):
  print('test:', str)
  window = 1
  longest = ''

  for i, ch in enumerate(str):

    leftWindow = i - window
    rigthWindow = i + window

    # odd = searchOddPalindrome(str, i)
    # if len(odd) > 1 : print('Odd result:', odd)
    # even = searchEvenPalindrome(str, i)
    # if len(even) > 1 : print('Even result:', even)
    print(searchPalindrome(str, i))

tests = [
  # 'jsndclhanslchansljchnajshdbcljhsdbclj',
  # 'jnasidsaofubsovbo12345654321erbvbqerob31240910412094102948128rq89r7890',
  # 'catacanawavawa',
  'catacanawavvawa'
]

for test in tests:
  print('Final result:', longestPalindrome(test))

 



 # catacanawavvawa
 # catac
 # aca
 # ana
 # awa
 # awavawa