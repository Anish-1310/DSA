def isValidSudoku(self, board):
        row = {}
        col = {}
        boxes = {}
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                box = (r//3,c//3)
                if r not in row:
                    row[r] = set()
                if c not in col:
                    col[c] = set()
                if box not in boxes:
                    boxes[box] = set()
                if (num in row[r] or num in col[c] or num in boxes[box]):
                    return False
                row[r].add(num)
                col[c].add(num)
                boxes[box].add(num)
        return True