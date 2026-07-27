class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # create set 
        longest = 0 # intialize longest

        for n in nums: # n iterate through nums (inital array)

            if ( n - 1 ) not in numSet: # if not a left neighbor 
                length = 0 # start a new sequence 
                while ( n + length ) in numSet: # check right neighnor 
                    length +=1 # if found add to length

                longest = max (length, longest)  # find the max 

        return longest 
        