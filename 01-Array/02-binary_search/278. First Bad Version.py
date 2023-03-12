# 278. First Bad Version
def findFirstBadVersion(n):
    l, r = 1, n
    while l + 1 < r:
        mid = (l + r) // 2
        if SVNRepo.isBadVersion(mid):     # based on bad_version_or_not
            r = mid
        else:
            l = mid
    
    if SVNRepo.isBadVersion(l): 
        return l
    return r
