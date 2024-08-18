package Heaps;

import java.util.PriorityQueue;

class Node implements Comparable<Node>{

    int data;
    int row;
    int col;

    public Node(int data, int row, int col) {
        this.data = data;
        this.row = row;
        this.col = col;
    }

    @Override
    public int compareTo(Node n){
        return Integer.compare(this.data, n.data);

    }
}

class SmallestRange
{
    static int[] findSmallestRange(int[][] KSortedArray,int n,int k)
    {
        //add your code here
        //add your code here
        int[] ans = new int[2];
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        PriorityQueue<Node> q = new PriorityQueue<>();



        for(int i = 0; i < k; i++){
            q.add(new Node(KSortedArray[i][0], i, 0));

            min = Math.min(min, KSortedArray[i][0]);
            max = Math.max(max, KSortedArray[i][0]);
        }

        ans[0] = min;
        ans[1] = max;

        while(!q.isEmpty()) {
            Node temp = q.poll();
            if(ans[1] - ans[0] > max - temp.data){
                ans[1] = max;
                ans[0] = temp.data;
            }

            temp.col++;
            if(temp.col == n)
                break;

            int x = KSortedArray[temp.row][temp.col];
            max = Math.max(max, x);
            q.add(new Node(x, temp.row, temp.col));
        }

        return ans;
    }
}
