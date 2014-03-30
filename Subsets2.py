class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        i = 0
        n = len(S)
        ans = []
        S.sort()
        while i < pow(2,n):
            row = []
            j = 0
            while j < n:
                if (i>>j) & 1 == 1:
                    row.append(S[j])
                j += 1
            if row not in ans:
                ans.append(row)
            i += 1
        return ans
