// https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3354/

class Solution {
    public boolean isPowerOfTwo(int n) {
       if(n<=0){ 
           return false;
       }
      
        if ((n & (n-1)) == 0){
            return true;
        }else{
            return false;
        }
    }
}