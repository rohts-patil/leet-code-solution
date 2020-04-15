### https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3300/

class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n = len(arr) 
        if(n == 1):
            return 0
        
        left = [0]*n  
        right = [0]*n 
        prod = [0]*n  
        left[0] = 1
        right[n - 1] = 1
        
        for i in range(1, n):  
            left[i] = arr[i - 1] * left[i - 1]  
            
        for j in range(n-2, -1, -1):
            right[j] = arr[j + 1] * right[j + 1]  
            
        for i in range(n):  
            prod[i] = left[i] * right[i]
            
        return prod