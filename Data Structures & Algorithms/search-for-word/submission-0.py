class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r,c,i):
            #out of bounds return empty array
            #in visited return empty array
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visited.add((r,c))
            for dr,dc in directions: 
                nr, nc = r + dr, c + dc
                if backtrack(nr, nc, i+1):
                    return True
            visited.remove((r,c))

            return False

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0):
                    return True

        return False