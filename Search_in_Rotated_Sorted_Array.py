# compare the start and the half element we could know the start point
# belongs to the head part or the tail part
# 4 5 6 7 0 1 2
# *     *     a[0] = 4 a[half] = 7 > 4 so the head belongs to the tail
# part
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A) == 0:
            return -1
        return self.solve(A, target, 0, len(A)- 1)

    def solve(self, a, target, start, end):
        if start > end:
            return -1
        half = int((end-start)/2) + start
        if a[start] == target:
            return start
        if a[end] == target:
            return end
        if a[half] == target:
            return half
        if a[start] < a[half]:
            if target > a[half] or target < a[start]:
                return self.solve(a, target, half+1, end-1)
            else:
                return self.solve(a, target, start+1, half-1)
        else:
            if target < a[half] or target > a[start]:
                return self.solve(a, target, start+1, half-1)
            else:
                return self.solve(a, target, half+1, end-1)
