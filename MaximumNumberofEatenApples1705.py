class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        expiry = []

        for i in range(len(days)):
            expiry.append(i+days[i])
        
        d = []
        for i in range(len(days)):

            if apples[i] == 0 and days[i] == 0:
                continue
            
            else:
                d.append((expiry[i] + 1, apples[i])) 
        
        d.sort()

        day = 1
        total_apples = 0

        while d != []:
            expire, no_apples =  d.pop(0)

            while no_apples != 0 and expire > day:
                no_apples -= 1
                total_apples += 1
                day += 1
            
        
        return total_apples