class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        pacific set = all row 0 all col 0
        atlantic set = all last row all last col

        for each cell explore 4 directions and see if you can reach a cell in a pacfic or atlantic set, if you can reach one add it into the corresponding set, keep exploring until you cant move anymore

        if a cell is already in a set dont continue exploring that cell
        
        
        
        """

        pac = set()
        atl = set() 

        ROWS, COLS = len(heights), len(heights[0])

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for i in range(COLS):
            #first row
            pac.add((0, i))
            #last row
            atl.add((ROWS-1, i))

        for i in range(ROWS):
            #first col 
            pac.add((i, 0))
            #last col
            atl.add((i, COLS-1))

        def explore(row, col, bucket):
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr,nc) in bucket or heights[row][col] > heights[nr][nc]:
                    continue 
               
                bucket.add((nr,nc))
                explore(nr, nc, bucket)
            




        #for each elem in pac and atl explore the directions it can flow by seeing if the next cell is greater than the current 
        for r,c in list(pac):
            explore(r,c, pac)

        for r,c in list(atl):
            explore(r,c, atl)
        

        intersection = pac & atl
        return list(intersection)
