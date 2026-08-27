class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # integer array --> piles 
        # piles[i] --> # of bananas in curtain pile 

        # h --> number of hours you eat all the bananas 

        # k --> decide bananas per hour eating rate  

        # trying to find at what minium rate each banana can eaten the fastest way  

        # If I choose a specific k, how many hours would it take to finish all the piles?
        # h is what you can't exceed 
        
        l, r = 1, max(piles) # set pointers
        res = r # set to right to start at max number 

        while l <= r: # make sure right isnt on the left 

            k = ( l + r ) // 2 # start from the middle 
            hours = 0 # set hours 

            for p in piles: # check in piles  
                hours += math.ceil(p/k) # do math to check h 

            if hours <= h: # if doesnt pass h
                res = min (res,k) # update min
                r = k - 1 # look for smaller 
            else: 
                l = k + 1 # look for bigger 

        return res 







        



                    