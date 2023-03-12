# 402. Remove K Digits Smallest Possible - mono-stack O(n)
def removeKdigits(num, k):
    stack = []
    for char in num:
        while stack and k and int(stack[-1]) > int(char):       # increasing
            stack.pop()
            k -= 1
        stack.append(char)

    while k:          
        stack.pop()
        k -= 1
    if not stack:
        return '0'

    return str(int("".join(stack)))