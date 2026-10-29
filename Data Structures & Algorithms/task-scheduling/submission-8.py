class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        ["X","X","Y","Y"]
        X: 2
        Y: 2

        2,2 

        (2, 0) (2, 0) maxHeap 
        cooldown = [] minheap

        time = 0
        heap = [(2,0)]
        cooldown = [(3,1)]

        time = 1 
        heap = []
        cooldown = [(3,1), (4,1)]

        time = 2
        heap = []
        cooldown = [(3,1), (4,1)]

        time = 3
        heap = [(1,3)]
        cooldown = [(4,1)]

        time = 4
        heap = [(4,1)]
        cooldown = [(4,1)]

        time = 5
        heap = []
        cooldown = []
        

        - maxHeap to represent what it available to complete (quantity, time)
        - minHeap to represent what is on cooldown (time, quantity)
        - at a certain time pop everything from cooldown that is <= curr time
        - when we pop from maxHeap we do n+1 to the time in our heap

        """

        counter = {}

        for t in tasks:
            if t not in counter:
                counter[t] = 1
            else:
                counter[t] += 1

        maxHeap = []
        cooldown = deque()
        

        for key, val in counter.items():
            maxHeap.append((-val))


        heapq.heapify(maxHeap)
    
        time = 0
        while maxHeap or cooldown:
            if maxHeap:
                quantity = heapq.heappop(maxHeap)

                cooldownTime = time + n
                newQuantity = quantity + 1
                if newQuantity < 0:
                    cooldown.append((newQuantity, cooldownTime))
            else:
                time = cooldown[0][1] 

            while cooldown and cooldown[0][1] <= time:
                quantity, _ = cooldown.popleft()
                heapq.heappush(maxHeap, (quantity))

            time += 1

        return time 

            

        

                


        










        