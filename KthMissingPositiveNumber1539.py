class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        ans = [x for x in range(1, arr[-1]+k+1)]
        # print(arr[-1])

        # print(ans)
        for i, n in enumerate(arr):
            ans.remove(n)

        return ans[k-1]

        # count = 0
        # if arr[0] != 1:
        #     count = arr[0] - 1

        # for i in range(1,len(arr)):
            
        #     count += arr[i] - arr[i-1] - 1     
        #     print(count)
        #     if count >= k:
        #         return arr[i-1] + count - k + 1 

        
        # if count <k:
        #     return arr[-1] + k - count 

        # start = 0
        # missing = []
        # for i, n in enumerate(arr):
        #     diff = n - start - 1
        #     missing += list(range(start,start+diff+1))
        
        # missing = missing[1:]

        # return missing[k]