class Solution:
    def compressedString(self, word: str) -> str:
        res = ''
        count = 1
        last_char = word[0]
        for i in range(1,len(word)):
            if word[i] == last_char and count < 9:
                count += 1
            else:
                res += (str(count) + last_char)
                last_char = word[i]
                count = 1
        res += (str(count) + word[-1])
        return res