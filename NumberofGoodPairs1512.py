class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        d = {}
        for i, n in enumerate(nums):

            if d.get(n):
                d[n] += 1
            else:
                d[n] = 1
        
        combination = 0
        for _,v in d.items():

            if v >= 2:
                combination += math.comb(v,2)

        return combination 
