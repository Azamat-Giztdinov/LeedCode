class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        last_char = sentence[0]
        for i in range(1,len(sentence)):
            if sentence[i] != ' ' and sentence[i -1] == ' 'and last_char != sentence[i]:
                    return False
            last_char = sentence[i] if sentence[i] != ' ' else last_char
        return last_char == sentence[0]
