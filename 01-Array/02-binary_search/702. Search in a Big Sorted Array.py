# 702. Search in a Big Sorted Array - First Position of Target
def searchBigSortedArray(reader, target):
    index = 0
    while reader.get(index) < target:
        index = index * 2 + 1
        
    l, r  = 0, index
    while l + 1 < r: 
        mid = (l + r) // 2
        
        if target <= reader.get(mid):
            r = mid
        else:
            l = mid
            
    if reader.get(l) == target:     # special case: [1, 1, 2, 3]
        return l
    elif reader.get(r) == target:
        return r
    else:
         return -1