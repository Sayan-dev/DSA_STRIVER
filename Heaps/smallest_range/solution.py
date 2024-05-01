import heapq
import sys

class node:
    def __init__(self, data,row,col):
        self.data =data
        self.row=row
        self.col=col
        
    def __lt__(self, other):
        return self.data<other.data
        
        
class Solution:
    def smallestRange(self, arr, n, k):
        min_heap = []
        # code here
        maxi = -sys.maxsize
        mini = sys.maxsize
        
        # store all starting element in min heap
        for i in range(k):
            element = arr[i][0]
            mini = min(mini,element)
            maxi = max(maxi,element)
            heapq.heappush(min_heap,node(element,i,0))

        # track start and end
        start, end = mini, maxi

        # process range
        while len(min_heap) != 0:
            temp = heapq.heappop(min_heap)
            mini = temp.data

            # update min range
            if maxi-mini<end-start:
                start,end = mini,maxi
            print(mini," ",maxi)
            print(start," ",end)

            # check for boundary condition and update max value by forwarding to the next value from min
            if temp.col + 1<n:
                maxi = max(maxi, arr[temp.row][temp.col+1])
                heapq.heappush(min_heap, node(arr[temp.row][temp.col+1],temp.row,temp.col+1))
            else:
                break
        
        return [start,end]      
          
