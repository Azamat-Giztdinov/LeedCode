class Solution:
    def intToRoman(self, num: int) -> str:
        roman_array =[1, 4, 5, 9, 10, 40, 50, 90,  100, 400,  500, 900, 1000]
        roman_dick = {1:'I',4: 'IV', 5:'V',9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90:'XC', 100:'C', 400: 'CD', 500:'D', 900: 'CM', 1000: 'M'}
        result = ''
        idx = len(roman_array) - 1
        while num:
            if num - roman_array[idx] >= 0:
                num -= roman_array[idx]
                result += roman_dick[roman_array[idx]]
            else:
                idx -= 1
        return result