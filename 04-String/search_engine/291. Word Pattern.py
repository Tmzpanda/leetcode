# 291. Word Pattern - given string is not separated - dfs O(len(string)^len(pattern))
"""
                                 abab  "redblueredblue"
                  a "r"    ...                            a "red"      ...   a "redbl"             
 b "e"  b "edb" ... b "eblue"  ...
 
 
# of matching for each recursion: len(string)
# of recursion: len(pattern) 
# time complexity = len(string) ^ len(pattern)  

"""

class Solution:
    
    def wordPatternMatch(self, pattern, string):
        return self.is_match(pattern, string, {}, set())
        
        
    def is_match(self, pattern, string, char_to_word, used):
        # break condition
        if not pattern:
            return not string
        
        char = pattern[0]
        
        # if pattern exists
        if char in char_to_word:
            word = char_to_word[char]
            if not string.startswith(word):
                return False        
            return self.is_match(pattern[1:], string[len(word):], char_to_word, used)
        
        # if pattern hasn't been assigned yet
        for i in range(len(string)):
            word = string[:i + 1]
            if word in used:        # one to one mapping
                continue
            
            used.add(word)
            char_to_word[char] = word
            
            if self.is_match(pattern[1:], string[i + 1:], char_to_word, used):
                return True     
                
            del char_to_word[char]
            used.remove(word)
            
        return False
