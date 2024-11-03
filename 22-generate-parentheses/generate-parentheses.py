class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generate(n, res, '(', 1, 0)
        return res
    def generate(self, n: int, res: List[str], s: str, countOpen: int, countClosed: int):
        if countClosed == n:
            res.append(s)
            return
        if countOpen < n:
            self.generate(n, res, s + '(', countOpen + 1, countClosed)
        if countClosed < countOpen:
            self.generate(n, res, s + ')', countOpen, countClosed + 1)
