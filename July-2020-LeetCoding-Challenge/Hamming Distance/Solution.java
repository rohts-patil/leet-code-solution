// https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3381/

class Solution {
    public int hammingDistance(int x, int y) {
         int xor = x ^ y, count = 0;
    for (int i=0;i<32;i++){ 
        count += (xor >> i) & 1;
    }
    return count;
    }
}