class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        - for each index store the min element from that index to the right and the index where that min element resides 
        - for each new index check the min element that was stored to the right and if the min element is > than our current element that means we can do our current element + len(heights - current_index) * heights[current_index]
        - can do the same for going to the right 
        
        
        - use a stack to put the index,val onto the stack 
        - for each new element pop from the stack if the current element is greater than the top of the stack that way the stack's top maintains the local minimas for the current index that is being explored 


        - when you reach a new element and you see from the stack that the top of the stack is less than the current element that is the bound you use 
        - that way this stack is live and consistently maintains the bounds 


        - a bound is established from the top of the stack and you stop popping once you reach a top that is less than the current element 
        """

        left_stack = []
        right_stack = []

        left_bounds = dict() 
        right_bounds = dict()

        def bounds_finder(stack, bounds, i, direction):
            while stack and heights[i] <= stack[-1][1]:
                stack.pop()

            if not stack: 
                if direction == "left":
                    bounds[i] = -1
                else:
                    bounds[i] = len(heights)
            else:
                bounds[i] = stack[-1][0]

            stack.append((i, heights[i]))

        for r in range(len(heights)-1,-1,-1):
            bounds_finder(right_stack, right_bounds, r, "right")



        area = float('-inf')
        for l in range(len(heights)):
            bounds_finder(left_stack, left_bounds, l, "left")
            right_bound = right_bounds[l]
            left_bound = left_bounds[l]

            length = right_bound - left_bound - 1 
       

            area = max(area, length * heights[l]) 

    
        return area





        


        
