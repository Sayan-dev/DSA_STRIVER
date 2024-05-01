import java.util.Arrays;

class MinimumHeightII {
    int getMinDiff(int[] arr, int n, int k) {
        // code here
        Arrays.sort(arr);

        int max = arr[n-1];
        int min = arr[0];

        int diff = max-min;



        for(int i=0; i<n; i++){
            if(arr[i]-k<=0)continue;
            max = Math.max(arr[i-1]+k,arr[n-1] -k);
            min = Math.min(arr[i]-k,arr[0]+k);
            diff = Math.min(diff, max-min);


        }



        return diff;

    }
}
