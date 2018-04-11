"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

:type s: str
:type p: str
:rtype: List[int]
"""
from collections import defaultdict

def findAnagrams(s, p):
    print('Test:', s, ' - ', p)
    anagrams = defaultdict(list)
    windowSize = len(p)
    
    for i in range(len(s) - windowSize + 1):
        e = windowSize + i
        currentWindow = ''.join(sorted(s[i:e]))
        anagrams[currentWindow].append(i)
        
    return anagrams[''.join(sorted(p))]


tests = [
    ('asdjnaksdnjk', 'as'),
    ('cbaebabacd', 'abc'),
    ('abab', 'ab'),
    ('abab', 'ba'),
    ('abab', 'd')
]

for longSting, shortString  in tests:
    print('results:', findAnagrams(longSting,shortString))
