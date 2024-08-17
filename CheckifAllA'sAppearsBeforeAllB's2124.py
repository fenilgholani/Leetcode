class Solution:
    def checkString(self, s: str) -> bool:

        if "ba" in s: return False
        return True        
        # maxi = 0
        # mini = len(s)

        # for index in range(len(s)):
        
        #     if s[index] == 'a' and maxi < index:
        #         maxi = index
            
        #     elif s[index] == 'b' and mini > index:
        #         mini = index

        #     print(maxi, mini)
        
        # if maxi > mini:
        #     return False
        
        # return True




            

            