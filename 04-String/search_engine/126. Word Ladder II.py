# 126. Word Ladder - all shortest sequences 

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    word_set = set(wordList)

    # bfs build graph
    graph = defaultdict(set)
    distance_dict = {beginWord: 0} 

    queue = deque([(beginWord, 0)])
    visited = set([beginWord])
    while queue:
        for i in range(len(queue)):
            word, distance = queue.popleft()
            distance_dict[word] = distance
            
            for j in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":       
                    next_word = word[:j] + char + word[j + 1:]
                    if next_word in word_set:
                        graph[next_word].add(word)
                        
                        if next_word not in visited:
                            visited.add(next_word)
                            queue.append((next_word, distance + 1))

    # backtrack
    def dfs(word, path):
        if word == beginWord:
            res.append(path[::-1])
            return

        for previous_word in graph[word]:
            if distance_dict[previous_word] == distance_dict[word] - 1:   # sequences of shortest length
                path.append(previous_word)
                dfs(previous_word, path)
                path.pop()

    res = []
    dfs(endWord, [endWord])

    return res






