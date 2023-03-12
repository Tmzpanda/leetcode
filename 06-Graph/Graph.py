
"""
  B --- D
 /|  /  | \
A | /   |  F
 \|/    |
  C --- E
  
https://www.youtube.com/watch?v=9wV1VxlfBlI 黄浩杰 BFS和DFS 第3讲 Dijkstra

"""

# adjacency list
unweighted_graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}
unweighted_graph.keys()


weighted_graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E":3 , "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}
