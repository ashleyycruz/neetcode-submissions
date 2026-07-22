class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0]) # always non empty 

        top, bot = 0, ROWS - 1 # two pointers: top row (o) & last row (-1)

        while top <= bot: # binary search till you fid target or not 
                
            row = (top + bot) // 2 # calc for binary search 

            if target > matrix[row][-1]: # look at the right most and check if target value is greater 
                top = row + 1 # down is large 

            elif target < matrix [row][0]: # look at the left most and check if target value is less than 
                bot = row - 1 # up is smaller 

            else:
                break       

        # second search starts 

        if not (top <= bot): # not in the range at all
            return False 

        row = (top + bot) // 2 # calc for binary search ( for row found )
        l, r = 0, COLS - 1 

        while l <= r: # if left passes 

            m = (l + r) // 2 # calc mid point 

            if target > matrix [row][m]: # if we find value is greater 
                l = m + 1 #search to the right

            elif target < matrix [row][m]: #if we find value is less 
                r = m - 1 # search to the left
            
            else:
                return True 

        return False   # if we still can't find anything     




