# 290. Word Pattern - given string is separated - O(n)
def wordPattern(pattern, string):
        words = string.split()
        if len(words) != len(pattern):
            return False
        
        mapping = {}
        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if mapping[pattern[i]] != words[i]:
                    return False
                
            else:
                if words[i] in mapping.values(): # one to one mapping
                    return False
                mapping[pattern[i]] = words[i]
                
        return True
        