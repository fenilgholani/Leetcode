class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        d = {}
        for i in edges:
            a,b = i

            if d.get(a):
                d[a] += 1
            else:
                d[a] = 1

            if d.get(b):
                d[b] += 1
            else:
                d[b] = 1
        
        for k,v in d.items():

            if v == len(d) - 1:
                return k
        
        return None