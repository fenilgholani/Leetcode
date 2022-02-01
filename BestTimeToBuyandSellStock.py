class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        start = 0
        end = 0
        mini  = 0
        
        while end < len(prices) and start <= end:
            
            if prices[start] > prices[end]:
                start = end
                end+=1
                
            else:
                mini = min(mini, prices[start]-prices[end])
                end +=1
                
        
        return abs(mini)
    