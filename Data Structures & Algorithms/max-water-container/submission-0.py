class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # two pointer --> start at ends 
        res = 0
        l,r = 0, len(heights) - 1 
         
        # go through the list 
        while l < r:
            area = ( r - l ) * min(heights[l], heights[r]) # weight X height
            res = max(res, area) # give max found

            if heights[l] < heights[r]: # if right bigger
                l += 1 # move left
            else:
                r -= 1 # or move right

        return res #print results 
            


                