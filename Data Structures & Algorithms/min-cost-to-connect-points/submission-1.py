class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = dict()

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)

                if i not in graph:
                    graph[i] = set()
                if j not in graph:
                    graph[j] = set()
                
                graph[i].add((dist, j))
                graph[j].add((dist, i))

        visited = set()
        minHeap = []
        cost = 0 

        heapq.heappush(minHeap, (0, 0))

        while minHeap and len(visited) < len(points):
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            cost += weight

            if node not in graph:
                continue 
            for neighWeight, neighNode in graph[node]:
                if neighNode not in visited:
                    heapq.heappush(minHeap, (neighWeight, neighNode))

        return cost


