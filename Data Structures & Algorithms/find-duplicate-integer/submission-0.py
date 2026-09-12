class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # created hashmap 
        integers = {}

        # while looping through nums 
        for number in nums:
        # if a new value is seen add to number and increase seen once 
            if number not in integers:
                integers[number] = 1

            else:     # if in hashmap already, add 1 
                return number
            # check what number has been seen the most & return




        