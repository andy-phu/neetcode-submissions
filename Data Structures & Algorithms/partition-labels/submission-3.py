class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        
        xyxxyzbzbbisl
             l
              r

        res = [xy,  ]

        xyxxyzbzbbi s l
        0123456789101112
        indexMap
        x : 0, 3
        y : 1, 4
        z: 5, 7
        b: 6, 9 
        i: 10, 10
        s: 11, 11
        l: 12, 12

        [(0,3) (1,4)] [(5,7) (6,9)] (10,10) (12,12)

        res = [(0,4), (5,7)]

        - put in a hashmap the characters first and last index seen can use min/max
        - put them into an array and sort the array based on the first index
        - and merge the tuples based on left[1] > right[0]
        - check the last elem in the array for this property and if it can be merged pop and put in last elem 0 and current index 1
        
        1st path: shift r and get the current substring
            - we store the current substring in our reuslt
            - start a new backtrack call where r += 1 and l = r + 1 
        2nd path: shift r and dont get the current substring until we reach the end 

        both paths if r is in a prev substring return false 




        - if r is in a prev substring then return false
        - else add l:r as a substring and 
            move r over -> expand and add current 
            move l to r+1 and move r to r+1 -> add current into res if no letters are in the prev substrings
        - keep track in a set what letters are used in a previous substring 
        """



        map = dict()
        for i,c in enumerate(s):
            if c not in map:
                map[c] = [i,i]
            else:
                map[c][1] = max(map[c][1], i)
        
        sortedArr = list(map.values())
        
        sortedArr.sort()
        print(sortedArr)
        res = []
        
        for first, last in sortedArr:
            if len(res) == 0:
                res.append((first, last))
            else:
                topFirst, topLast = res[-1][0], res[-1][1]
                
                if topLast > first:
                    res.pop()
                    res.append((topFirst, max(topLast, last)))
                else:
                    res.append((first, last))



        final = []
        for l,r in res:
            final.append(r-l+1)

        return final

                
            