class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()

        graph = dict()
        indegrees = dict()

        for n in range(numCourses):
            indegrees[n] = 0

        for c, p in prerequisites:
            if p not in graph:
                graph[p] = []
            graph[p].append(c)
            indegrees[c] += 1

        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        #will contain the classes we can take first without waiting
        res = []
        while queue:
            node = queue.popleft()

            if indegrees[node] == 0:
                res.append(node)
            if node in graph:
                for neigh in graph[node]:
                    #decrement the edges in degrees 
                    indegrees[neigh] -= 1

                    if indegrees[neigh] == 0:
                        queue.append(neigh)
            
        if len(res) == numCourses:
            return res
        else:
            return []
                

     