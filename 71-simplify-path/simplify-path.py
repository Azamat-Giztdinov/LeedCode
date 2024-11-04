class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        arr = path.split('/')
        for i in arr:
            if i == '' or i == '.':
                continue
            if i == '..':
                if res:
                    res.pop()
            else:
                res.append(i)
        return '/' + '/'.join(res)