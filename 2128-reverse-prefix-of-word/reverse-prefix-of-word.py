class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            return ch+word[:word.index(ch)][::-1]+word[word.index(ch)+1:]
        return word    


        