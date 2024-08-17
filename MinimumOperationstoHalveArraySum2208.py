class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        summ = 0
        op = 0
        a = [i*-1 for i in nums]
        heapq.heapify(a)

        for i in nums:
            summ += i

        halfsum = summ

        while halfsum > summ/2.0:

            num = heapq.heappop(a) * -1
            halfsum = halfsum - num/2.0
            heapq.heappush(a, num/2.0 * -1)
            op += 1


        return op

        

        # nums.sort(reverse=True)
        # summ = 0
        # index = 0
        # op = 0

        # # Get the sum
        # for i in nums:
        #     summ += i
        # print(summ)

        # summ1 = summ

        # while index < len(nums)-1:

        #     print(nums)
        #     halfsum = summ1 - nums[index]/2.0
        #     summ1 -= nums[index]/2.0
        #     nums[index] /= 2.0

        #     print(halfsum)
        #     if nums[index] < nums[index+1]:
        #         if index != 0 and nums[index - 1] > nums[index + 1]:
        #             index-=1
        #         else:
        #             index += 1

        #     op += 1

        #     if halfsum < summ/2.0:
        #         return op

        # return op



    #     op = 0
        
    #     index, number, summ = self.maximum(nums)
    #     halfsum = summ - number/2.0
    #     # print(halfsum ,summ , number)

    #     while halfsum > summ/2.0:
    #         op += 1
    #         nums[index] = number/2.0
    #         # print(halfsum ,summ , number)
    #         index, number, halfsum = self.maximum(nums)
            
            
    #     return op

    # def maximum(self, nums):

    #     summ = nums[0]
    #     maxi = nums[0]
    #     i = 0
    #     for index in range(1,len(nums)):
    #         if maxi < nums[index]:
    #             maxi = nums[index]
    #             i = index
    #         summ += nums[index]

    #     return (i,maxi, summ)


    #     # for i in nums:
    #     #     halfsum += i/2.0
    #     #     op += 1
            
    #     #     print(halfsum + summ - i)
    #     #     if halfsum + summ - i < summ/2:
    #     #         return op
        
    #     return op