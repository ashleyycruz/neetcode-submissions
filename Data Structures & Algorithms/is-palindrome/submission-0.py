class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0

        # clean string 
        clean_list = []

        # loop through every character in s
        for ch in s:

            if ch.isalnum(): # character and numbers 

                # convert each character to lowercase
                clean_list.append(ch.lower())

        # set right
        right = len(clean_list) - 1

        while left < right:

            if clean_list[left] == clean_list[right]:

                left += 1
                right -= 1

            else:

                return False

        return True   


        
        