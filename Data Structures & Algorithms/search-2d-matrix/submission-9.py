class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        for m in range(len(matrix)):
            if (target > matrix[m][0] and target < matrix[m][-1]) or target == matrix[m][0] or target == matrix[m][-1]:
                row = m
                break; 

        if row == -1:
            return False

        l,r = 0, len(matrix[0])
        print(f"row: {row}")
        while l <= r: 
            mid = (l + r) // 2
            print(f"mid: {mid}")
            curr = matrix[row][mid] 
            print(curr)
            if curr == target:
                return True 
            elif curr < target: 
                l = mid + 1 
            elif curr > target:
                r = mid - 1
        
        return False