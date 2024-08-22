class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        m, n = len(isWater), len(isWater[0])
        visited = [[False for j in range(n)] for i in range(m)]
        q = []
        ans = [[0 for j in range(n)] for i in range(m)]
        # print(visited)
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i,j, 0))
        
        while q != []:
            # print(q)
            i, j, count = q.pop(0)

            if visited[i][j]:
                continue
            
            elif not visited[i][j]:
                visited[i][j] = True
                ans[i][j] = count

                if i-1 >= 0 and not visited[i-1][j]:
                    q.append((i-1, j, count + 1))
                if j-1 >= 0 and not visited[i][j - 1]:
                    q.append((i, j-1, count + 1))
                if i+1 < len(isWater) and not visited[i+1][j]:
                    q.append((i+1, j, count + 1))
                if j+1 < len(isWater[0]) and not visited[i][j+1]:
                    q.append((i, j+1, count + 1))

        
        return ans        
                
    # def bfs(self, visited, isWater, q, ans):
        
    #     # print(q)
    #     i, j, count = q.pop(0)

    #     if i >= len(isWater) or j >= len(isWater[0]) or i < 0 or j < 0:
    #         return
        
    #     if visited[i][j]:
    #         return
        
    #     elif not visited[i][j]:
    #         visited[i][j] = True
    #         ans[i][j] = count

    #         q.append((i-1, j, count + 1))
    #         q.append((i, j-1, count + 1))
    #         q.append((i+1, j, count + 1))
    #         q.append((i, j+1, count + 1))

    #         while q != []:
    #             self.bfs(visited, isWater, q, ans)

                     




