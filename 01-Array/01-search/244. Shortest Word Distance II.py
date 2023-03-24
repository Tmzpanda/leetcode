# 244. Shortest Word Distance II - data structure for frequent queries

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.index_dict = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.index_dict[word].append(i)
        
        
    def shortest(self, word1: str, word2: str) -> int:
        arr1 = self.index_dict[word1]
        arr2 = self.index_dict[word2]
        res = sys.maxsize

        p1, p2 = 0, 0
        while p1 < len(arr1) and p2 < len(arr2):
            res = min(res, abs(arr1[p1] - arr2[p2]))
            if arr1[p1] < arr2[p2]:
                p1 += 1
            else:
                p2 += 1
        
        return res
        
