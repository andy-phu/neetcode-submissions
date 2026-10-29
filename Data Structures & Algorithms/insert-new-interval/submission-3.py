class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """

        [[1,3],[4,6]], newInterval = [2,5]
            i j 

        res = [[1,5]]

        - put each element in intervals into a new array and when we find an element whose start is > than our start 
        - then we put our new interval first and then the current element
        - then we do a pass overmerging intervals 


        - [[1,5]]
        - check if our new start is < top of stack end
        - then we pop off the stack and get the min(currStack, newStack) and max(currEnd, newEnd)


        - go through intervals and append all intervals where the end < new start 
        - then append ours next and run the merge intervals using an array 
        """ 


        i = 0
        newStart, newEnd = newInterval[0], newInterval[1]
        res = []
        l,r = 0, len(intervals) - 1

        #binary search to find start that is greater than our new start
        
        while l <= r:
            mid = (l+r) // 2
            start, end = intervals[mid][0], intervals[mid][1]

            if start < newStart:
                l = mid + 1 
            else:
                r = mid - 1

        #r would contain the point to insert
        intervals.insert(l, newInterval)
        res = []
        for interval in intervals:
            start, end = interval[0], interval[1]
            
            if not res or res[-1][1] < start:
                res.append(interval)
            else:
                res[-1] = [min(res[-1][0], start), max(res[-1][1], end)]
        return res 




       