class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        
        def dfs(cost, index):

            nonlocal ans

            if cost == target:
                ans = cost
                return
                            
            if abs(target - cost) < abs(target - ans) or (abs(target - cost) == abs(target - ans) and cost < target):
                ans = cost
            
            if cost > target:
                return

            if index == len(toppingCosts):
                return
            
            for i in range(3):
                # print(cost,  i * toppingCosts[index], index)
                dfs(cost + i * toppingCosts[index], index + 1)



        ans = sys.maxsize
        for i in baseCosts:
            dfs(i, 0)

        return ans


        # def dfs(cost, index):
        #     nonlocal ans

        #     if index == len(toppingCosts):
        #         return 

        #     if cost == target:
        #         ans = target
        #         return
            
        #     # if abs(target - cost) < abs(target - ans):
        #     #     ans = cost
        #     #     print(cost, ans)
            
        #     for i in range(3):
        #         ans = cost + i * toppingCosts[index]
        #         dfs(cost + i * toppingCosts[index], index+1)
            
            


        # ans = sys.maxsize

        # for i in baseCosts:
        #     print("COST",i)
        #     dfs(i,0)

        # return ans


            

    
