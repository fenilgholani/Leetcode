class Solution:
    def minOperations(self, n: int) -> int:
        
        lst = [2*i+1 for i  in range(n)]
        avg = 0
        summ = 0
        for i in lst:
            summ += i

        avg = summ // n
        op = 0
        for i in range(n//2):
            op += avg - lst[i]
        
        return op



