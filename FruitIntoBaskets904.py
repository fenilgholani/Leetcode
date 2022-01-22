class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
       
        #[0,1,2,2]
        # s
        #     e
        #
        #1:1
        #2:2
        start = 0
        end = 0
        max_val = 0
        d = {}
        
        
        while end < len(fruits):
            
            d[fruits[end]] = end
            
            
            if len(d) > 2:
                
                min_val = min(d.values())
                del d[fruits[min_val]]
                
                max_val = max(max_val, end-start)
                
                start = min_val+1
            
            end+=1
            
        return max(max_val, end-start)