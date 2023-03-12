# 211. Design Trie
class TrieNode: 
    def __init__(self,val):
        self.children = {}             # char_to_node
        self.end = False
        

class WordDictionary:
    def __init__(self):
        self.root = TrieNode(0)        
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.end = True
            
            
    def search(self, word: str) -> bool:
        def dfs(i, node):
            # break
            if i == len(word):
                return node.end
            
            if word[i] != '.':
                if word[i] not in node.children:
                    return False
                return dfs(i + 1, node.children[word[i]])
            
            else:
                for node in node.children.values():
                    if dfs(i + 1, node):
                        return True
                return False
        
        return dfs(0, self.root)
    