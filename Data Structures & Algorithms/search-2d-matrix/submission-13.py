class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][0] == target or matrix[mid][-1] == target or (target > matrix[mid][0] and target < matrix[mid][-1]):
                row = mid 
                break
            elif  matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1 

        if row == -1:
            return False


        l,r = 0, len(matrix[0])

        while l <= r: 
            mid = (l + r) // 2
            curr = matrix[row][mid] 

            if curr == target:
                return True 
            elif curr < target: 
                l = mid + 1 
            elif curr > target:
                r = mid - 1
        
        return False