class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #construct graph and run bfs 
        #for each layer only add nodes whose layer is less than k
        
        #if the node that we are at is equal to destination update our minPath

        #key = src value = array of tuples of dest, weight
        graph = dict()
        minPath = float('inf')
        prices = [float('inf')] * n 
        prices[src] = 0


        for s, d, price in flights:
            if s not in graph:
                graph[s] = [(d, price)]
                heapq.heapify(graph[s])
            else:
                heapq.heappush(graph[s], (d, price))

        q = deque()
        if src not in graph:
            return -1
        
        
        q.append((src, 0, 0))

        while q:
            d,p, stop = q.popleft()
            
            if stop > k+1: 
                continue

            if d == dst:
                minPath = min(minPath, p)
                continue
            

            if d in graph:
                for child, childPrice in graph[d]:
                    newPrice = childPrice + p 
                    if newPrice < prices[child]:
                        q.append((child, newPrice, stop + 1))
                        prices[child] = newPrice

            

        if minPath == float('inf'):
            return -1
        else:
            return minPath






