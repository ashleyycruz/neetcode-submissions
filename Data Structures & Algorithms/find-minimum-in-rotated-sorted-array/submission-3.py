class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = nums[0]
        i = 0

        while i < len(nums):
            if nums[i] < min_num:
                min_num = nums[i]

            i += 1

        return min_num







