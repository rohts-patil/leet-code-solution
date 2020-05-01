// https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3307/


class Solution {
    public int subarraySum(int[] arr, int k) {
        int n = arr.length; 
        HashMap <Integer, Integer> prevSum = new HashMap<>();  
        int sum = k;
        int res = 0;  
  
        int currsum = 0;  
        
        for (int i = 0; i < n; i++) {  
    
            currsum += arr[i];  
        
            
            if (currsum == sum)   
                res++;          
          
            if (prevSum.containsKey(currsum - sum))   
                res += prevSum.get(currsum - sum);  
                
        
            Integer count = prevSum.get(currsum); 
            if (count == null) 
                prevSum.put(currsum, 1); 
            else
                prevSum.put(currsum, count+1);  
        }  
        
        return res;  
    }
}