# 974. Subarray Sums Divisible by K
def subarraysDivByK(nums: List[int], k: int) -> int:
    n = len(nums)
    psum = 0
    psumModK_to_freq = defaultdict(int)    
    psumModK_to_freq[0] = 1    
    res = 0

    for num in nums:
        psum += num
        psumModK = psum % k
        if psumModK in psumModK_to_freq:
            res += psumModK_to_freq[psumModK]
        psumModK_to_freq[psumModK] += 1

    return res
        
