class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        - store the left parenthesis index inside one stack
        - everytime we get a right parenthesis pop from left parenthesis stack
        - everytime we get a start put its index in a separate stack
        - after we gone through the whole string we keep trying to pop the left parenthesis stack if the top of the star stack is greater index than the left parenthesis 

        (*(*
        
        
        """



        leftStack = []
        starStack = []


        for i, c in enumerate(s):
            if c == "(":
                leftStack.append(i)
            elif c == "*":
                starStack.append(i)
            elif c == ")":
                if len(leftStack) > 0:
                    leftStack.pop()
                elif len(starStack) > 0:
                    starStack.pop()
                else:
                    return False 

        while True:
            if len(leftStack) == 0:
                return True

            if len(starStack) == 0: 
                return False 

            if leftStack[-1] < starStack[-1]:
                leftStack.pop()
                starStack.pop()
            else:
                return False 

        
