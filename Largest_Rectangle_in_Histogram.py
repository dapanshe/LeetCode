## dic keeps the index record of the left nearest element in height which is
## smaller than current one, which need do this both from left and from right
## the amortized running time is O(N)
## There is a solution with only one traverse used stack which I have not 
## implemented yet
## the dic for [2,   1, 5, 6, 2, 3] 
##          is [-1, -1, 1, 2, 1, 4] 
class Solution:
    # @param height, a list of integer
    # @return an integer
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
