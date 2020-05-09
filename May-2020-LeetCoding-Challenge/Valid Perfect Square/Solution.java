// https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/

class Solution {
    public boolean isPerfectSquare(int num) {
        int i = 1, j = num;
        while(i <= j){
            int mid = i + (j-i)/2;
            int res = num/mid, tail = num%mid;
            if(tail == 0 && res == mid) return true;
            else if(res < mid){
                j = mid-1;
            } else i = mid+1;
        }
        return false;
    }
}