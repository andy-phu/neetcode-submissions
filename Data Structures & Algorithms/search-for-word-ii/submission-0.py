class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def insert(self, word):
        cur = self 

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isWord = True 

    def search(self, word):
        cur = self

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False

        return cur.isWord 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        - go all directions for each cell
        - before going in a direction check if the next cell is in any of the i + 1 word and if the i + 1 > len(word) skip that word 
        - create a trie and for each node in the trie it should contain whether it's an end of the word or not
        - if there are more children on that branch it keeps exploring til it gets to the leaf
        - for all the words in the list put them into a trie 
        - 
        """ 

        root = TrieNode()
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        res = set()
        for word in words:
            root.insert(word)

        def dfs(r,c, node, word):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] not in node.children or (r,c) in visited:
                return 

            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visited.remove((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")

        return list(res)



    