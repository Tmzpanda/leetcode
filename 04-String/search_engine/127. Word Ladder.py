# 127. Word Ladder - length of shortest sequences

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:

    # build graph
    graph = defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            graph[pattern].append(word)

    # bfs
    queue = deque([beginWord])
    visited = set([beginWord])
    res = 1
    while queue:
        for i in range(len(queue)):
            word = queue.popleft()
            if word == endWord:
                return res
            # neighbors
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for next_word in graph[pattern]:
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append(next_word)

        res += 1

    return 0

        


        
