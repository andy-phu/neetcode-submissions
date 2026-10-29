class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #if there is a symbol pop 2 from stack and put the first to the right and second to the left 

        numberStack = []
        
        for t in tokens: 
        
          
            res = 0

            if t == "+":
                res = numberStack.pop() + numberStack.pop() 
                numberStack.append(res)
            elif t == "*":
                res = numberStack.pop() * numberStack.pop() 
                numberStack.append(res)
            elif t == "/":
                right, left = numberStack.pop(), numberStack.pop()
                res = int(float(left) / right )
                numberStack.append(res)
            elif t == "-":
                right, left = numberStack.pop(), numberStack.pop()
                res = left - right 
                numberStack.append(res)
            else:
                numberStack.append(int(t))


        return numberStack[0]