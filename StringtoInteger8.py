class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        
        positive = True
        
        if(s==''):
            return 0
        if len(s) > 1:
            if(s[0] == '-' and s[1] == '+') or (s[1] == '-' and s[0] == '+'):
                return 0
            if(s[0] == '-' or s[0] == '+'):
                if(s[0] == '-'):
                    positive = False
                s = s[1:]
        
        
        for i,ch in enumerate(s):
            if ch.isalpha() or ch ==' ' or ch == '.' or ch == '-' or ch == '+':
                s = s[0:i]
                break
            
        
        
        num = 0
        
        for i in range(len(s)-1, -1, -1):
            
            if s[i] == '0':
                num += 0 * pow(10, len(s) - 1 - i)    
            elif s[i] == '1':
                num += 1 * pow(10, len(s) - 1 - i)
            elif s[i] == '2':
                num += 2 * pow(10, len(s) - 1 - i)
            elif s[i] == '3':
                num += 3 * pow(10, len(s) - 1 - i)
            elif s[i] == '4':
                num += 4 * pow(10, len(s) - 1 - i)
            elif s[i] == '5':
                num += 5 * pow(10, len(s) - 1 - i)
            elif s[i] == '6':
                num += 6 * pow(10, len(s) - 1 - i)
            elif s[i] == '7':
                num += 7 * pow(10, len(s) - 1 - i)
            elif s[i] == '8':
                num += 8 * pow(10, len(s) - 1 - i)
            elif s[i] == '9':
                num += 9 * pow(10, len(s) - 1 - i)
                
        
        if positive == False:
            num *=-1
            
        if num < -2147483648:
            num = -2147483648
            
        elif num > 2147483647:
            num = 2147483647
        
        return num