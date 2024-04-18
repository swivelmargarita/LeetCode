class Solution:
    def isValidBlock(self, block: list[list[str]]):
        n = 3
        digits = set()
        for i in range(n):
            for j in range(n):
                if block[i][j] in digits:
                    return False
                digits.add(block[i][j])
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = 9
        for i in range(0, n, 3):#From [0 to n) adding 3 each iteration
            for j in range(0, n, 3):
                nums = set()
                for row in board[i:i+3]:
                    for num in row[j:j+3]:
                        if num in nums:
                            return False
                        if num != '.':
                            nums.add(num)
        for i in range(n):
            nums = set()
            for j in range(n):
                num = board[i][j]
                if num in nums:
                    return False
                if num != '.':
                    nums.add(num)

        for i in range(n):
            nums = set()
            for j in range(n):
                num = board[j][i]
                if num in nums:
                    return False
                if num != '.':
                    nums.add(num)
        return True

   
if __name__ == "__main__":

    board = [["5","3",".",".","7",".",".",".","."]
             ,["6",".",".","1","9","5",".",".","."]
             ,[".","9","8",".",".",".",".","6","."]
             ,["8",".",".",".","6",".",".",".","3"]
             ,["4",".",".","8",".","3",".",".","1"]
             ,["7",".",".",".","2",".",".",".","6"]
             ,[".","6",".",".",".",".","2","8","."]
             ,[".",".",".","4","1","9",".",".","5"]
             ,[".",".",".",".","8",".",".","7","9"]]
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    solution = Solution().isValidSudoku(board)
    print(solution)

         
