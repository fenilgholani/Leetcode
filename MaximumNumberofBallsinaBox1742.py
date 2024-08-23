class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        d = {}

        for i in range(lowLimit, highLimit+1):
            summ = 0
            while i != 0:
                r = i % 10
                i = i // 10
                summ += r
            
            if d.get(summ):
                d[summ] += 1
            else:
                d[summ] = 1
        
        maxx = 0
        # print(d)
        for k,v in d.items():

            if maxx < v:
                maxx = v
        
        return maxx