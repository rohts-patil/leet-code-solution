// https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3390/

class Solution {
    public double angleClock(int hour, int minutes) {
        double min = minutes * 6;
        double hr = hour * 30 + (double)minutes/2;
        double angle = Math.abs(hr-min);
        return Math.min(angle,360-angle);
    }
}