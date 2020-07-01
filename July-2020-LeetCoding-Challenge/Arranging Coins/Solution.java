// https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3377/

class Solution {
    public int arrangeCoins(int n) {

        if (n == 0) {
            return 0;
        }

        int i = 1;
        int step = 0;

        while (true) {
            if (n - i < 0) {
                break;
            } else {
                n = n - i;
                i++;
                step++;
            }

        }

        return step;
    }
}