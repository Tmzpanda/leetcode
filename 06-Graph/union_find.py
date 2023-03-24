

##############




"""
https://www.youtube.com/watch?v=gpmOaSBcbYA 黄浩杰 并查集 第二讲
https://www.youtube.com/watch?v=zos--xohLT0 黄浩杰 第三讲 union优化
0 -- 1
    / \
    2  3
    |\ |
    5  4 
"""





from collections import defaultdict



class UnionFind():
    def __init__(self):
        self.parent = defaultdict(lambda: -1)
        self.rank = defaultdict(int)



    def find_root(self, x):
        x_root = x
        while self.parent[x_root] != -1:
            x_root = self.parent[x_root]

        return x_root

    def union(self, x, y):
        x_root = self.find_root(x)
        y_root = self.find_root(y)

        # if x and y in the same set
        if x_root == y_root:
            return False

        # if x and y in different sets, then union
        else:
            self.parent[x_root] = y_root
            return True
        
        # # optimization by rank
        # else:
        #     if self.rank[x_root] > self.rank[y_root]:
        #         self.parent[y_root] = x_root

        #     elif self.rank[y_root] > self.rank[x_root]:
        #         self.parent[x_root] = y_root

        #     else:
        #         self.parent[y_root] = x_root
        #         self.rank[y_root] += 1

        #     return True



        
edges = [
    [0, 1], [1, 2], [1, 3],
    [2, 4], [3, 4], [2, 5]
]

for edge in edges:
    uf = UnionFind()
    x, y = edge[0], edge[1]
    if UnionFind.union(x, y): 
        print("Cycle detected!")
    else:
        print("No cycle detected!")
