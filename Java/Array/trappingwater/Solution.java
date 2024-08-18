package Array.trappingwater;

public class Solution {
    static long trappingWater(int arr[], int n) {
        // Your code here
        long[] maxLeft = new long[n];

        long[] maxRight = new long[n];

        long max = arr[0];
        for(long i = 0;i<n;i++){
            maxLeft[i] = max;
            max = Math.max(arr[i],max);
        }
        max = arr[n-1];
        for(long i = n-1;i>=0;i--){


            maxRight[i] = max;
            max =Math.max(arr[i],max);

        }
        long vol = 0;
        for(long i=0;i<n;i++){
            long tempvol = Math.min(maxLeft[i],maxRight[i]) - arr[i];
            if(tempvol>=0){
                vol+=tempvol;

            }

        }
        return vol;
    }
}
