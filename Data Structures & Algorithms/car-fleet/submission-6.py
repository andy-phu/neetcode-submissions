class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carArr = []


        for i in range(len(position)):
            carArr.append((position[i], speed[i]))

        #sort in descending order 

        carArr.sort()
        stack = []


        for c in carArr[::-1]:
            time = (target-c[0]) / c[1]
            stack.append(time)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)