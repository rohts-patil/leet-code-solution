// https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/548/week-5-july-29th-july-31st/3406/

class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
         return DFS(s, wordDict.stream().collect(Collectors.toSet()), new HashMap<String, LinkedList<String>>());
    }
    
    List<String> DFS(String s, Set<String> wordDict, HashMap<String, LinkedList<String>> map) {
    if (map.containsKey(s)) 
        return map.get(s);
        
    LinkedList<String>res = new LinkedList<String>();     
    if (s.length() == 0) {
        res.add("");
        return res;
    }               
    for (String word : wordDict) {
        if (s.startsWith(word)) {
            List<String>sublist = DFS(s.substring(word.length()), wordDict, map);
            for (String sub : sublist) 
                res.add(word + (sub.isEmpty() ? "" : " ") + sub);               
        }
    }       
    map.put(s, res);
    return res;
}
    
}