class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):   # visit all rows and cols at once 
            for col in range(9):
                value = board[row][col]

                if value == '.': # skip empty value 
                    continue

                box_index = (row // 3) * 3 + (col // 3) # 3x3 formula 

                # checking if value in any set indepedently else false 
                if value in rows[row] or value in cols[col] or value in boxes[box_index]:
                    return False
                # if value passes all three 
                rows[row].add(value)
                cols[col].add(value)
                boxes[box_index].add(value)

        return True