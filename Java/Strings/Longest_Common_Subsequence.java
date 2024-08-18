package Strings;


import java.util.ArrayList;

// Best Approach (Tabulation)
public class Longest_Common_Subsequence {
    //Function to find the length of longest common subsequence in two strings.
    public int lcs(int x, int y, String s1, String s2)
    {
        // your code here

        int[][] dp_s1_s2 = new int[x][y];


        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                if(s1.charAt(i) == s2.charAt(j)){
                    if(i-1>=0 && j-1>=0){

                        dp_s1_s2[i][j] = 1+ dp_s1_s2[i-1][j-1];
                        continue;

                    } else {
                        dp_s1_s2[i][j] = 1;
                        continue;
                    }
                }
                int dpRow = 0;
                int dpCol = 0;
                if(i-1>=0){
                    dpRow = dp_s1_s2[i-1][j];
                }
                if(j-1>=0){
                    dpCol =dp_s1_s2[i][j-1];

                }

                dp_s1_s2[i][j] = Math.max(dpRow,dpCol);
            }
        }


        return dp_s1_s2[x-1][y-1];

    }

}

// Approach 1: Memoization
//class Solution
//{
//    private int fn(int x,int y,String s1,String s2,int[][] dp_s1_s2){
//
//        if(x<0 || y<0){
//            return 0;
//        }
//
//        if(dp_s1_s2[x][y] != -1){
//            return dp_s1_s2[x][y];
//        }
//
//
//
//        if(s1.charAt(x) == s2.charAt(y)){
//
//            dp_s1_s2[x][y] = 1 + fn(x-1,y-1,s1,s2,dp_s1_s2);
//            return dp_s1_s2[x][y];
//        }
//
//        dp_s1_s2[x][y] = Math.max(fn(x-1,y,s1,s2,dp_s1_s2),fn(x,y-1,s1,s2,dp_s1_s2));
//        return dp_s1_s2[x][y];
//
//    }
//
//    //Function to find the length of longest common subsequence in two strings.
//    public int lcs(int x, int y, String s1, String s2)
//    {
//        // your code here
//        // return this.fn(a-1,b-1,s1,s2);
//
//        int[][] dp_s1_s2 = new int[x][y];
//        for (int i = 0; i < x; i++) {
//            for (int j = 0; j < y; j++) {
//                dp_s1_s2[i][j] = -1;
//            }
//        }
//        int ans = this.fn(x-1,y-1,s1,s2, dp_s1_s2);
//        return ans;
//
//    }
//
//
//}
