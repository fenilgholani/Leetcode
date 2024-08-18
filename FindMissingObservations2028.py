class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        summ = 0
        for i in rolls:
            summ += i
        
        sum_n = mean * (n+len(rolls))-summ

        if sum_n < n or sum_n > 6*n:
            return []

        ans = []

        while sum_n:
            dice = min(sum_n - n + 1, 6) 
            ans.append(dice)
            sum_n -= dice
            n-=1

        return ans          

        
    #     n_list = []
    #     ans = []

    #     if sum_n > n*6:
    #         return []

    #     self.helper(n_list, n, sum_n, ans)
    #     return ans
    
    # def helper(self, n_list, n, sum_n, ans):
    
    #     print(n_list, n, sum_n, ans)
        
    #     if n == 0 and sum_n == 0:
    #         ans = n_list
    #         return ans

    #     if n == 0:
    #         return ans

    #     else:

    #         for i in range(1,7):
    #             ans = self.helper(n_list+[i], n-1, sum_n-i, ans)   
    #         return ans