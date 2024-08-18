package Array.ChocolateDistribution;

import java.io.*;
import java.util.*;
public class Driver
{
    public static void main (String[] args)
    {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while(t-- > 0)
        {
            int n = sc.nextInt();
            ArrayList<Integer> arr = new ArrayList<>();
            for(int i = 0;i<n;i++)
            {
                int x = sc.nextInt();
                arr.add(x);
            }
            int m = sc.nextInt();

            Solution ob = new Solution();

            System.out.println(ob.findMinDiff(arr,n,m));
        }

    }
}