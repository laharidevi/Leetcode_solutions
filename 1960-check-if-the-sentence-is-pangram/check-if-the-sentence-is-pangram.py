class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        m = set(sentence)
        if len(m) == 26:
            return True
        else:
            return False
        
        
        