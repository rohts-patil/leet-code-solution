// https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/


class Solution {
    public int findComplement(int num) {
         int X = 1;
        while (num > X){
            X = X * 2 + 1;
        }
        return X - num;
    }
}