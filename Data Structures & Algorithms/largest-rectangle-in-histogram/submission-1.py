class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        - for each index calculate the furthest the index can extend to the left and if you reach another element that is less than the top of the stack calculat the area because you can't extend more to the right 
        
        """





        stack = []
        area = 0

        for i in range(len(heights)):
            current_height = heights[i]

            if not stack: 
                stack.append((i, current_height))
            else:
                popped_index = -1 
                while stack and current_height < stack[-1][1]:
                    popped = stack.pop()
                    popped_index = popped[0]
                    popped_height = popped[1]

                    area = max(area, popped_height * (i - popped_index))

                if popped_index != -1: 
                    stack.append((popped_index, current_height))
                else: 
                    stack.append((i, current_height))


        while stack: 
            popped = stack.pop()
            popped_index = popped[0]
            popped_height = popped[1]

            area = max(area, popped_height * (len(heights) - popped_index))


        return area




