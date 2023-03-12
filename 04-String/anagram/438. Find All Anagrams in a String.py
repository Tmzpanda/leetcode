# 438. Find All Anagrams in a String

def findAnagrams(self, s: str, p: str) -> List[int]:
  
    # initialize
    p_char_freq = defaultdict(int)
    s_char_freq = defaultdict(int)
    for i in range(len(p)):
        p_char_freq[p[i]] += 1
        s_char_freq[s[i]] += 1
        
    res = [0] if s_char_freq == p_char_freq else []

    # sliding window
    l = 0
    for r in range(len(p), len(s)):
        s_char_freq[s[r]] += 1
        s_char_freq[s[l]] -= 1
        if s_char_freq[s[l]] == 0:
            s_char_freq.pop(s[l])

        l += 1
        if s_char_freq == p_char_freq:
            res.append(l)

    return res
