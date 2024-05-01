from solution import Solution, Jobs
from controller import Controller





new_controller = Controller()
solution_instance = Solution()

data = new_controller.readInput()

n =int(data[0])

jobs = []

for i in range (1,n+1):
    job = [int(x) for x in data[i].split(",")]
    jobs.append(Jobs(no=job[0],dead=job[1], point=job[2]))

print(f"{jobs}")

output = solution_instance.jobSequence(n,jobs)
new_controller.writeOutput(f"{output} \n\n\n\nThanks")

