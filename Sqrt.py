## use binary search
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0
        start = 1
        end = x
        while start<=end:
            half = start + int((end-start)/2)
            if half > x/half:
                end = half - 1
            else:
                ans =  half
                start = half + 1
        return ans
