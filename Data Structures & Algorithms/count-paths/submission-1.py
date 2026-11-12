class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def backtrack(row,col):
            if (row,col) in cache: 
                return cache[(row,col)]
            if row >= m or col >= n: 
                return 0 

            if row == (m-1) and col == (n-1): 
                return 1 

            cache[(row,col)] = backtrack(row+1, col) + backtrack(row, col +1)
            return cache[(row,col)] 
            
        return backtrack(0,0)

            


        

            