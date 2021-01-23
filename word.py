""""
# Word Ladder - length - bfs O(m^2 * n) O(m^2 * n), where m = len(s)
                       - bidirectional bfs O(m^2 * n) O(m^2 * n)
              - all possible solutions - bfs + dfs backtrack
              




# Word Break - world - if possible/number of solutions - dp O(n^2)
                     - all solutions - dfs memoization (recursion top-down with return)  
# Decode Ways - dp - O(n)   


# Word Search - one word - dfs T << O(m*n * 3^len(word))
              - several words - prefix backtrack 
              
# Word Pattern - given string is separated - O(n)
               - given string is not separated - dfs O(len(string)^len(pattern))

# Wildcard - dp O(m*n)

""""




# *********************************************** Word Pattern **************************************************************
# Word Pattern 
 # given string is separated - O(n)
 """
                                  abab  "red blue red blue"
                     a "red"                                 
                     b "blue"           
 
 """
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
        


# given string is not separated - O(len(string)^len(pattern))


      
#*********************************************** Wildcard **************************************************************
