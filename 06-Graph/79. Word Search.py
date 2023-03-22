# 79. Word Search - if exists

# dfs O(mn * 3^L)
def exist(self, board, word):
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if dfs(board, i, j, {(i, j)}, word, 1):
                    return True
    return False
    

def dfs(board, i, j, visited, word, index):
    if index == len(word):
        return True

    for delta in DIRECTIONS:
        x, y = i + delta[0], j + delta[1]
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visited and board[x][y] == word[index]:
            visited.add((x, y))
            if self.dfs(board, x, y, visited, word, index + 1):
                return True
            visited.discard((x, y))

    return False
 
