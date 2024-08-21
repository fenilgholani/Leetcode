class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        mult = 1
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                mult *= -1
            else:
                mult *= 1
        
        return mult