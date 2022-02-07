class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        
        i = 0
        
        while i < len(nums):
            
            if not nums[i] in d:
                d[nums[i]] = i
            
            i+=1
        
        i = 0
        
        while i < len(nums):
            
            if (target - nums[i]) in d and not d[target - nums[i]] == i :
                return [i,d[target - nums[i]]]
            
            else:
                i+=1
            
        # print(d)
        
        return None
            

                
                
            