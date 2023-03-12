# 49. Group Anagrams


# use sorted string as the key for each anagram group
# O(n*klogk)
from collections import defaultdict
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_dict = defaultdict(list)
    
    for word in strs:
        anagram = ''.join(sorted(word))
        anagram_dict[anagram].append(word)

    return anagram_dict.values()
  
  
# use char_counts as the key for each anagram group
# O(nk)
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_dict = defaultdict(list)
    
    for word in strs:
        char_counts = [0] * 26
        for char in word:
            char_counts[ord(char) - ord('a')] += 1

        anagram_dict[tuple(char_counts)].append(word) # use char_count as the key

    return anagram_dict.values()
