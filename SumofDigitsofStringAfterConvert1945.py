class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        transform = ""
        for ch in s:
            transform += str(ord(ch) - ord('a')+1)
        
        for i in range(k):
            
            summ = 0
            for j in transform:
                summ += int(j)

            transform = str(summ)  
        
        return int(transform)