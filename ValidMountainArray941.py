class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
  

        i = 0
    
        while i < len(arr)-1:

            if arr[i] == arr[i+1]:
                return False
            
            elif arr[i] > arr[i+1]:
                if i == 0:
                    return False
                break
            
            i+=1
        
        if i == len(arr)-1:
            return False
        
        while i < len(arr) -1:
            
            if arr[i] <= arr[i+1]:
                return False
            
            i+=1
        
        return True
            
            

        

#         uphill = True
#         i = 0
#         peak = False
        
#         while i < len(arr)-1:
            
#             if uphill and !peak and arr[i] > arr[i+1]:    
#                 peak = True
#                 uphill = False
            
#             elif !uphill and peak and arr[i] =< arr[i+1]:
#                 return False
            
#             elif arr[i] >= arr[i+1]:
#                 return False
            
#             i+=1
            
#         return True