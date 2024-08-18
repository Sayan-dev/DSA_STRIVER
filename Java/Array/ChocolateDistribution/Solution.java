package Array.ChocolateDistribution;

import java.util.ArrayList;
import java.util.Collections;

public class Solution
{
    public long findMinDiff (ArrayList<Integer> a, int n, int m)
    {
        // your code here
        // 1 packet
        // minimize max - min
        Collections.sort(a);
        int min = a.get(0);
        int max = a.get(m-1);

        int diff = max-min;
        int index= 0 ;
        while(index+m<=n){
            diff = Math.min(diff, a.get(index+m-1)-a.get(index));
            index++;
        }


        return diff;
    }

}
