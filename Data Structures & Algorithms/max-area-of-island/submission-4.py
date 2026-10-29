class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            total = 0

            q = deque()

            q.append((r,c))
            grid[r][c] = 0 
            while q:
                for i in range(len(q)):
                    qr, qc = q.popleft()
                    total += 1

                    #check all four directions and only go in a direction if that
                    #number in that cell equals 1 and it's in bounds
                    #everytime we add to the queue we should mark that cell as 0 after

                    for dr, dc in directions:
                        nr, nc = qr + dr, qc + dc

                        if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == 1:
                            q.append((nr, nc))
                            grid[nr][nc] = 0

            return total

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r,c))
        
        return maxArea 


