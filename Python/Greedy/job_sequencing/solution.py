from typing import List


class Jobs:
    def __init__(self, no, dead, point):
        self.no = no
        self.dead = dead
        self.point = point

class Solution:
    def jobSequence(self, n, jobs: List[Jobs]):
        job_list = sorted(jobs, key=lambda x:(x.point), reverse=True)
        profit = 0
        max_deadline = -1 
        for i in range(n):
             if job_list[i].dead>max_deadline:
                 max_deadline = job_list[i].dead
        jobs = [-1 for i in range(max_deadline)]
        for i in range(n):
            if jobs[job_list[i].dead-1]==-1:
                jobs[job_list[i].dead-1] = job_list[i].no
                profit += job_list[i].point
            else:
                for j in range(job_list[i].dead-1,-1,-1):
                    print(j, job_list[i].no)
                    if jobs[j]==-1:
                        jobs[j]=job_list[i].no
                        profit += job_list[i].point
                        break
        return [profit, jobs]

