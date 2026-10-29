class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def compatible(word1, word2):
            mismatches = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    mismatches += 1
                if mismatches > 1:
                    return False
            return True


        graph = {}
        wordList.append(beginWord)
        for i in range(len(wordList)):
            currentWord = wordList[i]
            for j in range(i+1, len(wordList)):
                neighWord = wordList[j]

                if compatible(currentWord, neighWord):
                    if currentWord not in graph:
                        graph[currentWord] = []
                    if neighWord not in graph:
                        graph[neighWord] = []

                    graph[currentWord].append(neighWord)
                    graph[neighWord].append(currentWord)
        queue = deque()
        res = 0
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)
        while queue: 
            res += 1         
            for i in range(len(queue)):
                curr = queue.popleft()  
    
                #get the neighbors and add it to the queue
                if curr == endWord:
                    return res 
                if curr not in graph:
                    continue
                for neigh in graph[curr]:
                    if neigh not in visited:
                        queue.append(neigh)
                        visited.add(neigh)
        return 0 

                




