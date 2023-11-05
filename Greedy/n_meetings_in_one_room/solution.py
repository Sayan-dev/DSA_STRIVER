from controller import Controller

class wrapper:
    def __init__(self, start, end, no):
        self.start = start
        self.end = end
        self.no = no

class Solution:

    def n_meetings(self,n:int, start: list[int], end:list[int]):
        # Write your code here
        meet_list = [wrapper(start[i],end[i],i) for i in range(n)]
        sorted(meet_list, key=lambda x:(x.end, x.end-x.start))
        answer = []
        answer.append(meet_list[0].no+1)
        max_limit = meet_list[0].end

        for i in range(1,n):
            if meet_list[i].start > max_limit:
                max_limit = meet_list[i].end
                answer.append(meet_list[i].no+1)
        


        return answer