class Solution:
    def isThree(self, n: int) -> bool:
        
        count = 0
        if n == 1 or n == 2:
            return False

        for i in range(2,n):

            if n % i == 0:
                count += 1
            
            if count >= 2:
                return False
        
        if count == 1:
            return True

        else:
            return False