class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        index1, index2 = 0, len(numbers) - 1 # two pointer 

        while index1 < index2: # while index2 is greater (the whole time & makes sure no duplicates ) 
            if  target < numbers[index1] + numbers[index2] : # too big
                index2 -= 1 # remove from index2
            elif target > numbers[index1] + numbers[index2]: # too small
                index1 += 1 # remove from index1
            else: 
                return [index1 +1 , index2 + 1] # else return answer 


