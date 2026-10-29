class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #go through each square and if it's a 1 then do dfs all sides counting
        #the number of connected 1's and compare it to "max area"
        #once you inspect a 1 convert it to a 0 


        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        area = 0 
        visited = set()
        def dfs(row,col):   
            nonlocal area
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 0 or (row,col) in visited:
                return 

            area += 1 
            visited.add((row,col))
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)
           

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r,c)
                    if area > maxArea:
                        maxArea = area
                    area = 0
                    grid[r][c] = 0


        return maxArea