# 560. Subarray with Sum Equals K

def subarraySum(nums: List[int], k: int) -> int:    
    n = len(nums)
    psum = 0
    psum_freq_dict = defaultdict(int)
    psum_freq_dict[0] = 1
    res = 0
    
    for num in nums: 
        psum += num
        if psum - k in psum_freq_dict:
            res += psum_freq_dict[psum - k]
        psum_freq_dict[psum] += 1

    return res
