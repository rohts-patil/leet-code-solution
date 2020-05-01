// https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3306/


/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface BinaryMatrix {
 *     public int get(int x, int y) {}
 *     public List<Integer> dimensions {}
 * };
 */

class Solution {
    public int leftMostColumnWithOne(BinaryMatrix binaryMatrix) {
        List<Integer> size = binaryMatrix.dimensions();
        int rows = size.get(0);
        int cols = size.get(1);
        int candidate = -1;
        for (int r = 0, c = cols - 1; r < rows && c >= 0; ) {
            if (binaryMatrix.get(r, c) == 1) {
                candidate = c;
                c--;
            } else {
                r++;
            }
        }
        return candidate;
    }
}