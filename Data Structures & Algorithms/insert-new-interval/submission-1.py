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

        while i < len(intervals):
            start,end = intervals[i][0], intervals[i][1]
            if end < newStart:
                res.append([start, end])
            else:
                break
            i+=1
        res.append([newStart, newEnd])

        for j in range(i, len(intervals)):
            topStart, topEnd = res[-1][0], res[-1][1]
            currStart, currEnd = intervals[j][0], intervals[j][1]

            if topEnd >= currStart:
                res.pop()
                res.append([min(topStart, currStart), max(topEnd, currEnd)])
            else:
                res.append([currStart, currEnd])
        return res 




       