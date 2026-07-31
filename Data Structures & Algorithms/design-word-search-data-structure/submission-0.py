class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False


class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.end=True
        

    def search(self, word: str) -> bool:

        def dfs(node, index):

            # Base case
            if index == len(word):
                return node.end

            ch = word[index]

            # Wildcard case
            if ch == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False

            # Normal character case
            if ch not in node.children:
                return False

            return dfs(node.children[ch], index + 1)

        return dfs(self.root, 0)
        
