# 3. Longest Substring Without Repeating Characters


def lengthOfLongestSubstring(self, s: str) -> int:
    start = 0
    unique_chars = set()
    longest = 0

    for end in range(len(s)):

        while s[end] in unique_chars:
            unique_chars.remove(s[start])
            start += 1

        unique_chars.add(s[end])
        longest = max(longest, end - start + 1)

    return longest


# 3. Longest Substring Without Repeating Characters - sliding window O(n)     
def lengthOfLongestSubstring(s):
    start = 0
    unique_chars = set()
    longest = 0

    for end in range(len(s)):

        while s[end] in unique_chars:
            unique_chars.remove(s[start])
            start += 1
            
        unique_chars.add(s[end])
        longest = max(longest, end - start + 1)
        
    return longest