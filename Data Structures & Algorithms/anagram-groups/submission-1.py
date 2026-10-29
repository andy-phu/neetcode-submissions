class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a an arr where each index represents a letter's numerical value
        #every word we come across convert it to the array representation then append to the map's arr of words based on the array representation

        hmap = dict()


        for word in strs: 
            #convert to array
            arr = [0] * 26
            for c in word: 
                arr[ord(c) - ord('a')] += 1
            
            tArr = tuple(arr)

            if tArr not in hmap:
                hmap[tArr] = [word]
            else:
                hmap[tArr].append(word)
        
        res = []
        for val in hmap.values():
            res.append(val)
        return res