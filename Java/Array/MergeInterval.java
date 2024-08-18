package Array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeInterval {
    public int[][] merge(int[][] intervals) {
        int n = intervals.length;
        // Overlapping means, end val of i >= start val of j
        Arrays.sort(intervals, (a, b)->a[0]-b[0]);

        List<int[]> answer = new ArrayList<int []>();



        int seek = 0;
        answer.add(intervals[0]);
        seek = 1;

        int listSeek = 0;
        while(seek<n){
            if(answer.get(listSeek)[1] >= intervals[seek][0]){
                if(answer.get(listSeek)[1] >= intervals[seek][1]){

                    answer.add(new int[]{answer.get(listSeek)[0],answer.get(listSeek)[1]});
                }else{

                    answer.add(new int[]{answer.get(listSeek)[0],intervals[seek][1]});
                }

                answer.remove(listSeek);

            }
            else{
                answer.add(intervals[seek]);

                listSeek+=1;
            }
            seek+=1;


        }

        int[][] finalAnswer = answer.toArray(new int[answer.size()][2]);
        return finalAnswer;

    }
}
