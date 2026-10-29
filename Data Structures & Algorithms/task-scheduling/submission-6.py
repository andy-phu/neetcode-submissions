class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        [(0,2), (0,2)]
        time = 1
        [(0,2), (4,1)]
        time =  2
        [(4,1),  (5,1)]
        time = 3
        [(4,1),  (5,1)]
        time = 4
        [(5,1)]
        time = 5
        []

        
        [(0,3), (0,1), (0,1)]
        time = 1
        [(2,1), (3,1), (5,2)]
        time = 2
        [(3,1), (5,2)]
        time = 3
        [(5,2)]
        time = 5
        [(9,1)]
        time = 9
        []
       

        [(0,2), (0,1)]
        time = 1
        [(0,1), (2,1)]
        time = 2 
        [(2,1)]
        time = 3 
        []





        - bucket the tasks in groups of timestamp in (0, count of duplicates in tasks)
        - create a min heap based on this bucket of array
        - pop from minheap and if the counter is < the timestamp then add the difference between timestamp and counter to the counter and decrement the count and add it back to the heap
        - add back to the heap and increment the timestamp by doing current timer + n+1
        """

        hMap = dict()

        for t in tasks:
            if t not in hMap:
                hMap[t] = 1
            else:
                hMap[t] += 1
      
        buckets = []
        for val in hMap.values():
            buckets.append((-val))
      
        heapq.heapify(buckets)
        q = deque()

        time = 0
        while q or buckets:
            time += 1
  
            if buckets:
                count = heapq.heappop(buckets)

                count += 1

                if count < 0:
                    q.append((count, time + n))
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                c, t = q.popleft()
                
                heapq.heappush(buckets, c)
            
        return time
            














