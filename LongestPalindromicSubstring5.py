class Solution(object):
    def longestPalindrome(self, s: str) -> str:
  
        i = 0
        start = 0
        end = 0

        while i < len(s)-1:
            
            pal1 = self.palindrome(s, i, i)
            pal2 = self.palindrome(s, i, i+1)
            # print(pal1)
            # print(pal2)
            maxi = max(pal1, pal2)
            
            if(maxi > end - start):
                start = i - int((maxi - 1)/2)
                end = i + int(maxi/2)
            i+=1
        
        return s[start:end+1]
    
    def palindrome(self, s, left, right):
                
        if s == None or left > right:
            return 0
        
        while left >=0 and right < len(s) and s[left] == s[right]:

            left -= 1
            right += 1

        # print(right - left - 1)
        return right - left - 1      
        
        
        # return str
#         def longs(s):
        
#             print(s)
            
#             if(s == "None"):
#                 return "None"

#             elif(len(s) == 1):
#                 return s
            
#             elif(len(s) == 2 and s[0] == s[-1]):
#                 return s
            
#             elif(len(s) == 2 and s[0] != s[-1]):
#                 return "None"
                
#             elif(s[0] == s[-1] and s != "None"):
#                 return s[0] + longs(s[1:-1]) + s[-1]
            
#             else:
#                 return "None"
            
            
            


#             # elif(s[0] == s[-2]):
#             #     return s[0] + self.longs(s[1:-2]) + s[-2]

# #             elif(s[1] == s[-1]):
# #                 return s[1] + self.longs(s[2:-2]) + s[-1]

# #             else:
# #                 return self.longs(s[1:-1])  
           
#         max_len = s[0]
#         for i in range(len(s)):
            
#             c = longs( s[i:])
#             if("None" not in c):
#                 if(len(c) > len(max_len)):
#                     max_len = c
#                 # print(c)
        
#         return max_len 