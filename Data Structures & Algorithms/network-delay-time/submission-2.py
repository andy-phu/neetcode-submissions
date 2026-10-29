class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = dict()
        # (time, target)
        minHeap = []
        visited = set()
        time = 0

        for src, target, time in times:
            if src not in graph:
                graph[src] = []
            graph[src].append((target, time))

  
        if k in graph: 
            visited.add(k)
            for neigh, neighTime in graph[k]:
                heapq.heappush(minHeap, (neighTime, neigh))

        while minHeap:
            nodeTime, node = heapq.heappop(minHeap)
            if node in visited:
                continue 
            visited.add(node)
            time = nodeTime
            if node not in graph:
                continue
            for neigh, neighTime in graph[node]:
                if neigh not in visited:
                    heapq.heappush(minHeap, (neighTime + nodeTime, neigh))
        
        return time if len(visited) == n else -1



            
