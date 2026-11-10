class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        - detect cycles 
        - for every node do a dfs and when you complete the dfs on a node mark it as true or false to say if this node leads to a cycle or not that way when we do a future node we don't have to do the same work 
        
        
        """
        
        if len(edges) > (n - 1):
            return False


        graph = dict()

        for i in range(n):
            graph[i] = []




        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)


        visited = set()  

        def dfs(node, parent):
            if node in visited: 
                return False 
            
            visited.add(node)

            for neigh in graph[node]:
                if neigh == parent:
                    continue 

                if not dfs(neigh, node):
                    return False 

            return True 



        res = dfs(0, -1)

        if res and len(visited) == n:
            return True 
        else:
            return False 
        
        


            
