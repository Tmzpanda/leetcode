# 3. Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    seen = set()
    longest = 0

    start = 0
    for i in range(n):
        while s[i] in seen:
            seen.remove(s[i])
            start += 1

        seen.add(s[i])
        longest = max(longest, i - start + 1)

    return longest
