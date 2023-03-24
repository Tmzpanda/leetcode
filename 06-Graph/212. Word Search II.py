# 212. Word Search II - multiple words

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):	
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()  
            cur = cur.children[char]
        cur.is_word = True
        
    def delete(self, word):	
        pass


def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    m, n = len(board), len(board[0])
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]

    trie = Trie()
    for word in words:		
        trie.insert(word)

    def dfs(i, j, trie_node, prefix):  
        if trie_node.is_word:
            res.append(prefix)
            trie.delete(prefix)     # optimize

        for delta in directions:
            x, y = i + delta[0], j + delta[1]
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and board[x][y] in trie_node.children:
                visited.add((x, y))
                dfs(x, y, trie_node.children[board[x][y]], prefix+board[x][y])
                visited.remove((x, y))

    res = []
    visited = set()
    for i in range(m):
        for j in range(n):
            if board[i][j] in trie.root.children:
                visited.add((i, j))
                dfs(i, j, trie.root.children[board[i][j]], board[i][j])    
                visited.remove((i, j))        

    return list(set(res))
