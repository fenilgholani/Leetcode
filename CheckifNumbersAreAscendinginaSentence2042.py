class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        lst = s.split()
        nums = []
        for ch in lst:

            if re.search("[0-9]+", ch):
                nums.append(int(re.findall("[0-9]+", ch)[0]))
        
        # print(nums)

        ans = nums[:]
        nums.sort()
        
        for i in range(len(ans)-1):
            if ans[i] == ans[i+1]:
                return False

        if ans == nums:
            return True

        
        return False