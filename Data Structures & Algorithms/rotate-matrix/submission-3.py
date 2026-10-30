class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        
            [1,2,3],
            [4,5,6],
            [7,8,9]
        

            [7,8,9],
            [4,5,6],
            [1,2,3]


            [3,4],
            [1,2]


            reverse the matrix vertically by making the last row now the first row 
            transpose is essentially swapping the row,col
        """


        matrix.reverse()
        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(len(matrix)):
            for c in range(r+1, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]  

        


        