class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
    
        if len(s) == 1 and k == 1:
            return s.upper()
        
        if len(s) == 1 and k == 2 and s[0] == '-':
            return ""
        
        if len(s) == 1 and k == 2:
            return s.upper()

        if(s.find('-') == -1):
            first_str = ""
            join_str = s.upper()
        
        
        else:
            first_str = s[:s.index('-')].upper()

            join_str = s[len(first_str):].replace('-', '').upper()
        
        # print(first_str)
        # print(join_str)
        
        if(len(join_str) == 0):
            join_str = first_str
            first_str = ""
            print(join_str)

        if( len(join_str) % k == 0):
            i = 0
            ch = ""
            for i in range(0, len(join_str), k):
                ch+="-" + join_str[0+i:k+i]
                
  
                
            # print(ch)
            if(first_str == ""):
                return ch[1:]
            
            if k < len(first_str):
                print("hello")
                ch1 = ""
                for i in range(0, len(first_str), k):
                    ch1+= first_str[0+i:k+i] + "-"
                first_str = ch1[:len(ch1)-1]  
            
            return first_str + ch
        
        
        else:
            print(len(join_str))
            extra = len(join_str) % k
            
            if len(first_str) - extra > 1 and (extra+len(join_str)) % k == 0:
                
                join_str = first_str[len(first_str)-extra:] + join_str
                first_str = first_str[:len(first_str)-extra]
        
                # print(first_str)
                # print(join_str)
                
                ch = ""
                for i in range(0, len(join_str), k):
                    ch+="-" + join_str[0+i:k+i]
                    

                # print(ch)
                return first_str + ch
            
            else:
                first_str += join_str[:extra]
                join_str = join_str[extra:]
        
                print(first_str)
                print(join_str)
                
                ch = ""
                for i in range(0, len(join_str), k):
                    ch+="-" + join_str[0+i:k+i]
                
                # print(ch)
                return first_str + ch
            

        return ""















