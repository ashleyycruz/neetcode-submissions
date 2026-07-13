class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        while l <= r: 
            
            m = l + (( r - l )// 2) # calcuate midpoint and add to l ( prevent overflow )
            
            if nums[m] > target: # if target is less 
                r = m - 1 # remove all to the right 
            elif nums[m] < target: # if target is larger
                l = m + 1 # remove all to the left
            else: 
                return m # middle point if one nums

        return -1                