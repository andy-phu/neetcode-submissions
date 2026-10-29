class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        - find the row where the first integer is the largest integer that is less than the target
        - then do binary search on the row to see if the target is in there 
        - before doing binary search you can check the last element in the row and see if our 
        target is less than it

         
        
        1, 10, 14
                  l      
               r
        
        """

        #binary search to find the correct row
        ROWS, COLS = len(matrix), len(matrix[0])
        l,r = 0, ROWS - 1

        while l <= r:
            mid = (l+r) // 2

            if matrix[mid][0] > target:
                r = mid - 1 
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                return True

        target_row = r

        if matrix[target_row][-1] < target:
            return False

        
        l,r = 0, COLS - 1

        while l <= r:
            mid = (l+r) // 2

            if matrix[target_row][mid] > target:
                r = mid - 1 
            elif matrix[target_row][mid] < target:
                l = mid + 1
            else:
                return True

        return False 

               