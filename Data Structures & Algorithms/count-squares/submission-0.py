class CountSquares:

    def __init__(self):
        self.counter = dict()
        self.x_bound = 0
        self.y_bound = 0

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point not in self.counter:
            self.counter[tuple(point)] = 1
        else:
            self.counter[tuple(point)] += 1

        self.x_bound = max(self.x_bound, point[0]) 
        self.y_bound = max(self.y_bound, point[1])

    def count(self, point: List[int]) -> int:
        """
        left-up expansion
        (2,1) : (1,1) (2,2) (1,2)
        (2,1) : (0,1) (0,3) (2,3)
        left : 0,-1
        up   : 0,1
        left-diag : -1, 1
        
        right-up expansion
        (2,1) : (3,1) (3,2) (2,2)
        
        add into a map the point and the amt of points at that coordinate
        """ 
        target_x = point[0]
        target_y = point[1]
        if not self.counter or (target_x > self.x_bound and target_y > self.y_bound):
            return 0

       
        highest_bound = max(self.x_bound, self.y_bound)

        def expansion(dir_x, dir_y):
            #keep expanding in this direction and total up the amount
            ways = 0

            for multiplier in range(1, highest_bound+1):
                current_ways = 0

                new_dir_x, new_dir_y = dir_x * multiplier, dir_y * multiplier

                new_horizontal = (target_x + new_dir_x, target_y)
                new_vertical = (target_x, target_y + new_dir_y)
                new_diagonal = (target_x + new_dir_x, target_y + new_dir_y)

                if new_horizontal in self.counter and new_vertical in self.counter and new_diagonal in self.counter:
                    current_ways = 1 

                    current_ways *= self.counter[new_horizontal]
                    current_ways *= self.counter[new_vertical]
                    current_ways *= self.counter[new_diagonal]

                ways += current_ways

            return ways
        
        return expansion(-1,1) + expansion(1,1) + expansion(1,-1) + expansion(-1,-1)

                

                
