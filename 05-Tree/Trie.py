# Trie

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
        self._delete(self.root, word, 0)
        
    def _delete(self, node, word, index):   # private method
        if index == len(word):
            if node.is_word:
                node.is_word = False
            return
        
        char = word[index]
        if char not in node.children:
            return

        child_node = node.children[char]
        self._delete(child_node, word, index + 1)

        if not child_node.children and not child_node.is_word:
            del node.children[char]
        
    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.is_word
    
    def startsWith(self, prefix) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        
