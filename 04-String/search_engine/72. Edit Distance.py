# dp O(m*n)
def minDistance(word1: str, word2: str) -> int:

    def dfs(word1, word2, memo):
        if (word1, word2) in memo:
            return memo[(word1, word2)]

        if word1 == word2:
            return 0

        if word1 == "":
            return len(word2)

        if word2 == "":
            return len(word1)

        if word1[0] == word2[0]:
            res = dfs(word1[1:], word2[1:], memo)

        else:
            res = min(dfs(word1, word2[1:], memo) + 1,
                      dfs(word1[1:], word2, memo) + 1
                     )

        memo[(word1, word2)] = res
        return res

    return dfs(word1, word2, {})