# 974. Subarray with Sum Equals - nK - hashmap O(n)
def subarraysDivByK(nums, k):
    n = len(nums)
    psum = 0
    psumModK_to_freq = {0: 1}     
    res = 0

    for i in range(n): 
        psum += nums[i]
        psumModK = psum % k
        if psumModK in psumModK_to_freq:
            res += psumModK_to_freq[psumModK]
          
        psumModK_to_freq[psumModK] = psumModK_to_freq.get(psumModK, 0) + 1           

    return res