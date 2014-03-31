## almost the same as N_Queens2.py
class Solution:
    # @return an integer
    def __init__(self):
        self.ans = []
    def solveNQueens(self, n):
        self.solve([], 0 ,n)
        return self.ans
    def solve(self, pos, i, n):
        if i == n:
            new_sol = []
            for point in pos:
                row = ''
                for j in range(0,n):
                    if j == point[1]:
                        row += 'Q'
                    else:
                        row += '.'
                new_sol.append(row)
            self.ans.append(new_sol)
            return
        for j in range(0,n):
            flag = False
            for point in pos:
                if point[0] == i:
                    flag = True
                if point[1] == j:
                    flag = True
                if j - point[1] == i - point[0]:
                    flag = True
                if j - point[1] == point[0] - i:
                    flag = True
            if flag == False:
                pos.append([i,j])
                self.solve(pos, i+1, n)
            if flag == False:
                pos.pop()
