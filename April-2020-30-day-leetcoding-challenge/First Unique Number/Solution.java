// https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3313/


class FirstUnique {

    private HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
    private Queue<Integer> myqueue = new LinkedList<>();
    
    public FirstUnique(int[] nums) {
         for (int i = 0; i < nums.length; i++) { 
             if(map.get(nums[i])==null){
                 map.put(nums[i],1);
             }else{
                 map.put(nums[i],map.get(nums[i])+1);
             }
          
            myqueue.add(nums[i]);
         }
    }
    
    public int showFirstUnique() {
        while(!myqueue.isEmpty() && map.get(myqueue.peek())>1)
            myqueue.remove();
        
        if(myqueue.isEmpty())
            return -1;
        return myqueue.peek();
    }
    
    public void add(int value) {
        if(map.get(value)==null){
            map.put(value,0);
        }
        map.put(value,map.get(value)+1);
        if(map.get(value)==1)
            myqueue.add(value); 
    }
}

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique obj = new FirstUnique(nums);
 * int param_1 = obj.showFirstUnique();
 * obj.add(value);
 */