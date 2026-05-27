class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()  

        #ranging
        for num in nums:  # check & add
            if num in seen: # not in seen then add
                return True # if found again return true
            seen.add(num) # not found so added to seen
        return False  
 




        