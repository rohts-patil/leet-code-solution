// https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3297/

class Solution {
    public int lastStoneWeight(int[] stones) {
        if (stones == null)
            return 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < stones.length; i++) {
            pq.offer(stones[i]);
        }
        while (pq.size() > 1) {
            int first = pq.poll();
            int second = pq.poll();
            if (first != second) {
                int rem = Math.abs(first - second);
                pq.offer(rem);
            }
        }
        return pq.size() == 1 ? pq.poll() : 0;
    }
}