// https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/

class Solution {
    public List<List<String>> groupAnagrams(String[] arr) {
         HashMap<String, List<String> > map = new HashMap<>(); 
  
      
        for (int i = 0; i < arr.length; i++) { 
  
             
            String word = arr[i]; 
            char[] letters = word.toCharArray(); 
            Arrays.sort(letters); 
            String newWord = new String(letters); 
            
            if (map.containsKey(newWord)) { 
                map.get(newWord).add(word); 
            } 
            else { 
                List<String> words = new ArrayList<>(); 
                words.add(word); 
                map.put(newWord, words); 
            } 
        } 
  
        ArrayList<List<String>> a = new ArrayList<List<String>>();
        for (String s : map.keySet()) { 
            List<String> values = map.get(s); 
            a.add(values);
        } 
        return a;
    }
}