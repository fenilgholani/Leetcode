class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.removespace(s)
        t = self.removespace(t)
        
        # print(s)
        # print(t)
        
        return s==t
    
    def removespace(self, s):
        
        t = []
        
        for ch in s:
            t.append(ch)
            
            if(ch == '#'):
                if len(t) >= 2:
                    t.pop()
                    t.pop()
                elif len(t) == 1:
                    t.pop()
        
        return t
        
