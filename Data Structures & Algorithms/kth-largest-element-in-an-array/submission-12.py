class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        [3,5]

        - use a min heap to store the k largest elements 
        - check the minheap and if the minheap is size k check if our current element is > the top if so pop and add our current element 

        """

        minheap = []
        
        for n in nums: 
            
            heapq.heappush(minheap, n)
            if len(minheap) > k:
                heapq.heappop(minheap)


        return minheap[0]