class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        return self.expand(digits, [], ['0','0','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'])
    
    def expand(self, digit, sol, val):
        
        if len(digit) == 0:
            return sol
        
        else:
            
            result = []
            
            if sol == []:
                result = [value for value in val[int(digit[0])]]
                return self.expand(digit[1:], result, val)

            else:
                for x in sol:

                    for alpha in val[int(digit[0])]:

                        result.append(x+alpha)

                return self.expand(digit[1:], result, val)
