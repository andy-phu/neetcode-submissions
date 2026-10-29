class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #[30,38,30,36,35,40,28]
        #[(40,5) (28,6)


        #add each to stack with temp, index
          #keep pop from stack when top of stack < current temp
        #add current temp to stack
        stack = []

        results = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                topVal, topI = stack.pop()

                distance = i - topI
                results[topI] = distance

            stack.append((temperatures[i],i))

        for s, i in stack:
            results[i] = 0

        return results
     