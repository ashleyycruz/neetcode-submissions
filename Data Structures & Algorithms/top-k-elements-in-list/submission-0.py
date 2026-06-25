class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        # Count how many times each number appears
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        # Sort numbers by frequency, highest first
        sorted_nums = sorted(hashmap, key=hashmap.get, reverse=True)

        # Return the first k numbers
        return sorted_nums[:k]