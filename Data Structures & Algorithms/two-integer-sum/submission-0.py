class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        # create a hashmap 
        prevMap = {} #val : index 

        for i, n in enumerate(nums): # enumerate turn value & index
            diff = target - n # find the different based on value
            if diff in prevMap:  # if diff is found
                return [prevMap[diff], i] # then return the pair
            prevMap[n] = i # stores the number and values