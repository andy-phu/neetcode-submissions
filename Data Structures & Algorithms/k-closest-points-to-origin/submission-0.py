class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pt_map = collections.defaultdict()
        distances = []
        #assign their distances as key and val as the pair
        for p in points:
            x = p[0]
            y = p[1]

            left = x ** 2 
            right = y ** 2 

            combined = left + right 
            distance = combined ** 0.5

            distances.append((distance, x,y))

        heapq.heapify(distances)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(distances)

            res.append([x,y])


            


        return res


        



