class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        [3, -1, 0, 1],
        [2,  2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, x]
        
        """


        visited = set()
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])

        directions = [(1,0), (0,-1), (-1,0), (0,1)]


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    queue.append((r,c))        
        steps = 0
        while queue:
            steps += 1 
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr, dc in directions:
                    newR, newC = r+dr, c+dc

                    if newR < 0 or newR >= ROWS or newC < 0 or newC >= COLS or (newR, newC) in visited or grid[newR][newC] == -1:
                        continue

                    grid[newR][newC] = steps 
                    visited.add((newR,newC))
                    queue.append((newR, newC))
