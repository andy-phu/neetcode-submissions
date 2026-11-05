class Solution:
    def trap(self, height: List[int]) -> int:
        """
         [0,2,0,3,1,0,1,3,2,1]
leftMax= [0,0,2,2,3,3,3,3,3,3]
rightMax=[3,3,3,3,3,3,3,2,1,0]
        
        
        
        
        
        """



        leftMax = []
        rightMax = []

        globalLeftMax = 0
        globalRightMax = 0
        for h in height: 
            if not leftMax:
                leftMax.append(0)
            else:
                leftMax.append(globalLeftMax)
            globalLeftMax = max(h, globalLeftMax)

        for i in range(len(height) - 1, -1, -1):
            if not rightMax:
                rightMax.append(0)
            else:
                rightMax.append(globalRightMax)
            globalRightMax = max(globalRightMax, height[i])
                
        rightMax.reverse()
        # print(leftMax)
        # print(rightMax)
        water = 0 
        for i in range(len(height)):
            curr = min(leftMax[i], rightMax[i]) - height[i]
            if curr > 0:
                water += curr 

        return water

            


            