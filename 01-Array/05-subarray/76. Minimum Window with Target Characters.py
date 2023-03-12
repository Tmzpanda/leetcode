

# 76. Minimum Window with - Target Characters - sliding window O(n)
class Solution:
    def minWindow(self, s, t):
        targetCharToFreq = self.buildCharToFreq(t)
        sourceCharToFreq = {}
        n = len(targetCharToFreq)
        matched = 0
        
        window = ""
        minLen = sys.maxsize
        l = 0
        for r in range(len(s)):
            sourceCharToFreq[s[r]] = sourceCharToFreq.get(s[r], 0) + 1
            if s[r] in targetCharToFreq and sourceCharToFreq[s[r]] == targetCharToFreq[s[r]]:
                    matched += 1

            while matched == n: 
                windowLen = r - l + 1
                if windowLen < minLen:
                    minLen = windowLen
                    window = s[l: r + 1]

                sourceCharToFreq[s[l]] -= 1
                if s[l] in targetCharToFreq and sourceCharToFreq[s[l]] < targetCharToFreq[s[l]]:
                    matched -= 1
  
                l += 1  
               
        return window
        
    def buildCharToFreq(self, s):
        targetCharToFreq = {}
        for c in s:
            targetCharToFreq[c] = targetCharToFreq.get(c, 0) + 1
               
        return targetCharToFreq