class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        cumul_odd = [0 for i in range(len(nums))]
        cumul_even = [0 for i in range(len(nums))]
        cumul_even[0] = nums[0]
        index = 0
        for i in range(1,len(nums)):

            if i % 2 == 0:
                cumul_even[i] = cumul_even[i-1] + nums[i]
                cumul_odd[i] = cumul_odd[i-1]
                
            else:
                cumul_even[i] = cumul_even[i-1]
                cumul_odd[i] = cumul_odd[i-1] + nums[i]
        
        # print(cumul_odd)
        # print(cumul_even)
        
        for i, n in enumerate(nums):

            odd = cumul_odd[i] + cumul_even[-1] - cumul_even[i]
            even = cumul_even[i] + cumul_odd[-1] - cumul_odd[i]
            # print(i)
            # print(odd, even)

            if i % 2 == 0:
                even -= n
            else:
                odd -= n

            if odd == even:
                index += 1
        
        return index
            











        # d = {}
        # sum_even = 0
        # sum_odd = 0
        # presum = []
        # for i in range(len(nums)):

        #     if i % 2 == 0:
        #         sum_even += nums[i]
        #         presum.append(sum_even)
        #     else:
        #         sum_odd += nums[i]
        #         presum.append(sum_odd)
        # odd=0
        # even=0
        # index = 0
        # curr_even = 0
        # curr_odd = 0
        # for i, n in enumerate(nums):

        #     odd = sum_even - curr_even + curr_odd
        #     even = sum_odd - curr_odd + curr_even
                
        #     if odd == even:
        #         index += 1

        #     if i % 2 == 0:
        #         curr_even += nums[i]

        #     else:
        #         curr_odd += nums[i]

        # return index
            


