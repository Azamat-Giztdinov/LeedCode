class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a, b = 0, 0
        for i in num1:
            a = a*10 + (ord(i)-48)
        for i in num2:
            b = b*10 + (ord(i)-48)
        return str(a * b)