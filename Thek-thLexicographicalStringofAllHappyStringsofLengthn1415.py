class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        q = ['a', 'b', 'c']
        ans = ""

        if n == 1 and k < 4:
            return q[k-1]

        while len(ans) < n and n != 1:

            ans = q.pop(0)

            if ans[-1] == 'a':
                q.append(ans+"b")
                q.append(ans+"c")
                
            
            elif ans[-1] == 'b':
                q.append(ans+"a")
                q.append(ans+"c")
            
            elif ans[-1] == 'c':
                q.append(ans+"a")
                q.append(ans+"b")
            
        
        if n == 1:
            return ""
    
        q.insert(0,ans)
        q = q[:-2]
        print(q)

        if k-1 >= len(q):
            return ""

        return q[k-1]
        

            
                
        
        

#     def helper(ans, n):
#         nonlocal k
#         if k == 0 and n == 0:
#             return ans
        
#         if k != 0 and n == 0:
#             k -= 1
#             return ""

#         if n != 0:

#             if ans[-1] == 'a':
#                 ans = helper(ans+"b", n-1) 
#                 ans = helper(ans+)   

        