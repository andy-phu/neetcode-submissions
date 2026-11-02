class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        3 paths:
        - if i and j do not equal each other then we can 
            - replace, delete, insert
        - replace would be just moving i and j to the right
        - insert would be moving i and j to the right 
        - delete would be moving i to the right and j stays still 
        - if they are equal we move i and j to the right and the operations is 0
        
        monkeys
           i
           3

        money
           j
        """

        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i,j)]
            #delete the remaining if there is more i left 
            if i == len(word1):
                return len(word2) - j
            elif j == len(word2):
                return len(word1) - i
            
            operations = 0 
            if word1[i] == word2[j]:
                operations += dfs(i+1, j+1)
            else:
                operations += (1 + min(dfs(i+1, j+1), dfs(i+1, j), dfs(i, j+1)))

            cache[(i,j)] = operations
            return operations
        
        return dfs(0,0)
            
            
