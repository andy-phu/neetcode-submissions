class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str) -> None:
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        
        curr.isWord = True



    def search(self, word: str) -> bool:
        
        def dfs(i, node):
            for j in range(i,len(word)):
                if word[j] in node.children:
                    node = node.children[word[j]]
                elif word[j] == "." and node.children:
                    for child in node.children:
                        if dfs(j+1, node.children[child]):
                            return True
                    return False
                else:
                    return False

            return node.isWord

        return dfs(0,self)
            


       
