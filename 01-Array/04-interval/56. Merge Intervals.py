# 56. Merge Intervals
# union set
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        print(intervals)
        
        result = []
        for interval in intervals:
            if len(result) == 0 or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        
        # res = sum(map(lambda x: x[1] - x[0], res))
        return result
    
# intersection
def find_intersections(intervals):
    intervals.sort(key=lambda x: x[0]) 
    
    merged = [intervals[0]]
    for current in intervals:
        last = merged[-1]
        if current[0] <= last[1]: # current interval overlaps with previous
            merged[-1] = (last[0], max(last[1], current[1])) # merge intervals
        else:
            merged.append(current) # no overlap, add current interval to merged
            
    return merged
