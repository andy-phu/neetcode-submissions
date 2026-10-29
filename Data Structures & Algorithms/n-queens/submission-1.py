class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # (0,0) (2,2) 
        # (0,0) (1,1) (1,3)

        # 2,1 : 1,0 1,2 0,3

        # 3,2 : 2,1 1,0 2,3

        #diagonal subtract r1-r2 c1-c2 and see if their differences equal each other
        #up, down check if any of the numbers in the array have the same r
        #right, left check if any of the numbers in the array have the same c

        #store the queen's positions in an array
        #construct the array at the end

        board = [["."]* n for i in range (n)]

        def populated(rows, cols, posDiagonals, negDiagonals, newR, newC): 
            if newR in rows or newC in cols or newR-newC in negDiagonals or newR + newC in posDiagonals:
                return False

            return True
        rows, cols, posDiagonals, negDiagonals = set(), set(), set(), set()
        res = []
        def backtrack(r):
            if r == n:
                #todo: reconstruct 2d array
                copyRow = []
                for r in range(n):
                    tempString = "".join(board[r])
                    copyRow.append(tempString)
                res.append(copyRow)
                return

            for c in range(n): 
                if populated(rows, cols, posDiagonals, negDiagonals, r, c):
                    board[r][c] = "Q"
                    rows.add(r)
                    cols.add(c)
                    posDiagonals.add(r+c)
                    negDiagonals.add(r-c)

                    backtrack(r+1)

                    board[r][c] = "."
                    rows.remove(r)
                    cols.remove(c)
                    posDiagonals.remove(r+c)
                    negDiagonals.remove(r-c)

        backtrack(0)
        return res

            
            

            



