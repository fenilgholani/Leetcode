class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        

        x = [x for x,_ in points]

        x.sort()
        maxx = 0

        for i in range(1, len(x)):
            diff = x[i] - x[i-1]
            if maxx < diff:
                maxx = diff
        
        return maxx