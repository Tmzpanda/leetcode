"""
# palindrome - middle out O(n^2)
             - dp O(n)
             
# prefix sum




"""



#********************************* palindrome **********************************************
# middle out 
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        longest = ""
        for middle in range(len(s)):
            sub1 = self.findPalindrome(s, middle, middle)
            sub2 = self.findPalindrome(s, middle, middle + 1)
            sub = max(sub1, sub2, key=lambda x: len(x))
            if len(sub) > len(longest):
                longest = sub
                
        return longest
        
    def findPalindrome(self, string, l, r):
        while l >= 0 and r < len(string):
            if string[l] != string[r]:
                break
            l -= 1
            r += 1
        
        l, r = l + 1, r - 1
        return string[l:r + 1]
        
        
# dp





















#********************************* prefix sum **********************************************
