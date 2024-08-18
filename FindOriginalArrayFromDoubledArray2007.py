class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        d = {}
        num_zero = 0
        ans = []
        if len(changed) % 2 != 0:
            return []

        for num in changed:
            
            if num == 0:
                num_zero += 1
            elif d.get(num):
                d[num] += 1
            else:
                d[num] = 1
            
        if num_zero % 2 != 0:
            return []

        changed.sort()

        for num in changed:

            # print(d)
            if num != 0 and d[num] != 0:

                if (d.get(num*2) and d[num] <= d[num*2]):
                        d[num*2] -= d[num]
                        for i in range(d[num]):
                            ans.append(num)
                        d[num] = 0

                elif (d.get(num//2) and d[num] >= d[num//2]):
                    d[num] -= d[num//2]
                    for i in range(d[num//2]):
                        ans.append(num//2)
                    d[num//2] = 0
                        
                else:
                    return []

        ans += [0 for i in range(num_zero//2)]

        # for k,v in d.items():

        #     if v > 0:
        #         for i in range(v):
        #             ans.append(k)
        
        return ans




















        # d = {}
        # d1 = {}
        # ans = []
        # for num in changed:

        #     if num % 2 == 0 and d.get(num//2):
        #         d[num//2] += 1
        #     elif num % 2 == 0 and not d.get(num//2):
        #         d[num//2] = 1   
        #     else:
        #         if d.get(num):
        #             d[num] += 1
        #         else:
        #             d[num] =1

        #     if d1.get(num):
        #         d1[num] += 1
        #     else:
        #         d1[num] = 1
            
        # print(d)
        # print(d1)
        
        # for k,v in d.items():

        #     if v % 2 != 0:
        #         return []
            
        #     else:
        #         # print(d1.get(k*2) and d1[k*2] == v//2)
        #         if d1.get(k*2) and d1[k*2] == v//2:
        #             for i in range(v//2):
        #                 ans.append(k)
        #         elif k == 0 and d1.get(k*2) and d1[k*2] == v:
        #             for i in range(v//2):
        #                 ans.append(k)
                
        #         else:
        #             return []
        # print(ans)
        # return ans
        