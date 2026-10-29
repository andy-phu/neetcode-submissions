class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #find substrings of length 3 
        #compare it to the array of s1 as a char array 

        charArray = []

        for i in range(26):
            charArray.append(0) 

        for c in s1:
            charArray[ord(c) - ord('a')] += 1

        #find the subStrings that are length of 3 



        for l in range(len(s2)):
            for r in range(l, len(s2)):
                if (r-l+1) == len(s1):
                    tempArray = []
                    for i in range(26):
                        tempArray.append(0)
                    for c in s2[l:r+1]:
                        tempArray[ord(c) - ord('a')] += 1

                    if tempArray == charArray:
                        return True 

        return False
