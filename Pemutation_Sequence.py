class Solution:
    # @return a string
    def getPermutation(self, n, k):
        fac = []
        i = 1
        fac.append(1)
        while i < n:
            fac.append(fac[-1]*i)
            i += 1
        a = []
        for i in range(1,n+1):
            a.append(i)
        ans = []
        while n > 0:
            ind = math.floor((k-1)/fac[n-1])
            ans.append(a.pop(ind))
            k -= ind * fac[n-1]
            n -= 1
        return ''.join(str(x) for x in ans)
