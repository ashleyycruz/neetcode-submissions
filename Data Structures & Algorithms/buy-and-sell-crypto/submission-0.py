class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        prices --> a int array 
        prices[i] --> price of NeetCoin on the ith day
        choose one day to buy 
        then a different day to sell 
        return maximum porfit 
        can choose to make no trancactions --> would make it zero 
        '''

        # two pointer
        # pointers next to each other
        left,right = 0 , 1
        profit = 0  
        # check if the value next is greater
        # if greater then keep moving to greatest value
        # track highest number 
        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left] # the subtraction 
                profit = max (profit, current_profit)
            else: 
                left = right 

            right += 1
        # return output
        return profit 
