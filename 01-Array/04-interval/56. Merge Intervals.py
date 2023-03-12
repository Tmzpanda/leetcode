# 56. Merge Intervals

# O(nlogn)
def merge(intervals: List[List[int]]) -> List[List[int]]:

    intervals = sorted(intervals)

    merged = [intervals[0]]
    for interval in intervals:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
            
    return merged
    

