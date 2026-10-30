class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        grid = {}

        ROWS, COLS = len(board), len(board[0])

        for i in range(ROWS):
        
            rows[i] = set()
            cols[i] = set()
            for j in range(COLS):
                grid[(i,j)] = set()

        for r in range(ROWS):
            for c in range(COLS):
                #check row
                val = board[r][c]
                if val == ".":
                    continue
                val = int(val)
                grid_row = r // 3 
                grid_key = c // 3

                if val < 1 or val > 9 or val in rows[r] or val in cols[c] or val in grid[(grid_row, grid_key)]:
                    print(grid)
                    return False 

                
                rows[r].add(val)
                cols[c].add(val)
                grid[(grid_row, grid_key)].add(val)
        return True


                


                
