
# 727. Minimum Window with - Target Subsequence - two pointers O(ST) = O((# of pattern found)*S*T)
def minWindow(S, T):
        
    minLen = len(S) + 1
    window = ""

    i, j = 0, 0
    while i < len(S):
        if S[i] == T[j]:
            j += 1
               
        if j == len(T):   # shrink
            end = i 
            j -= 1
            while j >= 0:
                if S[i] == T[j]:
                    j -= 1
                i -= 1
            i += 1
            j += 1
            if end - i + 1 < minLen:
                minLen = end - i + 1
                window = S[i:end + 1]
               
        i += 1
     
    return window