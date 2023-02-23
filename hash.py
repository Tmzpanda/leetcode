# 451. Sort Characters By Frequency
def frequencySort(s: str) -> str:
    char_freq = {}
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    sorted_char_freq = sorted(char_freq.items(), key=lambda item: item[1], reverse=True)

    res = []
    for item in sorted_char_freq:
        res.extend([item[0]] * item[1])

    return "".join(res)
