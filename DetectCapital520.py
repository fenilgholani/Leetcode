class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if(word.isupper()):
            return True
        
        if word.islower():
            return True
            
        
        start = word[0].isupper()
        
        if start:
            
            if word[1:].islower():
                return True
            
        return False
        
        