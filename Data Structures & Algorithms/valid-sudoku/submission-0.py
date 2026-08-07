class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmap = {}

        for i, row in enumerate(board):
            hmap[i] = tuple(row)
            
        # check rows
        for row in hmap:
            check_dupes = set()
            for i in hmap[row]:
                if i == ".":
                    continue
                elif i in check_dupes:
                    return False
                
                check_dupes.add(i)
                    
        # check columns
        for j in range(9):  # need 0th element of each row 
            check_dupes = set()
            for row in hmap:
                cand = hmap[row][j]
                if cand == ".":
                    continue
                elif cand in check_dupes:
                    return False
                
                check_dupes.add(cand)
                    
        # check squares
        squares = [set() for _ in range(0, 9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue 
                
                box_idx = (r//3) * 3 + (c//3)
                
                if val in squares[box_idx]:
                    return False
                squares[box_idx].add(val)
        
        return True