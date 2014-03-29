# solve this problem by the Kth element of two sorted arrays 
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        k = len(A) + len(B)
        if k%2 == 1:
            return self.findKthTwoArray(A,B,(k+1)/2)
        else:
            x = self.findKthTwoArray(A,B,k/2)
            y = self.findKthTwoArray(A,B,k/2+1)
            return (x+y)/2.0
    def findKthTwoArray(self,a,b,k):
        if len(a) == 0:
            return b[k-1]
        if len(b) == 0:
            return a[k-1]
        if k == 1:
            return min(a[0],b[0])
        if len(a) > len(b):
            a, b = b, a
        if len(a) < (k-1)/2.0:
            a_tail = len(a) - 1
            b_tail = k - len(a) - 1
        else:
            if k % 2 == 0:
                a_tail = k/2 - 1
                b_tail = k/2 - 1
            else:
                a_tail = (k-1)/2 - 1
                b_tail = (k+1)/2 - 1
        if a[a_tail] == b[b_tail]:
            return a[a_tail]
        elif a[a_tail] < b[b_tail]:
            # the range of a,b in recursions need to pay attentions
            return self.findKthTwoArray(a[a_tail+1:],b[:b_tail+1],k-a_tail-1)
        else:
            return self.findKthTwoArray(a[:a_tail+1],b[b_tail+1:],k-b_tail-1)
