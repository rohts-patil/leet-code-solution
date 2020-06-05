// https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3351/

class Solution {
    int cnt=0;
    TreeMap<Integer, Integer> map= new TreeMap<>();
    Random rnd= new Random();
    public Solution(int[] w) {
         for (int idx=0; idx<w.length; idx++){
            cnt+=w[idx];
            map.put(cnt, idx);
        }
    }
    
    public int pickIndex() {
        int key= map.higherKey(rnd.nextInt(cnt));
        return map.get(key);
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
