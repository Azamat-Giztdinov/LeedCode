class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        lexems = deque()
        for i in expression:
            if i == ',' or i == '(':
                continue
            if i in ['t', 'f','!','&','|']:
                lexems.append(i)
            else:
                hs_true = False
                hs_false = False
                while lexems[-1] not in ['!', '&', '|']:
                    value = lexems.pop()
                    if value == 't':
                        hs_true = True
                    else:
                        hs_false = True
                oper = lexems.pop()
                if oper == '!':
                    lexems.append('t' if not hs_true else 'f')
                elif oper == '&':
                    lexems.append('f' if hs_false else 't')
                else:
                    lexems.append('t' if hs_true else 'f')
        return lexems[-1] == 't'

    