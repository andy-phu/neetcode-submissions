class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        - amt of closing has to be less than the amt of opening parenthesis
        - when closing == opening == n then we return 1
        - two choices add a closing and add an opening 
        - can add an opening whenever
        - can add a closing only when opening > closing 

        
        
        
        """
        res = []
        dp = dict()
        def backtrack(opening, closing, path):
            if closing == opening == n:
                res.append("".join(path))
                return 

            ways = 0
            #add an opening
            if opening < n:
                path.append("(")
                backtrack(opening + 1, closing, path)
                path.pop()

            #add a closing if opening > closing 
            if opening > closing and closing < n:
                path.append(")")
                backtrack(opening, closing + 1, path)
                path.pop()

        backtrack(0,0,[])
        return res 

           
        
        

            


