## use the function from problem Largest Rectangle in Histogram
## the other thing is simple
class Solution:
    # @param height, a list of integer
    # @return an integer
    def maximalRectangle(self, matrix):
        row_len = len(matrix)
        if row_len == 0:
            return 0
        col_len = len(matrix[0])
        i = 0
        while i < row_len:
            j = 0
            while j < col_len:
                matrix[i][j] = int(matrix[i][j])
                j += 1
            i += 1
        row = matrix[0]
        ans = self.largestRectangleArea(row)
        i = 1
        while i < row_len:
            j = 0
            while j < col_len:
                if matrix[i][j] == 1:
                    row[j] += 1
                else:
                    row[j] = 0
                j += 1
            ans = max(ans, self.largestRectangleArea(row))
            i += 1
        return ans
                    
        
    def largestRectangleArea(self, height):
        x = self.solve(height)
        height.reverse()
        y = self.solve(height)
        length = len(height)
        i = 0
        ans = 0
        height.reverse()
        while i < length:
            ans = max(ans, height[i] * (length - 2 - x[i] - y[length-1-i]))
            i += 1
        return ans

    def solve(self, height):
        dic = {}
        length = len(height)
        if length == 0:
            return 0
        dic[0] = -1
        i = 1
        while i < length:
            tmp = i - 1
            while tmp >= 0:
                if height[i] > height[tmp]:
                    break
                tmp = dic[tmp]
            dic[i] = tmp
            i += 1
        return dic
