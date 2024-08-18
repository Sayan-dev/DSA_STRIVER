package Strings;

import java.util.*;

public class GetSecondMostCommonString {
        String secFrequent(String arr[], int N) {
            HashMap<String, Integer> map = new HashMap<>();
            for (int i = 0; i < N; i++) {
                if (map.containsKey(arr[i])) map.put(arr[i], map.get(arr[i]) + 1);
                else map.put(arr[i], 1);
            }

            ArrayList<Map.Entry<String, Integer>> sol = new ArrayList<>();
            for (Map.Entry<String, Integer> entry : map.entrySet()) {
                sol.add(entry);
            }
            Collections.sort(sol, new Comparator<Map.Entry<String, Integer>>() {
                public int compare(Map.Entry<String, Integer> entry1, Map.Entry<String, Integer> entry2) {
                    return entry1.getValue().compareTo(entry2.getValue());
                }
            });

            if (sol.size() - 2 < 0) {
                return "";
            }

            return sol.get(sol.size() - 2).getKey();

        } // your code here
}
