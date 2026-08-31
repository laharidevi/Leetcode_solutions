class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        m = word.find(ch)
        if m == -1:
            return word
        else:
            return word[:m+1][::-1] + word[m+1:]
        