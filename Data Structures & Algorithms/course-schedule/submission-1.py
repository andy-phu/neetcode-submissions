class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if there is a cycle return false
        #if the course is not in the prereq map then return true
        #run dfs on all numbers from 0 - len(numCourses-1)
        #everytime we run dfs we add to visited set
        #everytime we finish dfs for that number we remove from visited
        #if we go through all the prereqs and none of them return false then we return true


        visited = set()
        prereq = dict()
        
        #populate our prereq map
        for p,c in prerequisites:
            if c in prereq:
                prereq[c].append(p)
            else:
                prereq[c] = [p]
        
        def dfs(n):
            if n in visited:
                return False
            
            if n not in prereq:
                return True
            
            visited.add(n)
            for child in prereq[n]:
                if not dfs(child):
                    return False
            visited.remove(n)
            del prereq[n]

            return True
        



        for n in range(numCourses):
            if not dfs(n):
                return False


        return True




