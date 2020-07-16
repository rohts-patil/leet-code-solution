// https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3392/

class Solution {
    public double myPow(double x, int n) {
        double nD = n;
        if(n==0 || x==1){
            return 1;
        } else if(n<0) {
            x = 1/x;
            nD=(-1)*(double)n;
        }
        return positivePow(x,nD);
    }

    private double positivePow(double x, double n){
        if(n==1 || x==0 || x==1){
            return x;
        } else {
            if(n%2==0){
                double halfPow = positivePow(x, n/2);
                return halfPow * halfPow;
            } else {
                double halfPow = positivePow(x, (n-1)/2);
                return halfPow * halfPow * x;
            }
        }
    }
}