## pay attention to the situration like '/home/../../../' 
## it should return '/'
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        a = path.split('/')
        ans = []
        for c in a:
            if c not in ['','.','..']:
                ans.append(c)
            if c == '..':
                if len(ans) != 0:
                    ans.pop()
        return '/'+'/'.join(ans)
