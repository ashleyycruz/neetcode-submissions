class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        one lane highway & in the same direction 
        array position = length n ( ith car in miles )
        array speed = length n ( ith car in mph )
        destination = positon target 
        no cars get pass ahead only be equal ( >= less than or equal to)
        if one catches up to a car fleet then considered to be part of the fleet
        a car fleet is a non non emptpy set of cars driving at same position & same speed
        a single car == car fleet 
        return # of different car fleets that arrive to target ( destination )
        '''

        # create pairs ( position, speed )
        pair = [[p, s]for p, s in zip(position, speed)]
        stack = []

        # sort & resverse 
        for p, s in sorted(pair)[::-1]:
        
        # meaure distance and calcuate time to target
            stack.append ((target - p) / s)

        # if higher or equal ( becomes a car fleet )
        # pop once a part of fleet 
        # if less ( doesnt go with that car fleet )

            if len(stack) >= 2 and stack [-1] <= stack [-2]:
                stack.pop()

        # return len of stack 
        return len(stack)






        