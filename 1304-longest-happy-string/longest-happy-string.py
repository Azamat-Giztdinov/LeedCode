class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        happy_string = ''
        end_char = ''
        count = 0
        while a or b or c:
            # print( a, b, c)
            if a > c and a > b and (end_char != 'a' or count < 2):
                if end_char != 'a':
                    count = 0
                happy_string += 'a'
                a-=1
                end_char = 'a'
                count +=1
            elif b > c and b > c and (end_char != 'b' or count < 2):
                if end_char != 'b':
                    count = 0
                happy_string += 'b'
                b-=1
                end_char = 'b'
                count +=1
            elif c > a and c > b and (end_char != 'c' or count < 2):
                if end_char != 'c':
                    count = 0
                happy_string += 'c'
                c-=1
                end_char = 'c'
                count +=1
            elif end_char != 'a' and a > 0:
                happy_string += 'a'
                a -= 1
                end_char = 'a'
                count = 1
            elif end_char != 'b' and b > 0:
                happy_string += 'b'
                b -= 1
                end_char = 'b'
                count = 1
            elif end_char != 'c' and c > 0:
                happy_string += 'c'
                c -= 1
                end_char = 'c'
                count = 1
            else:
                break
            # print(happy_string)
        return happy_string