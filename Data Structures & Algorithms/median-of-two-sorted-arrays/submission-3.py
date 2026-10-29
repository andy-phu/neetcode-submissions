class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A 

        total = len(A) + len(B)
        half = total // 2 
        l,r = 0, len(A)-1
        while True:
            tailA = (l + r) // 2
            lengthA = tailA + 1 
            lengthB = half - lengthA 
            tailB = lengthB - 1  

            # expanded form of tailB: half - (tailA + 1) - 1 

            aRight = float("inf")
            bRight = float("inf")
            aValue = float("-inf")
            bValue = float("-inf")
            if tailA+1 < len(A): 
                aRight = A[tailA+1]
            if tailB + 1 < len(B):
                bRight = B[tailB+1]
            if tailA >= 0:
                aValue = A[tailA]
            if tailB >= 0:
                bValue = B[tailB] 

            #first check if we sectioned off the right left partition for both arrays

            if aValue <= bRight and bValue <= aRight:
                #even we want to get the mean between the largest in the left partition and the smallest from right partition
                if total % 2 == 0:
                    smallRight = min(aRight, bRight)
                    largeLeft = max(aValue, bValue)
                    return (smallRight + largeLeft) / 2 
                else:
                    return min(aRight, bRight)
            elif aValue > bRight:
                r = tailA - 1
            else: 
                l = tailA + 1 


            

                

            



