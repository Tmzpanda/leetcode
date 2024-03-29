# 263. Ugly Number
def isUgly(n: int) -> bool:
    if n <= 0:
        return False

    factors = [2, 3, 5]
    for factor in factors:
        while n % factor == 0:
            n //= factor

    return n == 1
  
  
