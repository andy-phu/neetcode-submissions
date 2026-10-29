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

        def populated(positions, newR, newC): 
  
            for r,c in positions:
                if r == -1 or c == -1:
                    return False
                #up,down
                #right,left
                if newR == r or newC == c:
                    return False
                #diagonal
                if abs(newR-r) == abs(newC-c):
                    return False

            return True
        
        res = []
        def backtrack(r, positions):
            if r == n and len(positions) == n:
                #todo: reconstruct 2d array
                grid = []
                for r,c in positions:
                    temp = []
                    for i in range(n):
                        if i == c:
                            temp.append("Q")
                        else:
                            temp.append(".")
                    stringArr = "".join(temp)
                    grid.append(stringArr)

                res.append(grid)
                return

            for c in range(n): 
                if populated(positions, r, c):
                    positions.append((r,c))
                    backtrack(r+1, positions)
                    positions.pop()

        backtrack(0,[])
        return res

            
            

            



