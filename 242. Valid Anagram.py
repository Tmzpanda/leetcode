# 242. Valid Anagram


# hashmap
from collections import defaultdict
def isAnagram(s: str, t: str) -> bool:
    char_freq = {}
    for char in s:
        char_freq[char] += 1

    for char in t:
        char_freq[char] -= 1

    return all(v == 0 for v in char_freq.values())
     


# sort 
def isAnagram(self, s: str, t: str) -> bool:
    
    return sorted(s) == sorted(t)
