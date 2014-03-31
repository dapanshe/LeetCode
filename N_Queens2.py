## brutal force find all solutions
class Solution:
    # @return an integer
    def __init__(self):
        self.ans = 0
    def totalNQueens(self, n):
        self.solve([],0 ,n)
        return self.ans
    def solve(self, pos, i, n):
        if i == n:
            self.ans += 1
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
