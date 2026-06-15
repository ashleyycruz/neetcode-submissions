class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #hashmap 

        # loop through s and make an hashmap 
        # set up key for every letter 
        if len(s) != len(t):
            return False

        count = {}

        for char in s:

            # adding/updating a key (incrementing count of a character)
            count[char] = count.get(char, 0) + 1

        for char in t:
            count[char] = count.get(char,0) - 1
            if count[char] < 0:  
                return False
                
        return True    




            






        