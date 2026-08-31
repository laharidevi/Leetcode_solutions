class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 1
        count = 0
        for i in range(len(sequence)):
            if len(word * k) <= len(sequence):
                if word * k in sequence:
                    count += 1
                    k += 1
        return count

       
       
    
            
            