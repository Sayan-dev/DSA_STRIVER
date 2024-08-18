package Array.trappingwater;


import java.io.*;
import java.util.*;
import java.lang.*;


public class Array {

        public static void main (String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
            while(t-->0){

                //size of array
                int n = Integer.parseInt(br.readLine().trim());
                int arr[] = new int[n];
                String inputLine[] = br.readLine().trim().split(" ");

                //adding elements to the array
                for(int i=0; i<n; i++){
                    arr[i] = Integer.parseInt(inputLine[i]);
                }

                Solution obj = new Solution();

                //calling trappingWater() function
                System.out.println(obj.trappingWater(arr, n));
            }
        }
    }

