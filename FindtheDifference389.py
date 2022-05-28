class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        i = 0
        s1 = sorted(s)
        t1 = sorted(t)
        
        while i < len(s1):
            
            if not t1[i] == s1[i]:
                return t1[i]
            
            # s = s[:s.index(t[i])] + s[s.index(t[i])+1:] 
            i+=1
            
        return t1[i]