class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        res = ''
        size = len(path)
        i = 0
        while i < size:
            if path[i] == '/':
                i += 1
                continue
            tmp = ''
            while i < size and path[i] != '/':
                tmp += path[i]
                i += 1
            if tmp == '..':
                if st:
                    st.pop()
            elif tmp != '.':
                st.append(tmp)
            i += 1
        while st:
            res = "/" + st.pop() + res
        return res if res else '/'