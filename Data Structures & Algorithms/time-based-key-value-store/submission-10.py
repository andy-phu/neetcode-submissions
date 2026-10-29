class TimeMap:

    def __init__(self):
        self.map = dict()


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        l,r = 0, len(self.map[key])-1

        while l < r: 
            mid = (r + l) // 2 #does floor division
            midTimestamp = self.map[key][mid][0]
            if midTimestamp < timestamp:
                l = mid + 1 
            elif midTimestamp > timestamp: 
                r = mid - 1 
            else:
                return self.map[key][mid][1]

        if self.map[key][l][0] <= timestamp:
            return self.map[key][l][1]
        elif l > 0: 
            return self.map[key][l-1][1]
        else:
            return ""





"""

alice : (1, happy) (2, sad) (3, sad) (5, mad)
get(alice, 1)



- binary search the sorted array of values
- when we arrive at the last element where there is only one value we evaluate 
- if the last elem <= our desired timestamp we return the value of the last elem
- else return the value of the elem to the one to the left if the index we are on is > 0 if it's = 0 then return -1
"""


