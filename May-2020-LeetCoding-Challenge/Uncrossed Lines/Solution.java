// https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3340/

class Solution {
    public int maxUncrossedLines(int[] a, int[] b) {
       int m = a.length, n = b.length;
        int[][] dp = new int[m+1][n+1];
        for(int i=1; i <= m; i++){
            for(int j=1; j <= n; j++){
                if(a[i-1] == b[j-1])
                    dp[i][j] = 1+dp[i-1][j-1];
                else
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[m][n];  
    }
}