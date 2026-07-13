class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialization
        col = {i: set() for i in range(9)}
        square = {(i,j): set() for i in range(3) for j in range(3)}
        
        for ri, row in enumerate(board):
            # Check Rule 1
            row_filtered = [e for e in row if e != "."]
            if len(set(row_filtered)) != len(row_filtered):
                return False
            
            for ci, elem in enumerate(row):
                if elem == ".":
                    continue

                # Check Rule 2
                if elem in col[ci]:
                    return False
                col[ci].add(elem)
            
                # Check Rule 3
                if elem in square[(ri // 3,ci // 3)]:
                    return False
                square[(ri // 3,ci // 3)].add(elem)
        
        return True